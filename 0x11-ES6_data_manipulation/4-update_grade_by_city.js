export default function updateStudentGradeByCity(arr, city, newGrades) {
  const filteredbyCity = (arr.filter((item) => item.location === city));

  const map = filteredbyCity.map((element) => {
    const container = { ...element };

    const filteredbyId = newGrades.find((item) => item.studentId === element.id);
    if (filteredbyId) {
      container.id = element.id;
      container.firstName = element.firstName;
      container.location = element.location;
      container.grade = filteredbyId.grade;
    } else {
      container.grade = 'N/A';
    }

    return container;
  });
  return map;
}
