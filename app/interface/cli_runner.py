from infrastructure.platform_repository import PlatformRepository
from infrastructure.browser_opener import BrowserOpener
from use_cases.open_platforms_in_time_range import OpenPlatformsInTimeRange

import sys

def run(force=False):
    repo = PlatformRepository()
    opener = BrowserOpener()
    use_case = OpenPlatformsInTimeRange(opener)

    platforms = repo.load_platforms()
    print(f"[DEBUG] Plataformas cargadas: {len(platforms)}")
    print(f"[DEBUG] Parámetro force recibido: {force}")
    print(f"[DEBUG] sys.argv: {sys.argv}")
    
    if force:
        print("[DEBUG] Modo forzado activado - abriendo todas las plataformas")
        for platform in platforms:
            print(f"[DEBUG] Abriendo: {platform.name} - {platform.url}")
            opener.open_url(platform.url)
    else:
        print("[DEBUG] Ejecutando lógica de horarios")
        use_case.execute(platforms)

if __name__ == "__main__":
    run(force="--force" in sys.argv)
