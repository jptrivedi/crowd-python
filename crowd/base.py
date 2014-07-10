import requests

class Crowd(object):

    def __init__(self, app_host, user, password):
        self.app_url = "https://%s/crowd/rest/usermanagement/latest" % app_host
        self.user = user
        self.password = password
        self.headers = {"Accept": "application/json"}

    def get(self, params, verify=False):
        r = requests.get(self.app_url, params=params, headers=self.headers, verify=verify, auth=(self.user, self.password))
        return r.text

    def delete(self, params, verify=False):
        r = requests.get(self.app_url, params=params, headers=self.headers, verify=verify, auth=(self.user, self.password))
        return r.status_code
