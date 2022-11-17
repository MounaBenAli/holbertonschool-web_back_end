import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft, sqft);
    this.floors = floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }

  // Setter & Getter for the attribute sqft
  set sqft(Nsqft) {
    this._sqft = Nsqft;
  }

  get sqft() { return this._sqft; }

  // Setter & Getter for the attribute floors
  set floors(Floors) {
    this._floors = Floors;
  }

  get floors() { return this._floors; }
}
