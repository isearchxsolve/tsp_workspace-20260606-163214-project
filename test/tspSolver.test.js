const tspSolver = require('../tspSolver');

describe('tspSolver', () => {
  it('should return a path', () => {
    const cities = [[0, 0], [10, 0], [5, 3], [0, 5]];
    const shortestPath = tspSolver(cities);
    expect(shortestPath).toBeInstanceOf(Array);
  });

  it('should return a path with the correct length', () => {
    const cities = [[0, 0], [10, 0], [5, 3], [0, 5]];
    const shortestPath = tspSolver(cities);
    expect(shortestPath.length).toBe(cities.length);
  });
});