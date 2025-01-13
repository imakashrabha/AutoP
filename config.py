from os import environ

API_ID = int(environ.get("API_ID", "27705761"))
API_HASH = environ.get("API_HASH", "822cb334ca4527a134aae97f9fe44fd6")
BOT_TOKEN = environ.get("BOT_TOKEN", "7714644836:AAHFIRQbZHMsxzBXvNtKxcHZyODEALu4vIk")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002492877612"))
ADMINS = int(environ.get("ADMINS", "6987158459"))
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002201654960"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://akashrabha2005:781120@cluster0.pv6yd2f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
