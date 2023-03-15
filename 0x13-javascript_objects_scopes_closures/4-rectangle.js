#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    // Check for positive w and h values
    if (w > 0 && h > 0) {
      this.width = w; // Initialize with the value of w
      this.height = h; // Initialize with the value of h
    }
  }

  // Exchanges the width and the height
  rotate () {
    // Swap attributes
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Multiplies width and height by 2
  double () {
    this.width *= 2; // Multiply width by 2
    this.height *= 2; // Multiply height by 2
  }

  // Prints the rectangle using the character 'X'
  print () {
    // Loop height times
    for (let i = this.height; i > 0; i--) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
