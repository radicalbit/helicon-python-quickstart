import time

from helicon_client import HeliconPublishClient

host = "<host>"
port = 443
client_id = "<client_id>"
client_secret = "<client_secret>"
tenant = "<tenant_name>"

stream_name = "<stream_name>"

if __name__ == '__main__':
    helicon_client = HeliconPublishClient(
        host=host, port=port, client_id=client_id, client_secret=client_secret, tenant_name=tenant)

    payload = f'{{"temperature": 26, "timestamp": {time.time()}}}'
    helicon_client.write(stream_name, payload)

    helicon_client.close()
