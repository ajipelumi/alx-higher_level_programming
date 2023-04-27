#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');

const id = argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, async (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body).characters;
    for (const key in data) {
      const peopleUrl = data[key];
      const peopleRes = await getRequest(peopleUrl);
      console.log(JSON.parse(peopleRes.body).name);
    }
  }
});

function getRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(response);
      }
    });
  });
}
