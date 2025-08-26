```py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.config import settings
from app.routes import upload, status, download
from app.ws import router as ws_router
from app.services.storage import cleanup_old
import threading, time


app = FastAPI(title='AI Media Enhancer')


origins = [o.strip() for o in settings.ALLOWED_ORIGINS.split(',') if o.strip()]
app.add_middleware(
CORSMiddleware,
allow_origins=origins or ['*'],
allow_methods=['*'],
allow_headers=['*'],
)


app.include_router(upload.router, prefix='/api')
app.include_router(status.router, prefix='/api')
app.include_router(download.router, prefix='/api')
app.include_router(ws_router)


# Serve results statically via Nginx outside; still expose for dev
app.mount('/results', StaticFiles(directory=settings.RESULTS_DIR), name='results')


# Background cleanup thread


def _janitor():
while True:
try:
cleanup_old(settings.CLEANUP_TTL_SECONDS)
except Exception:
pass
time.sleep(3600)


threading.Thread(target=_janitor, daemon=True).start()


@app.get('/health')
async def health():
return { 'ok': True }
```
