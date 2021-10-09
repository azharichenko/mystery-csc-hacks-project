import json
from pathlib import Path
from typing import NamedTuple, Optional

DATA_DIR: Path = Path.cwd() / "data"
CONFIG_FILE: Path = DATA_DIR / "config.json"


class ProjectConfiguration(NamedTuple):
    api_key: str = "Insert Algorand node API key here"
    custodian_wallet_mnemonic: str = "Insert custodian wallet mnemonic phrase here"


config: Optional[ProjectConfiguration] = None


def _init_configuration_file() -> None:
    print("Please fill out the config.json file in the newly created data directory")
    with CONFIG_FILE.open("w") as f:
        json.dump(ProjectConfiguration()._asdict(), f)


def fetch_configuration() -> ProjectConfiguration:
    global config
    if config is None:
        raise RuntimeError("Project configuration hasn't been loaded")
    return config


def load_current_project_state() -> bool:
    """Loads in current configuration and SQLite database
    If project state is missing the project will initialize it
    and request the user fill out the configuration file before
    rerunning the script again.
    """
    if not DATA_DIR.exists():
        DATA_DIR.mkdir()
        _init_configuration_file()
        return False

    global config
    with CONFIG_FILE.open("r") as f:
        config = ProjectConfiguration(**json.load(f))

    return True
