from unittest.mock import patch

import pytest

from lab import create_cluster as create, ClusterCreationError, ServerNameError


class TestCluster:
    def setup(self):
        # Given params
        self.environment = 'DEV'
        self.vm_profile = 'small.1vCPU.1GoRAM'
        self.version = '10.0'
        build_name = patch('lab.cluster.build_name')
        self.build_name = build_name.start()

    def test_should_return_cluster_with_details(self):
        # When
        cluster = create(self.environment, self.vm_profile, self.version)

        # Then
        assert cluster.uuid is not None
        assert cluster.vm_profile == 'small.1vCPU.1GoRAM'
        assert cluster.version == '10.0'
        assert cluster.environment == 'DEV'
        assert cluster.server_name is not None
        expected_hostname = f'cluster-pg-10-dev-{cluster.id[:8]}.cloud.com'
        assert cluster.hostname == expected_hostname

    def test_should_call_build_name_with_right_params(self):
        # When
        cluster = create(self.environment, self.vm_profile, self.version)

        # Then
        self.build_name.assert_called_once_with(environment=self.environment,
                                                db_engine='POSTGRESQL',
                                                hostname=cluster.hostname)

    def test_should_raise_when_unable_to_get_server_name(self):
        # Given
        self.environment = 'FOO'
        self.build_name.side_effect = ServerNameError(error='unknown')

        # When
        with pytest.raises(ClusterCreationError) as error:
            create(self.environment, self.vm_profile, self.version)

        # Then
        assert error.value.args == 'unknown environment `FOO`'
