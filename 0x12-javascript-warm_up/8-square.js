#!/usr/bin/node

const [, , size] = process.argv;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('x'.repeat(size));
  }
}
