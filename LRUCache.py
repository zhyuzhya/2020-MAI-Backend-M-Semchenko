from collections import OrderedDict
 
class LRUCache:
 
    def __init__(self, capacity: int = 10) -> None:
        self.cache = OrderedDict()
        self.capacity = capacity
 
    def get(self, key: str) -> str:
        if key not in self.cache:
            return ''
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
 
    def set(self, key: str, value: str) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

    def rem(self, key: str) -> None:
        del self.cache[key]


cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
print(cache.get('Jesse')) # вернёт 'James'
cache.rem('Walter')
print(cache.get('Walter')) # вернёт ''
