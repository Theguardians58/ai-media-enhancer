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
