function isTriangleNumber(number) {
  let layers = Math.ceil((2 * number) ** (1 / 2));
  // console.log(779  376 ** (1 / 2))
  return (layers * (layers + 1)) / 2 === number;

}

isTriangleNumber(3)
