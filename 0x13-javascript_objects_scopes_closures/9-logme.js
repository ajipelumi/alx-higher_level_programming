#!/usr/bin/node
let count = 0; // Initialize count

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count += 1;
};
