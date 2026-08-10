from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int | None = None

@app.get("/users", summary="查询所有用户", response_model=list[User])
def read_users() -> list[User]:
    print("查询所有用户")
    return [
        User(id="1", name="John", age=20),
        User(id="2", name="Jane", age=25),
        User(id="3", name="Jim", age=30)
    ]

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=False)
