from cluster import create_cluster


class TestCluster:
    def test_should_return_cluster_with_details(self):
        # Given
        environment = 'DEV'
        vm_profile = 'small.1vCPU.1GoRAM'
        version = '10.0'

        # When
        cluster = create_cluster(environment, vm_profile, version)

        # Then
        assert cluster.uuid is not None
        assert cluster.vm_profile == 'small.1vCPU.1GoRAM'
        assert cluster.version == '10.0'
        assert cluster.environment == 'DEV'
        assert cluster.server_name is not None
        expected_hostname = f'cluster-pg-10-dev-{cluster.id[:8]}.cloud.com'
        assert cluster.hostname == expected_hostname
