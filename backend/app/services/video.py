```py
import os, subprocess, glob
from app.services.enhancer import ImageEnhancer
from app.services.notify import publish_progress


FFMPEG = 'ffmpeg'
FFPROBE = 'ffprobe'


def run(cmd):
subprocess.check_call(cmd, shell=True)


class VideoEnhancer:
def __init__(self, device='cuda'):
self.ie = ImageEnhancer(device=device)


def enhance_video(self, task_id: str, in_path: str, scale=4, denoise=0.2, sharpen=0.2) -> str:
workdir = os.path.dirname(in_path)
stem, _ = os.path.splitext(os.path.basename(in_path))
frames_dir = os.path.join(workdir, f"{stem}_frames")
os.makedirs(frames_dir, exist_ok=True)
publish_progress(task_id, stage='extract_frames', percent=5)
run(f"{FFMPEG} -y -i '{in_path}' -qscale:v 2 '{frames_dir}/%07d.png'")
frames = sorted(glob.glob(os.path.join(frames_dir, '*.png')))
n = len(frames)
for i, fr in enumerate(frames, start=1):
self.ie.enhance_image(task_id, fr, scale, denoise, sharpen)
publish_progress(task_id, stage='upscale', percent=5 + int(90*i/max(n,1)), item=os.path.basename(fr))
publish_progress(task_id, stage='encode', percent=96)
out_path = os.path.join(workdir, f"{stem}_enhanced.mp4")
run(f"{FFMPEG} -y -r 30 -i '{frames_dir}/%07d_enhanced.png' -i '{in_path}' -map 0:v -map 1:a? -c:v libx264 -preset slow -crf 17 -c:a copy '{out_path}'")
publish_progress(task_id, stage='cleanup', percent=98)
run(f"rm -rf '{frames_dir}'")
publish_progress(task_id, stage='video_done', percent=100)
return out_path
```
