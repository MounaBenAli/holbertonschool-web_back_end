const redis = require('redis');

const RedisClient = redis.createClient();

(async () => {
  await RedisClient.connect();
})();

RedisClient.on('ready', () => {
  console.log('Redis client connected to the server');
});

RedisClient.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});
