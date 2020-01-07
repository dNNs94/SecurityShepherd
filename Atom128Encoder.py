# Found that Atom128 Encoding is used via: http://qbarbe.free.fr/crypto/eng_atom128d.php by trial and error
# Found at: https://sinister.ly/Thread-Source-Hazz15-Zong22-Megan35-Atom128 - 07.01.2020 19:55
# Modified for personal needs - credits to Deque

import base64


class Atom128Encoder:

    @staticmethod
    def encode(string):
        base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        atom128 = "/128GhIoPQROSTeUbADfgHijKLM+n0pFWXY456xyzB7=39VaqrstJklmNuZvwcdEC"
        lookup = dict(zip(base, atom128))
        b64 = base64.b64encode(string.encode('utf-8')).decode()
        result = "".join([lookup[x] for x in b64])
        return result

    @staticmethod
    def decode(cipher):
        base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        atom128 = "/128GhIoPQROSTeUbADfgHijKLM+n0pFWXY456xyzB7=39VaqrstJklmNuZvwcdEC"
        revlookup = dict(zip(atom128, base))
        b64 = "".join([revlookup[x] for x in cipher])
        result = base64.b64decode(b64)
        return result


def encode(string):
    encoder = Atom128Encoder()
    return encoder.encode(string)


def decode(cipher):
    try:
        encoder = Atom128Encoder()
        return encoder.decode(cipher)
    except KeyError:
        return "no valid encoding"
    except TypeError:
        return "no correct padding"
