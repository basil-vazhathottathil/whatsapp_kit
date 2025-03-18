import time
import pandas as pd
import pywhatkit as kit

df = pd.read_csv('contacts.csv')

invite_link='https://chat.whatsapp.com/IpIdU2xcZECHvaCYVc2oC5'

delay=15

for index, row in df.iterrows():
    # Use the phone number directly without any modifications
    phone_number = str(row["Phone"]).strip()

    message = f"you are invited to join our WhatsApp group. Click here to join: {invite_link}"

    try:
        print(f"Sending invite to {phone_number}...")
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=delay)
        time.sleep(10)
    except Exception as e:
        print(f"Failed to send to {phone_number}: {e}")

print('done')
