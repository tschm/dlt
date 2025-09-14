# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.15.3"
#     "fastecdsa==3.0.1"
# ]
# ///

import marimo

__generated_with = "0.15.3"
app = marimo.App()

with app.setup:
    from fastecdsa import curve, keys
    import marimo as mo


@app.cell
def _():
    # generate a private key!
    private_key = keys.gen_private_key(curve.P521)
    return (private_key,)


@app.cell
def _(private_key):
    public_key = keys.get_public_key(private_key, curve.P521)
    return (public_key,)



@app.cell
def _(public_key):
    # The public key is a point
    public_key
    return


@app.cell
def _(private_key):
    # The public key is the nth of an elliptic curve where n is the private key
    private_key * curve.P521.G
    return


@app.cell
def _():
    # Given this public key you can not compute the private key!
    return


if __name__ == "__main__":
    app.run()
