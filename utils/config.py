import os
from dotenv import load_dotenv


# loads .env file, will not overide already set enviroment variables
load_dotenv()


DEBUG = os.getenv('DEBUG', 'False') in ['True', 'true']

# NEXUS
NEXUS_URL = os.environ["NEXUS_URL"].strip()
NEXUS_CLIENT_ID = os.environ["NEXUS_CLIENT_ID"].strip()
NEXUS_CLIENT_SECRET = os.environ["NEXUS_CLIENT_SECRET"].strip()
NEXUS_REALM = os.environ["NEXUS_REALM"].strip()
NEXUS_AUTH_TYPE = os.environ["NEXUS_AUTH_TYPE"].strip()

# SMS
SMS_URL = "https://smssys.dk/sms"
SMS_USER = os.environ["SMS_USER"].strip()
SMS_PASS = os.environ["SMS_PASS"].strip()

# Door codes - string of comma separated values, e.g. "#1234,#5678"
DOOR_CODES = os.environ["DOOR_CODES"].strip().split(",")
