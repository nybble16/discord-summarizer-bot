from cachetools import LRUCache


class AsyncLRUCache:
    def __init__(self, maxsize=100):
        self.cache = LRUCache(maxsize=maxsize)

    async def get(self, key):
        return self.cache.get(key)

    async def set(self, key, value):
        self.cache[key] = value
        if len(self.cache) > self.cache.maxsize:
            self.cache.popitem()
