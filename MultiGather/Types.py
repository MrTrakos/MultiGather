from dataclasses import dataclass
from typing import Dict, Optional, Union

@dataclass
class Config:
    timeout: int = 25
    redirect: bool = False
    max_connection_limit: int = 1000
    proxy: Optional[Union[str, Dict[str, str]]] = None  # Support for proxy

@dataclass
class Request:
    url: str
    amount: int = 1
    method: str = "GET"
    headers: Optional[Dict[str, str]] = None
    params: Optional[Dict[str, str]] = None
    json: Optional[Dict[str, str]] = None
    data: Optional[Dict[str, str]] = None

@dataclass
class Response:
    status: int
    url: str
    content: bytes
    headers: Dict[str, str]
    body: Optional[str] = None
    text: Optional[str] = None
    exception: Optional[str] = None
    json: Optional[Dict[str, str]] = None