```ts
import ReconnectingWebSocket from 'reconnecting-websocket';
import { useEffect, useRef, useState } from 'react';


export interface ProgressEvent {
task_id: string;
percent: number; // 0..100
stage: string; // e.g., "extract_frames", "upscale", "encode"
message?: string;
item?: string; // filename
done?: boolean;
download_url?: string;
}


export default function useProgress(wsUrl: string) {
const [events, setEvents] = useState<ProgressEvent[]>([]);
const wsRef = useRef<ReconnectingWebSocket | null>(null);


useEffect(() => {
const ws = new ReconnectingWebSocket(wsUrl);
wsRef.current = ws;
ws.addEventListener('message', (e) => {
const data = JSON.parse(e.data) as ProgressEvent;
setEvents(prev => [...prev, data]);
});
return () => { ws.close(); };
}, [wsUrl]);


const latest = events[events.length - 1];
return { events, latest };
}
```
