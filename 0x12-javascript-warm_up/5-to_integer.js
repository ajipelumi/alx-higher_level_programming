#!/usr/bin/node
const argv = require('process').argv;

if (!argv[2]) { // No arguments passed
  console.log('Not a number');
} else if (isNaN(argv[2])) { // Argument passed is not a number
  console.log('Not a number');
} else { // Convert to number with parseInt
  console.log(`My number: ${parseInt(argv[2])}`);
}
