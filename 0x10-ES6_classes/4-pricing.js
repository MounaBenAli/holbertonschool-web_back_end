export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount; 
    this.currency = currency; 
  }

  // Setters & Getters for the attribute amount
  set amount(Amount) {
    this._amount = Amount;
  }

  get amount() { return this._amount; }

  // Setters & Getters for the attribute currency
  set currency(newCurrency) {
    this._currency = newCurrency;
  }

  get currency() { return this._currency; }

  // method displayFullPrice() Implementation
  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`;
  }

  // static method convertPrice() Implementation
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
};
