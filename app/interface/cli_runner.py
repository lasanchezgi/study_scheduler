from infrastructure.platform_repository import PlatformRepository
from infrastructure.browser_opener import BrowserOpener
from use_cases.open_platforms_in_time_range import OpenPlatformsInTimeRange

import sys

def run(force=False):
    repo = PlatformRepository()
    opener = BrowserOpener()
    use_case = OpenPlatformsInTimeRange(opener)

    platforms = repo.load_platforms()
    if force:
        for platform in platforms:
            opener.open_url(platform.url)
    else:
        use_case.execute(platforms)

if __name__ == "__main__":
    run(force="--force" in sys.argv)
