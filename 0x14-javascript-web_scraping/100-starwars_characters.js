#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');

const id = argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body).characters;
    for (const key in data) {
      const peopleUrl = data[key];
      request(peopleUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
