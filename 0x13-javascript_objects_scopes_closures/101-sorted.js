#!/usr/bin/node
const dict = require('./101-data').dict;

const arr = Object.entries(dict); // Turn object to array
const arrValues = Object.values(dict); // Get the values in the object

// Sort and remove duplicate values
const sortArrValues = arrValues.filter((x, idx, arrValues) => {
  return (arrValues.indexOf(x) === idx); // Eliminates duplicate values
});

const newDict = {}; // Empty object to store result
for (const item of sortArrValues) {
  const list = []; // Empty array to store keys with the same values
  for (const [key, value] of arr) {
    if (value === item) { // Identical key is met
      list.push(key); // Add key to array
    }
  }
  newDict[item] = list; // Array is attached to item
}

console.log(newDict); // Print object
