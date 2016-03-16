from mock import MagicMock
from mock import Mock
from mock import call
from nose.plugins.skip import Skip
from nose.plugins.skip import SkipTest
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from unittest import TestCase
from ..JenkinsPluginResolver import JenkinsPluginResolver


class Test_JekinsPluginResolver(TestCase):

    def test_the_test(self):
        assert_equal(0, 0)

    def test_uc_post(self):
        raise SkipTest

    def test_load(self):
        raise SkipTest

    def test_dump(self):
        raise SkipTest

    def test_clear(self):
        raise SkipTest
