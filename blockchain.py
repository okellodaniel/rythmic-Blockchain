import datetime as _dt
import hashlib as _hashlib
import json as _json

class Blockchain:
    def __init__(self) -> None:
        self.chain = list()
        genesis_block = self.create_genesis_block(data='I am the genesis block', proof=1, prevoius_hash='0', index=1)
    
    def create_genesis_block(self, data: str, proof: int, prevoius_hash: str, index:int) -> dict:
        block = {
                'index': index,
                'timestamp': str(_dt.datetime.now()),
                'data': data,
                'proof': proof,
                'previous_hash': prevoius_hash
                }
        
        return block
