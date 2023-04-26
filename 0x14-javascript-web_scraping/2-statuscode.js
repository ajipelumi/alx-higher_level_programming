#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');

const url = argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(`code: ${response.statusCode}`);
});
