/* eslint-disable jest/expect-expect */
/* eslint-disable jest/prefer-expect-assertions */
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('validate the usage of Utils.calculateNumber', () => {
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    sinon.assert.calledWith(calculateNumberSpy, 'SUM', 100, 20);
    calculateNumberSpy.restore();
  });
});
