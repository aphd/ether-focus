# Introduciton

[![BlockCypher](https://github.com/aphd/ether-focus/actions/workflows/block-schedule.yml/badge.svg)](https://github.com/aphd/ether-focus/actions/workflows/block-schedule.yml)

https://aphd.github.io/ether-focus/

# Analysis

```
cd analysis
```

# EIP-1559
1. Gas Price (prima di EIP-1559).
Nel sistema precedente (prima della EIP-1559), l'utente impostava un singolo valore, il gas price, che era il prezzo per unità di gas che l'utente era disposto a pagare. Più alto era il gas price, più velocemente la transazione veniva inclusa in un blocco, perché i miner tendevano a selezionare le transazioni con il gas price più alto per massimizzare il loro guadagno.


2. EIP-1559 e la separazione tra Base Fee e Priority Fee.   
Con l'introduzione della EIP-1559 (Ethereum Improvement Proposal 1559), il modello di commissione è stato modificato, separando la commissione in due componenti principali:
Base Fee: Una commissione di base che viene bruciata (cioè distrutta). La base fee è determinata dinamicamente dalla rete in base alla domanda di spazio nei blocchi. La base fee si adatta automaticamente in modo che la rete non sia né troppo congestionata né troppo vuota.
Priority Fee (tip): Una mancia che l'utente paga direttamente ai miner (o validatori nella rete Ethereum 2.0). Questo è l'importo che l'utente aggiunge per incentivare i miner a trattare la sua transazione come una priorità. L'utente può scegliere quanto "generosa" essere questa mancia.



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
