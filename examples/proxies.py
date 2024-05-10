from MultiGather.Client import Connection
from MultiGather.Types import Request, Config

from asyncio import run

Client = Connection(
    Config(
        timeout=15,
        redirect=False, max_connection_limit=1000
    )
)
async def main():
    URL = "https://jsonplaceholder.typicode.com/comments/1"
    Proxy = {
        "http": "http://proxy:port",
        "https": "https://proxy:port"
    } 
    # Or you can use:
    # Proxy = "http://proxy:port"
    requestList = await Client.sendRequest(
        Request(
            method='GET', # Or you can use POST.
            url=URL, 
            amount=1, proxy=Proxy
        )
    )
    # /|\
    #  |
    # Its return always list.
    return requestList[-1]
getLastCommnet = run(main())
print(getLastCommnet)