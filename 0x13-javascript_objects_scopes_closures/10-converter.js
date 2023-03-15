#!/usr/bin/node

exports.converter = function (base) {
  function numConvert (num) {
    return num.toString(base); // Return converted number
  }
  return numConvert; // Return numConvert function
};
