//most of the basic code for websocket connection through python and js is copied at its base
// from Miguel Grinberg

const sio = io();

sio.on('connect', () => {
  console.log('connected');
  sio.emit('sum', {numbers: [1, 2]}, (result) => {
    console.log(result);
  });
});

sio.on('disconnect', () => {
  console.log('disconnected');
});

sio.on('mult', (data, cb) => {
  const result = data.numbers[0] * data.numbers[1];
  cb(result);
});