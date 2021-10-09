import json
from pathlib import Path
from typing import NamedTuple, Optional

from stackunderflowed.models import connect_or_init_db

DATA_DIR: Path = Path.cwd() / "data"
CONFIG_FILE: Path = DATA_DIR / "config.json"


class ProjectConfiguration(NamedTuple):
    api_key: str = "Insert Algorand node API key here"
    custodian_wallet_mnemonic: str = "Insert custodian wallet mnemonic phrase here"
    work_token_id: int = -1
    experience_token_id: int = -1


config: Optional[ProjectConfiguration] = None


def _init_configuration_file() -> None:
    print("Please fill out the config.json file in the newly created data directory")
    with CONFIG_FILE.open("w") as f:
        json.dump(ProjectConfiguration()._asdict(), f, indent=4)


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

    if not CONFIG_FILE.exists():
        _init_configuration_file()
        return False

    global config
    with CONFIG_FILE.open("r") as f:
        config = ProjectConfiguration(**json.load(f))

    connect_or_init_db()

    return True


checked = load_current_project_state()

if not checked:
    exit()
