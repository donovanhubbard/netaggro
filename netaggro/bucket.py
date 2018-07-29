from datetime import datetime
import calendar
import pytz


def datetime_by_sec(seconds,dt):
    """
    buckets date time object. Bucket size is in seconds
    """
    orig_tz = dt.tzinfo
    utc=dt.replace(tzinfo=pytz.UTC)
    #epoch = int(utc.strftime('%s'))
    epoch = calendar.timegm(utc.timetuple())
    offset = epoch % seconds
    new_epoch = epoch - offset
    utc =  datetime.fromtimestamp(new_epoch,pytz.UTC)
    return utc.replace(tzinfo=orig_tz)
    

def datetime_by_min(minutes,dt):
    """
    buckets date time object. Bucket size is in minutes
    """
    return datetime_by_sec(60*minutes,dt) 
