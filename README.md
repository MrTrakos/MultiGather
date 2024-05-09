
# MultiGather

**You can install package by:**
```bash
pip install MultiGather
```

**Simple example for POST:**
```python
import asyncio
from MultiGather import Client
from MultiGather.Types import Config, Request

# Replace with the actual URL for your POST endpoint.
url = "https://your-api-endpoint/posts"

# Replace with the data you want to send in the POST request
data = {"title": "New Post", "body": "This is a sample post content", "userId": 1}

async def main():
    client = Client.Connection(Config(timeout=10))  # Set timeout to 10 seconds (optional)

    # Prepare a POST request object
    post_request = Request(method="POST", url=url, json=data, amount=5) ## gonna send 5 requests

    # Send the requests asynchronously and collect responses
    responses = await client.sendRequest(post_request)

    # Print the status code for each response
    for response in responses:
        print(f"POST response status: {response.status}")

asyncio.run(main())
```
**Simple example for GET:**
```python
import asyncio
from MultiGather import Client
from MultiGather.Types import Config, Request
# Replace with the actual URL for your GET endpoint
url = "https://your-api-endpoint/posts"

async def main():
    client = Client.Connection(Config(timeout=10))  # Set timeout to 10 seconds (optional)

    # Prepare a GET request object
    get_request = Request(method="GET", url=url, amount=5) # send 5 requests.

    # Send the requests asynchronously and collect responses
    responses = await client.sendRequest(get_request)

    # Print the status code for each response
    for response in responses:
        print(f"GET response status: {response.status}")

asyncio.run(main())
```

**Simple example for use proxy:**
```python
import asyncio
from MultiGather import Client
from MultiGather.Types import Config, Request
# Replace with the actual URL for your GET endpoint
url = "https://your-api-endpoint/posts"
proxy = "scheme://ip:port"

async def main():
    client = Client.Connection(Config(timeout=10, proxy=proxy))  # Set timeout to 10 seconds (optional)

    # Prepare a GET request object
    get_request = Request(method="GET", url=url, amount=5) # send 5 requests.

    # Send the requests asynchronously and collect responses
    responses = await client.sendRequest(get_request)

    # Print the status code for each response
    for response in responses:
        print(f"GET response status: {response.status}")

asyncio.run(main())
```