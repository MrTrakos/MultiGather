
# MultiGather

**You can install package by:**
```bash
pip install MultiGather
```

**Simple example for POST:**
```python
import asyncio
from MultiGather.Types import Config, Request
from MultiGather.Client import Connection

# Replace with the actual URL for your POST endpoint
url = "https://your-api-endpoint/posts"

async def main():
    # Prepare a GET request object
    request = Request(url=url, amount=5, method="POST") # send 5 requests.

    config = Config(timeout=30) # set config (timeout: 30)

    client = Connection(request=config) # Client object

    # Send the requests asynchronously and collect responses
    responses = await client.sendRequest(request) 

    # Print the status code for each response
    for response in responses:
        print(f"GET response status: {response.status}")

asyncio.run(main())

```

**Simple example for GET:**
```python
import asyncio
from MultiGather.Types import Config, Request
from MultiGather.Client import Connection

# Replace with the actual URL for your GET endpoint
url = "https://your-api-endpoint/posts"

async def main():
    # Prepare a GET request object
    request = Request(url=url, amount=5, method="GET") # send 5 requests.

    config = Config(timeout=30) # set config (timeout: 30)

    client = Connection(request=config) # Client object

    # Send the requests asynchronously and collect responses
    responses = await client.sendRequest(request) 

    # Print the status code for each response
    for response in responses:
        print(f"GET response status: {response.status}")

asyncio.run(main())

```

**Simple example for use proxy:**
```python
import asyncio
from MultiGather.Types import Config, Request
from MultiGather.Client import Connection

# Replace with the actual URL for your GET endpoint
url = "https://your-api-endpoint/posts"
# Replace with the actual proxy 
proxy = "scheme://ip:port"

async def main():
    # Prepare a GET request object
    request = Request(url=url, amount=5, method="GET") # send 5 requests.

    config = Config(timeout=30, proxy=proxy) # set config (timeout: 30, proxy: proxy)

    client = Connection(request=config) # Client object

    # Send the requests asynchronously and collect responses
    responses = await client.sendRequest(request) 

    # Print the status code for each response
    for response in responses:
        print(f"GET response status: {response.status}")

asyncio.run(main())

```
