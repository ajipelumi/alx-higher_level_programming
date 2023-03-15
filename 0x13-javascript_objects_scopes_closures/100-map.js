#!/usr/bin/node
const list = require('./100-data').list;

const map1 = list.map((x, idx) => x * idx); // Multiply list item by index
console.log(list); // Print original list
console.log(map1); // Print new list
