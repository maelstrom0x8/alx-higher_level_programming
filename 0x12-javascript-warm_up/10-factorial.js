#!/usr/bin/node

const [, , N] = process.argv;

if (isNaN(N)) {
  console.log(1);
} else {
  function factorial (num) {
    if (num === 0) { return 1; }
    return factorial(num - 1) * num;
  }

  console.log(factorial(N));
}
