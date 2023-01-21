export default function appendToEachArrayValue(array, appendString) {
  let arr = [];
  for (const val of array) {
    arr = [...arr, appendString + val];
  }
  return arr;
}
