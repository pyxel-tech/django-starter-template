import logging

logger = logging.getLogger(__name__)


def create_log(message: str, level: str = 'info'):
    level = level.lower()
    log_func = getattr(logger, level, logger.info)
    log_func(message)
