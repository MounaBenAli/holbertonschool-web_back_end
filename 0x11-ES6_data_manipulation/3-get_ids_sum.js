export default function getStudentIdsSum(arr) {
  const initialValue = 0;
  const sum = (arr.reduce((accum, currentValue) => currentValue.id + accum, initialValue));
  return sum;
}
