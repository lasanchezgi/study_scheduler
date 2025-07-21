from datetime import datetime
from domain.study_platform import StudyPlatform
from infrastructure.browser_opener import BrowserOpener

class OpenPlatformsInTimeRange:
    def __init__(self, browser_opener: BrowserOpener):
        self.browser_opener = browser_opener
        self.opened_today = set()

    def execute(self, platforms: list[StudyPlatform]):
        now = datetime.now().time()
        print(f"[DEBUG] Hora actual: {now}")
        for platform in platforms:
            print(f"[DEBUG] Evaluando {platform.name} entre {platform.start_time} y {platform.end_time}")
            if platform.is_current_time_in_range(now) and platform.name not in self.opened_today:
                self.browser_opener.open_url(platform.url)
                self.opened_today.add(platform.name)

