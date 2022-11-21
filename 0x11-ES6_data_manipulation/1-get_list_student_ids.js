export default function getListStudentIds(arr) {
  if (Array.isArray(arr)) {
    return (arr.map((item) => item.id));
  }

  return [];
};
