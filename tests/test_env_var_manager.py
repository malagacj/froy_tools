import os
import unittest
from unittest.mock import patch
from src.froy_tools.env_var_manager import EnvVarManager


class TestEnvVarManager(unittest.TestCase):

    def setUp(self):
        """Set up the EnvVarManager instance for testing."""
        self.env_var_name = 'TEST_VAR'
        self.default_value = 'default_value'
        self.env_manager = EnvVarManager(self.env_var_name, self.default_value)

    @patch.dict(os.environ, {}, clear=True)
    def test_set_dir(self):
        """Test setting the environment variable."""
        self.env_manager.set_dir('test_directory')
        self.assertEqual(os.environ.get(self.env_var_name), 'test_directory')

    @patch.dict(os.environ, {}, clear=True)
    def test_set_dir_empty(self):
        """Test setting an empty directory does not change the environment variable."""
        self.env_manager.set_dir('')  # Attempt to set an empty directory
        self.assertIsNone(os.environ.get(self.env_var_name))  # The env var should not be set

    @patch.dict(os.environ, {}, clear=True)
    def test_get_dir_with_env_var_set(self):
        """Test getting the directory when the environment variable is set."""
        os.environ[self.env_var_name] = 'test_directory'
        self.assertEqual(self.env_manager.get_dir(), 'test_directory')

    @patch.dict(os.environ, {}, clear=True)
    def test_get_dir_without_env_var_set(self):
        """Test getting the directory when the environment variable is not set."""
        self.assertEqual(self.env_manager.get_dir(), self.default_value)

    @patch.dict(os.environ, {}, clear=True)
    def test_clear_env_var(self):
        """Test clearing the environment variable."""
        os.environ[self.env_var_name] = 'test_directory'
        self.env_manager.clear()
        self.assertIsNone(os.environ.get(self.env_var_name))

    @patch.dict(os.environ, {}, clear=True)
    def test_clear_env_var_when_not_set(self):
        """Test clearing the environment variable when it was never set."""
        # Ensure the variable is not set before clearing
        self.assertIsNone(os.environ.get(self.env_var_name))
        self.env_manager.clear()  # This should not raise any errors
        self.assertIsNone(os.environ.get(self.env_var_name))

if __name__ == '__main__':
    unittest.main()
