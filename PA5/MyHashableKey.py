class MyHashableKey:
    def __init__(self,int_val,str_val):
        self.int = int_val
        self.str = str_val

    def __eq__(self,other):
        return self.int == other.int and self.str == other.str

    def __hash__(self):
        ''' Returns the class' hash value '''
        total = 0
        for i in range(len(self.str)):
            # The +i in the total algorithm makes it so two keys with the same intiger and
            # anagrammatical strings dont share the same hash value. (Or if their ASCII number sums happen to be the same value)
            total += (ord(self.str[i]) **(self.int+i+1))
        total += self.int
        return total 



if __name__ == '__main__':
    key = []
    leng = 8
    for i in range(400):
        key.append(MyHashableKey(i,f"{i*4}"))
    lis = []
    for i in range(400):
        index = hash(key[i]) % leng
        lis.append(index)
    for i in range(leng):
        print(f"{i} = {lis.count(i)}")

    key1 = MyHashableKey(0,'ab')
    key2 = MyHashableKey(0,'ba')
    print(hash(key1))
    print(hash(key2))


