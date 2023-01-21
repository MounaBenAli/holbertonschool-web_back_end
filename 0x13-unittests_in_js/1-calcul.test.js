const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('type == SUM', () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
      assert.strictEqual(calculateNumber('SUM', 2, 3.7), 6);
      assert.strictEqual(calculateNumber('SUM', 1, -1), 0);
      assert.equal(calculateNumber('SUM', 0.4, 1.5), 2);
  });

  it('type == SUBTRACT', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
      assert.equal(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
      assert.equal(calculateNumber('SUBTRACT', 0.4, 1.6), -2);
      assert.strictEqual(calculateNumber('SUBTRACT', 4.5, 2), 3);
  });

  describe('type == DIVIDE', () => {
    describe('when b is not zero', () => {
      it('should return the division of the two numbers rounded to the nearest integer', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        assert.strictEqual(calculateNumber('DIVIDE', -1, 1), -1);
        assert.strictEqual(calculateNumber('DIVIDE', 0.0, 2), 0);
        assert.equal(calculateNumber('DIVIDE', 1.6, -4.6), -0.4);
      });
    });

    describe('when b is zero', () => {
      it('should return Error', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
      });
    });
  });

});