```py
import os, uuid, shutil, time
from app.config import settings


os.makedirs(settings.TEMP_DIR, exist_ok=True)
os.makedirs(settings.RESULTS_DIR, exist_ok=True)


def _rand_name(prefix: str, ext: str):
return f"{prefix}-{uuid.uuid4().hex}{ext}"


def save_upload(file) -> str:
name = _rand_name("upload", os.path.splitext(file.filename)[1].lower())
path = os.path.join(settings.TEMP_DIR, name)
with open(path, 'wb') as f:
shutil.copyfileobj(file.file, f)
return path


def promote_result(temp_path: str, suffix: str = "") -> str:
base = os.path.basename(temp_path)
root, ext = os.path.splitext(base)
final = os.path.join(settings.RESULTS_DIR, f"{root}{suffix}{ext}")
shutil.move(temp_path, final)
return final


def signed_url(path: str, host_base: str) -> str:
# For demo: return Nginx-served /results path
base = os.path.basename(path)
return f"{host_base}/results/{base}"


def cleanup_old(ttl_seconds: int):
now = time.time()
for folder in [settings.TEMP_DIR, settings.RESULTS_DIR]:
for name in os.listdir(folder):
p = os.path.join(folder, name)
try:
if os.stat(p).st_mtime < now - ttl_seconds:
os.remove(p)
except IsADirectoryError:
continue
except FileNotFoundError:
pass
```
