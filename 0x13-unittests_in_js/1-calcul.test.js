const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber type == SUM', () => {
  it('should return the sum of the two numbers rounded to the nearest integer', () => {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    assert.strictEqual(calculateNumber('SUM', 2, 3.7), 6);
    assert.strictEqual(calculateNumber('SUM', 1, -1), 0);
    assert.strictEqual(calculateNumber('SUM', 0.4, 1.5), 2);
  });
});

describe('calculateNumber type == SUBTRACT', () => {
  it('should return the difference of the two numbers rounded to the nearest integer', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
    assert.strictEqual(calculateNumber('SUBTRACT', 0.4, 1.6), -2);
    assert.strictEqual(calculateNumber('SUBTRACT', 4.5, 2), 3);
  });
});

describe('calculateNumber type == DIVIDE', () => {
  it('should return the division of the two numbers rounded to the nearest integer', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 2, 2.5), 0.6666666666666666);
    assert.strictEqual(calculateNumber('DIVIDE', 0.0, 2), 0);
    assert.strictEqual(calculateNumber('DIVIDE', -1, 1), -1);
    assert.strictEqual(calculateNumber('DIVIDE', 1, 0), 'Error');
  });
});