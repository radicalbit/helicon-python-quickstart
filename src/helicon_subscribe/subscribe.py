import atexit
from typing import Dict, Any

from helicon_subscribe.helicon_subscribe_client import HeliconSubscribeClient

keycloakUrl = "<keycloak-url>"
grpcHost = "<grpc-host>"
grpcPort = 0  # "<grpc-port-as-int>"
clientId = "<client-id>"
clientSecret = "<client-secret>"
tenant = "<tenant-name>"
stream_name = "<stream_name>"


def process(event: Dict[str, Any]):
    print(event)


if __name__ == '__main__':
    helicon_client = HeliconSubscribeClient(keycloak_url=keycloakUrl, server_host=grpcHost, server_port=grpcPort,
                                            client_id=clientId, client_secret=clientSecret, tenant_name=tenant)

    helicon_client.subscribe_json(stream_name, process)

    atexit.register(helicon_client.close)
