import pytest

from server import build_name, ServerNameError


class TestBuildName:

    environment = 'DEV'
    db_engine = 'POSTGRESQL'
    hostname = 'ddaplx01.fr.world.socgen'

    def test_should_raise_when_environment_is_unknown(self):
        # Given
        self.environment = 'UNKNOWN-ENV'

        # When
        with pytest.raises(ServerNameError) as error:
            build_name(self.environment, self.db_engine, self.hostname)

        # Then
        error = error.value.args[1]
        message = 'Environment `{env}` is unknown'.format(env=self.environment)
        assert error['message'] == message
        details = 'Only these environments are allowed: DEV, HML, PRD'
        assert error['details'] == details

    def test_should_raise_when_db_engine_is_unknown(self):
        # Given
        self.db_engine = 'UNKNOWN-ENGINE'

        # When
        with pytest.raises(ServerNameError) as error:
            build_name(self.environment, self.db_engine, self.hostname)

        # Then
        error = error.value.args[1]
        message = 'Engine `{env}` is unknown'.format(env=self.db_engine)
        assert error['message'] == message
        details = 'Only these engines are allowed: POSTGRESQL, ORACLE'
        assert error['details'] == details

    @pytest.mark.parametrize('environment, engine, prefix',
                             [
                                 ('DEV', 'POSTGRESQL', 'DPG'),
                                 ('HML', 'POSTGRESQL', 'HPG'),
                                 ('PRD', 'POSTGRESQL', 'PPG'),
                                 ('DEV', 'ORACLE', 'DOR'),
                                 ('HML', 'ORACLE', 'HOR'),
                                 ('PRD', 'ORACLE', 'POR'),
                              ])
    def test_should_build_right_server_name(self, environment, engine, prefix):
        # When
        result = build_name(environment, engine, self.hostname)

        # Then
        assert result == '{p}DAPLX01F'.format(p=prefix)
