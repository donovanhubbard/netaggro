import logging


class LengthBuffer:
    """
    Temporarily holds a collection of objects. It will flush all the objects
    to the reducer once the collection is greater than max_size
    """

    def __init__(self,max_size):
        self.buffer = list()
        self.max_size = max_size
        self.reducers = list()
        self.logger = logging.getLogger(__name__)
    #end function

    def register_reducer(self,r):
        """
        Adds a new reducer that will recieve objects.
        """
        self.reducers.append(r)

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

        if self.reducers == None or len(self.reducers) == 0:
            self.logger.warn('buffer is being flushed, but there are no registered reducers to flush to')

        for r in self.reducers:
            r.process(self.buffer)

        self.buffer=list()
    #end function

    def __len__(self):
        """
        Returns how many objects are in the buffer
        """
        return len(self.buffer)
    #end function




#end class
