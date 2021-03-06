from lexicon.providers.zonomi import Provider
from integration_tests import IntegrationTests
from unittest import TestCase
import pytest

# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from integration_tests.IntegrationTests
class ZonomiProviderTests(TestCase, IntegrationTests):

    Provider = Provider
    provider_name = 'zonomi'
    domain = 'pcekper.com.ar'
        
    def _test_engine_overrides(self):
        overrides = super(ZonomiProviderTests, self)._test_engine_overrides()
        overrides.update({'api_endpoint': 'https://zonomi.com/app'})
        return overrides
    
    def _filter_query_parameters(self):
        return ['api_key']


    # TODO: the following skipped suite and fixtures should be enabled
    @pytest.mark.skip(reason="new test, missing recording")
    def test_Provider_when_calling_update_record_should_modify_record_name_specified(self):
        return

    @pytest.fixture(autouse=True)
    def skip_suite(self, request):
        if request.node.get_marker('ext_suite_1'):
            pytest.skip('Skipping extended suite')