#!/usr/bin/node
const argv = require('process').argv; // store command-line arguments

if (!argv[2]) {
  console.log('Missing number of occurrences');
} else {
  // loop argv[2] times
  while (argv[2] > 0) {
    console.log('C is fun');
    argv[2]--; // decrement argv[2]
  }
}
