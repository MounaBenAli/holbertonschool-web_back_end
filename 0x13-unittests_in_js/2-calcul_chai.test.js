/* eslint-disable jest/expect-expect */
const chai = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber type == SUM', () => {
  // eslint-disable-next-line jest/prefer-expect-assertions
  it('should return the sum of the two numbers rounded to the nearest integer', () => {
    chai.expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    chai.expect(calculateNumber('SUM', 2, 3.7)).to.equal(6);
    chai.expect(calculateNumber('SUM', 1, -1)).to.equal(0);
    chai.expect(calculateNumber('SUM', 0.4, 1.5)).to.equal(2);
  });
});

describe('calculateNumber type == SUBTRACT', () => {
  // eslint-disable-next-line jest/prefer-expect-assertions
  it('should return the difference of the two numbers rounded to the nearest integer', () => {
    chai.expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    chai.expect(calculateNumber('SUBTRACT', 1.5, 3.7)).to.equal(-2);
    chai.expect(calculateNumber('SUBTRACT', 0.4, 1.6)).to.equal(-2);
    chai.expect(calculateNumber('SUBTRACT', 4.5, 2)).to.equal(3);
  });
});

describe('calculateNumber type == DIVIDE', () => {
  // eslint-disable-next-line jest/prefer-expect-assertions
  it('should return the division of the two numbers rounded to the nearest integer', () => {
    chai.expect(calculateNumber('DIVIDE', 2, 2.5)).to.equal(0.6666666666666666);
    chai.expect(calculateNumber('DIVIDE', 0.0, 2)).to.equal(0);
    chai.expect(calculateNumber('DIVIDE', -1, 1)).to.equal(-1);
    chai.expect(calculateNumber('DIVIDE', 1, 0)).to.equal('Error');
  });
});
