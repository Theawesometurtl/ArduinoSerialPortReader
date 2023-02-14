from socketIO import sendMessage
import asyncio


loop = asyncio.get_event_loop()
loop.run_until_complete(sendMessage('hi, this is from another file'))
