// Home.tsx or index.tsx
'use client';

import Card from "./components/card/Card";

export default function Home() {
  return (
    <div 
      className="flex flex-col justify-center items-center min-h-screen"
      style={{backgroundImage: "url('/bg.jpg')", backgroundSize: 'cover', backgroundPosition: 'center'}}
    >
      <Card />
    </div>
  );
}

