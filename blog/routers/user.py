from fastapi import APIRouter
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas, database
from ..repository import user

router = APIRouter(tags=["Users"], prefix="/user")


@router.post("/signup", response_model=schemas.ShowUser)
def signup(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.signup(request=request, db=db)


@router.get("", response_model=List[schemas.ShowUser])
def get_all_users(db: Session = Depends(database.get_db)):
    return user.get_all(db=db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id, db: Session = Depends(database.get_db)):
    return user.get_by_id(id=id, db=db)
