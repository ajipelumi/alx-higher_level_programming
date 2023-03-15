#!/usr/bin/node
const argv = require('process').argv;
const fs = require('fs');

let str = ''; // Declare string to store content

// Read first file
fs.readFile(argv[2], 'utf8', (err, data) => {
  if (err) throw err; // Encounters error
  str = data; // Store content in str

  // Read second file
  fs.readFile(argv[3], 'utf8', (err, data) => {
    if (err) throw err; // Encounters error
    str += data; // Concatenate content to str

    // Write into destination file
    fs.writeFile(argv[4], str, 'utf8', (err) => {
      if (err) throw err; // Encounters error
    });
  });
});
