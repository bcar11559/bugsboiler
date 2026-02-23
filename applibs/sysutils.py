from applibs.logger import ApplicationLogger
logger = ApplicationLogger.logger

import platform

def get_platform():
    """Check if running micropython and log platform information."""
    platform_info = platform.platform()
    processor_info = platform.processor()
    if platform_info.startswith("MicroPython"):
        logger.debug(f'Running MicroPython: {platform_info}')
        logger.debug(f'Processor Info: {processor_info}')
        return True
    else:
        logger.debug(f'Running CPython: {platform_info} ')
        logger.debug(f'Processor Info: {processor_info} ')
        return False