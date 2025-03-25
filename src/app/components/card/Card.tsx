import React from 'react'
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"

function Card() {
  return (
    <div>
        <Textarea/>
        <Button>choose your csv file</Button>
        <Button>Send messages</Button>
    </div>
  )
}

export default Card