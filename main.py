from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/test")
async def test():
    return {"message": "It works good! version = 20260605_1051"}

@app.get("/get_key1")
async def get_key1():
    return {"message": os.getenv("test_key1")}

@app.get("/get_key365")
async def get_key1():
    return {"message": os.getenv("file:///Users/shenwenwei/Downloads/AI%E4%BA%BA%E6%89%8D%E6%96%B9%E8%88%9F%E8%A8%88%E7%95%AB_%E7%B6%B2%E7%AB%99_%E4%BA%92%E5%8B%95%E7%89%88%203/AI%E4%BA%BA%E6%89%8D%E6%96%B9%E8%88%9F%E8%A8%88%E7%95%AB_%E7%B6%B2%E7%AB%99_%E4%BA%92%E5%8B%95%E7%89%88/index.html")}

@app.get("/get_project")
async def get_key():
    return {"message": os.getenv("PROJECT_ID")}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
