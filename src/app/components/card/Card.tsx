import React from 'react'
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"

function Card() {
  return (
    <div className="bg-gray-500 p-8 rounded-lg shadow-md w-[400px] space-y-4 border-black border-2">
      <div className='flex flex-col space-y-4'>
        <Textarea className="w-full bg-white border-black border-2"/>
        <div className="flex items-center gap-4 justify-start">
          <Button className="w-40">choose your csv file</Button>
          <label className="text-sm">name</label>
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