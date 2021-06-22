from Block import Block

class BlockChain:
    
    def __init__(self):
        self.chain = []
        self.pool = []
        self.difficulty = 10
        self.genosis = self.get_genosis()

    def get_genosis(self):
        gen = Block('', 0, 0, False)
        gen.prev_block_hash = '0'*64
        gen.hash = '0'*64
        self.chain.append(gen)
        return gen

    def get_last_block(self):
        return self.chain[-1]

    def proof_of_work(self, block:Block):
        print((int(block.hash, 16) < 2**(256-self.difficulty)) and (block.prev_block_hash == self.get_last_block().hash))
        return (int(block.hash, 16) < 2**(256-self.difficulty) and (block.prev_block_hash == self.get_last_block().hash))

    def add_to_chain(self, block:Block):
        if self.proof_of_work(block):
            self.chain.append(block)
        else: print('not added')



