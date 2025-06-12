import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from os import makedirs, path
from pathlib import Path
import json
import logging

logger = logging.getLogger(__name__)

SITE = 'https://ultimateframedata.com/smash'
DATA_DIR = Path.cwd() / 'data'
RAW_DATEFILE = DATA_DIR / 'rawdatefile'
CHAR_DATA_DIR = DATA_DIR / 'smash_character_data'

class CharacterList(dict):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CharacterList, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        return CharacterList()

def get_data():
    """
    Download and cache Smash Ultimate frame data if not present or outdated.
    Returns the cleaned data as a dictionary.
    """
    DATA_DIR.mkdir(exist_ok=True)
    CHAR_DATA_DIR.mkdir(exist_ok=True)

    # Check if we need to redownload (older than 3 months)
    if RAW_DATEFILE.exists():
        try:
            with open(RAW_DATEFILE, 'r') as f:
                last_download = datetime.fromisoformat(f.read().strip())
            if datetime.now() - last_download < timedelta(days=90):
                logger.info("Data is up to date. No need to redownload.")
                return "file already exists, no need to redownload everything"
        except Exception as e:
            logger.warning(f"Could not parse date file: {e}")

    # Download and process data
    try:
        response = requests.get(SITE, timeout=10)
        response.raise_for_status()
        cleaned_data = clean_data(response.content)
        with open(RAW_DATEFILE, 'w') as f:
            f.write(datetime.now().isoformat())
        return cleaned_data
    except requests.RequestException as e:
        logger.error(f"Failed to fetch data: {e}")
        return {}

def clean_data(data):
    """
    Parse the main page and process each character.
    """
    soup = BeautifulSoup(data, 'html.parser')
    raw_character_list = soup.find(id='charList').find_all('a')
    results = {}

    for character in raw_character_list[1:]:
        title = character.get('title')
        url = character.get('href')
        results[title] = create_local_data_structure(title, url)
    return results

def get_character_data(link):
    """
    Fetch and parse move data for a single character.
    """
    site = 'https://ultimateframedata.com'
    try:
        webpage = requests.get(f"{site}/{link}", timeout=10)
        webpage.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Failed to fetch character data for {link}: {e}")
        return {}

    soup = BeautifulSoup(webpage.content, 'html.parser')
    all_moves = soup.find(id="contentcontainer").find_all(class_="movecontainer")
    nice_moves = {}

    for move in all_moves:
        move_data = move.find_all('div')
        movename = 'move'
        nice_entry = {}
        for entry in move_data:
            try:
                gif = entry.find('a')
                if gif and 'data-featherlight' in gif.attrs:
                    nice_entry[entry['class'][0]] = gif['data-featherlight']
                elif str(entry['class'][0]) == 'movename':
                    movename = entry.getText().strip().lower().replace(' ', '_').replace('.', '')
                    nice_entry[entry['class'][0]] = entry.getText().strip()
                else:
                    nice_entry[entry['class'][0]] = entry.getText().strip()
            except (KeyError, AttributeError):
                logger.debug('Could not parse entry for move data.')
        nice_moves[movename] = nice_entry.copy()
    return nice_moves

def create_local_data_structure(title, url):
    """
    Combine character info and moves, save to file, and update singleton.
    """
    title_key = title.strip().lower().replace(' ', '_')
    moves = get_character_data(url)
    character_data = {'url': url, 'date': datetime.now().isoformat(), 'moves': moves}

    # Update singleton
    x = CharacterList.get_instance()
    x[title_key] = character_data

    # Save to file
    CHAR_DATA_DIR.mkdir(exist_ok=True)
    with open(CHAR_DATA_DIR / f"{title_key}.json", 'w') as char_file:
        json.dump(character_data, char_file, indent=2)

    return character_data
