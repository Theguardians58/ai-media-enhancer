```py
from celery import Celery
from app.config import settings
from app.services.enhancer import ImageEnhancer
from app.services.video import VideoEnhancer
from app.services.storage import promote_result
from app.services.notify import publish_progress


celery = Celery('tasks', broker=settings.BROKER_URL, backend=settings.RESULT_BACKEND)


@celery.task(bind=True)
def enhance_media(self, task_id: str, kind: str, paths: list[str], scale=4, denoise=0.2, sharpen=0.2):
try:
if kind == 'image':
ie = ImageEnhancer('cuda')
outs = []
for i, p in enumerate(paths, start=1):
publish_progress(task_id, stage='image', percent=int(100*i/len(paths))-1, item=p)
out = ie.enhance_image(task_id, p, scale, denoise, sharpen)
outs.append(out)
finals = [promote_result(o) for o in outs]
else:
ve = VideoEnhancer('cuda')
out = ve.enhance_video(task_id, paths[0], scale, denoise, sharpen)
finals = [promote_result(out)]
publish_progress(task_id, stage='done', percent=100)
return finals
except Exception as e:
publish_progress(task_id, stage='error', percent=100, message=str(e))
raise
```
