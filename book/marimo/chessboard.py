# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.15.3",
#     "mod==0.3.0"
# ]
# ///

"""Demonstration of the chessboard problem and binary/hexadecimal number representations."""

import marimo

__generated_with = "0.15.3"
app = marimo.App()

with app.setup:
    import marimo as mo
    from mod import Mod


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
        # Remember the grains on the Chessboard
        """
    )
    return


@app.cell
def _():
    c = int(2**64 - 1)
    return (c,)


@app.cell
def _(c):
    hex(c)
    return


@app.cell
def _():
    # Display hexadecimal representation
    print("Hexadecimal representation:")
    return


@app.cell
def _(c):
    bin(c)
    return


@app.cell
def _():
    11 % 5
    return


@app.cell
def _():
    Mod(11, 5)
    return


if __name__ == "__main__":
    app.run()
