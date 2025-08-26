```py
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from app.config import settings
from redis import Redis


router = APIRouter()


r = Redis.from_url(settings.RESULT_BACKEND)


@router.get('/status/{task_id}')
async def status(task_id: str):
# Minimal status using celery backend or Redis keys; for demo, empty
return ORJSONResponse({ 'task_id': task_id, 'status': 'running' })
```
