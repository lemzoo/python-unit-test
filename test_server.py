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

    def test_should_build_right_server_name(self):
        # Given
        self.environment = 'DEV'
        self.db_engine = 'POSTGRESQL'
        self.hostname = 'ddaplx01.fr.world.socgen'

        # When
        result = build_name(self.environment, self.db_engine, self.hostname)

        # Then
        assert result == 'DPGDAPLX01F'
