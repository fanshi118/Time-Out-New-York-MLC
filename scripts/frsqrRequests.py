#!/usr/bin/env python
# -*- coding: utf-8 -*-

# all documentation is here
# https://developer.foursquare.com/docs/venues/explore
# Parameter:
#     Input: lat, lon, k(kth FRSQR credential)
#     Output: venue_id, venue_name, venue_category

import json
import requests
from settings import FRSQR_CLIENT_IDS, FRSQR_CLIENT_SECRETS


def VenueSearch(lat, lon, k):
    '''venue search, returns list of compact venues for specific area'''

    # sw=%s&ne=%s&client_id=%s&client_secret=%s&intent=browse" % (sw, ne,
    # CLIENT_ID, CLIENT_SECRET)
    CLIENT_ID = FRSQR_CLIENT_IDS[k]
    CLIENT_SECRET = FRSQR_CLIENT_SECRETS[k]

    baseUrl = "https://api.foursquare.com/v2/venues/search"
    payload = {'ll': str(lat) + ',' + str(lon),
               'client_id': CLIENT_ID,
               'client_secret': CLIENT_SECRET,
               'v': "20160318"
               }
    res = json.loads(requests.get(baseUrl, params=payload).text)
    venue = res['response']['venues'][0]
    vid = venue['id']
    vname = venue['name']
    try:
        vcat = venue['categories'][0]['name']
    except IndexError:
        vcat = 'NA'
    return [vid, vname, vcat]
