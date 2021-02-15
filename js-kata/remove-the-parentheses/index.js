function removeParentheses(s) {
  let n = s.length;
  let i = 0;
  let count = 0;
  let strArr = []
  while (n) {
    if (s[i] === ")") --count
    else if (s[i] === "(") ++count
    else {
      count == 0 && strArr.push(s[i])
    };
    ++i;
    --n;
  }
  console.log({ res: strArr.join("") })
  return strArr.join("")
}

removeParentheses("(first group) (second group) (third group)")