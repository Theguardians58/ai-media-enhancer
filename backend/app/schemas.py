```py
from pydantic import BaseModel
from typing import Optional, List, Literal, Dict


class UploadResult(BaseModel):
task_id: str
items: List[Dict[str, str]]


class ProgressEvent(BaseModel):
task_id: str
percent: float
stage: str
message: Optional[str] = None
item: Optional[str] = None
done: bool = False
download_url: Optional[str] = None
```
