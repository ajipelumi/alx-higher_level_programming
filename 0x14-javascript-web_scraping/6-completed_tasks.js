#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');

const url = argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const count = {};
    let id = 1;
    for (const key in data) {
      if (data[key].userId === id) {
        if (data[key].completed) {
          count[id] = count[id] ? count[id] + 1 : 1;
        }
      } else {
        id += 1;
      }
    }
    console.log(count);
  }
});
