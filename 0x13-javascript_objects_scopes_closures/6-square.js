#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call super to initialize size
  }

  charPrint (character = 'X') {
    for (let i = this.size; i > 0; i--) {
      console.log(character.repeat(this.size));
    }
  }
}

module.exports = Square;
