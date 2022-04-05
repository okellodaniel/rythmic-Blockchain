import datetime as _dt
import hashlib as _hashlib
import json as _json

class Blockchain:
    def __init__(self) -> None:
        self.chain = list()
        genesis_block = self._create_block(data='I am the genesis block', proof=1, prevoius_hash='0', index=1)

        self.chain.append(genesis_block)

    def mine_block(self,data:str) -> dict:
        previous_block = self.get_previous_block()
        previous_proof = previous_block['proof']
        proof = None
        index = len(self.chain) + 1
    

    
    def _proof_pf_work(self,previos_proof: int,data: str, index:int) -> int:
        new_proof = 1
        check_proof = False
        while check_proof is False:

    def _to_digest(self,)        

    def get_previous_block(self)-> dict:
        return self.chain[-1]
    
    def _create_block(self, data: str, proof: int, prevoius_hash: str, index:int) -> dict:
        block = {
                'index': index,
                'timestamp': str(_dt.datetime.now()),
                'data': data,
                'proof': proof,
                'previous_hash': prevoius_hash
                }
        
        return block
