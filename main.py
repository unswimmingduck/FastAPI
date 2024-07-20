from fastapi import FastAPI
from app05 import app05
from app06 import app06
import uvicorn


app = FastAPI()

app.include_router(app05, tags=["上传文件"])
app.include_router(app06, tags=["获取request响应"])

if __name__ == "__main__":
    # 连接的地址是 http://127.0.0.1:8181
    uvicorn.run(app='main:app', host='127.0.0.1', port=8181, reload=True)