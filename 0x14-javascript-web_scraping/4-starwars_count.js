#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');

const id = 18;
const url = argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    let count = 0;
    const data = JSON.parse(body).results;
    for (const key in data) {
      for (const item in data[key].characters) {
        if (data[key].characters[item].includes(`/people/${id}`)) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
