class Piece:
    size = -1

    @staticmethod
    def buildPiece(size):
        retVal = Piece()
        retVal.size = size
        return retVal


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def print(self):
        for x in range(0, len(self.items) - 1):
            print(" " + str(x) + " | " + " " + str(self.items[x].size))

class Stick:
    stack = Stack()

    def addPiece(self, piece):
        self.stack.push(piece)

    def removePiece(self):
        return self.stack.pop() if not self.stack.isEmpty() else None

    def print(self):
        self.stack.print()


def randoff(i, a, b, c):
    if i <= 0 : return
    randoff(i-1, a, c, b)
    c.addPiece(a.removePiece())
    randoff(i-1, b, a , c)





def main():
    a = Stick()
    b = Stick()
    c = Stick()

    pieceCount = 0
    for x in range(8, 1, -1):
        a.addPiece(Piece.buildPiece(x))
        pieceCount = 1 + pieceCount
    printSticks(a, b, c)
    randoff(pieceCount, a, b, c)
    printSticks(a, b, c)


def printSticks(_a, _b, _c):
    print("A: ")
    _a.print()
    print()
    print("B: ")
    _b.print()
    print()
    print("C: ")
    _c.print()
    print()


if __name__ == "__main__":
    main()