#!/usr/bin/node
const request = require('request');

const api = 'https://swapi-api.hbtn.io/api';
const id = process.argv[2];

request(`${api}/films/${id}`, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;

  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          console.log(JSON.parse(body).name);
          resolve(body);
        }
      });
    });
  }
});
