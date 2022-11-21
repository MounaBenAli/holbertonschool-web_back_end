export default function getStudentsByLocation(arr, city) {
  return (arr.filter((item) => item.location === city));
}
