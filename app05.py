from fastapi import APIRouter
from fastapi import File      # 接受字节流
from typing import List
from fastapi import UploadFile



app05 = APIRouter()

@app05.post("/file")
async def get_file(file: bytes=File()):
    # 适合小文件上传
    print("file", file)
    return {
        "file": "file"
    }
    

# 多文件上传
@app05.post("/files")
async def get_files(file: List[bytes] =File()):
    # 适合小文件上传
    print("file", len(file))
    return {
        "file": len(file)
    }    
    
    
@app05.post("/upload_files")
async def upload_files(file: UploadFile):
    # 适合小文件上传，使用Upload结构体的时候返回的是文件句柄
    print("file", file)
    return {
        "file": file.filename
    }    