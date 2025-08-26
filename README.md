# ai-media-enhancer
```md
# AI Media Enhancer


## Quick start
1) Install Docker + NVIDIA Container Toolkit for GPU.
2) Copy `.env.example` to `.env` and adjust domains/paths.
3) `mkdir -p data/tmp data/results`
4) `docker compose up --build`
5) Open http://localhost:5173 (dev) and http://localhost:8080/results for CDN-like static results.


## API
- `POST /api/upload` (multipart): files[], type=image|video, preset, params
- `GET /api/status/{task_id}`: JSON status
- `WS /ws/progress/{task_id}`: progress events
- `GET /api/download/{task_id}`: signed redirect to result


## Security & Privacy
- Temp files under `TEMP_DIR` with random names.
- Auto cleanup job removes files older than `CLEANUP_TTL_SECONDS`.
- CORS limited via `ALLOWED_ORIGINS`.
- Only exposes signed, time-limited download tokens.


## Models
- GPU: Real-ESRGAN via `realesrgan` Python package.
- TF.js Lite: optional client-side enhancement when selected.
```

# Security Checklist
- Validate MIME types and size limits (add to `upload` route).
- Generate random filenames; never echo user path.
- CORS restricted via env.
- Signed, time-limited downloads via `/api/download/{token}` (token created when task completes; see enhancement task to emit URL).
- Auto cleanup.
- Run as non-root in hardened Dockerfile for production.


---


# Emitting Download URLs from Tasks


In `tasks.py`, after `promote_result`, sign and publish a WebSocket event with `download_url` so the frontend can render the before/after slider.


```py
from itsdangerous import TimestampSigner
from app.config import settings
from app.services.storage import promote_result
from app.services.notify import publish_progress


signer = TimestampSigner(settings.SECRET_KEY)


# ... after finals are created
for f in finals:
token = signer.sign(f).decode()
# The frontend will open /api/download/{token} which redirects to Nginx /results
publish_progress(task_id, stage='done', percent=100, done=True, download_url=f"/api/download/{token}")
```


(Integrate this snippet into `tasks.py` as desired.)


---
# Batch Processing
- The upload endpoint accepts multiple files; images are processed in sequence (extend to parallel if GPU mem allows).
- Progress events include `item` = filename and cumulative percent.


---


# Format Support
- Images: PNG, JPG, JPEG, WEBP (OpenCV handles most). Consider Pillow for extras.
- Videos: MP4, MOV, WebM (via ffmpeg).


---


# Production Hardening Ideas
- Add auth (JWT) if needed.
- S3-compatible object storage + CDN (replace `storage.promote_result` and `signed_url`).
- GPU multi-worker with queue priorities.
- Tiling for large frames to reduce VRAM; stream-encode to avoid large temp storage.
- Deduplicate uploads via content hash.

# Run it

1.Install Docker + NVIDIA Container Toolkit.

2.Copy .env.example → .env, adjust ALLOWED_ORIGINS, etc.

3.mkdir -p data/tmp data/results

4.docker compose up --build

5.Open the frontend at http://localhost:5173. Results are served (with caching) via Nginx at http://localhost:8080/results.

What you get

Drag-and-drop uploads, preset/custom controls, before/after slider, real-time progress via WebSockets.

Client-side “Lite” mode hook for TF.js (toggle in UI), and server-side GPU Real-ESRGAN for heavy lifts.

Frame-by-frame video upscale (extract → enhance → re-encode with original audio) to HD/4K by scale.

Async queue (Celery) + Redis; progress events published and streamed to the client.

Temporary storage with hourly janitor cleanup; signed, time-limited download URLs.

Batch image processing; multiple video formats via FFmpeg.

If you want, I can tailor it for your exact deployment (e.g., S3 + CloudFront, auth/JWT, or tiling for ultra-high-res).
