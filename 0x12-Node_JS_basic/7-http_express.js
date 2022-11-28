const express = require('express');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.send('This is the list of our students');
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});

module.exports = app;
