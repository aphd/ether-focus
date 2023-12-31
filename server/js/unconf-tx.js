const fs = require('node:fs').promises;
const CSV_FILE = `csv/main.eth.csv`;
const JSON_FILE = `json/unconfirmed-txs.json`;

const main = async () => {
	const data = await fs.readFile(CSV_FILE, 'utf8').catch((e) => (`${e}`));
	const rows = data.split(`\n`).slice(1, -1).sort(onSort);
	const unconfirmedTxs = rows.map(onRows).slice(-400);
	await fs.writeFile(JSON_FILE, JSON.stringify(unconfirmedTxs), 'utf8').catch((e) => (`${e}`));
};

const onSort = (a, b) => {
	const dateA = new Date(a.split(',')[3]).getTime();;
	const dateB = new Date(b.split(',')[3]).getTime();;
	return dateA - dateB;
}

const onRows = (e) => {
	const values = e.split(",");
	return {
		time: values[3]?.slice(0,16), 
		count: values[8], 
		high_gas_price: values[9], 
		low_gas_price: values[11],
		high_priority_fee: values[12],
		// medium_priority_fee,
		low_priority_fee: values[14],
		// base_fee
	}
}

main();
