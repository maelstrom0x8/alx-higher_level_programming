#!/usr/bin/node

const Squaro = require('./5-square');

class Square extends Squaro {
  charPrint = function (char) {
    const c = char || 'x';
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  };
}

module.exports = Square;
