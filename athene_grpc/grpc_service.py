import sys, os.path as path
import json
import argparse
import requests

import grpc
import time
from concurrent import futures
sys.path.append("./service_spec")
import athenefnc_pb2 as pb2
import athenefnc_pb2_grpc as pb2_grpc

server_port = None

class GRPCserver(pb2_grpc.AtheneStanceClassificationServicer):
    def __init__(self, _athene_rest_addr):
        self.athene_rest_api_addr = _athene_rest_addr
    def stance_classify(self, req, ctxt):
        headline = req.headline
        body = req.body
        lbld_pred = json.loads(requests.post(self.athene_rest_api_addr,
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps({'headline' : headline, 'body': body})).text)
        stance_pred = pb2.Stance()
        stance_pred.agree = float(lbld_pred['agree'])
        stance_pred.disagree = float(lbld_pred['disagree'])
        stance_pred.discuss = float(lbld_pred['discuss'])
        stance_pred.unrelated = float(lbld_pred['unrelated'])
        return stance_pred


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Athene Stance Detection System')
    parser.add_argument('--athene-addr', action='store', type=str, required=True)
    parser.add_argument('--listen', action='store', type=str, required=True)
    args = parser.parse_args()
    athene_addr = args.athene_addr
    server_port = args.listen
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_AtheneStanceClassificationServicer_to_server(GRPCserver(athene_addr), grpc_server)
    grpc_server.add_insecure_port('[::]:' + server_port)
    grpc_server.start()
    print("GRPC Server Started on port: " + server_port)
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Exiting....")
        grpc_server.stop(0)
