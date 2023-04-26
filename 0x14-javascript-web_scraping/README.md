The `request` module in JavaScript is a widely used library for making HTTP requests.
It provides a simple and flexible API for making HTTP requests to various endpoints.

Here is we can use request in JavaScript:
```javascript
const request = require('request');

request('https://www.example.com', function (error, response, body) {
  if (!error && response.statusCode == 200) {
    console.log(body);
  }
});
```

Working with **JSON (JavaScript Object Notation)** is an essential part of web development using JavaScript.
Here are some basic steps for working with JSON in JavaScript:

1. Parsing JSON: The `JSON.parse()` method is used to parse a JSON string and convert it into a JavaScript object.
```javascript
const jsonString = '{"name": "John", "age": 30}';
const jsonObj = JSON.parse(jsonString);
console.log(jsonObj.name); // Output: "John"
```

2. Accessing JSON data: We can access JSON data using dot notation or bracket notation.
```javascript
const jsonObj = {name: "John", age: 30};
console.log(jsonObj.name); // Output: "John"
console.log(jsonObj['age']); // Output: 30
```

We can also use the built-in `fs` module to read and write files.
Here are some examples of how to read and write a file using fs:

To read a file:
```javascript
const fs = require('fs');

fs.readFile('/path/to/file.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
```

To write to a file:
```javascript
const fs = require('fs');

fs.writeFile('/path/to/file.txt', 'Hello, World!', err => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('File written successfully!');
});
```
