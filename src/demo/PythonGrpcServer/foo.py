import grpc
from concurrent import futures

import foo_pb2_grpc
import foo_pb2

class Foo(foo_pb2_grpc.FooServicer):
    def GetFoo(self, request, context):
        return foo_pb2.FooResponse(message='Python based gRPC server receives over Unix Domain Socket: ' + request.message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    foo_pb2_grpc.add_FooServicer_to_server(Foo(), server)

    server.add_insecure_port('unix:///tmp/foo.sock')
    server.start()

    print('gRPC server started using Unix Domain Socket')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()