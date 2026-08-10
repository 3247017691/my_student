# 作业: 基于 FastAPI 开发"图书信息查询"API接口
# ==========================================================
#
# 【作业需求】
#     使用 FastAPI 框架, 开发一个简单的"图书馆图书信息查询"API接口服务,
#     用于查询图书馆中的图书列表信息。
#
# 【具体要求】
#     1. 安装 FastAPI 与 uvicorn 依赖库
#        - 命令: uv add fastapi uvicorn  (或 pip install fastapi uvicorn)
#
#     2. 创建一个 FastAPI 实例对象, 并指定:
#        - title       = "图书信息查询系统"
#        - description = "一个简单的图书馆图书信息查询API"
#        - version     = "1.0.0"
#
#     3. 使用 Pydantic 模型定义图书数据结构 (类名: Book), 包含以下字段:
#        - id      : int   图书ID
#        - name    : str   图书名称
#        - author  : str   作者
#        - price   : float 价格
#        - stock   : int   库存数量
#
#     4. 开发以下 3 个 API 接口:
#        (1) GET /
#            - 功能: 根路径, 返回欢迎信息
#            - 返回: {"message": "欢迎使用图书信息查询系统!"}
#
#        (2) GET /books
#            - 功能: 获取所有图书列表
#            - summary: "获取所有图书列表"
#            - response_model: list[Book]
#            - 返回: 至少包含 3 本图书信息的列表, 图形信息定义在代码中即可
#            - 提示: 在控制台打印 "获取图书列表..."
#
#        (3) GET /books/count
#            - 功能: 获取图书总数量
#            - summary: "获取图书总数"
#            - 返回: {"total": 图书数量}
#
#     5. 通过代码方式启动 FastAPI 服务
#        - host = "0.0.0.0"
#        - port = 8000
#
#     6. 启动后测试:
#        - 在浏览器访问 http://localhost:8000/                   访问首页
#        - 在浏览器访问 http://localhost:8000/books              查看图书列表
#        - 在浏览器访问 http://localhost:8000/books/count        查看图书数量
#        - 在浏览器访问 http://localhost:8000/docs               查看自动生成的接口文档
# ==========================================================
# """

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="图书信息查询系统",
    description="一个简单的图书馆图书信息查询API",
    version="1.0.0"
)

class Book(BaseModel):
    id: int
    name: str
    author: str
    price: float
    stock: int

books = [
    Book(id=1, name="Python编程", author="张三", price=39.9, stock=10),
    Book(id=2, name="数据结构与算法", author="李四", price=49.9, stock=5),
    Book(id=3, name="计算机网络", author="王五", price=29.9, stock=8),
]


@app.get("/")
async def root():
    """根路径，返回欢迎信息"""
    return {"message":'欢迎使用图书信息查询系统'}

@app.get("/books", response_model=list[Book], summary='获取图书列表')
async def get_books():
    """获取所有图书列表"""
    print("获取图书列表...")
    return books

@app.get("/books/count", summary='获取图书总数')
async def get_books_count():
    """获取图书总数"""
    return {"total":len(books)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
