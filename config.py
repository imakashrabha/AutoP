from os import environ

API_ID = int(environ.get("API_ID", "27705761"))
API_HASH = environ.get("API_HASH", "822cb334ca4527a134aae97f9fe44fd6")
BOT_TOKEN = environ.get("BOT_TOKEN", "7260514430:AAGhXF1Fe8VwS6xri7DERjhOksZGSQs1D9I")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002452631532"))
ADMINS = int(environ.get("ADMINS", "7246242686"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://akashrabha2005:781120@cluster0.pv6yd2f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
