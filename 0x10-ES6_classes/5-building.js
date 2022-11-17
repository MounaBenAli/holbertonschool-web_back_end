export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this.sqft = sqft;
  }

  // Setters & Getters for the attribute sqft
  set sqft(Nsqft) {
    this._sqft = Nsqft;
  }

  get sqft() { return this._sqft; }
}
