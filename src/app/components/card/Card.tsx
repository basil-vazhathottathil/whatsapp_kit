// Card.tsx
'use client';

import React, { useRef, useState } from 'react'
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import axios from 'axios'; // Make sure to install axios

function Card() {
  const [message, setMessage] = useState<string>('');
  const [filename, setFileName] = useState<string>('');
  const [file, setFile] = useState<File | null>(null);
  const [sendStatus, setSendStatus] = useState<string>('');
  const fileInputRef = useRef<HTMLInputElement>(null);
  
  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    if (selectedFile) {
      // Validate CSV file
      if (selectedFile.type !== 'text/csv' && !selectedFile.name.endsWith('.csv')) {
        alert('Please select a CSV file');
        return;
      }
      
      setFile(selectedFile);
      setFileName(selectedFile.name);
      console.log('File selected:', {
        name: selectedFile.name,
        type: selectedFile.type,
        size: selectedFile.size + ' bytes'
      });
    }
  };

  const handleSendMessages = async () => {
    // Validate inputs
    if (!file) {
      alert('Please select a CSV file');
      return;
    }
    
    if (!message.trim()) {
      alert('Please enter a message');
      return;
    }

    // Create FormData to send file and message
    const formData = new FormData();
    formData.append('file', file);
    formData.append('message', message);

    try {
      // Set sending status
      setSendStatus('Sending messages...');

      // Send request to backend
      const response = await axios.post('http://localhost:8000/send-whatsapp-messages/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      // Handle response
      const { total_contacts, sent_messages, failed_messages, error_details } = response.data;
      
      // Update status message
      setSendStatus(`
        Total: ${total_contacts}, 
        Sent: ${sent_messages}, 
        Failed: ${failed_messages}
      `);

    } catch (error) {
      console.error('Error sending messages:', error);
      setSendStatus('Failed to send messages. Please try again.');
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
          <Button 
            className="w-40" 
            onClick={handleSendMessages}
            disabled={!file || !message.trim()}
          >
            start sending
          </Button>
          <label className="text-sm">
            {sendStatus || 'Ready to send'}
          </label>
        </div>
      </div>
    </div>
  )
}

export default Card