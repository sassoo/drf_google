"""
    utils
    ~~~~~

    Helper methods for communicating with the following Google
    services:

        Geocoding API
        Places API
"""

import requests

from datetime import datetime
from django.conf import settings
from geopy.geocoders import GoogleV3


GOOGLE_KEY = settings.GOOGLE_KEY
PLACES_URL = 'https://maps.googleapis.com/maps/api/place/details/json'


def geocode(address, key=GOOGLE_KEY):
    """ Find lat/lng from Google Maps from an address

    :param address:
        string address
    :raises:
        IOError in the event that communicating with google
        fails for any reason.
    :return:
        A dict containing (lat, lng, tz)
    """

    geo = GoogleV3(key)

    try:
        loc = geo.geocode(address, exactly_one=True)
        if loc.raw.get('partial_match'):
            return None

        tz = geo.timezone((loc.latitude, loc.longitude))
        tz = tz.localize(datetime.now())
        tz = tz.strftime('%Z')

        return {'lng': loc.longitude, 'lat': loc.latitude, 'tz': tz}
    except AttributeError:
        return None
    except:
        raise IOError('error contacting google geocode')


def places(place_id, key=GOOGLE_KEY):
    """ Given a Google Places ID query the Google Places API

    A dict containing a more helpful & concise version of Google's
    results is return & looks like:

        {
            open_now: boolean
            open_times: [{
                day: 'Monday',
                time: '9am - 5pm'
            }]
        }

    :raises:
        IOError in the event that communicating with google
        fails for any reason.
    :return:
        A python dictionary of the Google Places API response
        or None if not found.
    """

    params = {'placeid': place_id, 'key': key}

    try:
        res = requests.get(PLACES_URL, params=params, verify=False)
        res.raise_for_status()
        res = res.json()['result']['opening_hours']
    except (AttributeError, KeyError):
        return {}
    except:
        raise IOError('error contacting google places')

    open_times = [
        {'day': text.split(':')[0], 'time': ':'.join(text.split(':')[1:])}
        for text in res['weekday_text']
    ]
    return {'open_now': res['open_now'], 'open_times': open_times}
