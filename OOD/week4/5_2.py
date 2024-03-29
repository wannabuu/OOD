class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_Node = Node(item)
        if(self.isEmpty()):
            self.head = new_Node
            self.tail = new_Node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_Node
            new_Node.previous = self.tail
            self.tail = new_Node

    def addHead(self, item):
        new_Node = Node(item)
        if L.isEmpty():
            self.head = new_Node
            self.tail = new_Node
        else:
            current = self.head
            new_Node.next = self.head
            current.previous = new_Node
            self.head = new_Node
            while current.next != None :
                current = current.next
            self.tail = current

    def insert(self, pos, item):
        new_Node = Node(item)
        if L.isEmpty():
            self.head = new_Node
            self.tail = new_Node
        else:
            current = self.head
            if pos < 0 and -pos < L.size():
                for _ in range(L.size() - 1 + pos):
                    current = current.next
            elif -pos >= L.size():
                self.addHead(new_Node.value)
                return
            elif pos > L.size():
                self.append(new_Node.value)
                return
            else:
                for _ in range(pos-1):
                    current = current.next
            new_Node.next = current.next
            new_Node.previous = current
            current.next = new_Node
            current = new_Node
            if current.next != None :
                current = current.next
                current.previous = new_Node
            while current.next != None :
                current = current.next
            self.tail = current


    def search(self, item):
        if self.isEmpty():
            return "Not Found"
        else:
            current = self.head
            while current:
                if str(current.value) == str(item):
                    return "Found"
                else:
                    current = current.next
            return "Not Found"

    def index(self, item):
        n = 0
        if self.isEmpty():
            return -1
        else:
            current = self.head
            while current:
                if str(current.value) == str(item):
                    return n
                else:
                    current = current.next
                    n += 1
            return -1

    def size(self):
        current = self.head
        n = 0
        while current:
            current = current.next
            n += 1
        return n

    def pop(self, pos):
        if L.size() <= pos or pos < -1 or L.isEmpty():
            return "Out of Range"
        else:
            current = self.head
            if pos == 0:
                if current.next == None:
                    self.head = None
                    self.tail = None
                else:
                    current = current.next
            elif pos == self.size() -1:
                while current.next.next != None:
                    current = current.next
                current.next = current.next.next
            else:
                for _ in range(pos-2):
                    current = current.next
                current.next = current.next.next
            return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())