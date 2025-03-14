import fs from "node:fs/promises";

const CSV_PATH = `./csv/inflation-deflation.csv`;
const etherscanApiKey = "DSKSZSWHV6XVPK755G4392I6T22UXQTVFS";
const blockcypherApiUrl = "https://api.blockcypher.com/v1/eth/main/blocks/";
const etherscanApiUrl = "https://api.etherscan.io/api";

const fetchData = async (url) => {
    const response = await fetch(url);
    return await response.json();
};

// Get the Total Ethereum Supply from Etherscan
const getEthereumSupply = async () => {
    const url = `${etherscanApiUrl}?module=stats&action=ethsupply&apikey=${etherscanApiKey}`;
    const data = await fetchData(url);
    return data.result;
};

// Get Block Data from BlockCypher API
const getBlockData = async (blockNumber) => {
    const url = `${blockcypherApiUrl}${blockNumber}`;
    return await fetchData(url);
};

// Get Block Reward from Etherscan API
const getBlockReward = async (blockNumber) => {
    const url = `${etherscanApiUrl}?module=block&action=getblockreward&blockno=${blockNumber}&apikey=${etherscanApiKey}`;
    const data = await fetchData(url);
    return data.result.blockReward;
};

// Get the latest block number from Etherscan API
const getLatestBlockNumber = async () => {
    const url = `${etherscanApiUrl}?module=proxy&action=eth_blockNumber&apikey=${etherscanApiKey}`;
    const data = await fetchData(url);
    return parseInt(data.result, 16); // Convert hex to decimal
};

// Calculate Burnt Fees using BlockCypher's base_fee and gas used per transaction
const calculateBurntFees = async (blockNumber) => {
    const blockData = await getBlockData(blockNumber);
    const baseFee = blockData.base_fee;
    const totalGasUsed = blockData.n_tx * 21000; // Approximate gas used per transaction
    return totalGasUsed * baseFee;
};

// Main function to fetch data and write to CSV
const main = async () => {
    const blockNumber = await getLatestBlockNumber(); // Get the latest block number

    const totalEthereumSupply = await getEthereumSupply();
    const blockData = await getBlockData(blockNumber);
    const blockReward = await getBlockReward(blockNumber); // Fetching the block reward
    const burntFees = await calculateBurntFees(blockNumber);

    const data = {
        block_height: blockData.height,
        date: blockData.time,
        total_ethereum_supply: totalEthereumSupply,
        blockReward: blockReward, // Now we have the block reward
        totalFees: blockData.fees,
        burntFees: burntFees,
    };

    const csvContent = `${data.block_height},${data.date},${data.total_ethereum_supply},${data.blockReward},${data.totalFees},${data.burntFees}\n`;

    await fs.appendFile(CSV_PATH, csvContent, "utf8");

    console.log(`Data saved to ${CSV_PATH}`);
};

// Execute main function
main();