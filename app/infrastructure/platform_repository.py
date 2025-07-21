import json
from pathlib import Path
from datetime import time
from domain.study_platform import StudyPlatform

class PlatformRepository:
    def __init__(self, config_path: str = "config/platforms_config.json"):
        self.config_path = Path(config_path)

    def load_platforms(self) -> list[StudyPlatform]:
        with self.config_path.open("r") as f:
            data = json.load(f)

        platforms = []
        for entry in data:
            start = time.fromisoformat(entry["start_time"])
            end = time.fromisoformat(entry["end_time"])
            platforms.append(StudyPlatform(entry["name"], entry["url"], start, end))

        return platforms
