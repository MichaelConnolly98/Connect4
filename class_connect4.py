


"""import math



class Slot:
    def __init__(self, index, slot, coords):
        self.colour = None
        self.index = index
        self.x = coords.x
        self.y = coords.y


 # Get the next slot in a given direction
    def next_slot(offsetX, offsetY):
        return self.parent.get(self.x + offsetX, self.y + offsetY)



class Slots:
 # Creates an array-like object of indexed slot objects
    def __init__(self, size=GRID_SIZE):
       self.size = size
    
    length = size ** 2;
 # 'this' same as 'self' in python
 # so the following will create self.0 = new Slot(...), self.1 = new Slot(...) etc
 # making an array like object
    slots = array_map(
 new Range(length),
 (i) => new Slot(this, i, this._getXY(i, size, length))
 );
 # Applies the map of slots to this (self) object
    def array_push(this, slots):
        self.size = size


 # Check if a given x, y coordinate is within the grid bounds
    def _withinBounds(x, y):
        return x >= 0 and x < self.size and y >= 0 and y < self.size

 # Get the x, y grid coordinates of a given index
    def _getXY(index, size, length):
        if (index >= length):
            print('Index out of bounds')

        if (index < 0):
            index = length + index

        x = index % size 
        y = math.floor(index / size)
        return x + y
 

    def get(x, y):
        if not(self._withinBounds(x, y)):
            return None
        return self[x + y * self.size]

    def getXY(index):
        return self._getXY(index, self.size, self.length)

    def Symbol_iterator():
        return new Iterator(this)


# grid size 8x8
slots = Slots(8)
# get slot by x, y
slot = slots.get(7, 3)
# get offset slots from that slot (xOffset, yOffset)
print(slot.next_slot(1, 0))
# null - out of bounds
print(slot.next_slot(0, 1))
# { colour: null, index: 39, slot: {}, parent: Slots, x: 7, y: 4 }
print(slot.nextSlot(-1, -1))
# { colour: null, index: 22, slot: {}, parent: Slots, x: 6, y: 2 }"""