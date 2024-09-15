from fastapi import APIRouter, HTTPException, status
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from .. import schemas, database, models, hashing, token

# from ..repository import user

router = APIRouter(tags=["Authentication"], prefix="/auth")


@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User doesn't exitst"
        )

    if not hashing.Hash.verify(secret=request.password, hashed_password=user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
        )
    access_token = token.create_access_token(data={"sub": user.email})
    return schemas.Token(access_token=access_token, token_type="bearer")
