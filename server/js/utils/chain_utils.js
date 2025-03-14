const etherscanApiUrl = "https://api.etherscan.io/api";
const etherscanApiKey = "DSKSZSWHV6XVPK755G4392I6T22UXQTVFS";

// Get the latest block number from Etherscan API
const getLatestBlockNumber = async () => {
    const url = `${etherscanApiUrl}?module=proxy&action=eth_blockNumber&apikey=${etherscanApiKey}`;
    const data = await fetchData(url);
    return parseInt(data.result, 16); // Convert hex to decimal
};

const fetchData = async (url) => {
    const response = await fetch(url);
    return await response.json();
};

export { getLatestBlockNumber, fetchData };
