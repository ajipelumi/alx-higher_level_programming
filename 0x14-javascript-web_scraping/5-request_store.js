#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');
const fs = require('fs');

const url = argv[2];
const file = argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(file, body, 'utf8', err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
