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

const KeyName = 'HolbertonSchools';
const values = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const [key, value] of Object.entries(values)) {
  RedisClient.hSet(KeyName, key, value, (error, reply) => console.log(`Reply: ${reply}`));
}

RedisClient.hGetAll(KeyName, (err, data) => console.log(data));
