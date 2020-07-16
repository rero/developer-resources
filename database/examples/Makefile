Q := @

all: prepare
	$Qpipenv run ./02_SimpleRequest.py
	$Qpipenv run ./03_TransactionRequest.py

prepare: dependencies
	$Qpipenv run ./00_DatabaseCreation.py
	$Qpipenv run ./01_SimpleInsertion.py

dependencies:
	$Qpipenv install --ignore-pipfile

clean:
	$Qrm -f database.db
