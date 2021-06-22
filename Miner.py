
from BlockChain import BlockChain
from Block import Block


class Miner:

    def __init__(self, chain):
        self.chain:BlockChain = chain

    def mine(self, block:Block):

        difficulty = self.chain.difficulty
        last_block_hash = self.chain.get_last_block().hash

        block.set_prev_block_hash(last_block_hash)
        block_hash = block.make_hash()
        
        while not int(block_hash, 16) < 2**(256-difficulty):
            block.nonce += 1
            block_hash = block.make_hash()

        self.chain.add_to_chain(block)
        return True
        
        
