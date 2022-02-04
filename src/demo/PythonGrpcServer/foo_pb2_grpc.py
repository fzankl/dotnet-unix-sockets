# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import foo_pb2 as foo__pb2


class FooStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetFoo = channel.unary_unary(
                '/Foo/GetFoo',
                request_serializer=foo__pb2.FooRequest.SerializeToString,
                response_deserializer=foo__pb2.FooResponse.FromString,
                )


class FooServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetFoo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FooServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetFoo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFoo,
                    request_deserializer=foo__pb2.FooRequest.FromString,
                    response_serializer=foo__pb2.FooResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Foo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Foo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetFoo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Foo/GetFoo',
            foo__pb2.FooRequest.SerializeToString,
            foo__pb2.FooResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)