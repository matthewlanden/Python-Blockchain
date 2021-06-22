
import hashlib
import json
from datetime import datetime




class Block:


    def __init__(self, model, year, sn, is_damaged):

        self.model = model
        self.year = year
        self.sn = sn
        self.is_damaged = is_damaged

        self.prev_block_hash = '1'*64
        self.nonce = 0
        self.hash = "0"*64

    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return str(self.__dict__)

    def make_hash(self):
        self.hash = hashlib.sha256(self.__str__().encode('utf-8')).hexdigest()
        return self.hash

    def set_prev_block_hash(self, prev_block_hash):
        self.prev_block_hash = prev_block_hash
    


