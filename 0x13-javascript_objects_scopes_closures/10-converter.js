#!/usr/bin/node

exports.converter = function (base) {
  return (value) => {
    return parseInt(value, 10).toString(base);
  };
};
