function DI(dependency) {
  this.dependency = dependency;
  this.inject = function (callback) {
    const obj = this.dependency;
    return function () {
      let str = callback.toString();
      let argu = str.slice(str.indexOf("(") + 1, str.indexOf(")")).split(", ");
      let funcArr = argu.map((el) => obj[el]).filter((el) => el);
      return callback(...funcArr);
    }.bind(obj);
  };
}

var deps = {
  dep1: function () {
    return "this is dep1";
  },
  dep2: function () {
    return "this is dep2";
  },
  dep3: function () {
    return "this is dep3";
  },
  dep4: function () {
    return "this is dep4";
  },
};

const di = new DI(deps);

const myFunc = di.inject(function (dep3, dep1, dep2) {
  return [dep1(), dep2(), dep3()].join(" -> ");
});
myFunc();
console.log(myFunc());
