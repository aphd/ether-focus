import { createLineChart } from './line';
import data from '../../../server/json/unconfirmed-txs.json';

console.log(`message: ${JSON.stringify(data)}`);
createLineChart(data);

