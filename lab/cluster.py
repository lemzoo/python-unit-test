from uuid import uuid4

from lab.server import build_name


class ClusterPostgreSQL:
    uuid = None
    vm_profile = None
    version = None
    environment = None
    hostname = None
    server_name = None

    def __init__(self, environment, vm_profile, version):
        self.uuid = uuid4()
        self.environment = environment
        self.vm_profile = vm_profile
        self.version = version
        self.build_host()

    @property
    def id(self):
        return str(self.uuid)

    def build_host(self):
        version = self.version.split('.')[0]
        env = self.environment
        host = f'cluster-pg-{version}-{env}-{self.id[:8]}.cloud.com'
        self.hostname = host.lower()


def create_cluster(environment, vm_profile, version):
        cluster = ClusterPostgreSQL(environment, vm_profile, version)
        cluster.server_name = build_name(environment=environment,
                                         db_engine='POSTGRESQL',
                                         hostname=cluster.hostname)
        return cluster
