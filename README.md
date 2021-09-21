#Helicon Python Sample App
This repository contains the files required to run the Helicon Python Quickstart.

Helicon is a simple, scalable, robust, code-free and generic platform to enable and productise the next generation of "online modified", real-time event stream ML/AI models.

## Set up the project

Run `pip install -r requirements.txt` to install the project.
To start to publish and/or subscribe to a topic stream you need to populate all the placeholder fields, defined like <placeholder>.
Then you can just run the `__main__` method inside each client example.

## Sample App
### Publish
This code is available at `helicon_publish/publish.py`. This example will publish as payload a json object like
```
{
"temperature": 26,
"timestamp": 1632143723
}
```
The method `time.time()` is part of the __Python 3__ code base, so you don't need to install anything else to use it.
```
keycloakUrl = "<keycloak-url>"
grpcHost = "<grpc-host>"
grpcPort = "<grpc-port>"
clientId = "<client-id>"
clientSecret = "<client-secret>"
tenant = "<tenant-name>"
stream_name = "<stream_name>"

if __name__ == '__main__':
    helicon_client = HeliconPublishClient(keycloakUrl=keycloakUrl, serverHost=grpcHost, serverPort=grpcPort,
    clientID=clientId, clientSecret=clientSecret, tenantName=tenant)

    payload = f'{{"temperature": 26, "timestamp": {time.time()}}}'
    helicon_client.write(stream_name, payload)
```
### Subscribe
Same for subscription, the code is available at `helicon_subscribe/subscribe.py`, and it is going to print the message, and its fields, defined above.
```
keycloakUrl = "<keycloak-url>"
grpcHost = "<grpc-host>"
grpcPort = 0  # "<grpc-port-as-int>"
clientId = "<client-id>"
clientSecret = "<client-secret>"
tenant = "<tenant-name>"
stream_name = "<stream_name>"


def process(event: Dict[str, Any]):
print(event)
print(event["temperature"])
print(event["timestamp"])


if __name__ == '__main__':
    helicon_client = HeliconSubscribeClient(keycloak_url=keycloakUrl, server_host=grpcHost, server_port=grpcPort,
    client_id=clientId, client_secret=clientSecret, tenant_name=tenant)

    helicon_client.subscribe_json(stream_name, process)
```
To be able to read the data you are writing with the publishing client you need to subscribe to the same stream.
The message received will be parsed as a generic json object before being processed from the response processor.
To handle generic messages you can use `subscribe_string(stream_name, process)`, which will parse the message response as UTF-8 string.

## How to Run the app

Running the `__main__` method inside `subscribe.py` manually or with `python3 subscribe.py` command from a terminal, you will start to receive messages as soon as they are written on the stream.

To publish 1 message you can run the `__main__` method inside `publish.py` manually or with `python3 publish.py` command from a terminal, or, for multiple messages, you can wrap it in a loop.

You should see printed the response on the terminal.

## Support
We're always happy to help with any other questions you might have! [Send us an email](mailto:support@radicalbit.io).