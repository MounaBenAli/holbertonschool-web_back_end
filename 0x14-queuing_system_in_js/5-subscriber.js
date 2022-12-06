const redis = require('redis');

const subscriber = redis.createClient();

(async () => {
  await subscriber.connect();
})();

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

subscriber.subscribe('holberton school channel', (message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe('holberton school channel');
    subscriber.quit();
  }
});
