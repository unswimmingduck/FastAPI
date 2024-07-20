## FastAPI环境配置：
### 1.配置好python环境
### 2.下载FastAPI包和uvicorn服务器，通过如下指令：
``` pip install fastapi```  
``` pip install uvicorn``` 
 
## 测试
配置完成后，运行文件中的main.py文件就可以启动微服务，微服务的地址为: http://127.0.0.1:8181。可以在main.py函数的第14行更改微服务地址。在启动微服务后，可以通过访问http://127.0.0.1:8181/docs在浏览器页面看到微服务的端口并进行简单测试。

启动微服务后，运行api.go文件就可以通过go语言调用微服务，目前调用的是微服务中的request接口，返回请求宿主的相关信息。
