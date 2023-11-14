#!/usr/bin/node

const coll = require('./100-data.js').list;

const l = coll.map((e, k) => { return e * k; });
console.log(l);
