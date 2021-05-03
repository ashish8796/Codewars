function numberOfPairs(gloves) {
  let gloveObj = {};

  gloves.forEach((glove) => {
    gloveObj[glove] = gloveObj[glove] ? ++gloveObj[glove] : 1;
    console.log(gloveObj);
  });

  return (num = Object.values(gloveObj).reduce(
    (acc, cv) => acc + (cv - (cv % 2)) / 2,
    0
  ));
}

numberOfPairs(["gray", "black", "purple", "purple", "gray", "black"]);
