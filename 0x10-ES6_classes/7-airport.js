export default class Airport {
  constructor(name, code) {
    this._name = name; // string
    this._code = code; // string
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
