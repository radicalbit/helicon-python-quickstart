# Radicalbit Platform Python Sample App
This repository contains the files required to run the Radicalbit Platform Python Quickstart.

The Radicalbit Platform is a simple, scalable, robust, code-free and generic platform to enable and productise the next generation of "online modified", real-time event stream ML/AI models.

## Set up the project

We suggest to use *venv* and install everything with it: Run `python3 -m venv venv` in your project home directory and `source venv/bin/activate` to create and activate the virtual environment venv.
Run `pip install --upgrade pip` to update pip to the latest version and tun `pip install -r requirements.txt` to install the project.
Make sure you are using +pip3* as package manager.
To start to publish and/or subscribe to a topic stream you need to populate all the placeholder fields, defined like \<placeholder\>.
Then you can just run the `__main__` method inside each client example.

## Sample App

### Publish

This code is available at `platform_publish/publish.py`. This example will publish as payload a json object like
```json
{
"temperature": 26,
"timestamp": 1632143723
}
```
The method `time.time()` is part of the __Python 3__ code base, so you don't need to install anything else to use it.
```python
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
```

### Subscribe
Same for subscription, the code is available at `platform_subscribe/subscribe.py`, and it is going to print the message, and its fields, defined above.
```python
import atexit
from typing import Dict, Any

from radicalbit_client import RadicalbitSubscribeClient

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
    radicalbit_client = RadicalbitSubscribeClient(host=host, port=port, client_id=client_id, client_secret=client_secret,
                                            tenant_name=tenant)

    radicalbit_client.subscribe_json(stream_name, process)

    atexit.register(radicalbit_client.close)
```
To be able to read the data you are writing with the publishing client you need to subscribe to the same stream.
The message received will be parsed as a generic json object before being processed from the response processor.
To handle generic messages you can use `subscribe_string(stream_name, process)`, which will parse the message response as UTF-8 string.

*For long-time subscribing operation, we suggest using our Bidirectional RadicalbitSubscribeClient, which you can find here: https://github.com/radicalbit/helicon-python-quickstart/blob/main/src/platform_subscribe/subscribe_bi.py.*

## How to Run the app

Running the `__main__` method inside `subscribe.py` manually or with `python3 subscribe.py` command from a terminal, you will start to receive messages as soon as they are written on the stream.

To publish 1 message you can run the `__main__` method inside `publish.py` manually or with `python3 publish.py` command from a terminal, or, for multiple messages, you can wrap it in a loop.

You should see printed the response on the terminal.

## How to Run publisher and subscriber concurrently

It is possible to run concurrently publish and subscribe operations:
```python
import atexit
import time
import threading
from typing import Dict, Any

from radicalbit_client import RadicalbitPublishClient
from radicalbit_client import RadicalbitSubscribeClient

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


def write_to_stream(radicalbit_client: RadicalbitPublishClient):
    for i in range(500):
        payload = f'{{"temperature": {i}, "timestamp": {time.time()}}}'
        radicalbit_client.write(stream_name, payload)

if __name__ == '__main__':
    platform_subscribe_client = RadicalbitSubscribeClient(host=host, port=port, client_id=client_id, client_secret=client_secret,
                                            tenant_name=tenant)
    platform_publish_client = RadicalbitPublishClient(host=host, port=port, client_id=client_id, client_secret=client_secret,
                                          tenant_name=tenant)

    sub_thread = threading.Thread(target=platform_subscribe_client.subscribe_json, args=(stream_name, process), daemon=True)
    pub_thread = threading.Thread(target=write_to_stream, args=(platform_publish_client,), daemon=True)
    
    sub_thread.start()
    pub_thread.start()
    
    pub_thread.join()
    sub_thread.join()
    
    atexit.register(platform_subscribe_client.close)
```

It is also possible to use another publish to publish messages red from the subscriber, changing the `process` method as follows:
```python
def process(response: Dict[str, Any]):
    # response won't arrive in json format, it should be parsed, i.e. json.dumps({k: list(response[k].values())[0] for k in response})
    radicalbit_client_publish.write(stream_name_2, response)
```

## Change the API version

The main branch is always updated with the latest version of the Radicalbit Platform API.

If you need to use an old version of the Radicalbit's API, you can switch between the project version using `git checkout tag_version`.

You can refer to the Radicalbit Platform documentation for looking more in the depth over the version's features.

## Support

We're always happy to help with any other questions you might have! [Send us an email](mailto:support@radicalbit.io).
