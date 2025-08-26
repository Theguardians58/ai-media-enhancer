```tsx
import React from 'react';
import type { Preset } from '../api';


export default function SettingsPanel({
preset, setPreset,
params, setParams,
processClientSide, setProcessClientSide
}: {
preset: Preset; setPreset: (p: Preset) => void;
params: { scale?: number; denoise?: number; sharpen?: number };
setParams: (p: any) => void;
processClientSide: boolean; setProcessClientSide: (b: boolean) => void;
}) {
return (
<div className="grid sm:grid-cols-2 gap-4">
<div className="bg-white p-4 rounded-2xl border">
<label className="block text-sm font-medium">Preset</label>
<select className="mt-1 w-full border rounded-xl p-2"
value={preset}
onChange={e => setPreset(e.target.value as Preset)}
>
<option value="lite">Lite (TF.js in browser)</option>
<option value="standard">Standard (x2)</option>
<option value="high">High (x4)</option>
<option value="ultra">Ultra (x4 + denoise/sharpen)</option>
</select>
<label className="flex items-center gap-2 mt-3 text-sm">
<input type="checkbox" checked={processClientSide} onChange={e=>setProcessClientSide(e.target.checked)} />
Prefer in-browser processing for lightweight tasks
</label>
</div>
<div className="bg-white p-4 rounded-2xl border">
<div className="grid grid-cols-3 gap-4">
<div>
<label className="block text-sm">Scale</label>
<input type="number" min={1} max={4} step={1} className="mt-1 w-full border rounded-xl p-2"
value={params.scale ?? 2}
onChange={e=>setParams({ ...params, scale: parseInt(e.target.value) })} />
</div>
<div>
<label className="block text-sm">Denoise</label>
<input type="number" min={0} max={1} step={0.1} className="mt-1 w-full border rounded-xl p-2"
value={params.denoise ?? 0.2}
onChange={e=>setParams({ ...params, denoise: parseFloat(e.target.value) })} />
</div>
<div>
<label className="block text-sm">Sharpen</label>
<input type="number" min={0} max={1} step={0.1} className="mt-1 w-full border rounded-xl p-2"
value={params.sharpen ?? 0.2}
onChange={e=>setParams({ ...params, sharpen: parseFloat(e.target.value) })} />
</div>
</div>
</div>
</div>
);
}
```
