export default class Currency {
  constructor(code, name) {
    this.code = code; // string
    this.name = name; // string
  }

  // Setters & Getters for the attribute code
  set code(Code) {
    this._code = Code;
  }

  get code() { return this._code; }

  // Setters & Getters for the attribute name
  set name(Name) {
    this._name = Name;
  }

  get name() { return this._name; }

  // method displayFullCurrency() Implementation
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
