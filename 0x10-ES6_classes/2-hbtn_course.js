export default class HolbertonCourse {
  constructor(name, length, students) {
    // this._name = name; //string
    // this._length = length; //number
    // this._students = students; //array of strings

    if (typeof name !== 'string') {
      throw Error();
    } else {
      this.name = name;
    }

    if (typeof length !== 'number') {
      throw Error();
    } else {
      this._length = length;
    }

    if (students.every((str) => typeof str !== 'string')) {
      throw Error();
    } else {
      this._students = students;
    }
  }
}
