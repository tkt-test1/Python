from collections import OrderedDict
import time

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 使ったキーを末尾に移動
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 既存のキーを更新して末尾に移動
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # 最も古いアイテムを削除
            self.cache.popitem(last=False)

# ===== サンプル実行 =====
if __name__ == "__main__":
    lru = LRUCache(3)
    lru.put(1, "A")
    lru.put(2, "B")
    lru.put(3, "C")
    print(lru.cache)  # {1: 'A', 2: 'B', 3: 'C'}

    print(lru.get(1)) # "A" → 1を最近使った扱いに
    lru.put(4, "D")   # 容量超え → 最も古いキー2が削除
    print(lru.cache)  # {3: 'C', 1: 'A', 4: 'D'}

    print(lru.get(2)) # -1 (削除済み)
