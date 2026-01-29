import asyncio
from telethon import TelegramClient, functions

api_id = 33539494
api_hash = '9884d0eab35ac1f2e352609dc4f6c827'
phone = '+79021923472'
client = TelegramClient('session_name', api_id, api_hash)

usernames = ['Your1Death']

async def main():
    await client.start(phone, password='sonyapidor')  # Пароль внутри функции!
    for target in usernames:
        try:
            user = await client.get_entity(target)
            await client(functions.messages.ReportRequest(
                peer=user,
                id=[0],
                reason=functions.InputReportReasonSpam(),
                message='Automated report.'
            ))
            print(f"Жалоба отправлена на {target}")
            await asyncio.sleep(5)
        except Exception as e:
            print(f"Ошибка с {target}: {e}")

asyncio.run(main())