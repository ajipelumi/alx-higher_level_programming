#!/usr/bin/node
let argv = require('process').argv;

if (!argv[2]) { // No argument passed
  console.log(0);
} else if (!argv[3]) { // One argument passed
  console.log(0);
} else {
  argv = argv.slice(2); // Shallow copy of array from index 2
  argv.sort((a, b) => a - b); // Sort in asceding order
  const len = argv.length; // Get array length
  console.log(argv[len - 2]); // Print second biggest integer
}
