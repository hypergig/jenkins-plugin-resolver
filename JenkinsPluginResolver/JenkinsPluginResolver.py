from urllib2 import urlopen
import json


class JenkinsPluginResolver(object):
    def __init__(self):
        self._plugins = dict()
        self._uc_post = self._load_update_center_post()
        self._load_update_center_post()

    def _load_update_center_post(self):
        url = 'https://updates.jenkins-ci.org/current/update-center.json'
        raw = urlopen(url).read()
        fixed = raw.lstrip('updateCenter.post(').rstrip('\n);')
        return json.loads(fixed)

    def clear(self):
        self._plugins = dict()

    def uc_post(self):
        return self._uc_post

    def dump(self):
        return self._plugins

    def load(self, plugin, version='latest'):
        # prevent a circular dependency from causing an infinite loop
        if plugin not in self._plugins:
            try:
                dependencies = self._uc_post['plugins'][plugin]['dependencies']
            except KeyError:
                raise RuntimeError(
                    "plugin '%s' doesn't exist in the Update Center" % plugin)
            self._plugins[plugin] = version
            for dependency in dependencies:
                self.load(dependency['name'])
        # support for version pinning, user specified versions override latest
        elif version != 'latest':
            self._plugins[plugin] = version
