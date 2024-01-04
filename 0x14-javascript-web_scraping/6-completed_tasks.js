#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completed = tasks.filter((task) => task.completed);
    const userCompleted = completed.reduce((countByUser, task) => {
      countByUser[task.userId] = (countByUser[task.userId] || 0) + 1;
      return countByUser;
    }, {});

    console.log(userCompleted);
  } else {
    console.error(`Error: ${error}`);
  }
});
