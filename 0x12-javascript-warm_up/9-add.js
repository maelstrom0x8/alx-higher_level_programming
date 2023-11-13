#!/usr/bin/node

const [, , first, second] = process.argv;

function add (a, b) {
  return a + b;
}

const fint = parseInt(first);
const sint = parseInt(second);

if (isNaN(fint) || isNaN(sint)) {
  console.log('NaN');
} else {
  console.log(add(fint, sint));
}
