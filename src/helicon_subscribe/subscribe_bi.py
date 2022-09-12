import atexit
from typing import Dict, Any

from helicon_client import HeliconSubscribeClientBi

host = "helicon.dev.radicalbit.io"
port = 443
client_id = "<client_id>"
client_secret = "<client_secret>"
tenant = "<tenant_name>"

stream_name = "test_test_2"


def process(event: Dict[str, Any]):
    print(event)
    print(event["temperature"])
    print(event["timestamp"])


if __name__ == '__main__':
    helicon_client = HeliconSubscribeClientBi(host=host, port=port, client_id=client_id, client_secret=client_secret,
                                              tenant_name=tenant)

    helicon_client.subscribe_json(stream_name, process)

    atexit.register(helicon_client.close)
