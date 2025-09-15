# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.15.3",
#     "fastecdsa==3.0.1"
# ]
# ///

"""Simplified implementation of digital signatures using the fastecdsa library."""

import marimo

__generated_with = "0.15.3"
app = marimo.App()

with app.setup:
    import fastecdsa.keys as keys
    from fastecdsa import ecdsa
    from fastecdsa.curve import secp256k1 as curve


@app.cell
def _():
    from hashlib import sha256

    private_key = keys.gen_private_key(curve)
    public_key = keys.get_public_key(private_key, curve)

    # We send the clear message...
    message = "I love this lecture"

    # standard signature, returns two integers
    r, s = ecdsa.sign(message, private_key, curve, hashfunc=sha256)
    print(r)
    print(s)

    # should return True as the signature we just generated is valid.
    valid = ecdsa.verify((r, s), message, public_key, curve, hashfunc=sha256)
    assert valid
    return


if __name__ == "__main__":
    app.run()
