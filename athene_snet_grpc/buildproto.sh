python3 -m grpc_tools.protoc \
              -I. \
              --python_out=. \
              --grpc_python_out=. \
              athene_grpc/service_spec/athenefnc.proto
