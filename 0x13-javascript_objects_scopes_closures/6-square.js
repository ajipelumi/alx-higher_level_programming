#!/usr/bin/node
const Square = require('./5-square');

class Square extends Square {
  const character = 'X';
	charPrint (character) {
	  for (let i = this.size; i > 0; i--) {
		console.log(character.repeat(this.size));
	  }
	}
}

module.exports = Square;
