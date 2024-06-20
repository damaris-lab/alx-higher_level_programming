#!/usr/bin/node
const printSquare = (...args) => {
  const sizeArg = args[0];
  const size = parseInt(sizeArg, 10);

  if (isNaN(size)) {
    console.log("Missing size");
    return;
  }

  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
};
