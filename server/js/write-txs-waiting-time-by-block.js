import fs from "node:fs/promises";
import { TOKENs } from "./tokens.js";
import { getLatestBlockNumber } from "./utils/chain_utils.js";

const API_URL = "https://api.blockcypher.com/v1/eth/main";
const PENDING_TXS_CSV_PATH = "./csv/txs-by-block.csv";
const WAITING_TIME_TXS_CSV_PATH = "./csv/waiting-time-txs-by-block.csv";
const LINE_TO_PROCESS = 20;

const onError = (msg) => {
    throw new Error(msg);
};

// TODO update this to give you a block number betwen a fixded minimum and a maximum that correposnd to the last block appended to the blockchain
const getRandomBlockNum = async () => {
    const maxBlockNumber = await getLatestBlockNumber();
    const minBlockNumber = 10000000; // was mined on approximately May 4th, 2020 under a Proof-of-Work (PoW) consensus mechanism.
    return Math.floor(Math.random() * (maxBlockNumber - minBlockNumber + 1)) + minBlockNumber;
};

const getTxHashByBlock = async (blockNum) => {
    const TOKEN = TOKENs[Math.floor(Math.random() * TOKENs.length)];
    const response = await fetch(`${API_URL}/blocks/${blockNum}?token=${TOKEN}`);
    if (!response.ok) onError(`HTTP error! Status: ${response.status}`);
    const { txids } = await response.json();
    return txids;
};

const getTransactionDetails = async (hash) => {
    const TOKEN = TOKENs[Math.floor(Math.random() * TOKENs.length)];
    const url = `${API_URL}/txs/${hash}?token=${TOKEN}`;
    const response = await fetch(url).catch(onError);
    if (!response.ok) return {};
    return await response.json();
};

const savePendingTransactionsToCSV = async (pendingTxs, block) => {
    const csvData = pendingTxs.map((hash) => `${block},${hash}`).join("\n") + "\n";
    await fs.appendFile(PENDING_TXS_CSV_PATH, csvData, "utf8");
    console.log(`Pending transactions appended to ${PENDING_TXS_CSV_PATH}`);
};

const processTransaction = async (line) => {
    const [block_height, hash] = line.split(",");
    const details = await getTransactionDetails(hash);
    const { confirmed, received, fees, gas_fee_cap, gas_price, gas_tip_cap, gas_used } = details;
    const csvEntry = `${block_height},${hash},${received},${confirmed},${fees},${gas_fee_cap},${gas_price},${gas_tip_cap},${gas_used}\n`;
    await fs.appendFile(WAITING_TIME_TXS_CSV_PATH, csvEntry, "utf8");
};

const processTransactions = async () => {
    const data = await fs.readFile(PENDING_TXS_CSV_PATH, "utf8");
    const lines = data.trim().split("\n");
    if (lines.length <= 1) return;
    const header = lines[0];
    const toProcess = lines.slice(1, LINE_TO_PROCESS + 1);
    const remaining = [header, ...lines.slice(LINE_TO_PROCESS + 1)];
    await fs.writeFile(PENDING_TXS_CSV_PATH, remaining.join("\n") + "\n", "utf8");

    for (const line of toProcess) await processTransaction(line);
};

const countLinesInFile = async (filePath) => {
    const data = await fs.readFile(filePath, "utf8");
    const pendingLines = data.trim().split("\n").length;
    console.log(`Lines in ${filePath}: ${pendingLines}`);
};

const main = async () => {
    const blcokNumer = (await getRandomBlockNum()) + 1;
    console.log("blcokNumer:", blcokNumer);
    const txs = await getTxHashByBlock(blcokNumer);
    await savePendingTransactionsToCSV(txs, blcokNumer);
    await processTransactions();

    await countLinesInFile(PENDING_TXS_CSV_PATH);
    await countLinesInFile(WAITING_TIME_TXS_CSV_PATH);
};

main();
