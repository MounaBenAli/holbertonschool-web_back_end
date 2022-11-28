const express = require('express');

const app = express();
const port = 1245;


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});


export default app;