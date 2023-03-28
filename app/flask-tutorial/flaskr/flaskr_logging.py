import logging
from datetime import datetime, timedelta
# import pytz


def log_config(app):
    # ロガーを生成する
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.INFO)

    # フォーマッターを生成する
    # tz = pytz.timezone('Asia/Tokyo')
    datefmt = '%Y-%m-%d %H:%M:%S %Z'
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s:%(name)s:%(message)s', datefmt=datefmt)

    # フォーマッターにタイムゾーンを設定する
    def jst_converter(*args):
        utc_dt = datetime.utcnow()
        jst_dt = utc_dt + timedelta(hours=9)
        return jst_dt.timetuple()

    formatter.converter = jst_converter

    # ハンドラーを生成する
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    # ロガーにハンドラーを設定する
    logger.addHandler(handler)

    # Flaskのロガーにロガーを設定する
    app.logger.addHandler(logger)


def sqlalchemy_logging_config(log_path):
    # SQLAlchemyのLoggerオブジェクトを取得する
    engine_logger = logging.getLogger('sqlalchemy.engine')
    # ログレベルを設定する
    engine_logger.setLevel(logging.INFO)
    # フォーマッターを生成する
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s:%(name)s:%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %Z'
        )
    # ファイルハンドラーを生成する
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)
    # SQLAlchemyのLoggerオブジェクトにファイルハンドラーを追加する
    engine_logger.addHandler(file_handler)
