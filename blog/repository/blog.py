from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session


from .. import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(blog: schemas.Blog, db: Session):
    new_blog = models.Blog(title=blog.title, desc=blog.desc, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_by_id(id, response: Response, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} is not available",
        )
    response.status_code = status.HTTP_200_OK
    return blog


def delete_by_id(id, response: Response, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Couldn't find the blog with id {id}",
        )

    blog.delete(synchronize_session=False)
    db.commit()
    response.status_code = status.HTTP_200_OK

    return {"message": "Succsfully deleted the blog"}


def update_by_id(id, new_blog, response: Response, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Couldn't find the blog with id {id}",
        )
    blog.update({"title": new_blog.title, "desc": new_blog.desc})
    db.commit()
    response.status_code = status.HTTP_202_ACCEPTED
    return "updated Succsfully"
