#from nose.plugins.skip import SkipTest
from nose.tools import assert_equal, raises
from mock import Mock, patch
from unittest import TestCase
from JenkinsPluginResolver.JenkinsPluginResolver import JenkinsPluginResolver
from os.path import dirname, realpath


class Test_JekinsPluginResolver(TestCase):
    @patch('JenkinsPluginResolver.JenkinsPluginResolver.urlopen')
    def setUp(self, mock_urlopen):
        test_json_loc = '{}/test-update-center.json'.format(
            dirname(realpath(__file__)))
        with open(test_json_loc) as f:
            test_json = f.read()

        # mock the read return
        mock = Mock()
        mock.read.return_value = test_json
        mock_urlopen.return_value = mock
        self.jpr = JenkinsPluginResolver()

    def test_the_test(self):
        assert_equal(0, 0)

    def test_uc_post(self):
        self.jpr.uc_post()

    def test_load(self):
        self.jpr.load('plugin_1')

    def test_dump(self):
        r = dict()
        assert_equal(self.jpr.dump(), r)

    def test_clear(self):
        self.jpr.clear()

    def test_resolve_plugin(self):
        self.jpr.load('plugin_1')
        r = {'plugin_1': 'latest', 'plugin_2': 'latest', 'plugin_3': 'latest'}
        assert_equal(self.jpr.dump(), r)

    def test_clear_plugins(self):
        self.jpr.load('plugin_1')
        self.jpr.clear()
        r = dict()
        assert_equal(self.jpr.dump(), r)

    def test_dupe_plugins(self):
        self.jpr.load('plugin_1')
        self.jpr.load('plugin_1')
        self.jpr.load('plugin_1')
        r = {'plugin_1': 'latest', 'plugin_2': 'latest', 'plugin_3': 'latest'}
        assert_equal(self.jpr.dump(), r)

    @raises(RuntimeError)
    def test_bad_plugin(self):
        self.jpr.load('plugin_4')

    def test_pinned_plugin(self):
        self.jpr.load('plugin_1', '2.3.5')
        r = {'plugin_1': '2.3.5', 'plugin_2': 'latest', 'plugin_3': 'latest'}
        assert_equal(self.jpr.dump(), r)
