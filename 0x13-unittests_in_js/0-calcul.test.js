const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('simple Math  Test', () => {
  it('should return round sum', () => {
    assert.strictEqual(calculateNumber(1.2, 2.5), 4);
    assert.strictEqual(calculateNumber(5.3, 3.5), 9);
    assert.strictEqual(calculateNumber(1.6, 3.5), 6);
    assert.strictEqual(calculateNumber(13.5, 0.9), 15);
  });
  it('if type input is str should return round sum', () => {
    assert.strictEqual(calculateNumber('1.2', '2.5'), 4);
    assert.strictEqual(calculateNumber('5.3', 3.5), 9);
    assert.strictEqual(calculateNumber(1.6, '3.5'), 6);
    assert.strictEqual(calculateNumber(true, 0.9), 2);
    assert.strictEqual(calculateNumber(false, 0.9), 1);
  });
});

