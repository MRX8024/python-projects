from telethon import TelegramClient, events
import asyncio

# https://core.telegram.org/api/obtaining_api_id
API_ID =
API_HASH = ''
RESPONSE = 'Привет! Подготовь кошелек, щас пойдет жара!'

# async def main(x):
#     print('start')
#     responded_users = await x.get_dialogs()
#     for dialog in responded_users:
#         print(dialog.name, dialog.id)
#     x.run_until_disconnected()
#
# asyncio.run(main(client))

init = True
init_users = {}
client = TelegramClient(str(API_ID), API_ID, API_HASH)
client.start()
@client.on(events.NewMessage())
async def normal_handler(event):
    global init, init_users
    if init:
        ids = []
        init_users = await client.get_dialogs()
        for user in init_users:
            if str(user.message.peer_id).startswith('PeerUser'):
                ids.append(user.id)
        init_users = ids
        print(init_users)
        init = False
    elif event.is_private and event.message.peer_id.user_id not in init_users:
        print('Send message')
        await event.respond(RESPONSE)
        init_users.append(event.message.peer_id.user_id)
client.run_until_disconnected()
