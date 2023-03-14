#!/usr/bin/node
const argv = require('process').argv; // store command-line arguments

if (!argv[2]) {
  console.log('Missing size');
} else if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  // loop argv[2] times
  while (argv[2] > 0) {
    console.log('X' * argv[2]); // log argv[2] times
    argv[2]--; // decrement argv[2]
  }
}
