#!/usr/bin/node
const request = require('request');
const BASE_URL = 'https://swapi-api.alx-tools.com/api/films';
const mid = process.argv[2];
const endpoint = `${BASE_URL}/${mid}`;

request.get(endpoint, (err, res, content) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(content);
    console.log(data.title);
  } else {
    console.error(`Error: ${err}`);
  }
});
