class MyComparableKey:
    def __init__(self,int_value,string_value):
        self.int = int_value
        self.string = string_value
    
    def __lt__(self,other):
        return True if self.int < other.int or self.int == other.int and self.string < other.string else False


    # This is the slightly more readable version of the function.
    #  To a skilled programmer the oneline method should be readable enough, but just in case
    # We included the other way to do it.
    
    #def __lt__(self,other):
    #    if self.int < other.int:
    #        return True
    #    elif self.int == other.int:
    #        if self.string < other.string:
    #            return True
    #    return False