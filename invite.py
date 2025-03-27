import os
import time
import pandas as pd
import pywhatkit as kit
import pyautogui
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Add CORS middleware to allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

def format_phone_number(phone):
    """
    Format phone number to international format with +91 prefix
    
    Args:
        phone (str/int): Phone number to format
    
    Returns:
        str: Formatted phone number with +91 prefix
    """
    try:
        # Convert to string and remove any whitespace
        phone = str(phone).strip()
        
        # Remove any existing '+' or '91' prefix
        phone = phone.replace('+', '')
        
        # Ensure number is 10 digits
        if len(phone) > 10:
            if phone.startswith('91'):
                phone=phone[2:]
        if len(phone) !=10:
            raise ValueError(f'too many digits')
        
        # Add +91 prefix
        return '+91' + phone
    except Exception as e:
        print(f"Phone number formatting error: {e}")
        return None

@app.post("/send-whatsapp-messages/")
async def send_whatsapp_messages(file: UploadFile = File(...), message: str = ""):
    """
    Endpoint to send WhatsApp messages from uploaded CSV
    
    Args:
        file (UploadFile): CSV file containing contact details
        message (str): Message to send
    
    Returns:
        dict: Result of message sending process
    """
    try:
        # Save uploaded file temporarily
        with open("temp_contacts.csv", "wb") as buffer:
            buffer.write(await file.read())
        
        # Read CSV file
        df = pd.read_csv("temp_contacts.csv")
        
        # Validate required columns
        required_columns = ["mobile", "full_name"]
        for col in required_columns:
            if col not in df.columns:
                raise HTTPException(status_code=400, detail=f"Missing required column: {col}")
        
        # Initialize tracking variables
        total_contacts = len(df)
        sent_messages = 0
        failed_messages = 0
        error_details = []
        
        # Process and send messages
        for index, row in df.iterrows():
            # Skip invalid numbers
            if pd.isna(row["mobile"]) or row["mobile"] == 0:
                failed_messages += 1
                error_details.append(f"Invalid number for {row['full_name']}")
                continue
            
            # Format phone number
            phone_number = format_phone_number(row["mobile"])
            if not phone_number:
                failed_messages += 1
                error_details.append(f"Cannot format number for {row['full_name']}")
                continue
            
            # Personalize message if possible
            personalized_message = message.replace("{name}", row["full_name"])
            
            try:
                # Send message using pywhatkit
                kit.sendwhatmsg_instantly(phone_number, personalized_message, wait_time=15)
                time.sleep(5)
                pyautogui.press('enter')
                time.sleep(8)
                
                sent_messages += 1
            except Exception as e:
                failed_messages += 1
                error_details.append(f"Failed to send to {row['full_name']}: {str(e)}")
        
        # Remove temporary file
        os.remove("temp_contacts.csv")
        
        return {
            "total_contacts": total_contacts,
            "sent_messages": sent_messages,
            "failed_messages": failed_messages,
            "error_details": error_details
        }
    
    except Exception as e:
        # Handle any unexpected errors
        return {
            "error": str(e),
            "message": "An error occurred during message sending"
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)