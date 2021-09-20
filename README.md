# Helicon Python Quickstart #

This repository contains a python publish and subscribe client example.

## How do I get set up? ##

* Run `pip install -e .` to install the project. 
  To start to publish and/or subscribe to a topic stream you need to populate all the placeholder fields, defined like <placeholder>.
  Then you can just run the `__main__` method inside each client example.

## Test cases ##

### Publish a temperature with timestamp ###
As part of this example, you are going to publish a json object like
```
{
"temperature": 26,
"timestamp": 1632143723
}
```
defined as string `payload = f'{{"temperature": 26, "timestamp": {time.time()}}}'`. The method `time.time()` is part of the __Python 3__ code base, so you don't need to install anything else to use it.

After that you have just to create the Helicon Python client and call the method `write()` passing the stream name as first argument, and the payload, you have just created, as second one.
```
helicon_client.write("stream_name", payload)
```
To publish that payload you can just run the `__main__` method inside `publish.py`

### Subscribe to a stream to read temperature with timestamp ###
To be able to read the data you are writing with the publishing client you need to subscribe to the same stream.

To do that you need to use `helicon_client.subscribe_json(stream_name, process)`, with process implemented to print the messages received.
Using `subscribe_json(stream_name, process)` the message received will be parsed as a generic json object before being processed from the response processor.
To handle generic messages you can use `subscribe_string("stream_name", process)`, which will parse the message response as UTF-8 string.

### Wrapping up everything all together ###

After your setup is ready, it's time to subscribe to a stream. Running the `__main__` method inside `subscribe.py` you will start to receive messages as soon as they are written on the stream.

To publish 1 message you can run the `__main__` method inside `publish.py`, or, for multiple messages, wrap it in a loop.

You should see printed the response on the terminal.