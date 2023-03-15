#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    // Check for positive w and h values
    if (w > 0 && h > 0) {
      this.width = w; // Initialize with the value of w
      this.height = h; // Initialize with the value of h
    }
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
