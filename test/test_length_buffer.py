import unittest
from netaggro import length_buffer

class TestLengthBuffer(unittest.TestCase):

    #def test_datetime(self):
    #    bucket.datetime(None, None)
    #    self.assertTrue(True)


    def test_add(self):
        buff = length_buffer.LengthBuffer(5)
        self.assertEqual(len(buff),0)
        buff.add({'id':'test1'})
        self.assertEqual(len(buff),1)
    #end function

    def test_adding_with_no_max_size_throws_exception(self):
        buff = length_buffer.LengthBuffer(5)
        buff.max_size = None

        with self.assertRaises(AttributeError) as context:
            buff.add({'id':'test'})

        self.assertTrue(context)
    #end function


    def test_adding_with_negative_max_size_throws_exception(self):
        buff = length_buffer.LengthBuffer(5)
        buff.max_size = -1

        with self.assertRaises(AttributeError) as context:
            buff.add({'id':'test'})

        self.assertTrue(context)
    #end function


    

#end class

if __name__=='__main__':
    unittest.main()

