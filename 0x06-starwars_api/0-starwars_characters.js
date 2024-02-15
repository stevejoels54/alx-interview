#!/usr/bin/node
const request = require('request');

const api = 'https://swapi-api.hbtn.io/api';
const id = process.argv[2];

request(`${api}/films/${id}`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  // get the characters
  const characters = JSON.parse(body).characters;
  // print each character
  characters.forEach((url) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
