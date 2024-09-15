from typing import List
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from ..repository import blog


from .. import schemas, database, oauth2

router = APIRouter(tags=["Blogs"], prefix="/blog")


@router.post("")
def create(new_blog: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(blog=new_blog, db=db)


@router.get("", response_model=List[schemas.ShowBlog])
def get_all_blogs(
    db: Session = Depends(database.get_db),
    get_current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.get_all(db)


@router.get("/{id}", response_model=schemas.ShowBlog)
def get_blog_by_id(id, response: Response, db: Session = Depends(database.get_db)):
    return blog.get_by_id(id=id, response=response, db=db)


@router.delete("/{id}")
def delete_blog_by_id(id, response: Response, db: Session = Depends(database.get_db)):
    return blog.delete_by_id(id=id, response=response, db=db)


@router.put("/{id}")
def update_blog_by_id(
    id,
    request: schemas.Blog,
    response: Response,
    db: Session = Depends(database.get_db),
):
    return blog.update_by_id(id=id, new_blog=request, response=response, db=db)
