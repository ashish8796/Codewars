const Calculator = function () {
  this.evaluate = (string) => {
    function findPriority(s) {
      const priorityObj = {
        4: ["[", "{", "]", "}"],
        3: ["^"],
        2: ["*", "/"],
        1: ["+", "-"],
        0: ["("],
      };

      for (let key in priorityObj) {
        if (priorityObj[key].includes(s)) {
          return key;
        }
      }
    }

    function cal(arr) {
      let operatorObj = {
        "*": function (a, b) {
          return a * b;
        },
        "+": function (a, b) {
          return a + b;
        },
        "-": function (a, b) {
          return a - b;
        },
        "/": function (a, b) {
          return a / b;
        },
      };

      const stack = [];

      for (let i = 0; i < arr.length; i++) {
        if (arr[i].match(/[0-9]/) == null) {
          let x = Number(stack.pop());
          let y = Number(stack.pop());

          let val = operatorObj[arr[i]](y, x);
          stack.push(val);
        } else {
          stack.push(arr[i]);
        }
      }

      console.log(stack.pop());
      return stack.pop();
    }

    string = string.split(" ");

    if (string.length === 1) {
      return Number(string.pop());
    }

    const stack = [];
    const queue = [];

    let i = 0;

    while (string[i]) {
      if (string[i].match(/[0-9]/) !== null) {
        queue.push(string[i]);
      } else if (string[i] == "(") {
        stack.push(string[i]);
      } else if (string[i] == ")") {
        let x = stack.pop();

        while (x !== "(") {
          queue.push(x);

          x = stack.pop();
        }
      } else {
        while (
          findPriority(stack[stack.length - 1]) >= findPriority(string[i])
        ) {
          queue.push(stack.pop());
        }

        stack.push(string[i]);
      }

      console.log({ stack, queue });

      i++;
    }

    while (stack.length !== 0) {
      queue.push(stack.pop());
    }

    cal(queue);
  };
};

const calculate = new Calculator();

calculate.evaluate("72 * 35 + 94 / 42");
