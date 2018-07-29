import unittest
import datetime
import pytz
from netaggro import bucket

class TestBucket(unittest.TestCase):

    #def test_datetime(self):
    #    bucket.datetime(None, None)
    #    self.assertTrue(True)

    def test_date_to_nearset_minute_by_sec(self):
        """
        attempt to bucket to nearest minute 
        """
        in_dt = datetime.datetime(2009,10,5,18,1,4,300,pytz.UTC)
        correct_dt = datetime.datetime(2009,10,5,18,1,0,0,pytz.UTC)
        out_dt = bucket.datetime_by_sec(60, in_dt)
        self.assertEqual(out_dt,correct_dt)
    #end function
    
    
    def test_date_to_nearset_5minute_by_sec(self):
        """
        attempt to bucket to nearest 5 minute 
        """
        in_dt = datetime.datetime(2009,10,5,18,17,45,300,pytz.UTC)
        correct_dt = datetime.datetime(2009,10,5,18,15,0,0,pytz.UTC)
        out_dt = bucket.datetime_by_sec(300, in_dt)
        self.assertEqual(out_dt,correct_dt)
    #end function

    def test_date_to_nearset_15minute_by_sec(self):
        """
        attempt to bucket to nearest 15 minute 
        """
        in_dt = datetime.datetime     (2009,10,5,18,17,45,300,pytz.UTC)
        correct_dt = datetime.datetime(2009,10,5,18,15,0,0,pytz.UTC)
        out_dt = bucket.datetime_by_sec(300, in_dt)
        self.assertEqual(out_dt,correct_dt)
    #end function
    
    def test_date_to_nearset_15minute_by_minute(self):
        """
        attempt to bucket to nearest 15 minute 
        """
        in_dt = datetime.datetime     (2009,10,5,18,17,45,300,pytz.UTC)
        correct_dt = datetime.datetime(2009,10,5,18,15,0,0,pytz.UTC)
        out_dt = bucket.datetime_by_min(15, in_dt)
        self.assertEqual(out_dt,correct_dt)
    #end function

    def test_date_timezone_should_match(self):
        """
        buckets to nearest minute but with none utc time zone
        """
        in_dt = datetime.datetime     (2009,10,5,18,17,45,300,pytz.timezone('US/Pacific'))
        correct_dt = datetime.datetime(2009,10,5,18,15,0,0,pytz.timezone('US/Pacific'))
        out_dt = bucket.datetime_by_min(15, in_dt)
        self.assertEqual(out_dt,correct_dt)
    #end function

    def test_date_already_bucketed(self):
        correct_dt = datetime.datetime(2009,10,5,18,15,0,0,pytz.UTC)
        in_dt = correct_dt
        out_dt = bucket.datetime_by_min(15, in_dt)
        self.assertEqual(out_dt,correct_dt)






#end class

if __name__=='__main__':
    unittest.main()

