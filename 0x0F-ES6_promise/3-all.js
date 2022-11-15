import { uploadPhoto, createUser } from './utils';

const promise1 = uploadPhoto();
const promise2 = createUser();

function handleProfileSignup() {
  return Promise.all([promise1, promise2])
    .then((values) => { console.log(values[0].body, values[1].firstName, values[1].lastName); })
    .catch(() => { console.log('Signup system offline'); });
}

export default handleProfileSignup;
