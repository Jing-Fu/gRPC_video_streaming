# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import camera_pb2 as camera__pb2

GRPC_GENERATED_VERSION = '1.67.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in camera_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CameraServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamFrames = channel.stream_unary(
                '/camera.CameraService/StreamFrames',
                request_serializer=camera__pb2.Frame.SerializeToString,
                response_deserializer=camera__pb2.Status.FromString,
                _registered_method=True)


class CameraServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamFrames(self, request_iterator, context):
        """定義流式上傳影像資料
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CameraServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamFrames': grpc.stream_unary_rpc_method_handler(
                    servicer.StreamFrames,
                    request_deserializer=camera__pb2.Frame.FromString,
                    response_serializer=camera__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'camera.CameraService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('camera.CameraService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CameraService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StreamFrames(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/camera.CameraService/StreamFrames',
            camera__pb2.Frame.SerializeToString,
            camera__pb2.Status.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
