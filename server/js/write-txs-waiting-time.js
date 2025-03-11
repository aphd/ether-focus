import fs from "node:fs/promises";
import { TOKENs } from "./tokens.js";

const API_URL = "https://api.blockcypher.com/v1/eth/main/txs";
const PENDING_TXS_CSV_PATH = "server/csv/pending-txs.csv";
const WAITING_TIME_TXS_CSV_PATH = "server/csv/waiting-time-txs.csv";
const LINE_TO_PROCESS = 10;

const getPendingTransactions = async () => {
    const TOKEN = TOKENs[Math.floor(Math.random() * TOKENs.length)];
    const response = await fetch(`${API_URL}?token=${TOKEN}`);
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

    const transactions = await response.json();
    const pendingTxs = transactions.filter((tx) => tx.block_height === -1);
    return pendingTxs.map(({ hash, received }) => ({ hash, received }));
};

const getTransactionDetails = async (hash) => {
    const TOKEN = TOKENs[Math.floor(Math.random() * TOKENs.length)];
    const response = await fetch(`${API_URL}/${hash}?token=${TOKEN}`);
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

    return await response.json();
};

const savePendingTransactionsToCSV = async (pendingTxs) => {
    const csvData = pendingTxs.map(({ hash, received }) => `${hash},${received}`).join("\n") + "\n";
    await fs.appendFile(PENDING_TXS_CSV_PATH, csvData, "utf8");
    console.log(`Pending transactions appended to ${PENDING_TXS_CSV_PATH}`);
};

const processTransactions = async () => {
    const data = await fs.readFile(PENDING_TXS_CSV_PATH, "utf8");
    const lines = data.trim().split("\n");
    if (lines.length <= 1) return;

    const header = lines[0];
    const toProcess = lines.slice(1, LINE_TO_PROCESS + 1);
    const remaining = [header, ...lines.slice(LINE_TO_PROCESS + 1)];
    await fs.writeFile(PENDING_TXS_CSV_PATH, remaining.join("\n") + "\n", "utf8");

    for (const line of toProcess) {
        const [hash, received_origin] = line.split(",");
        const details = await getTransactionDetails(hash);
        const { block_height, confirmed, received, fees, gas_fee_cap, gas_price, gas_tip_cap, gas_used } = details;
        const csvEntry = `${block_height},${hash},${received_origin},${received},${confirmed},${fees},${gas_fee_cap},${gas_price},${gas_tip_cap},${gas_used}\n`;
        await fs.appendFile(WAITING_TIME_TXS_CSV_PATH, csvEntry, "utf8");
    }
};

const countLinesInFile = async (filePath) => {
    const data = await fs.readFile(filePath, "utf8");
    const pendingLines = data.trim().split("\n").length;
    console.log(`Lines in ${filePath}: ${pendingLines}`);

};

const main = async () => {
    const pendingTxs = await getPendingTransactions();
    await savePendingTransactionsToCSV(pendingTxs);
    await processTransactions();

    // TOOD print  how many line is made the file PENDING_TXS_CSV_PATH and WAITING_TIME_TXS_CSV_PATH
    await countLinesInFile(PENDING_TXS_CSV_PATH);
    await countLinesInFile(WAITING_TIME_TXS_CSV_PATH);
};

main();
