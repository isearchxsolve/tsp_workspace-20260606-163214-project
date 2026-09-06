const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json());

app.get('/api/tsp', (req, res) => {
    // Placeholder for TSP algorithm
    res.send('Travelling Salesman Problem API');
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});