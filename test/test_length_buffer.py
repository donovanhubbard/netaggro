import unittest
from netaggro import length_buffer

class TestBucket(unittest.TestCase):

    #def test_datetime(self):
    #    bucket.datetime(None, None)
    #    self.assertTrue(True)


    def test_add(self):
        buff = length_buffer.LengthBuffer(5)
        self.assertEqual(len(buff),0)
        buff.add({'id':'test1'})
        self.assertEqual(len(buff),1)



    

#end class

if __name__=='__main__':
    unittest.main()

