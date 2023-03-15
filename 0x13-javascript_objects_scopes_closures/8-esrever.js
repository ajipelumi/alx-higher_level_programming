#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length; // Get list length
  const newList = []; // New list
  // Loop through list to store items in reverse
  for (let i = 0; i < list.length; i++) {
    newList[i] = list[len - 1];
    len--;
  }
  return newList; // Return reversed list
};
