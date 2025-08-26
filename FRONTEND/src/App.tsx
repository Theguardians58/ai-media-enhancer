```tsx
import React, { useMemo, useState } from 'react';
import DropArea from './components/DropArea';
import BeforeAfter from './components/BeforeAfter';
import ProgressItem from './components/ProgressItem';
import TopBar from './components/TopBar';
import SettingsPanel from './components/SettingsPanel';
import useProgress from './hooks/useWebSocket';
import { uploadFiles, wsUrl, Preset } from './api';


export default function App() {
const [files, setFiles] = useState<File[]>([]);
const [taskId, setTaskId] = useState<string | null>(null);
const [preset, setPreset] = useState<Preset>('high');
const [params, setParams] = useState({ scale: 4, denoise: 0.2, sharpen: 0.2 });
const [processClientSide, setProcessClientSide] = useState(false);


const onDrop = (f: File[]) => setFiles(prev => [...prev, ...f]);


const { events, latest } = useProgress(taskId ? wsUrl(taskId) : '');


const start = async () => {
if (!files.length) return;
const type = files.every(f => f.type.startsWith('image/')) ? 'image' : files.every(f => f.type.startsWith('video/')) ? 'video' : 'mixed';
const res = await uploadFiles(files, { type, preset, params, processClientSide });
setTaskId(res.task_id);
};


const preview = useMemo(() => files[0] ? URL.createObjectURL(files[0]) : '', [files]);
const doneEvent = events.find(e => e.done && e.download_url);


return (
<div className="min-h-screen bg-gray-100">
<div className="max-w-6xl mx-auto px-4">
<TopBar />

<div className="grid md:grid-cols-2 gap-6 mt-4">
<div className="space-y-4">
<SettingsPanel
preset={preset}
setPreset={setPreset}
params={params}
setParams={setParams}
processClientSide={processClientSide}
setProcessClientSide={setProcessClientSide}
/>
<DropArea onDrop={onDrop} />
<div className="flex gap-2 flex-wrap mt-2">
{files.map((f, i) => (
<span key={i} className="text-xs bg-white border rounded-full px-3 py-1">{f.name}</span>
))}
</div>
<button onClick={start} className="mt-2 px-4 py-2 rounded-xl bg-black text-white disabled:opacity-50" disabled={!files.length}>
Enhance {files.length ? `(${files.length})` : ''}
</button>
<div className="space-y-2 mt-4">
{events.map((ev, i) => <ProgressItem key={i} ev={ev} />)}
</div>
</div>


<div className="space-y-4">
{preview && !doneEvent && (
<div className="bg-white p-4 rounded-2xl border">
<h2 className="font-semibold mb-2">Preview</h2>
<img src={preview} className="max-h-96 w-full object-contain" />
</div>
)}
{doneEvent && (
<div className="bg-white p-4 rounded-2xl border">
<h2 className="font-semibold mb-2">Before / After</h2>
<BeforeAfter beforeUrl={preview} afterUrl={doneEvent.download_url!} />
</div>
)}
</div>
</div>
</div>
</div>
);
}
```
