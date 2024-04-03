class MyQueue:

    def __init__(self):
        self.s1_help = []
        self.s2_queue = []

    def push(self, x: int) -> None:
        self.s1_help.append(x)
        self.s2_queue = self.s1_help[::-1]

    def pop(self) -> int:
        popped = self.s2_queue.pop()
        self.s1_help = self.s2_queue[::-1]
        return popped

    def peek(self) -> int:
        return self.s2_queue[-1]

    def empty(self) -> bool:
        return len(self.s2_queue) == 0
