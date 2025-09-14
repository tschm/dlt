# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.15.3",
#     "mod==0.3.0"
# ]
# ///

import marimo

__generated_with = "0.15.3"
app = marimo.App()

with app.setup:
    from mod import Mod

@app.cell(hide_code=True)
def _(mo):
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


app._unparsable_cell(
    r"""
    ??hex
    """,
    name="_"
)


@app.cell
def _(c):
    bin(c)
    return


@app.cell
def _():
    11 % 5
    return


@app.cell
def _(Mod):
    Mod(11, 5)
    return



if __name__ == "__main__":
    app.run()
