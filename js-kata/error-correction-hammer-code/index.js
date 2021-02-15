function encode(text) {
  let s = text
    .split("")
    .map((s) => s.charCodeAt(0))
    .map((num) => {
      let r = num.toString(2);
      return r.length < 8 ? "0".repeat(8 - r.length) + r : r;
    })
    .map((s) =>
      s
        .split("")
        .map((ss) => (ss === "0" ? "0".repeat(3) : "1".repeat(3)))
        .join("")
    )
    .join("");

  // console.log(s);
  return s;
}

function decode(bits) {
  let strArr = [];
  for (let i = 0; i < bits.length; i += 3) {
    strArr.push(bits.substr(i, 3));
  }

  let newArr = strArr.map((s) =>
    s.split("").reduce((a, el) => (a += +el), 0) < 2 ? "0" : "1"
  );
  let res = newArr
    .map((_, i) => {
      if (i % 8 === 0) {
        return String.fromCharCode(
          parseInt(newArr.slice(i, i + 8).join(""), 2)
        );
      }
    })
    .filter((el) => el)
    .join("");
  // console.log({ strArr, newArr, res });
  return res;
}

let nAns = decode(
  "100111111000111001000010000111111000000111001111000111110110111000010111"
);

let ans = encode("hey");

let nRes = "hey";

let res =
  "000111111000111000000000000111111000000111000111000111111111111000000111";
console.log(ans === res);
console.log(nAns === nRes);
