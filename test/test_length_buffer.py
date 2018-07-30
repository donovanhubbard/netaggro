from unittest import TestCase
from netaggro import length_buffer
from unittest.mock import patch, Mock, MagicMock

class TestLengthBuffer(TestCase):

    #def test_datetime(self):
    #    bucket.datetime(None, None)
    #    self.assertTrue(True)


    @patch('netaggro.reducer.Reducer')
    def test_add(self,mock_reducer):
        buff = length_buffer.LengthBuffer(5)
        self.assertEqual(len(buff),0)
        buff.add({'id':'test1'})
        self.assertEqual(len(buff),1)
        mock_reducer.process.assert_not_called()
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

    @patch('netaggro.reducer.Reducer')
    def test_adding_item_forces_flush(self,mock_reducer):
        obj = {'id':'test'}

        buff = length_buffer.LengthBuffer(0)
        buff.register_reducer(mock_reducer)
        buff.add(obj)
        
        self.assertEqual(len(buff),0)
        mock_reducer.process.assert_called_once_with([obj])
    #end function

    @patch('netaggro.reducer.Reducer')
    def test_adding_multiple_objects_forces_flush(self,mock_reducer):
        obj1 = {'id':'test'}
        obj2 = {'id':'test'}

        buff = length_buffer.LengthBuffer(1)
        buff.register_reducer(mock_reducer)
        buff.add(obj1)
        buff.add(obj2)
        
        self.assertEqual(len(buff),0)
        mock_reducer.process.assert_called_once_with([obj1,obj2])
    #end function

    @patch('netaggro.reducer.Reducer')
    @patch('netaggro.reducer.Reducer')
    def test_adding_multiple_reducers_forces_flush(self,mock_reducer1,mock_reducer2):
        obj = {'id':'test'}
        buff = length_buffer.LengthBuffer(0)
        buff.register_reducer(mock_reducer1)
        buff.register_reducer(mock_reducer2)
        buff.add(obj)

        mock_reducer1.process.assert_called_once_with([obj])
        mock_reducer2.process.assert_called_once_with([obj])
    #end function
    

#end class


if __name__=='__main__':
    unittest.main()

