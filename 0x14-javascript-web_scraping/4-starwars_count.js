#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (err, res, body) {
  if (!err) {
    const res = JSON.parse(body).results;
    const moviesWithWedge = res.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0);

    console.log(moviesWithWedge);
  }
});
