import marimo

__generated_with = "0.15.3"
app = marimo.App()


@app.cell
def _():
    from fastecdsa import curve, keys
    return curve, keys


@app.cell
def _(curve, keys):
    # generate a private key!
    private_key = keys.gen_private_key(curve.P521)
    return (private_key,)


@app.cell
def _(curve, keys, private_key):
    public_key = keys.get_public_key(private_key, curve.P521)
    return (public_key,)


@app.cell
def _(private_key):
    # The private key is an integer
    private_key
    return


@app.cell
def _(public_key):
    # The public key is a point
    public_key
    return


@app.cell
def _(curve, private_key):
    # The public key is the nth of an elliptic curve where n is the private key
    private_key * curve.P521.G
    return


@app.cell
def _():
    # Given this public key you can not compute the private key!
    return


if __name__ == "__main__":
    app.run()
