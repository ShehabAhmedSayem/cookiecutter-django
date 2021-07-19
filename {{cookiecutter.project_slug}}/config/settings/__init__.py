from pathlib import Path

import environ

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
env = environ.Env()
env.read_env(str(ROOT_DIR / ".env"))

if env.bool("DJANGO_PRODUCTION"):
    from .production import *
else:
    from .local import *
