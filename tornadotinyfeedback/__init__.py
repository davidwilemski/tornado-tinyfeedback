
import os
from tornado import httpclient
import urllib

class Client(object):
    def __init__(self, component, host=None, port=None):
        self.component = component

        self.host = host
        self.port = port
        self.component = component

        self.http = httpclient.AsyncHTTPClient()

        if not host:
            self.host = os.environ.get('TINYFEEDBACK_HOST', '127.0.0.1')
        if not port:
            self.port = os.environ.get('TINYFEEDBACK_PORT', 8000)

    def send(self, data, callback):
        url = 'http://{}:{}/data/{}'.format(self.host, self.port, self.component)
        self.http.fetch(url, callback, method='POST', body=urllib.urlencode(data))

    def _callback(self, response):
        # ignore success/failure
        print response
