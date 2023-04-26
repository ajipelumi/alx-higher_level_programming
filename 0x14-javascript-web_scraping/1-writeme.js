#!/usr/bin/node
const argv = require('process').argv;
const fs = require('fs');

const file = argv[2];
const content = argv[3];

fs.writeFile(file, content, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
