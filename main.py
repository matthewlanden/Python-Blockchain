from BlockChain import BlockChain
from Block import Block
from Miner import Miner

import threading
import random

chain = BlockChain()
miner = Miner(chain)


item2 = Block('Subaru', 2010, 322346523, False)

class minethread(threading.Thread):
    def run(self):
        for i in range(random.randint(10, 40)):
            item = Block('McLaren', 2020, i, False)
            miner.mine(item)
            
        

a = minethread(name='mining')
a.start()
b = minethread(name='mining')
b.start()
c = minethread(name='mining')
c.start()

        
