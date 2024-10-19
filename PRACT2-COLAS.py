class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 

class Queue:
    def __init__(self):
        self.top = None  
        self.tail = None 
        self.size = 0  

    def está_vacío(self):
        return self.size == 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.está_vacío():
            self.top = new_node  
        else:
            self.tail.next = new_node  
        self.tail = new_node 
        self.size += 1
        print(f"Agregado: {item}")

    def dequeue(self):
        if self.está_vacío():
            print("La cola está vacía, no se puede eliminar.")
            return None
        removed_item = self.top.data
        self.top = self.top.next  
        self.size -= 1
        if self.está_vacío():
            self.tail = None  
        print(f"Eliminado: {removed_item}")
        return removed_item

    def front(self):
        if self.está_vacío():
            return None
        return self.top.data

    def print_info(self):
        print("\n********* QUEUE DUMP *********")
        print(f"Size: {self.size}")
        current_node = self.top
        index = 1
        while current_node:
            print(f"** Element {index}")
            print(f"   Customer: {current_node.data['customer']}")
            print(f"   Quantity: {current_node.data['qtty']}")
            print("   ------------")
            current_node = current_node.next
            index += 1
        print("******************************\n")

    def get_nth(self, pos):
        if pos <= 0 or pos > self.size:
            return None
        current_node = self.top
        for _ in range(pos - 1):
            current_node = current_node.next
        return current_node.data

queue = Queue()
queue.enqueue({'customer': 'cust1', 'qtty': 20})
queue.enqueue({'customer': 'cust2', 'qtty': 30})
queue.enqueue({'customer': 'cust3', 'qtty': 40})
queue.enqueue({'customer': 'cust4', 'qtty': 50})

queue.print_info()

print(f"Primer elemento en la cola: {queue.front()}")
queue.dequeue()
queue.print_info()

nth_element = queue.get_nth(3)
print(f"Tercer elemento en la cola: {nth_element}")
