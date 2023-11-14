#!/usr/bin/node

exports.esrever = function (list) {
  const rev = list.slice();

  for (let i = 0, j = rev.length - 1; i < j; i++, j--) {
    const temp = rev[i];
    rev[i] = rev[j];
    rev[j] = temp;
  }

  return rev;
};
