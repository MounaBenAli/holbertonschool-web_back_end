export default class HolbertonClass {
  constructor(size, location) {
    this._size = size; // number
    this._location = location; // string
  }

  valueOf() { return this._size; }

  toString() { return this._location; }
}
