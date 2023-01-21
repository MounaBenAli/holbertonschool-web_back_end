/* eslint-disable  no-nested-ternary */
function calculateNumber(type, a, b) {
  return type === 'SUM'
    ? Math.round(a) + Math.round(b)
    : type === 'SUBTRACT'
      ? Math.round(a) - Math.round(b)
      : type === 'DIVIDE' && Math.round(b) !== 0
        ? Math.round(a) / Math.round(b)
        : 'Error';
}
module.exports = calculateNumber;
