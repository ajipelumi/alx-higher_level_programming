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
    for (const key in data) {
      const userId = data[key].userId;
      const completed = data[key].completed;
      if (completed) {
        count[userId] = count[userId] ? count[userId] + 1 : 1;
      }
    }
    console.log(count);
  }
});
