from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID", "6989623"))
    API_HASH = getenv("API_HASH", "077c18ef264de1c09a32ee2d5c00c79b")
    BOT_TOKEN = getenv("BOT_TOKEN", "7623920537:AAEplKS_apaZ-yDodJKZlATGdHd55eDwc6U")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "BQFSNtkAT5npiGKtiQbpSX4DQMrebG7JwIZbf_XzsxeHn1i2tk2IAIX2Y7VC4VlZAhn2Vge-fyDKFidbOM1faE6SbTaky8vrdr30fvy2yharl5Sn4pRKFpSIrvMzouml-qqV6nQUxH9g5T-rphcH83HnTEVTQu5uyJd10akHv8stTgA7_ESqv9VZcQ7UjmzkVQqJDkzB31qWl0HhNuhCDvWoQog4xCUDuVD8QpfivJrF2mPxxEV3QDvPUE5kEA9fCcTHMgCdxe7rkwTSJCUqD3V49vjiW1MZSiMIvlj32mavf2pbK6nYBWN5WMXyDv4qKG2xys2ExTgIOzE7PTPJjAJzcOgyzQAAAAFZCminAA")
    BASE_URL = getenv("BASE_URL").rstrip('/')
    DATABASE_URL = getenv("DATABASE_URL","mongodb+srv://kkvjhx15ef:Nq5qDQpj1XpHeCjY@cluster0.izercbs.mongodb.net/?retryWrites=true&w=majority")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL").split("-1001927512100,")]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "admin")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "surfTG")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "surfTG")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
    HIDE_CHANNEL = bool(getenv('HIDE_CHANNEL', 'False'))