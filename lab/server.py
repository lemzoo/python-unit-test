ALLOWED_ENVIRONMENT = ['DEV', 'HML', 'PRD']


ALLOWED_ENGINE = {
    'POSTGRESQL': 'PG',
    'ORACLE': 'OR'
}


class ServerNameError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


def build_name(environment, db_engine, hostname):
    # TODO: environment should be DEV, HML or PRD
    if environment not in ALLOWED_ENVIRONMENT:
        msg = f'Environment `{environment}` is unknown'
        environments = ', '.join(ALLOWED_ENVIRONMENT)
        details = f'Only these environments are allowed: {environments}'
        raise ServerNameError(message=msg, details=details)

    # TODO: db_engine should be POSTGRESQL or ORACLE
    engine = ALLOWED_ENGINE.get(db_engine)
    if not engine:
        msg = f'Engine `{db_engine}` is unknown'
        engines = ', '.join(ALLOWED_ENGINE.keys())
        details = f'Only these engines are allowed: {engines}'
        raise ServerNameError(message=msg, details=details)

    # TODO: use hostname to build the ID
    hostname = hostname.replace('.', '')
    hostname = hostname.replace('-', '')
    prefix_id = []

    host_len = len(hostname)
    for item in range(0, host_len):
        if item != (host_len - 1):
            prefix_id.append(hostname[item + 1])

    prefix_id = ''.join(prefix_id)
    prefix_id = prefix_id.upper()[:8]
    name = f'{environment[0]}{engine}{prefix_id}'
    return name
