```tsx
import React from 'react';
import { ProgressEvent } from '../hooks/useWebSocket';


export default function ProgressItem({ ev }: { ev: ProgressEvent }) {
return (
<div className="rounded-xl p-4 bg-gray-50 border flex items-center gap-4">
<div className="w-20 text-sm text-gray-500">{ev.stage}</div>
<div className="flex-1">
<div className="h-2 rounded bg-gray-200">
<div className="h-2 rounded bg-gray-800" style={{ width: `${ev.percent}%` }}></div>
</div>
<div className="text-xs text-gray-600 mt-1">{ev.message || ev.item}</div>
</div>
{ev.done && ev.download_url && (
<a className="text-blue-600 text-sm" href={ev.download_url} target="_blank">Download</a>
)}
</div>
);
}
```
