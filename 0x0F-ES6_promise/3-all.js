import { uploadPhoto, createUser } from './utils';

const promise1 = uploadPhoto();
const promise2 = createUser();

function handleProfileSignup() {
  Promise.all([promise1, promise2])
    .then((values) => console.log(values[0].body, values[1].firstName, values[1].lastName))
    .catch(() => new Error('Signup system offline'))
    .finally(() => {});
}

export default handleProfileSignup;
