import sys, os.path as path
import json
import os

import requests

import grpc
import time
from concurrent import futures

sys.path.append("./service_spec")
import athenefnc_pb2_grpc as pb2_grpc
import athenefnc_pb2 as pb2


server_port = os.environ['ATHENE_GRPC_ADD'] # port ATHENE service runs

class GRPCserver(pb2_grpc.AtheneStanceClassificationServicer):
    def stance_classify(self, req, ctxt):
        headline = req.headline
        body = req.bodiy
        lbld_pred = json.loads(requests.post("http://demo.nunet.io:13321",
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps({'headline' : headline, 'body': body})).text)
        stance_pred = pb2.Stance()
        stance_pred.agree = float(lbld_pred['agree'])
        stance_pred.disagree = float(lbld_pred['disagree'])
        stance_pred.discuss = float(lbld_pred['discuss'])
        stance_pred.unrelated = float(lbld_pred['unrelated'])
        return stance_pred


if __name__ == '__main__':
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
