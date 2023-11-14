#!/usr/bin/node

let count = 0;

exports.logMe = function (arg) {
  console.log(`${count}: ${arg}`);
  count += 1;
};
