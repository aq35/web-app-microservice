import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

# 出力するディレクトリの指定
log_dir = "./storage/logs"

# ログファイル名の設定
today = datetime.now().strftime("%Y-%m-%d")
filename = os.path.join(log_dir, f"app_{today}.log")

# ログファイルの設定
handler = RotatingFileHandler(filename, maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)

# ロガーの設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# ログのフォーマットを設定
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)