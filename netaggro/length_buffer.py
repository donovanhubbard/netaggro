
class LengthBuffer:
    """
    Temporarily holds a collection of objects. It will flush all the objects
    to the reducer once the collection is greater than max_size
    """

    def __init__(self,max_size):
        self.buffer = list()
    #end function


    def add(self,obj):
        """
        Adds the object to the buffer's collection. Adding more than the 
        max_size will cause the buffer to flush
        """
        self.buffer.append(obj)
    #end function


    def __len__(self):
        return len(self.buffer)
    #end function


#end class
