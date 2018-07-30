
class LengthBuffer:
    """
    Temporarily holds a collection of objects. It will flush all the objects
    to the reducer once the collection is greater than max_size
    """

    def __init__(self,max_size):
        self.buffer = list()
        self.max_size = max_size
    #end function

    def register_reducer(self,r):
        """
        
        """
        self.reducers = r

    def add(self,obj):
        """
        Adds the object to the buffer's collection. Adding more than the 
        max_size will cause the buffer to flush
        """
        if self.max_size == None or self.max_size < 0:
            raise AttributeError('Must set max_size to an int greater than or equal to 0')

        self.buffer.append(obj)

        if len(self.buffer) > self.max_size:
            self.flush()
    #end function

    def flush(self):
        """
        Sends everything in the buffer to the reducer. Clears the buffer.
        """
        self.reducers.process(self.buffer)

        self.buffer=list()
    #end function



    def __len__(self):
        return len(self.buffer)
    #end function




#end class
