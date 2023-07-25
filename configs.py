# (c) @PbAjay
import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "24237617"))
    API_HASH = os.environ.get("API_HASH", "8ec32b4085f1e3cf56c34a6afe1cc590")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5822225258:AAHzJCvixTXkRIvnTaIwaF0SNcQtXTz8Keo")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 5791145987))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://sonukumarkrbbu61:52EO6iqQL1diHODm@db.op4pluq.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001953206885"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
