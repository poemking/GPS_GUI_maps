import urllib
def getaddress(location, width, height, zoom):
    locationnospaces = urllib.quote_plus(location)
    address = "http://maps.googleapis.com/maps/api/staticmap?\
center={0}&zoom={1}&size={2}x{3}&format=gif&sensor=false"\
.format(locationnospaces, zoom, width, height)
    return address

import webbrowser
webbrowser.open(getaddress("23.0054945,120.2225718", 640, 480, 18))