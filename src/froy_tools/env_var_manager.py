import os
import logging
from typing import Optional


# Logger setup
logger = logging.getLogger(__name__)


class EnvVarManager:
    """
    A class to manage environment variables related to directory settings.

    Attributes:
        env_var (str): The environment variable name.
        default_value (str): The default value to return if the environment variable is not set.
    """

    def __init__(self, env_var: str, default_value: str):
        """
        Initializes the EnvVarManager with the environment variable name and default value.

        Args:
            env_var (str): The name of the environment variable.
            default_value (str): The default value if the environment variable is not set.
        """
        self.env_var = env_var
        self.default_value = default_value

    def set_dir(self, directory: str) -> None:
        """
        Sets the directory path in the environment variable.

        Args:
            directory (str): The directory path to set.

        Returns:
            None
        """
        if not directory:
            logger.warning(f"Attempted to set an empty directory name for {self.env_var}")
            return

        os.environ[self.env_var] = directory
        logger.debug(f'Set {self.env_var}: %s', directory)

    def get_dir(self) -> str:
        """
        Retrieves the directory path from the environment variable.

        Returns:
            str: The directory path from the environment variable or the default value.
        """
        value = os.environ.get(self.env_var, self.default_value)
        logger.debug(f'{self.env_var}: %s', value)
        return value

    def clear(self) -> None:
        """
        Clears the environment variable.

        Returns:
            None
        """
        if self.env_var in os.environ:
            del os.environ[self.env_var]
            logger.debug(f'{self.env_var} has been cleared')
        else:
            logger.debug(f'{self.env_var} was not set')
