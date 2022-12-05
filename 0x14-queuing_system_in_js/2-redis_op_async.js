const redis = require('redis');

const RedisClient = redis.createClient();
const { promisify } = require('util');

const getAsync = promisify(RedisClient.get).bind(RedisClient);

(async () => {
  await RedisClient.connect();
})();

RedisClient.on('ready', () => {
  console.log('Redis client connected to the server');
});

RedisClient.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
  RedisClient.set(schoolName, value, (error, reply) => {
    redis.print(`Reply: ${reply}`);
  });
}

async function displaySchoolValue(schoolName) {
  const reply = await getAsync(schoolName);
  console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

/// //
