import sys, os.path as path
import json

import requests

import grpc
import time
from concurrent import futures
sys.path.append("./service_spec")
import athene_grpc.service_spec.athenefnc_pb2_grpc as pb2_grpc
import athene_grpc.service_spec.athenefnc_pb2 as pb


server_port = None

class GRPCserver(pb2_grpc.AtheneStanceClassificationServicer):
    def stance_classify(self, req, ctxt):
        headline = req.headline
        body = req.body
        lbld_pred = json.loads(requests.post("http://athene_system:13321",
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps({'headline' : headline, 'body': body})).text)
        stance_pred = pb2.Stance()
        stance_pred.agree = float(lbld_pred['agree'])
        stance_pred.disagree = float(lbld_pred['disagree'])
        stance_pred.discuss = float(lbld_pred['discuss'])
        stance_pred.unrelated = float(lbld_pred['unrelated'])
        return stance_pred


if __name__ == '__main__':
    server_port = 7008
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_AtheneStanceClassificationServicer_to_server(GRPCserver(), grpc_server)
    grpc_server.add_insecure_port('[::]:' + server_port)
    grpc_server.start()
    print("GRPC Server Started on port: " + server_port)
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Exiting....")
        grpc_server.stop(0)
