import atexit
from typing import Dict, Any

from radicalbit_client import RadicalbitSubscribeClientBi

host = "<host>"
port = 443
client_id = "<client_id>"
client_secret = "<client_secret>"
tenant = "<tenant_name>"

stream_name = "<stream_name>"


def process(event: Dict[str, Any]):
    print(event)
    print(event["temperature"])
    print(event["timestamp"])


if __name__ == '__main__':
    radicalbit_client = RadicalbitSubscribeClientBi(host=host, port=port, client_id=client_id, client_secret=client_secret,
                                              tenant_name=tenant)

    radicalbit_client.subscribe_json(stream_name, process)

    atexit.register(radicalbit_client.close)
