import logging


logger = logging.getLogger("main")
logging.basicConfig(level=logging.INFO)

#파일로 저장
#stream_handler = logging.StreamHandler("my.log",mode="a",encoding="utf-8")
#logger.addHandler(stream_handler)

logger.debug("틀렸어")
logger.info("확인해")
logger.warning("조심해")
logger.error("에러났어")
logger.critical("심각해")