class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        new_head = Doubly_Linked_List_Node(x)
        new_head.next = self.head
        if self.head is not None:
            self.head.prev = new_head

        self.head = new_head
        if self.tail is None:
            self.tail = new_head

    def insert_last(self, x):
        new_tail = Doubly_Linked_List_Node(x)
        new_tail.prev = self.tail
        if self.tail is not None:
            self.tail.next = new_tail
        self.tail = new_tail
        if self.head is None:
            self.head = new_tail

    def delete_first(self):
        if self.head is None:
            return None

        old_head = self.head
        if old_head.next is None:
            self.tail = None
            self.head = None
        else:
            new_head = old_head.next
            new_head.prev = None
            self.head = new_head
        
        return old_head.item

    def delete_last(self):
        if self.tail is None:
            return None

        old_tail = self.tail
        if old_tail.prev is None:
            self.tail = None
            self.head = None
        else:
            new_tail = old_tail.prev
            new_tail.next = None
            self.tail = new_tail

        return old_tail.item

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        x1_prev = x1.prev
        x2_next = x2.next

        x1_prev.next = x2_next
        x2_next.prev = x1_prev

        x1.prev = None
        L2.head = x1
        x2.next = None
        L2.tail = x2
        
        return L2

    def splice(self, x, L2):
        x_next = x.next

        x.next = L2.head
        L2.head.prev = x

        L2.tail.next = x_next
        x_next.prev = L2.tail

        L2.head = None
        L2.tail = None
        pass
