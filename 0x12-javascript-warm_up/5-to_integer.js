#!/usr/bin/node
const argv = require('process').argv;

if (!argv[2]) {
  console.log('Not a number');
} else if (typeof argv[2] === 'string' || typeof argv[2] === 'number') {
  console.log(`My number: ${argv[2]}`);
} else {
  console.log('Not a number');
}
