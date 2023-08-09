""" Module to load or create the initial configuration from the config.ak file. """

import pickle

from data.global_var import DIR_DATA

DEFAULT_CONFIG = {
    "language": "en",
    "theme": "dark",
    "time_to_start": 3,
}

def get_config() -> dict:
    """
    Open or create the config.ak file, place the cursor at the beginning
    and load the information, if it does not exist,
    open the file and place the default configuration in it.
    """
    try:
        with open(f"{DIR_DATA}config.ak", "rb") as configuration:
            config = pickle.load(configuration)
    except FileNotFoundError:
        with open(f"{DIR_DATA}config.ak", "wb") as configuration:
            pickle.dump(DEFAULT_CONFIG, configuration)
        with open(f"{DIR_DATA}config.ak", "ab+") as configuration:
            configuration.seek(0)
            config = pickle.load(configuration)

    return config

def change_config(new_config: dict) -> None:
    """
    Open the config.ak file and place the new
    configuration received in the new_config variable.
    """
    with open(f"{DIR_DATA}config.ak", "wb") as configuration:
        pickle.dump(new_config, configuration)

global_config_program = get_config()
