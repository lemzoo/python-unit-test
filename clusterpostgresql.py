from uuid import uuid4

from server import build_name


class Cluster:
    vm_profile = None
    engine = None
    version = None
    environment = None
    hostname = None
    server_name = None

    @staticmethod
    def generate_host(environment, engine, version):
        uuid = uuid4()
        uuid = str(uuid)
        host = 'cluster-{env}-{engine}-{version}-{id}.cloud.com'
        host = host.format(env=environment, engine=engine,
                           version=version.split('.')[0], id=uuid[:8])
        return host.lower()


def create_cluster(environment, engine, vm_profile, version):
        cluster = Cluster()
        cluster.environment = environment
        cluster.engine = engine
        cluster.vm_profile = vm_profile
        cluster.version = version
        cluster.hostname = Cluster.generate_host(environment, engine, version)
        cluster.server_name = build_name(environment, engine, cluster.hostname)

        return cluster
