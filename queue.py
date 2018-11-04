class Queue:
    def __init__(self):
        self.queue=list()

    def add(self,data):
        self.queue.insert(0,data)

    def size(self):
        return len(self.queue)
    def pop(self):
        self.queue.pop()
    def printq(self):
        for i in self.queue:
            print(i,)


def main():

    q = Queue()
    for i in range(10,20):
        q.add(i)

    print(q.size())

    q.pop()
    q.add(100)
    q.printq()
    print("*****************")
    q.pop()
    q.printq()

main()
