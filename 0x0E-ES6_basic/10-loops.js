export default function appendToEachArrayValue(array, appendString) {
  return array.map((val) => appendString + val);
}
