import os
from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
import requests

class Settings(BaseSettings):
    session_cookie: str = Field(alias="SESSION_COOKIE")
    year: int = Field(alias="YEAR")

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), "../.env")
    )   

def __get_cache_folder() -> str:
    return os.path.join(os.path.dirname(__file__), "../.cache")

def __get_cache_filename(year: int, day: int) -> str:
    return f"{year}_{day:02}.cache" 

def __get_cache(year: int, day: int) -> Optional[str]:
    file_path = os.path.join(
        __get_cache_folder(),
        __get_cache_filename(year, day)
    )
    if os.path.exists(file_path):
        with open(file_path, 'r') as cache_file:
            return cache_file.read()

def __set_cache(year: int, day: int, value: str) -> str:
    folder_path = __get_cache_folder()
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    file_path = os.path.join(folder_path, __get_cache_filename(year, day))
    with open(file_path, 'w') as cache_file:
        cache_file.write(value)

    return value

def get_input(day):
    settings = Settings()

    cache = __get_cache(settings.year, day)
    if cache: return cache

    url = f"https://adventofcode.com/{settings.year}/day/{day}/input"
    cookies = {"session": settings.session_cookie}
    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        return __set_cache(settings.year, day, response.text.strip())
    else:
        response.raise_for_status()