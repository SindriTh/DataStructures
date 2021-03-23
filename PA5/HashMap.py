from Bucket import *

class HashMap:
    def __init__(self):
        ''' Initializes the HashMap class '''
        self._count = 0
        self._size = 4
        self._map = [Bucket() for _ in range(self._size)]

    def _request_rebuild(self):
        ''' Determines if a rebuild is neccesary '''
        if self._count >= self._size * 1.2:
            self._rebuild()

    def _rebuild(self):
        ''' Rebuilds the array with double the size '''
        self._size *= 2
        temp_lis = [Bucket() for _ in range(self._size)]
        for i in range(int(self._size/2)):
            curr_node = self._map[i]._head
            while curr_node != None:
                temp_lis[self._get_hashed_index(curr_node.key)].insert(curr_node.key,curr_node.data)
                curr_node = curr_node.next
        self._map = temp_lis
    
    def _get_hashed_index(self,key):
        ''' Returns the bucket index for the key '''
        return hash(key) % self._size

    def insert(self,key,data):
        ''' Inserts data into the correct bucket '''
        self._request_rebuild()
        self._map[self._get_hashed_index(key)].insert(key,data)
        self._count += 1

    def update(self,key,data):
        ''' Updates the data of a specific item '''
        self._map[self._get_hashed_index(key)].update(key,data)
    
    def find(self,key):
        ''' Returns the data associated with a specific key '''
        return self._map[self._get_hashed_index(key)].find(key)

    def contains(self,key):
         ''' Returns a boolean weather or not the key is found '''
         return self._map[self._get_hashed_index(key)].contains(key)
    
    def remove(self,key):
        ''' Removes a specific item using its key '''
        self._map[self._get_hashed_index(key)].remove(key)
        self._count -= 1
    
    def __setitem__(self,key,data):
        ''' Allows the setitem syntax '''
        try:
            self.update(key,data)
        except NotFoundException:
            self.insert(key,data)
    
    def __getitem__(self,key):
        ''' Allows the getitem syntax '''
        return self.find(key)
    
    def __len__(self):
        ''' Returns the number of datasets in the map '''
        return self._count


if __name__ == '__main__':
    hm = HashMap()
    hm.insert('1a','a')
    hm.insert('2a','b')
    hm.insert('3a','c')
    hm.insert('4a','d')
    hm.insert('5a','e')
    hm.insert('6a','f')
    hm.insert('7a','g')
    print(len(hm))
    print(hm.find('2a'))
    hm['3a'] = 'cc'
    sam = hm['3a']
    print(sam)
    hm.remove('1a')
    hm.remove('2a')
    hm.remove('3a')
    hm.remove('4a')
    print(len(hm))