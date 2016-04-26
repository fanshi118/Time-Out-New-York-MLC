# script for scraping 4sq venue info using the files parsed from spark

import urllib2
import json
import glob
import csv
import pandas as pd
import numpy as np
from datetime import datetime


def getLatLons(lat_lon=[]):
    for data in glob.glob("../data/*output/part*"):
        f = open(data, 'r')
        csv_reader = csv.reader(f)
        for record in csv_reader:
            lat_lon.append((float(record[-3]), float(record[-2])))
    return list(set(lat_lon))


def scrapeVenues(lat_lon, CLIENT_ID, CLIENT_SECRET, TODAY, venues=[]):
    for i in lat_lon:
        url = 'https://api.foursquare.com/v2/venues/search?ll=%.8f,%.8f&client_id=%s&client_secret=%s&v=%s' % (
            i[0], i[1], CLIENT_ID, CLIENT_SECRET, TODAY)
        request = urllib2.urlopen(url)
        venue = json.load(request)
        try:
            venues.append((venue['response']['venues'][0]['name'], venue[
                          'response']['venues'][0]['categories'][0]['name']))
        except:
            venues.append(('None', 'None'))
        return venues


def main():
    # get lat lon to search
    lat_lon = getLatLons()

    # start scraping
    CLIENT_ID = "E5TAAUJBIE4E14EZUNJAN50JROS5SUIC53GA3KCDHJ0MAWZF"
    CLIENT_SECRET = "0P2IDPCCPRNPT532QDPHZG52Q1OC0AJ355QDQFL5ODRMRRKX"
    TODAY = "%04d%02d%02d" % (
        datetime.today().year, datetime.now().month, datetime.now().day)
    venues = scrapeVenues(lat_lon, CLIENT_ID, CLIENT_SECRET, TODAY)

    # write things out
    df = pd.DataFrame()
    df['lat'] = [i[0] for i in lat_lon]
    df['lon'] = [i[1] for i in lat_lon]
    df['venue_name'] = [i[0] for i in venues]
    df['venue_type'] = [i[1] for i in venues]
    df.to_csv('../data/venues.csv', index=False)

if __name__ == "__main__":
    main()
