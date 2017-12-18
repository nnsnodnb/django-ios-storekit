try:
    from unittest import mock
except ImportError:
    import mock


from django.conf import settings
try:
    from django.test.runner import DiscoverRunner as TestRunnerBase
except ImportError:
    from django.test.simple import DjangoTestSuiteRunner as TestRunnerBase


class TestRunner(TestRunnerBase):
    def setup_test_environment(self, **kwargs):
        super(TestRunner, self).setup_test_environment(**kwargs)
        settings.TESTING = True

    def teardown_test_environment(self, **kwargs):
        super(TestRunner, self).teardown_test_environment(**kwargs)
        settings.TESTING = True
