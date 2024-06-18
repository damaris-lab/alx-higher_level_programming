#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rowStr;
    for (let i = 0; i < this.height; i++) {
      rowStr = '';
      for (let j = 0; j < this.width; j++) {
        rowStr += 'X';
      }
      console.log(rowStr);
    }
  }
}
module.exports = Rectangle;
