```py
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from itsdangerous import TimestampSigner, BadSignature
from app.services.storage import signed_url
from app.config import settings


router = APIRouter()


signer = TimestampSigner(settings.SECRET_KEY)


@router.get('/download/{token}')
async def download(token: str, request: Request):
try:
path = signer.unsign(token, max_age=3600).decode()
except BadSignature:
return RedirectResponse(url='/', status_code=302)
base = str(request.base_url).rstrip('/')
return RedirectResponse(url=signed_url(path, base), status_code=302)
```
