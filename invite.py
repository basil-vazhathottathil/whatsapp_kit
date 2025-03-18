import time
import pandas as pd
import pywhatkit as kit
import pyautogui  # Add this import at the top

df = pd.read_csv('contacts.csv')

invite_link = 'https://chat.whatsapp.com/IpIdU2xcZECHvaCYVc2oC5'
delay = 15

for index, row in df.iterrows():
    # Add the + symbol before the phone number
    phone_number = "+" + str(row["Phone"]).strip()
    
    message = f"you are invited to join our WhatsApp group. Click here to join: {invite_link}"

    try:
        print(f"Sending invite to {phone_number}...")
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=delay)
        time.sleep(2)  # Wait for message to be ready
        pyautogui.press('enter')  # Press enter to send message
        time.sleep(8)  # Wait before next message
        print("Message sent successfully")
    except Exception as e:
        print(f"Error details: {str(e)}")
        print(f"Failed to send to {phone_number}")

print('Script completed')
