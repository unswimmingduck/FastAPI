from fastapi import APIRouter
from fastapi import File      # 接受字节流
from typing import List
from fastapi import UploadFile
from fastapi import Request


app06 = APIRouter()

@app06.post("/request")
async def request(re:Request):
    
    print("request has been used")
    return{
        "URL": re.url,
        "客户端IP": re.client.host,
        "客户端请求宿主": re.headers.get("user-agent"),
        "cookie": re.cookies
    }