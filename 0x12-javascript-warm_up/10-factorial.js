#!/usr/bin/node
const argv = require('process').argv; // store command-line arguments

function fact (num) {
  if (isNaN(num)) { // Passed argument is not a number
    return 1;
  } else if (num === 1) { // Base case
    return 1;
  } else {
    const result = num * fact(num - 1);
    return result;
  }
}

const n = parseInt(argv[2]); // Parse argument as int
const factorial = fact(n); // Find the factorial of n
console.log(factorial); // Print factorial
