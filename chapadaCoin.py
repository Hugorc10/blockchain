import hashlib
import json


class Block():
    def __init__(self, nonce, tstamp, transaction, prevhash=''):
        self.nonce = nonce
        self.tstamp = tstamp
        self.transaction = transaction
        self.prevhash = prevhash
        self.hash = self.calcHash()

    def calcHash(self):
        block_string = json.dumps({"nonce": self.nonce, "tstamp": self.tstamp,
                                  "transation": self.transaction, "prevshash": self.prevhash}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self):
        string = "nonce: " + str(self.nonce) + "\n"
        string += "tstamp" + str(self.tstamp) + "\n"
        string += "transaction: " + str(self.transaction) + "\n"
        string += "prevhas " + str(self.prevhash) + "\n"
        string += "hash " + str(self.hash) + "\n"
        return string


class BlockChain():
    def __init__(self):
        self.chain = [self.generateGenesisBlock(), ]

    def generateGenesisBlock(self):
        return Block(0, ' 01/01/2017 ', 'Gensis Block')

    def getLastBlock(self):
        return self.chain[-1]

    def addBlock(self, newBlock):
        newBlock.prevhash = self.getLastBlock().hash
        newBlock.hash = newBlock.calcHash()
        self.chain.append(newBlock)

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            prevb = self.chain[i-1]
            currb = self.chain[i]
            if (currb.hash != currb.calcHash()):
                print("Invalid block")
                return False
            if (currb.prevhash != prevb.hash):
                print("Invalid chain")
                return False
        return True


chapadaCoin = BlockChain()
chapadaCoin.addBlock(Block(1, '20/05/2017', 100))
chapadaCoin.addBlock(Block(2, '21/05/2017', 20))
chapadaCoin.chain[1].transaction = 333
chapadaCoin.chain[1].hash = chapadaCoin.chain[1].calcHash()
for b in chapadaCoin.chain:
    print(b)
print(chapadaCoin.isChainValid())
