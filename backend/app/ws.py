```py
from fastapi import APIRouter, WebSocket
import redis, json
from app.config import settings


router = APIRouter()


@router.websocket('/ws/progress/{task_id}')
async def ws_progress(websocket: WebSocket, task_id: str):
await websocket.accept()
r = redis.Redis.from_url(settings.REDIS_URL)
pubsub = r.pubsub()
pubsub.subscribe(f'progress:{task_id}')
try:
# initial ping
await websocket.send_text(json.dumps({ 'task_id': task_id, 'stage': 'connected', 'percent': 0 }))
for message in pubsub.listen():
if message['type'] != 'message':
continue
await websocket.send_text(message['data'].decode())
finally:
pubsub.close()
```
