import os
API_ID = int(os.getenv("22058221"))
API_HASH = os.getenv("7d2453623cc2b68f3560edfb610e3dc0")
BOT_TOKEN = os.getenv("5667003589:AAHahG1prVECnazZIGRBNsS-TB3CkgLzun8")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("@raghul_0ott", "").split()})
