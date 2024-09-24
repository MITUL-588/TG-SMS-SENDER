import os
try:
  from telethon import TelegramClient
except:
  os.system("pip install telethon")
  from telethon import TelegramClient
  pass
from telethon.errors import SessionPasswordNeededError
try:
  from dotenv import load_dotenv
except:
  os.system("pip install python-dotenv")
  from dotenv import load_dotenv
  pass
load_dotenv()
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("MY_NUMBER")
async def send_message(phone_number, receiver_number, message):
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(phone=phone_number)
    if await client.is_user_authorized() == False:
        try:await client.sign_in(phone=phone_number)
        except SessionPasswordNeededError:
            password = input("Enter your 2FA password: ")
            await client.sign_in(password=password)
    try:
        await client.send_message(receiver_number, message)
        print(f"Message Succesfully sent to {receiver_number}")
    except Exception as e:
        print(f"Failed to send message: {str(e)}")
    await client.disconnect()

if __name__ == '__main__':
    os.system("clear")
    line = 45*'-'
    print(f"""\n           ┏┳┓┏┓  ┏┓┳┳┓┏┓  ┏┓┏┓┳┓┳┓┏┓┳┓\n            ┃ ┃┓  ┗┓┃┃┃┗┓  ┗┓┣ ┃┃┃┃┣ ┣┫\n            ┻ ┗┛  ┗┛┛ ┗┗┛  ┗┛┗┛┛┗┻┛┗┛┛┗\n{line}\n<\> CODED BY  :  ALTALIMUL ISLAM (MITUL)\n<\> TOOL      :  TG SMS SENDER""")
    print(line)
    receiver_number = input("Enter receiver's TG number or username: ")
    print(line)
    message = input("Enter Your message to send: ")
    print(line)
    import asyncio
    asyncio.run(send_message(phone_number, receiver_number, message))
