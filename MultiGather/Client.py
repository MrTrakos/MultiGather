import aiohttp
import asyncio
from Types import Response, Request, Config

class Connection:
    def __init__(self, request: Config):
        self.request = request

    async def sendRequest(self, request: Request):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=self.request.max_connection_limit), timeout=aiohttp.ClientTimeout(total=self.request.timeout)) as session:
            tasks = [self._sendRequest(request=request, session=session) for _ in range(request.amount)]
            return await asyncio.gather(*tasks)

    async def _sendRequest(self, session: aiohttp.ClientSession, request: Request):
        try:
            async with session.request(
                    method=request.method, url=request.url,
                    headers=request.headers, json=request.json,
                    data=request.data, params=request.params,
                    proxy=self.request.proxy
            ) as response:
                response.raise_for_status()
                content_type = response.headers.get('content-type', '')
                json_content = await response.json() if 'application/json' in content_type else None
                return Response(
                    status=response.status, url=str(response.url),
                    headers=response.headers, json=json_content,
                    text=await response.text(), content=await response.read()
                )
        except (aiohttp.ClientError, aiohttp.ServerTimeoutError) as e:
            return Response(status=609, url=request.url, headers={}, content=str(e), exception=True)
        except Exception as e:
            return Response(status=609, url=request.url, headers={}, content=str(e), exception=True)
