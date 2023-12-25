import { createLineChart } from './line';
import data from '../json/main.json';

console.log(`message: ${JSON.stringify(data)}`);
createLineChart(data);

