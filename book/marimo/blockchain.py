# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.15.3"
# ]
# ///

"""Implementation of a simple blockchain with blocks linked by cryptographic hashes."""

import marimo

__generated_with = "0.15.3"
app = marimo.App()


@app.cell
def _():
    import json
    from hashlib import sha256

    class Block:
        """Represents a block in a blockchain with message, timestamp, and reference to previous block."""

        def __init__(self, message, time, reference=None):
            """Initialize a new Block.

            Args:
                message: Content of the block
                time: Timestamp of the block
                reference: Hash of the previous block (None for genesis block)
            """
            self.message = message
            self.time = time
            self.reference = reference

        @property
        def hash(self):
            """Calculate the hash of this block based on its contents.

            Returns:
                str: SHA-256 hash of the block's contents
            """
            x = {"message": self.message, "time": self.time, "reference": self.reference}
            return sha256(json.dumps(x).encode()).hexdigest()

    class Chain:
        """Represents a blockchain - a sequence of linked blocks."""

        def __init__(self):
            """Initialize a new empty blockchain."""
            self.__chain = []

        def append(self, message, time):
            """Add a new block to the chain.

            Args:
                message: Content for the new block
                time: Timestamp for the new block
            """
            # append a block to the chain

            # if there is at least one block in the chain
            if len(self.__chain) >= 1:
                # compute the hash digest of the last block
                reference = self.__chain[-1].hash
            else:
                reference = None

            # compute the Block
            block = Block(message=message, time=time, reference=reference)

            # append it to the chain
            self.__chain.append(block)

        def __getitem__(self, item):
            """Access a block in the chain by index.

            Args:
                item: Index of the block to retrieve

            Returns:
                Block: The requested block
            """
            return self.__chain[item]

        @property
        def valid(self):
            """Check if the blockchain is valid by verifying all block references.

            Returns:
                bool: True if the chain is valid, False otherwise
            """
            for a, b in zip(self.__chain[:-1], self.__chain[1:]):
                if a.hash != b.reference:
                    return False

            return True

    return (Chain,)


@app.cell
def _(Chain):
    chain = Chain()
    chain.append(message="A", time=1)
    chain.append(message="B", time=2)
    chain.append(message="C", time=3)
    chain.append(message="D", time=4)

    # the chain is valid because the recomputed hash code
    # for block n is matching the reference in block n+1
    assert chain.valid

    # we chain the message of the 3rd block
    # and therefore the hash code for Block 3
    # is not matching the reference in Block 4
    chain[2].message = "Thomas was here"
    assert not chain.valid
    return


if __name__ == "__main__":
    app.run()
