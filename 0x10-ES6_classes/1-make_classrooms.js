import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const C1 = new ClassRoom(19);
  const C2 = new ClassRoom(20);
  const C3 = new ClassRoom(34);
  return [C1, C2, C3];
}
