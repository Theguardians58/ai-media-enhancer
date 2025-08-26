```ts
export const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000';
export const WS_BASE = import.meta.env.VITE_WS_BASE || 'ws://localhost:8000';


export type Preset = 'lite' | 'standard' | 'high' | 'ultra';


export interface UploadResponse { task_id: string; items: {name: string, type: 'image'|'video'}[] }


export async function uploadFiles(
files: File[],
payload: {
type: 'image' | 'video' | 'mixed';
preset: Preset;
params: { scale?: number; denoise?: number; sharpen?: number };
processClientSide?: boolean;
}
) {
const form = new FormData();
files.forEach(f => form.append('files', f));
form.append('type', payload.type);
form.append('preset', payload.preset);
form.append('params', JSON.stringify(payload.params));
form.append('clientLite', String(!!payload.processClientSide));


const res = await fetch(`${API_BASE}/api/upload`, { method: 'POST', body: form });
if (!res.ok) throw new Error(await res.text());
return (await res.json()) as UploadResponse;
}


export async function getStatus(taskId: string) {
const res = await fetch(`${API_BASE}/api/status/${taskId}`);
return res.json();
}


export function wsUrl(taskId: string) {
return `${WS_BASE}/ws/progress/${taskId}`;
}
```
