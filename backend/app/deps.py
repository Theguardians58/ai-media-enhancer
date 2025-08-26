```py
from fastapi import Header, HTTPException


async def verify_origin(origin: str | None = Header(None)):
# Additional hooks for auth can be placed here
return True
```
