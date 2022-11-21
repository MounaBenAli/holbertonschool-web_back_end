export default function getStudentIdsSum(arr) {
  const initialValue = 0;
  const sum = (arr.reduce((accumulator, currentValue) => {
    return currentValue.id + accumulator}, initialValue));
  return sum;
};
