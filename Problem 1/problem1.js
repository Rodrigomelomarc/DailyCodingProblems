const list = [10, 15, 3, 7];

function SumsList(k, list) {
  for (let i = 0; i < list.length; i++) {
    for (let j = i + 1; j < list.length; j++) {
      result = list[i] + list[j];
      if (result == k) {
        return true;
      }
    }
  }
  return false;
}

console.log(SumsList(35, list));
