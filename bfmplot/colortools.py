"""
Contains methods to convert hex colors to rgb colors
and to brighten/darken colors.
"""


import numpy as np

def h2r(_hex):
    """
    Convert a hex string to an RGB-tuple.
    """
    if _hex.startswith('#'):
        l = _hex[1:]
    else:
        l = _hex
    return [ a/255. for a in bytes.fromhex(l) ]

def r2h(rgb):
    """
    Convert an RGB-tuple to a hex string.
    """
    return '#%02x%02x%02x' % tuple([ int(a*255) for a in rgb ])

def tohex(color):
    """
    Convert any color to its hex string.
    """

    if type(color) == str:
        if len(color) in (6, 7):
            try:
                h2r(color)
                return color
            except:
                pass
        try:
            return hex_colors[color]
        except KeyError as e:
            raise ValueError("unknown color: '" + color +"'")
    elif type(color) in (list, tuple, np.ndarray) and len(color) == 3:
        return r2h(color)
    else:
        raise ValueError("Don't know how to interpret color " + str(color))

def torgb(color):
    """
    Convert any color to an rgb tuple.
    """

    if type(color) == str:
        if len(color) in (6, 7):
            try:
                return h2r(color)
            except:
                pass
        try:
            return colors[color]
        except KeyError as e:
            raise ValueError("unknown color: '" + str(color) +"'")
    elif type(color) in (list, tuple, np.ndarray) and len(color) == 3:
        return color
    else:
        raise ValueError("Don't know how to interpret color " + str(color))


def brighter(rgb,base=2):
    """
    Make the color (rgb-tuple) a tad brighter.
    """
    _rgb = tuple([ a**(1/base) for a in torgb(rgb) ])
    return _rgb

def darker(rgb,base=2):
    """
    Make the color (rgb-tuple) a tad darker.
    """
    _rgb = tuple([ (a)**base for a in torgb(rgb) ])
    return _rgb
