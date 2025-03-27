'use client';

import React, { useRef, useState } from 'react'
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"

function Card() {
  const [message, setMessage] = useState<string>('');
  const [filename, setFileName] = useState<string>('');
  const [file, setFile] = useState<File | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  
  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setFile(file);
      setFileName(file.name);
      // Log file details for testing
      console.log('File selected:', {
        name: file.name,
        type: file.type,
        size: file.size + ' bytes'
      });
    }
  };

  const handleButtonClick = () => {
    fileInputRef.current?.click();
  };

  return (  
    <div className="bg-gray-500 p-8 rounded-lg shadow-md w-[400px] space-y-4 border-black border-2">
      <div className='flex flex-col space-y-4'>
        <input 
          type="file"
          accept='.csv'
          onChange={handleFileSelect}
          ref={fileInputRef}
          style={{ display: 'none' }}  // Hide the default input
        />
        <Textarea 
          className="w-full bg-white border-black border-2"
          placeholder='enter the message to be sent here'
          value={message}
          onChange={(e)=> setMessage(e.target.value)}
        />
        <div className="flex items-center gap-4 justify-start">
          <Button className="w-40" onClick={handleButtonClick}>choose your file</Button>
          <label className='text-sm'>{filename || 'No file selected'}</label>
        </div>
        
        <div className="flex items-center gap-4 justify-start">
          <Button className="w-40">start sending</Button>
          <label className="text-sm">done?</label>
        </div>
      </div>
    </div>
  )
}

export default Card