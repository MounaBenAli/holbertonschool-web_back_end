function handleResponseFromAPI(promise) {
  return new Promise((resolve, reject) => {
    // executor
    console.log('Got a response from the API');
    if (promise) {
      resolve({ status: 200, body: 'Success' });
    } else {
      reject(new Error());
    }
  });
}

export default handleResponseFromAPI;
