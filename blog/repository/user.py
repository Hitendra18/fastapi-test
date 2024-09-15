from fastapi import HTTPException, status
from sqlalchemy.orm import Session


from .. import models, schemas, hashing


def signup(request: schemas.User, db: Session):
    hashed_password = hashing.Hash.encrypt(request.password)
    user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all(db: Session):
    users = db.query(models.User).all()
    return users


def get_by_id(id, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Couldn't find user with id {id}",
        )
    return user
