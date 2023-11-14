#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print = function () {
    for (let i = 0; i < this.height; i++) {
      console.log('x'.repeat(this.width));
    }
  };
}

module.exports = Rectangle;
