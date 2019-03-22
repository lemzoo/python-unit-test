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
        msg = 'Environment `{env}` is unknown'.format(env=environment)
        details = 'Only these environments are allowed: DEV, HML, PRD'
        raise ServerNameError(message=msg, details=details)

    # TODO: db_engine should be POSTGRESQL or ORACLE
    engine = ALLOWED_ENGINE.get(db_engine)
    if engine not in ALLOWED_ENGINE:
        msg = 'Engine `{env}` is unknown'.format(env=db_engine)
        details = 'Only these engines are allowed: POSTGRESQL, ORACLE'
        raise ServerNameError(message=msg, details=details)

    # TODO: use hostname to build the ID
    hostname = hostname.replace('.', '')
    prefix_id = []
    for item in range(0, len(hostname)):
        if (item + 1) == len(hostname):
            pass
        else:
            prefix_id.append(hostname[item + 1])

    prefix_id = ''.join(prefix_id)
    prefix_id = prefix_id.upper()
    return '{env}{engine}{id}'.format(env=environment[0], engine=engine,
                                      id=prefix_id[:8])
