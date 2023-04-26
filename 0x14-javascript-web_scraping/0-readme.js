#!/usr/bin/node
const argv = require('process').argv;
const fs = require('fs');

const file = argv[2];
fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
