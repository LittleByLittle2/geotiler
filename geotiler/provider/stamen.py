﻿"""
>>> p = BaseProvider('toner')
>>> p.getTileUrls(Coordinate(25322, 10507, 16)) #doctest: +ELLIPSIS
('http://tile.stamen.com/toner/16/10507/25322.png',)

>>> p = TonerProvider()
>>> p.getTileUrls(Coordinate(25322, 10507, 16)) #doctest: +ELLIPSIS
('http://tile.stamen.com/toner/16/10507/25322.png',)

>>> p = TerrainProvider()
>>> p.getTileUrls(Coordinate(25322, 10507, 16)) #doctest: +ELLIPSIS
('http://tile.stamen.com/terrain/16/10507/25322.png',)

>>> p = WatercolorProvider()
>>> p.getTileUrls(Coordinate(25322, 10507, 16)) #doctest: +ELLIPSIS
('http://tile.stamen.com/watercolor/16/10507/25322.png',)
"""

from math import pi

from ..core import Coordinate
from ..geo import MercatorProjection, deriveTransformation
from .base import IMapProvider
from .. import tiles

class BaseProvider(IMapProvider):
    def __init__(self, style):
        # the spherical mercator world tile covers (-π, -π) to (π, π)
        t = deriveTransformation(-pi, pi, 0, 0, pi, pi, 1, 0, -pi, -pi, 0, 1)
        self.projection = MercatorProjection(0, t)

        self.style = style

    @property
    def tile_width(self):
        return 256

    @property
    def tile_height(self):
        return 256

    def get_tile_urls(self, coordinate):
        zoom, column, row = coordinate.zoom, coordinate.column, coordinate.row
        return ('http://tile.stamen.com/%s/%d/%d/%d.png' % (self.style, zoom, column, row),)

class TonerProvider(BaseProvider):
    def __init__(self):
        BaseProvider.__init__(self, 'toner')

class TerrainProvider(BaseProvider):
    def __init__(self):
        BaseProvider.__init__(self, 'terrain')

class WatercolorProvider(BaseProvider):
    def __init__(self):
        BaseProvider.__init__(self, 'watercolor')

if __name__ == '__main__':
    import doctest
    doctest.testmod()