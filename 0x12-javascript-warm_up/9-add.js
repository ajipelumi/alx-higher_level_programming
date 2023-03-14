#!/usr/bin/node
const argv = require('process').argv; // store command-line arguments

function add (a, b) {
  const result = a + b;
  return result;
}

const n1 = parseInt(argv[2]); // Parse first argument as int
const n2 = parseInt(argv[3]); // Parse second argument as int
const sum = add(n1, n2); // Add integers
console.log(sum); // Print sum
