// In this Kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.

// solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]

function solve(arr) {
  let uniqArr = [...new Set(arr)];
  let repeatArr = []
  for (let i = 0; i < uniqArr.length; i++) {
    let count = 0;
    for (let n = 0; n < arr.length; n++) {
      if (uniqArr[i] === arr[n]) count++;
    }
    repeatArr.push({ [uniqArr[i]]: count });
  }
  repeatArr.sort((obj1, obj2) => {
    // if()
    obj2[Object.keys(obj2)[0]] - obj1[Object.keys(obj1)[0]]
  })
  console.log(repeatArr)
}

solve([2, 3, 5, 3, 7, 9, 5, 3, 7])