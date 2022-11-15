import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

const promise1 = signUpUser();
const promise2 = uploadPhoto();
const promises = [promise1, promise2];

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled(promises)
    .then((results) => results.forEach((result) => {
      console.log(
        ` status: ${result.status} `,
        ` value: ${result.value} `,
      );
    }));
}
