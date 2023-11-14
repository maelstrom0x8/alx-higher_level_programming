#!/usr/bin/node

exports.nbOccurences = function (coll, elem) {
  let count = 0;
  if (coll && elem) {
    for (const e of coll) {
      if (e === elem) { count += 1; }
    }
    return count;
  }
  return 0;
};
