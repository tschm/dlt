import marimo

__generated_with = "0.15.3"
app = marimo.App()


@app.cell
def _():
    # %matplotlib inline
    import matplotlib.pyplot as plt
    import numpy as np

    plt.style.use("seaborn-whitegrid")
    return np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We are solving the birthday problem using a Monte-Carlo simulation, e.g. given a class with $m$ members we run $n$ experiments and count those of them with duplicates. 
        """
    )
    return


@app.cell
def _(np):
    # function to detect if there are any duplicates in x
    def has_duplicates(x):
        """Check if the input sequence contains any duplicate elements.

        Args:
            x: A sequence (list, array, etc.) to check for duplicates

        Returns:
            bool: True if duplicates exist, False otherwise
        """
        # that's a standard trick in computer science, pump all entries of an array/vector/etc. into a set and count
        return not (len(x) == len(set(x)))


    def monte_carlo(m=5, n=100, s=np.arange(1, 366)):
        """Perform Monte Carlo simulation for the birthday paradox problem.

        Args:
            m: Number of people in each experiment (default: 5)
            n: Number of experiments to run (default: 100)
            s: Array of possible values to choose from (default: days of year 1-365)

        Returns:
            float: Probability of having at least one duplicate
        """
        # create a matrix of size experiments x m, where each element is picked from an array s
        a = np.random.choice(s, (n, m))
        # apply the function has_duplicates for each row
        return sum(np.apply_along_axis(func1d=has_duplicates, arr=a, axis=1)) / a.shape[0]
    return (monte_carlo,)


@app.cell
def _(monte_carlo, np):
    x = np.arange(1, 60)
    y = np.array([monte_carlo(m=a, n=5000) for a in x])

    # this isn't any faster but somewhat looks cleaner?
    f = np.vectorize(monte_carlo)
    y = f(x, n=5000)
    return x, y


@app.cell
def _(plt, x, y):
    plt.plot(x, y)
    plt.xlabel("Number of Elements")
    plt.ylabel("Probability of at least one duplicate")
    plt.title("Birthday Paradox")
    plt.show()
    return


@app.cell
def _():
    # For plotting in Python you could start here:
    # https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html

    # For the Birthday problem
    # https://en.wikipedia.org/wiki/Birthday_problem
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
