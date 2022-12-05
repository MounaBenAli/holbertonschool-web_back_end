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

function setNewSchool(schoolName, value) {
  RedisClient.set(schoolName, value, (error, reply) => {
    redis.print(`Reply: ${reply}`);
  });
}

function displaySchoolValue(schoolName) {
  RedisClient.get(schoolName, (error, reply) => {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
