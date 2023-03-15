#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (character = 'X') {
    for (let i = this.height; i > 0; i--) {
      console.log(character.repeat(this.width));
    }
  }
}

module.exports = Square;
