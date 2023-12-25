const fs = require('node:fs').promises;
const CSV_FILE = `csv/main.eth.csv`;
const JSON_FILE = `json/unconfirmed-txs.json`;

const main = async () => {
	const data = await fs.readFile(CSV_FILE, 'utf8').catch((e) => (`${e}`));
	const rows = data.split(`\n`).slice(1, -1);
	const unconfirmedTxs = rows.map(onRows).slice(-500);
	const r = await fs.writeFile(JSON_FILE, JSON.stringify(unconfirmedTxs), 'utf8').catch((e) => (`${e}`));
};

const onRows = (e) => {
	const values = e.split(",");
	return {time: values[3]?.slice(0,16), count: values[8]}
}

main();
