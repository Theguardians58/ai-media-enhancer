```py
from fastapi import APIRouter, UploadFile, File, Form, Request
from fastapi.responses import ORJSONResponse
from typing import List
from app.services.storage import save_upload
from app.tasks import enhance_media
import uuid, json


router = APIRouter()


@router.post('/upload')
async def upload(
request: Request,
files: List[UploadFile] = File(...),
type: str = Form('image'),
preset: str = Form('high'),
params: str = Form('{}'),
clientLite: str = Form('false'),
):
task_id = uuid.uuid4().hex
saved = [save_upload(f) for f in files]
p = json.loads(params or '{}')


# Map presets to parameters
preset_map = {
'lite': dict(scale=2, denoise=0.0, sharpen=0.1),
'standard': dict(scale=2, denoise=0.1, sharpen=0.1),
'high': dict(scale=4, denoise=0.2, sharpen=0.2),
'ultra': dict(scale=4, denoise=0.3, sharpen=0.3),
}
merged = { **preset_map.get(preset, {}), **p }


# Fire async task
kind = 'video' if type=='video' else 'image'
if type == 'mixed':
# naive split: treat as images if majority are images
kind = 'image'
enhance_media.delay(task_id, kind, saved, **merged)


return ORJSONResponse({ 'task_id': task_id, 'items': [{'name': f.filename, 'type': type}] })
```
