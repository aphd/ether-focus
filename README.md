# Introduciton

[![BlockCypher](https://github.com/aphd/ether-focus/actions/workflows/block-schedule.yml/badge.svg)](https://github.com/aphd/ether-focus/actions/workflows/block-schedule.yml)

https://aphd.github.io/ether-focus/

# Analysis

```
cd analysis
```

# CSV Table
Table describing each column in the provided CSV file.

| **Name**              | **Description**                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------------|
| **name**              | The name of the blockchain or network (e.g., `ETH.main`).                                            |
| **height**            | The block height (i.e., the index number of the block in the blockchain).                           |
| **hash**              | The unique hash of the current block, used to identify it (e.g., a SHA-256 hash).                   |
| **time**              | The timestamp when the block was mined or created, in ISO 8601 format.                             |
| **latest_url**        | URL linking to the current block's information via an API (e.g., BlockCypher).                     |
| **previous_hash**     | The hash of the previous block in the chain, linking the blocks together.                          |
| **previous_url**      | URL linking to the previous block's information via an API (e.g., BlockCypher).                    |
| **peer_count**        | The number of peers (nodes) connected to the blockchain network.                                    |
| **unconfirmed_count** | The number of unconfirmed transactions in the network waiting to be processed.                     |
| **high_gas_price**    | The highest gas price observed in the block, used for transaction processing priority.             |
| **medium_gas_price**  | The median gas price observed in the block, used for transaction processing priority.              |
| **low_gas_price**     | The lowest gas price observed in the block, used for transaction processing priority.              |
| **high_priority_fee** | The highest fee paid for high-priority transactions in the block.                                  |
| **medium_priority_fee** | The fee paid for medium-priority transactions in the block.                                      |
| **low_priority_fee**  | The fee paid for low-priority transactions in the block.                                           |
| **base_fee**          | The base transaction fee for the block, as per the Ethereum network’s EIP-1559 transaction model.   |
| **last_fork_height**  | The block height at which the most recent fork occurred in the Ethereum blockchain.                |
| **last_fork_hash**    | The hash of the block at which the most recent fork occurred in the Ethereum blockchain.           |
