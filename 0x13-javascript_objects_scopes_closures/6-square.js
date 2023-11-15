#!/usr/bin/node

const Squaro = require('./5-square');

class Square extends Squaro {
  charPrint (char) {
    const c = char === undefined ? 'X' : char;

    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += c;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
