import marimo

__generated_with = "0.15.3"
app = marimo.App()


@app.cell
def _():
    import numpy as np


    class Person:
        """Represents a participant in the Diffie-Hellman key exchange protocol."""

        def __init__(self, n):
            """Initialize a person with a random secret number.

            Args:
                n: Upper bound for the random secret (exclusive)
            """
            self.__secret = np.random.choice(np.arange(1, n))
    return Person, np


@app.cell
def _(Person):
    alice = Person(5)
    return


@app.cell
def _(Person):
    bob = Person(5)
    return


@app.cell
def _(np):
    np.random.choose(5)
    return


@app.cell
def _(np):
    np.random.choice(np.arange(1, 5))
    return


@app.cell
def _():
    # Pick a prime number
    p = 7
    n = 3
    return (p,)


@app.cell
def _(np, p):
    import pandas as pd

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
def _(a, np):
    a["n^power"] = np.power(a["n"], a["power"])
    return


@app.cell
def _(a):
    a
    return


@app.cell
def _(a, np):
    a["n^power mod power"] = np.mod(a["n^power"], 7)
    return


@app.cell
def _(a):
    a
    return


if __name__ == "__main__":
    app.run()
