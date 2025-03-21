import time
import pandas as pd
import pywhatkit as kit
import pyautogui

# Read CSV with correct column names
csv='' 

df = pd.read_csv(csv)
message= "sup , this is where the text is supposed to be"
delay = 25

def format_phone_number(phone):
    # Convert to string and remove any whitespace
    phone = str(phone).strip()
    # Remove any existing '+' or '91' prefix
    phone = phone.replace('+', '')
    # Add +91 prefix to cleaned number
    return '+91' + phone

for index, row in df.iterrows():
    # Skip rows where mobile number is 0
    if row["mobile"] == 0:
        print(f"Skipping {row['full_name']} - Invalid mobile number")
        continue
        
    # Format phone number and get name
    phone_number = format_phone_number(row["mobile"])
    name = row["full_name"].strip()
    
    # # Personalized message
    # message = f"Hi {name},\nWe are thrilled to invite you to the Karma Marathon! 🏃‍♂️\nJoin us for an exciting evening filled with energy and fun.\n📅 Date: 21st March 2025\n⏰ Time: 8:00 PM\nWe can't wait to see you there!\n{meeting_invite_link}"

    try:
        print(f"Sending message to {name} ({phone_number})...")
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=delay)
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(8)
        print(f"Message sent successfully to {name}")
    except Exception as e:
        print(f"Error sending to {name}: {str(e)}")
        continue

print('Script completed')
