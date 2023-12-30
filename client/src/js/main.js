const { createLineChart } = require('./line.js');
const { createGasPriceChart } = require('./gas-price.js');
const { createFeePriceChart } = require('./fee.js');
const data = require('../../../server/json/unconfirmed-txs.json');

createLineChart(data);
createGasPriceChart(data);
createFeePriceChart(data);

