#!/usr/bin/node

const [, , ...args] = process.argv;

function max (arr) {
  let umax = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > umax) { umax = arr[i]; }
  }
  return umax;
}

const nmax = max(args);
const filter = args.filter((i, a) => { return i < nmax; });
console.log(max(filter));
