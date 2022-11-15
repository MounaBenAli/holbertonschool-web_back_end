export default function uploadPhoto(filename) {
  Promise.reject(new Error(`${filename} cannot be processed`)).then(
    () => {

    },
    (error) => {
      console.error(error);
    },
  );
}
