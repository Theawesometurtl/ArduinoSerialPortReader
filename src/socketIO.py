import socketio

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '/': './src/public/'
})


async def sendMessage(message):
    await sio.emit('message', message)
    print('this ran')

    
@sio.event
async def sum(sid, data):
    result = data['numbers'][0] + data['numbers'][1]
    return {'result': result}

@sio.event
async def connect(sid, environ):
    print(sid, 'connected')


@sio.event
async def disconnect(sid):
    print(sid, 'disconnected')


