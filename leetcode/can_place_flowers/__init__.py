class Solution:
    def can_place_flowers(self, flowerbed: list[int], n: int) -> bool:
        size = len(flowerbed)
        count = 0
        for i, v in enumerate(flowerbed):
            if count == n:
                return True
            # 가운데 값이 0, 처음 index, 마지막 index
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (size - 1 == i or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
        return True if count >= n else False


print(Solution().can_place_flowers([1, 0, 0, 0, 1], 1))
# print(Solution().can_place_flowers([1, 0, 0, 0, 1], 2))
# print(Solution().can_place_flowers([1, 0, 0, 0, 0, 1], 2))
# print(Solution().can_place_flowers([0, 0, 1, 0, 1], 1))
