import six
from six.moves import urllib
import json
from decimal import Decimal

BASE_URL = 'https://maps.googleapis.com/maps/api'
PLACE_URL = BASE_URL + '/place'
GEOCODE_API_URL = BASE_URL + '/geocode/json?'
RADAR_SEARCH_API_URL = PLACE_URL + '/radarsearch/json?'
NEARBY_SEARCH_API_URL = PLACE_URL + '/nearbysearch/json?'
TEXT_SEARCH_API_URL = PLACE_URL + '/textsearch/json?'
AUTOCOMPLETE_API_URL = PLACE_URL + '/autocomplete/json?'
DETAIL_API_URL = PLACE_URL + '/details/json?'
CHECKIN_API_URL = PLACE_URL + '/check-in/json?sensor=%s&key=%s'
ADD_API_URL = PLACE_URL + '/add/json?sensor=%s&key=%s'
DELETE_API_URL = PLACE_URL + '/delete/json?sensor=%s&key=%s'
PHOTO_API_URL = PLACE_URL + '/photo?'

MAXIMUM_SEARCH_RADIUS = 50000
RESPONSE_STATUS_OK = 'OK'
RESPONSE_STATUS_ZERO_RESULTS = 'ZERO_RESULTS'


def _get_place_details(place_id, api_key, sensor=False,
                       language='en'):
    """Gets a detailed place response.
    keyword arguments:
    place_id -- The unique identifier for the required place.
    """
    url, detail_response = _fetch_remote_json(DETAIL_API_URL,
                                              {'placeid': place_id,
                                               'sensor': str(sensor).lower(),
                                               'key': api_key,
                                               'language': language})
    _validate_response(url, detail_response)
    return detail_response['result']

def _fetch_remote_json(service_url, params=None, use_http_post=False):
    """Retrieves a JSON object from a URL."""
    if not params:
        params = {}

    request_url, response = _fetch_remote(service_url, params, use_http_post)
    if six.PY3:
        str_response = response.read().decode('utf-8')
        return (request_url, json.loads(str_response, parse_float=Decimal))
    return (request_url, json.load(response, parse_float=Decimal))


def _validate_response(url, response):
    """Validates that the response from Google was successful."""
    if response['status'] not in [RESPONSE_STATUS_OK,
                                  RESPONSE_STATUS_ZERO_RESULTS]:
        error_detail = ('Request to URL %s failed with response code: %s' %
                        (url, response['status']))
        raise GooglePlacesError(error_detail)


def _fetch_remote(service_url, params=None, use_http_post=False):
    if not params:
        params = {}

    encoded_data = {}
    for k, v in params.items():
        if isinstance(v, six.string_types):
            v = v.encode('utf-8')
        encoded_data[k] = v
    encoded_data = urllib.parse.urlencode(encoded_data)

    if not use_http_post:
        query_url = (service_url if service_url.endswith('?') else
                     '%s?' % service_url)
        request_url = query_url + encoded_data
        request = urllib.request.Request(request_url)
    else:
        request_url = service_url
        request = urllib.request.Request(service_url, data=encoded_data)
    return (request_url, urllib.request.urlopen(request))   