from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "21846639"))
        self.API_HASH = getenv("API_HASH", "2cebc99bd8378b5237b31ea8e7496d79")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8913524572:AAEVVBg7Aq2G5A8uaI-wjYMIVGWjujTLn-A")
        self.MONGO_URL = getenv("MONGO_DB_URI", "mongodb+srv://Devvusz:Devvuszxx05231@cluster0.3rfouod.mongodb.net/?appName=Cluster0")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1001973634248"))
        self.LOG_CHAT_ID = int(getenv("LOG_CHAT_ID", "-1004356536394"))
        self.OWNER_ID = int(getenv("OWNER_ID", "1499705163"))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("STRING_SESSION", "BQFNWm8AXgFl0DopZqvwxcFQBvu9Fp_TAOFpWYz3scJfkocXcef0WLe1Yg4M51yhW_eKjHsGJG3caHwXaxkea9ERh2Y7aFcXdA3qWPerdRFk7ULs76EN4nsXT6dFGcYeb7UuCUDz3mSDdijc9_6XYJi1-QoBuMrLWDH6zzBUBzq0WZCj5EY1v4DWvYY5q1e3RQx6ZRsC0S5l3mN2EMXIIQ2rlG7qPqcjNL6PqyRX6_wBb4UjghI5GjvWqbrFXfOPRnB_YxvJ1aOzNrNed7uY96spBVPlNJuSe-QqS69yEz7buTs0VY9SMbyZIU4ph2cWXPmdwKYGoPtY4yB0zjOI6BWuXA1b5AAAAABsFeBfAA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/fallenx")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
    
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://files.manuscdn.com/user_upload_by_module/session_file/310519663872339253/wOJoKQEpzmWqSsBR.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.manuscdn.com/user_upload_by_module/session_file/310519663872339253/TehaWblGJgJbhpRf.jpg")
        self.START_IMG = getenv("START_IMG", "https://files.manuscdn.com/user_upload_by_module/session_file/310519663872339253/FAygWDbnmPqKLAni.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
