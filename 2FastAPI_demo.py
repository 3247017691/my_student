
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: str
    name: str
    age: int | None = None


@app.get("/users")
def read_users():
    return [
        {"id": "1", "name": "John", "age": 20},
        {"id": "2", "name": "Jane", "age": 25},
        {"id": "3", "name": "Jim", "age": 30}
    ]

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=False)
