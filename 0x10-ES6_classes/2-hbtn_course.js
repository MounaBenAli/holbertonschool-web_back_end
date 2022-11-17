export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name; // string
    this.length = length; // number
    this.students = students; // array of strings
  }

  // Setters & Getters for the attribute name
  set name(Name) {
    if (typeof Name !== 'string') {
      throw TypeError('Name must be a string');
    } else {
      this._name = Name;
    }
  }

  get name() { return this._name; }

  // Setters & Getters for the attribute number
  set length(Length) {
    if (typeof Length !== 'number') {
      throw TypeError('Length must be a number');
    } else {
      this._length = Length;
    }
  }

  get length() { return this._length; }

  // Setters & Getters for the attribute students
  set students(Students) {
    if (Students.every((str) => typeof str !== 'string')) {
      throw TypeError('Students must be an array of strings');
    } else {
      this._students = Students;
    }
  }

  get students() { return this._students; }
}
