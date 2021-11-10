import atexit
from typing import Dict, Any

from helicon_subscribe.helicon_subscribe_client import HeliconSubscribeClient

authorization_server = "<authorization-server>"
grpc_host = "<grpc-host>"
grpc_port = 0  # "<grpc-port-as-int>"
client_id = "<client-id>"
client_secret = "<client-secret>"
tenant = "<tenant-name>"
stream_name = "<stream-name>"


def process(event: Dict[str, Any]):
    print(event)
    print(event["temperature"])
    print(event["timestamp"])


if __name__ == '__main__':
    helicon_client = HeliconSubscribeClient(authorization_server=authorization_server, server_host=grpc_host,
                                            server_port=grpc_port, client_id=client_id, client_secret=client_secret,
                                            tenant_name=tenant)

    helicon_client.subscribe_json(stream_name, process)

    atexit.register(helicon_client.close)
