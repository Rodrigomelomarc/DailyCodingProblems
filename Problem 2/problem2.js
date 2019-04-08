const numbers = [1, 2, 3, 4, 5];

function solve(arr) {
  const newArr = [];
  for (i = 0; i < arr.length; i++) {
    let aux = arr[i];
    delete arr[i];
    newArr[i] = arr.reduce((a, b) => a * b);
    arr[i] = aux;
  }
  return console.log(newArr);
}

solve(numbers);
