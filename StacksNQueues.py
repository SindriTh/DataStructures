class Stack:
    def __init__(self):
        self.capacity = 4
        self.stack = [0]*self.capacity
        self.size = 0

    def pop(self):
        if self.size > 0:
            self.size -= 1
            popped = self.stack[self.size]
            self.stack[self.size] = 0
            return popped

    def push(self,value):
        if self.size >= self.capacity:
            self.resize()
        
        self.stack[self.size] = value
        self.size += 1


    def resize(self):
        self.resized_stack = [0]*self.capacity*2
        for i in range(self.capacity):
            self.resized_stack[i] = self.stack[i]

        self.stack = self.resized_stack
        self.capacity *= 2

    def __str__(self):
        outstring = ""
        for i in range(self.size):
            outstring += f" {self.stack[i]}"
        return outstring


# stakki = Stack()
# stakki.push(5)
# print(stakki)
# stakki.push(6)
# print(stakki)
# stakki.push(7)
# print(stakki)
# stakki.push(8)
# print(stakki)
# stakki.push(9)
# print(stakki)
# stakki.push(10)
# print(stakki)
# stakki.push(11)
# print(stakki)
# stakki.pop()
# print(stakki)
# stakki.pop()
# print(stakki)

class Queue:
    def __init__(self):
        self.capacity = 4
        self.queue = [0]*self.capacity
        self.startindex = 0
        self.stopindex = 0
        self.size = 0

    def remove(self):
        if self.size >= 1:
            removed = self.queue[self.startindex]
            self.queue[self.startindex] = 0
            self.startindex += 1
            self.size -= 1
            return removed

    def add(self,value):
        if self.startindex != 0 and self.stopindex == self.capacity:
            self.stopindex = 0
        elif self.startindex == self.stopindex or self.stopindex == self.capacity:
            self.resize()
        self.size += 1
        self.queue[self.stopindex] = value
        self.stopindex += 1


    def resize(self):
        self.resized_queue = [0]*self.capacity*2

        #if self.stopindex !=

        for i in range(self.capacity):
            self.resized_queue[i] = self.queue[i]

        self.queue = self.resized_queue
        self.capacity *= 2

    def __str__(self):
        outstring = ""
        if self.stopindex < self.startindex:
            for i in range(self.startindex,self.capacity):
                outstring += f" {self.queue[i]}"
            for i in range(self.stopindex):
                outstring += f" {self.queue[i]}"
        else:
            for i in range(self.startindex,self.stopindex):
                outstring += f" {self.queue[i]}"
        return outstring

queue = Queue()
queue.add(1)
print(queue)
queue.add(2)
print(queue)
queue.add(3)
print(queue)
queue.add(4)
print(queue)
queue.add(5)
print(queue)
queue.add(6)
print(queue)
queue.add(7)
print(queue)
print(queue.remove())
print(queue.remove())
print(queue)
queue.add(8)
print(queue)
queue.add(9)
print(queue)
queue.add(10)
print(queue)
queue.add(11)
print(queue)