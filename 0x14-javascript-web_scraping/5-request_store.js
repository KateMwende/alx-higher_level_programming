#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];

request(url, (error, reponse, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
