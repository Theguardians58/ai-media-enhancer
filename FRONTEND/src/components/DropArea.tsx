```tsx
import React from 'react';
import { useDropzone } from 'react-dropzone';


type Props = { onDrop: (files: File[]) => void };


export default function DropArea({ onDrop }: Props) {
const { getRootProps, getInputProps, isDragActive } = useDropzone({
accept: { 'image/*': [], 'video/*': [] },
multiple: true,
onDrop
});


return (
<div
{...getRootProps()}
className={`border-2 border-dashed rounded-2xl p-8 text-center cursor-pointer transition ${
isDragActive ? 'bg-gray-100' : 'bg-white'
}`}
>
<input {...getInputProps()} />
<p className="text-lg">Drag & drop images/videos here, or click to select</p>
<p className="text-sm text-gray-500 mt-2">Supports batch upload. PNG/JPG, MP4/MOV/WebM.</p>
</div>
);
}
```
