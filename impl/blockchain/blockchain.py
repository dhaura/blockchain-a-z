# Blockchain Implementation

import datetime
import hashlib
import json
from flask import Flask, jsonify

'''
*
* Class that defines the blockchain.
*
'''


def proof_of_work(prev_proof):
    new_proof = 1
    is_proof_found = False

    while not is_proof_found:
        hash_op = hashlib.sha256(str(new_proof**2 - prev_proof**2).encode()).hexdigest()
        if hash_op[:4] == '0000':
            is_proof_found = True
        else:
            new_proof += 1

    return new_proof


def get_hash(block):
    encoded_block = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(encoded_block).hexdigest()


def is_chain_valid(chain):
    prev_block = chain[0]
    block_index = 1

    while block_index < len(chain):
        block = chain[block_index]
        if block['previous_hash'] != get_hash(prev_block):
            return False
        prev_proof = prev_block['proof']
        proof = block['proof']
        hash_op = hashlib.sha256(str(proof**2 - prev_proof**2).encode()).hexdigest()
        if hash_op[:4] != '0000':
            return False
        prev_block = block
        block_index += 1

    return True


class Blockchain:

    def __int__(self):
        self.chain = []
        self.create_block(proof=1, prev_hash='0')

    def create_block(self, proof, prev_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': prev_hash
        }
        self.chain.append(block)
        return block

    def get_prev_block(self):
        return self.chain[-1]

