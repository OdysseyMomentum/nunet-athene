import sys, os.path as path
import json
import os

import requests

import grpc
import time
from concurrent import futures

sys.path.append("./athene_grpc/service_spec")
import athenefnc_pb2_grpc as pb2_grpc
import athenefnc_pb2 as pb2
from resutils import *

server_port = os.environ['SERVICE_PORT'] # port ATHENE service runs

class GRPCserver(pb2_grpc.AtheneStanceClassificationServicer):
    def stance_classify(self, req, ctxt):
        try:
            telemetry=resutils()
            start_time=time.time()
            cpu_start_time=telemetry.cpu_ticks()
        except:
            print("telemetry is not working")
        headline = req.headline
        body = req.body
        lbld_pred = json.loads(requests.post("http://demo.nunet.io:13321",
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps({'headline' : headline, 'body': body})).text)
        stance_pred = pb2.Stance()
        stance_pred.agree = float(lbld_pred['agree'])
        stance_pred.disagree = float(lbld_pred['disagree'])
        stance_pred.discuss = float(lbld_pred['discuss'])
        stance_pred.unrelated = float(lbld_pred['unrelated'])
        try:
            memory_used=telemetry.memory_usage()
            time_taken=time.time()-start_time
            cpu_used=telemetry.cpu_ticks()-cpu_start_time
            net_used=telemetry.block_in()
            telemetry.call_telemetry(str(cpu_used),str(memory_used),str(net_used),str(time_taken))
        except:
            print("telemetry is not working")
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
