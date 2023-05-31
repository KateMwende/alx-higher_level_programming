#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const dict = {};

  for (let i = 0; i < JSON.parse(body).length; i++) {
    const user = JSON.parse(body)[i].userId;
    const comp = JSON.parse(body)[i].completed;
    if (isNaN(dict[user]) && comp) {
      dict[user] = 1;
    } else if (comp) {
      dict[user] += 1;
    }
  }
  console.log(dict);
});
