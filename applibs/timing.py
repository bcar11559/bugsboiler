from applibs.logger import ApplicationLogger
logger = ApplicationLogger.logger

import time
import ntptime
from machine import RTC
from micropython import const

_TS_FORMAT = const("{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}.{:03d}Z")

rtc = RTC()

def set_clock(ntpserver='svl1.ntp.se', ntptimeout=5):
    '''
    Set the board RTC with the NTP time.
    '''
    try:
        ntptime.host = ntpserver
        ntptime.timeout = ntptimeout
        ntptime.settime()
        logger.debug(f"RTC set to {timestamp()} from {ntpserver}")
    except OSError as e:
        if 'ETIMEDOUT' in str(e):
            logger.exception(f"RTC set time from {ntpserver} failed due to timeout.")
        else:
            logger.exception(f"RTC set time from {ntpserver} failed.")


def timestamp(time_secs=None):
    """Format the time as a formatted string timestamp."""
    if time_secs is None:
        if rtc is None:
            return time.time()  
        else:
            # (year, month, day, weekday, hours, minutes, seconds, microseconds)
            time_tuple = rtc.datetime()
            return _TS_FORMAT.format(
                time_tuple[0],
                time_tuple[1],
                time_tuple[2],
                time_tuple[4],
                time_tuple[5],
                time_tuple[6],
                time_tuple[7],
            )
    else:
        # (year, month, mday, hour, minute, second, weekday, yearday)
        time_tuple = time.localtime(time_secs)
        return _TS_FORMAT.format(
            time_tuple[0],
            time_tuple[1],
            time_tuple[2],
            time_tuple[3],
            time_tuple[4],
            time_tuple[5],
            0,
        )