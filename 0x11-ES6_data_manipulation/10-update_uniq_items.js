export default function updateUniqueItems(Updatedmap) {
  if (Updatedmap instanceof Map) {
    try {
      Updatedmap.forEach((key, value) => {
        if (key === 1) {
          Updatedmap.set(value, 100);
        }
      });
    } catch (e) {
      throw Error('Cannot process');
    }
  }
  return Updatedmap;
}
