#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0; // Declare count
  for (const idx in list) {
    // If searchElement is met
    if (list[idx] === searchElement) {
      count += 1; // Increment count
    }
  }
  return count; // Return number of occurences
};
