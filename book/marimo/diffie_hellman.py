# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.15.3",
#     "numpy==2.2.3",
#     "pandas>2.0"
# ]
# ///

import marimo

__generated_with = "0.15.3"
app = marimo.App()

with app.setup:
    import numpy as np
    import pandas as pd

@app.cell
def _():
    class Person:
        """Represents a participant in the Diffie-Hellman key exchange protocol."""

        def __init__(self, n):
            """Initialize a person with a random secret number.

            Args:
                n: Upper bound for the random secret (exclusive)
            """
            self.__secret = np.random.choice(np.arange(1, n))
    return Person


@app.cell
def _(Person):
    alice = Person(5)
    return


@app.cell
def _(Person):
    bob = Person(5)
    return


@app.cell
def _():
    np.random.choice(5)
    return


@app.cell
def _():
    np.random.choice(np.arange(1, 5))
    return


@app.cell
def _():
    # Pick a prime number
    p = 7
    n = 3
    return (p,)


@app.cell
def _(p):
    index = np.arange(0, p + 1)
    a = pd.DataFrame(index=index, data=3, columns=["n"])
    a
    return (a,)


@app.cell
def _(a):
    a["power"] = a.index
    return


@app.cell
def _(a):
    a
    return


@app.cell
def _(a):
    a["n^power"] = np.power(a["n"], a["power"])
    return


@app.cell
def _(a):
    a
    return


@app.cell
def _(a):
    a["n^power mod power"] = np.mod(a["n^power"], 7)
    return


@app.cell
def _(a):
    a
    return


if __name__ == "__main__":
    app.run()
