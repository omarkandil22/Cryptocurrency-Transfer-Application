# Cryptocurrency Transfer Application

<div style="display:block;margin:auto;height:80%;width:80%">
  <img src="blockchain-simulation.gif">
</div>

The github repository contains a basic implementation of a blockchain and its client using Python. This blockchain has the following features:

- Possibility of adding multiple nodes to the blockchain
- Proof of Work (PoW)
- Simple conflict resolution between nodes
- Transactions

The blockchain client has the following features:

- Generation of transactions. 

This github repository also contains 2 dashboards: 

- "Blockchain Frontend" for miners. 
- "Blockchain Client" for users to send transactions. 


# Dependencies

- Works with ```Python 3.8.8``` 

# Installation

1. install [python](https://www.python.org/downloads/)
2. install required packages:
    ```pip install requests```
    ```pip install flask```
    ```pip install flask-core```
3. install [git](https://git-scm.com/downloads)
4. download the code from Github
    ```git clone https://github.com/omarkandil22/Cryptocurrency-Transfer-Application.git```

# How to run the code

1. To start a blockchain node, go to ```blockchain``` folder and execute the command below:
```python blockchain.py -p 5000```
2. You can add a new node to blockchain by executing the same command and specifying a port that is not already used. For example, ```python blockchain.py -p 5001```
3. TO start the blockchain client, go to ```blockchain_client``` folder and execute the command below:
```python blockchain_client.py -p 8080```
4. You can access the blockchain frontend and blockchain client dashboards from your browser by going to localhost:5000 and localhost:8080
