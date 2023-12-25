const { createLineChart } = require('./line.js');
const data = require('../../../server/json/unconfirmed-txs.json');

createLineChart(data);

