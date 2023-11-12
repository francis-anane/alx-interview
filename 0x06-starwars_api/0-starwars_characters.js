#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Retrieve the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API endpoint URL for the specified movie
const filmEndpoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;

// Arrays to store character URLs and names
let characterURLs = [];
const characterNames = [];

// Function to make an asynchronous request to get character URLs from the movie
const requestCharacterURLs = async () => {
  // Use a Promise to handle the asynchronous nature of the request
  await new Promise(resolve => {
    request(filmEndpoint, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        console.error('Error: ', err, '| StatusCode: ', res.statusCode);
      } else {
        // Parse the JSON response body
        const jsonBody = JSON.parse(body);
        // Extract character URLs from the movie
        characterURLs = jsonBody.characters;
        // Resolve the Promise to indicate completion
        resolve();
      }
    });
  });
};

// Function to make asynchronous requests to get character names from their URLs
const requestCharacterNames = async () => {
  // Check if there are characters to process
  if (characterURLs.length > 0) {
    // Iterate over each character URL
    for (const characterURL of characterURLs) {
      // Use a Promise to handle the asynchronous nature of the request
      await new Promise(resolve => {
        request(characterURL, (err, res, body) => {
          if (err || res.statusCode !== 200) {
            console.error('Error: ', err, '| StatusCode: ', res.statusCode);
          } else {
            // Parse the JSON response body
            const jsonBody = JSON.parse(body);
            // Extract character names from the response
            characterNames.push(jsonBody.name);
            // Resolve the Promise to indicate completion
            resolve();
          }
        });
      });
    }
  } else {
    console.error('Error: Got no characters for some reason');
  }
};

// Function to print character names to the console
const printCharacterNames = async () => {
  // Make asynchronous requests to get character URLs and names
  await requestCharacterURLs();
  await requestCharacterNames();

  // Iterate over each character name and print it to the console
  for (const name of characterNames) {
    // Determine whether to add a newline based on the position of the name in the array
    if (name === characterNames[characterNames.length - 1]) {
      process.stdout.write(name);
    } else {
      process.stdout.write(name + '\n');
    }
  }
};

// Invoke the function to print character names
printCharacterNames();

