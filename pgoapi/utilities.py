"""
pgoapi - Pokemon Go API
Copyright (c) 2016 tjado <https://github.com/tejado>
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
Author: tjado <https://github.com/tejado>
"""

import time
import random
import logging

# other stuff
from s2sphere import LatLng, Angle, Cap, RegionCoverer, math

log = logging.getLogger(__name__)

EARTH_RADIUS = 6371000  # radius of Earth in meters


def to_camel_case(value):
    return ''.join(word.capitalize() if word else '_'
                   for word in value.split('_'))


def get_cell_ids(lat, long, radius=500):
    # Max values allowed by server according to this comment:
    # https://github.com/AeonLucid/POGOProtos/issues/83#issuecomment-235612285
    if radius > 1500:
        radius = 1500  # radius = 1500 is max allowed by the server
    region = Cap.from_axis_angle(
        LatLng.from_degrees(lat, long).to_point(),
        Angle.from_degrees(360 * radius / (2 * math.pi * EARTH_RADIUS)))
    coverer = RegionCoverer()
    coverer.min_level = 15
    coverer.max_level = 15
    cells = coverer.get_covering(region)
    cells = cells[:100]  # len(cells) = 100 is max allowed by the server
    return sorted([x.id() for x in cells])


def get_time(ms=False):
    if ms:
        return int(time.time() * 1000)
    else:
        return int(time.time())


def get_format_time_diff(low, high, ms=True):
    diff = (high - low)
    if ms:
        m, s = divmod(diff / 1000, 60)
    else:
        m, s = divmod(diff, 60)
    h, m = divmod(m, 60)

    return (h, m, s)


def parse_api_endpoint(api_url):
    if not api_url.startswith("https"):
        api_url = 'https://{}/rpc'.format(api_url)

    return api_url


def weighted_choice(choices):
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"
