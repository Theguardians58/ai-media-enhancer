```tsx
import React, { useRef, useState } from 'react';


interface Props {
beforeUrl: string;
afterUrl: string;
}


export default function BeforeAfter({ beforeUrl, afterUrl }: Props) {
const [pos, setPos] = useState(50);
const ref = useRef<HTMLDivElement>(null);


return (
<div className="relative w-full max-w-3xl aspect-video rounded-2xl overflow-hidden shadow">
<img src={beforeUrl} className="absolute inset-0 w-full h-full object-contain" />
<div style={{ width: `${pos}%` }} className="absolute inset-0 overflow-hidden">
<img src={afterUrl} className="w-full h-full object-contain" />
</div>
<input
aria-label="comparison slider"
type="range"
min={0}
max={100}
value={pos}
onChange={(e) => setPos(parseInt(e.target.value))}
className="absolute bottom-2 left-1/2 -translate-x-1/2 w-1/2"
/>
</div>
);
}
```
