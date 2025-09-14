# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.15.3",
#     "numpy==2.2.3",
#     "pandas>2.0",
#     "matplotlib==3.10.0"
# ]
# ///

"""Exploration of large numbers, binary/hexadecimal representations, and their applications in cryptography."""

import marimo

__generated_with = "0.15.3"
app = marimo.App()

with app.setup:
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    plt.style.use("seaborn-v0_8-whitegrid")


@app.cell
def _():
    # be careful here, the last element is never included
    np.arange(0, 5)
    return


@app.cell
def _():
    # first notice how this leads to an overflow (without any warning)
    np.power(2, np.arange(0, 65))
    return


@app.cell
def _():
    _grains = np.sum(np.power(2.0, np.arange(0, 256)))
    print(_grains)
    n = 20000 * 25 * 1000 * 50000.0
    print(n)
    print(_grains / n)
    print(np.log2(50000 * 1000 * 25))
    np.power(2.0, 34) / 20000
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
        I guess it's fair to say that powers of $2$ grow very fast. This is exponential growth in practice...
        We would need approximately $750000$ superships, each packed with $20000$ containers,
        each container packed with $25$ tons of rice.

        Annual production of rice in tons is $700 000 000$
        We would produce for the next 500 years at the current rate...
        """
    )
    return


@app.cell
def _():
    (np.power(2.0, 64) - 1) / (50000 * 1000 * 700000000)
    return


@app.cell
def _():
    _grains = np.power(2, 4) - 1
    print(_grains)
    print(hex(_grains))
    return


@app.cell
def _():
    integer = int("affe", 16)
    return (integer,)


@app.cell
def _(integer):
    bin(integer)
    hex(integer)
    integer
    return


@app.cell
def _():
    frame = pd.DataFrame(index=np.arange(0, 16))
    frame["binary"] = pd.Series({a: format(a, "0>4b") for a in frame.index})
    frame["hexadecimal"] = pd.Series({a: format(a, "0>1x") for a in frame.index})
    return (frame,)


@app.cell
def _(frame):
    frame
    return


@app.cell
def _():
    # It's trivial to convert any hashcode into a binary or decimal form...
    return


@app.cell
def _():
    # age of the universe in seconds
    # number of atoms in the universe
    # operations the world-fastest supercomputer can perform per second 200 petaflops = 200 * 10^15
    return


@app.cell
def _():
    # Every integer can be represented as binary, hexadecimal or decimal number. A hashcode is a hexadecimal number...
    # In fact, it's fair to say that typcially a hashcode is a large hexadecimal number.
    # Nevertheless, the range of possible hashcodes is finite!
    # So collisions do exist.
    # It's just very hard to find them. If you find them, we should write a paper together...
    # It's trivial to compute the hashcode of any given string...
    # It's kind of impossible to do the inverse (which does not exist as mapping is not injective)
    # but find one string that results in that hashcode
    # You would have to apply brute force
    # We are very interested in the problem of finding a hashcode below a given threshold,
    # that problem is already hard enough...
    # All collisions for simpler hash functions have been found using a birthday attack...
    return


if __name__ == "__main__":
    app.run()
