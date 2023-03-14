#!/usr/bin/node
exports.callMeMoby = function (num, func) {
  while (num > 0) { // Loop num times
    func(); // Call function
    num--; // Decrement num
  }
};
