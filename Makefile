doc:
	cd client && yarn install && yarn build

unconf:
	cd server && yarn unconf

block:
	cd server && yarn block

waitingTxs:
	cd server && yarn waitingTime

waitingTxsByBlock:
	cd server && yarn waitingTimeByBlock

inflationDeflationTraker:
	cd server && yarn inflationDeflationTracker
