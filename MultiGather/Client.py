import aiohttp
import asyncio
from .Types import Response, Request, Config

class Connection:
    def __init__(self, request: Config):
        self.connector = aiohttp.TCPConnector(limit=request.max_connection_limit)  # Set connection limit
        
    async def sendRequest(self, request: Request):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=Config.timeout)) as session:
            
            tasks = [self._sendRequest(request=request, session=session) for _ in range(request.amount)]
            return await asyncio.gather(*tasks) ## Send the tasks to be processed.
    async def _sendRequest(self, session: aiohttp.ClientSession, request: Request):
        try:
            async with session.request(
                    method=request.method, url=request.url,
                    headers=request.headers, json=request.json,
                    data=request.data, params=request.params,
                    proxy=request.proxy
            ) as response:
                
                response.raise_for_status()
                content_type = response.headers.get('content-type', '')
                json_content = await response.json() if 'application/json' in content_type else None
                
                if request.onlySuccess and response.status != 200:
                    return Response(status=response.status if response.status else 0, url=request.url, headers={}, content=None, exception=False, proxy=request.proxy, params=request.params)
                return Response(
                    status=response.status, url=str(response.url),
                    headers=response.headers, json=json_content,
                    text=await response.text(), content=await response.read(), exception=False,
                    proxy=request.proxy, params=request.params
                )
        except (aiohttp.ClientError, aiohttp.ServerTimeoutError, aiohttp.ClientProxyConnectionError) as e:
            return Response(status=response.status if response.status else 0, url=request.url, headers={}, content=str(e), exception=True, proxy=request.proxy, params=request.params)
        except Exception as e:
            return Response(status=response.status if response.status else 0, url=request.url, headers={}, content=str(e), exception=True, proxy=request.proxy, params=request.params)
