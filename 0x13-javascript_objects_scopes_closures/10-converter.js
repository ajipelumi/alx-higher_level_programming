#!/usr/bin/node

exports.converter = function (base) {
  function numConvert (num) {
    let convertedNumber = ''; // Initialize string to store converted number
    while (num > 0) {
      let remainder = num % base; // Get remainder
      if (remainder > 9) { // Hex conversion
        const list = ['a', 'b', 'c', 'd', 'e', 'f'];
        remainder = list[remainder - 10];
      }
      convertedNumber += remainder; // Concatenate remainder to string
      num = Math.floor(num / base); // Divide num by base to continue loop
    }
    // Reverse string before returning
    convertedNumber = convertedNumber.split('').reverse().join('');
    return (convertedNumber || '0'); // Return converted number
  }
  return numConvert; // Return numConvert function
};
