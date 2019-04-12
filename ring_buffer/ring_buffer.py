class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # remove oldest and insert newest
    self.storage.pop(self.current)
    self.storage.insert(self.current, item)

    if self.current == 4:
      self.current = 0
    else:
      self.current +=1
    
  def get(self):
    # Return elements in a new array
    arr = []
    for x in self.storage:
      if x is not None:
        arr.append(x)
    return arr
    