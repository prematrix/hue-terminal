import requests
import json


class Hapi:

    def __init__(self, ip, user, group):
        self.ip = ip
        self.user = user
        self.url = 'http://{}/api/{}'.format(ip, user)
        self.group = group

    def lights(self):
        url = '{}{}'.format(self.url, '/lights')
        res = requests.get(url)
        return json.loads(res.content)

    def lights_on(self, args=None):
        url = '{}/groups/{}/action'.format(self.url, self.group)
        payload = {
            'on': True
        }
        requests.put(url, data=json.dumps(payload))

    def lights_off(self, args=None):
        url = '{}/groups/{}/action'.format(self.url, self.group)
        payload = {
            'on': False
        }
        requests.put(url, data=json.dumps(payload))

    def group_brightness(self, args):
        url = '{}/groups/{}/action'.format(self.url, self.group)
        payload = {
            'bri': int(args)
        }
        requests.put(url, data=json.dumps(payload))

    def scenes(self):
        url = '{}/scenes'.format(self.url)
        res = requests.get(url)
        return json.loads(res.content)

    def choose_scene(self, name):
        url = '{}/groups/{}/action'.format(self.url, self.group)
        payload = {
            'scene': name
        }
        requests.put(url, data=json.dumps(payload))
