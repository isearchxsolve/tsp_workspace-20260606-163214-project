function tspSolver(cities) {
  // Note: The Travelling Salesman Problem is NP-hard and cannot be solved in O(n) time complexity.
  // This implementation uses a nearest neighbor approach, which is a simple heuristic.
  const startCity = cities[0];
  const visited = new Set([startCity]);
  const path = [startCity];
  let currentCity = startCity;

  while (visited.size < cities.length) {
    let nearestCity = null;
    let minDistance = Infinity;

    for (const city of cities) {
      if (!visited.has(city)) {
        const distance = calculateDistance(currentCity, city);
        if (distance < minDistance) {
          minDistance = distance;
          nearestCity = city;
        }
      }
    }

    visited.add(nearestCity);
    path.push(nearestCity);
    currentCity = nearestCity;
  }

  return path;
}

function calculateDistance(city1, city2) {
  return Math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2);
}

module.exports = tspSolver;