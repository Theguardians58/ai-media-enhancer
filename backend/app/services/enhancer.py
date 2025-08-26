```py
import cv2, numpy as np
from app.config import settings
from app.services.notify import publish_progress


# Real-ESRGAN minimal wrapper
try:
from realesrgan import RealESRGAN
except Exception:
RealESRGAN = None


class ImageEnhancer:
def __init__(self, device: str = 'cuda'):
self.device = device
self.model = None


def _load(self):
if self.model: return
if RealESRGAN is None:
raise RuntimeError('Real-ESRGAN package not available')
self.model = RealESRGAN(device=self.device, scale=4)
self.model.load_weights(settings.REAL_ESRGAN_MODEL)


def enhance_image(self, task_id: str, img_path: str, scale=4, denoise=0.2, sharpen=0.2) -> str:
self._load()
publish_progress(task_id, stage='load', percent=5, item=img_path)
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
sr = self.model.predict(img)
if denoise>0:
sr = cv2.fastNlMeansDenoisingColored(sr, None, denoise*10, denoise*10, 7, 21)
if sharpen>0:
kernel = np.array([[0,-sharpen,0],[-sharpen,1+4*sharpen,-sharpen],[0,-sharpen,0]])
sr = cv2.filter2D(sr, -1, kernel)
out_path = img_path.replace('.','_enhanced.',1)
cv2.imwrite(out_path, sr)
publish_progress(task_id, stage='image_done', percent=100, item=img_path)
return out_path
```
