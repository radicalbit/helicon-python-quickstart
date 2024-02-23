import time

from radicalbit_client import RadicalbitPublishClient

host = "<host>"
port = 443
client_id = "<client_id>"
client_secret = "<client_secret>"
tenant = "<tenant_name>"

stream_name = "<stream_name>"

if __name__ == '__main__':
    radicalbit_client = RadicalbitPublishClient(
        host=host, port=port, client_id=client_id, client_secret=client_secret, tenant_name=tenant)

    payload = f'{{"temperature": 26, "timestamp": {time.time()}}}'
    radicalbit_client.write(stream_name, payload)

    radicalbit_client.close()
