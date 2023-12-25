const fs = require('node:fs').promises;
const {TOKENs} = require('./tokens');

const main = async () => {
	const FN = process.env.FN || `main.eth.csv`;
	const json = await getBlockcypher();
	await fs.appendFile(FN, `${Object.values(json).join(',')}\n`, 'utf8').catch((e) => (`${e}`));
};

const getBlockcypher = async () => {
	const TOKEN = TOKENs[Math.floor(Math.random() * TOKENs.length)];
    const url = `https://api.blockcypher.com/v1/eth/main?token=${TOKEN}`;
    const result = await fetch(url);
    return await result.json();
};
main();
