from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    print("I received a request on /")
    return {"data": {"name": "Hitendra"}}


@app.get("/about")
def about():
    return {"data": "about page"}


@app.get("/blog")
def blog(limit: Optional[int] = 10, published: Optional[bool] = True):
    return {
        "data": f"you requested for {limit} blogs from database that are published {published}"
    }


@app.get("/blog/unpublished")
def unpublished():
    return {"message": "You will get list of unpublished blogs"}


@app.get("/blog/{id}")
def blog_by_id(id: int):
    return {"blog_id": id + 10}


@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"comments": [id, "second", "third"]}


class Blog(BaseModel):
    title: str
    description: str
    published: Optional[bool] = False


@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": blog, "message": "blog created successfully"}
