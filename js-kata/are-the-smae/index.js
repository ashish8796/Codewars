let array1 = [121, 144, 19, 161, 19, 144, 19, 11];
let array2 = [231, 14641, 20736, 361, 25921, 361, 20736, 361];

function comp(array1, array2) {
  //return (array1.length && array2.length) && array1.every(el=> array2.includes(el**2))
  array1.forEach((el) => {
    array2.splice(array2.indexOf(el ** 2), 1);
  });
  console.log(array2);
  return array2.length > 0 ? false : true;
}

comp(array1, array2);
