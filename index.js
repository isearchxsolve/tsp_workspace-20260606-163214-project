const tspSolver = require('./tspSolver');

const main = () => {
  const cities = [[0, 0], [10, 0], [5, 3], [0, 5]];
  const shortestPath = tspSolver(cities);
  console.log(shortestPath);
};

main();