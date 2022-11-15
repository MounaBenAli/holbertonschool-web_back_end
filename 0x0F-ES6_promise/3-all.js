import { createUser, uploadPhoto } from './utils';

function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((values) => { console.log(values[0].body, values[1].firstName, values[1].lastName); })
    .catch(() => { console.log('Signup system offline'); });
}
export default handleProfileSignup;
