################################################################################################

from project.scripts.check_postgres_version import check_postgres_version

from unittest.mock import MagicMock, Mock, patch

################################################################################################

# @patch("project.scripts.check_postgres_version.dbengine.connect")
# def test_check_postgres_version(mock_connect):
#   mock_connection = MagicMock()

#   mock_result = MagicMock()
#   mock_result.scalar_one.return_value = ""

#   mock_connection.execute.return_value = mock_result
#   mock_connect.return_value.__enter__.return_value = mock_connection

#   check_postgres_version()
#   mock_connection.execute.assert_called_once()

################################################################################################
