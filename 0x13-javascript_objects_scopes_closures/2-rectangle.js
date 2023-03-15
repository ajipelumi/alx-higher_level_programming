#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    // Check for positive w and h values
    if (w > 0 && h > 0) {
      this.width = w; // Initialize with the value of w
      this.height = h; // Initialize with the value of h
    }
  }
}

module.exports = Rectangle;
