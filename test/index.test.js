const nearestNeighbour = require('../index.js');

describe('nearestNeighbour', () => {
  it('should return the correct path', () => {
    const graph = [
      [0, 10, 15, 20],
      [10, 0, 35, 25],
      [15, 35, 0, 30],
      [20, 25, 30, 0]
    ];
    const expected = [0, 1, 3, 2, 0];
    expect(nearestNeighbour(graph)).toEqual(expected);
  });
});