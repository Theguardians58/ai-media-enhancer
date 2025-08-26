```py
import json
import redis
from app.config import settings


r = redis.Redis.from_url(settings.REDIS_URL)


def publish_progress(task_id: str, **kwargs):
payload = {"task_id": task_id, **kwargs}
r.publish(f"progress:{task_id}", json.dumps(payload))
```
