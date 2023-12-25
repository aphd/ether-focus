const { createLineChart } = require('./line.js');
const data = require('../../../server/json/unconfirmed-txs.json');

console.log(`message: ${JSON.stringify(data)}`);
createLineChart(data);

