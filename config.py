import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7556497777:AAF4VoCDNvHvQ_DiAfpT9uP703UFzClvcgY")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24473318"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e7dd0576c5ac0ff8f90971d6bb04c8f5")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6697397532"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://mehuldb:ymLdv8Sf2UW49x2m@withcluster.akoofaz.mongodb.net/") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "mehuldb")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
