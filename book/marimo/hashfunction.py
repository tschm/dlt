import marimo

__generated_with = "0.15.3"
app = marimo.App()


@app.cell
def _():
    import hashlib
    return (hashlib,)


@app.cell
def _():
    x = "HEC, Lausanne"
    return (x,)


@app.cell
def _(hashlib, x):
    hashlib.sha256(x.encode()).hexdigest()
    return


@app.cell
def _():
    # Compare with https://passwordsgenerator.net/sha256-hash-generator/
    return


if __name__ == "__main__":
    app.run()
