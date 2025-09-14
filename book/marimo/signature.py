import marimo

__generated_with = "0.15.3"
app = marimo.App()


@app.cell
def _():
    import hashlib

    from fastecdsa import keys
    from fastecdsa.curve import secp256k1 as curve
    from mod import Mod
    return Mod, curve, hashlib, keys


@app.cell
def _(hashlib):
    # every message needs to be hashed into a number
    def encryptstring(hashstr):
        """Convert a string message into a numeric hash value.

        Args:
            hashstr: The string to be hashed

        Returns:
            int: The numeric representation of the SHA-256 hash of the input string
        """
        return int(hashlib.sha256(hashstr.encode()).hexdigest(), 16)
    return (encryptstring,)


@app.cell
def _(curve, keys):
    # The private key is a random number from [ 1 , p − 1 ] where
    # p is the order of the underlying Galoisfield
    privatekey = keys.gen_private_key(curve)

    # The publickey is
    publickey = curve.G * privatekey
    return privatekey, publickey


@app.cell
def _(curve):
    # There are n solutions on the elliptic curve
    # including the point at ”infinity”
    n = curve.q

    # We send the clear message . . .
    message = "I love this lecture"
    return message, n


@app.cell
def _(curve, keys):
    # nonce
    i = keys.gen_private_key(curve)
    print(type(i))
    # nonce on elliptic curve
    P = curve.G * i
    return P, i


@app.cell
def _(Mod, P, encryptstring, i, message, n, privatekey):
    # compute the signature
    r = Mod(P.x, n)
    inv_i = Mod(i, n).inverse

    s = (inv_i * (encryptstring(message) + r * privatekey))._value
    return r, s


@app.cell
def _(Mod, encryptstring, message, n, r, s):
    # The sender transmits (r,s) , the clear message and his public key
    # s depends on the private key and the hashcode of the message.
    # However it is not possible to extract the private key from s

    # check the signature
    w = Mod(s, n).inverse
    u1 = encryptstring(message) * w
    u2 = r * w
    return u1, u2


@app.cell
def _(curve, publickey, r, u1, u2):
    # addition of two residue classes and multiplication with Point
    (curve.G * u1._value + publickey * u2._value).x == r
    return


if __name__ == "__main__":
    app.run()
