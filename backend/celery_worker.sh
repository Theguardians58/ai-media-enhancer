```bash
#!/usr/bin/env bash
set -e
celery -A app.tasks.celery worker --loglevel=INFO
```
