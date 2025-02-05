import os
from dotenv import load_dotenv


def set_env_variables():
    """
    Load environment variables from a .env file and set them in os.environ.
    """
    dotenv_path = ".env"
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path, override=True)
        print("Environment variables loaded.")
    else:
        raise FileNotFoundError("The .env file was not found!")


set_env_variables()
