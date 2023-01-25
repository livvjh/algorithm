class Solution:
    @staticmethod
    def can_construct(ransom_note: str, magazine: str) -> bool:
        if 1 <= len(ransom_note) and len(magazine) <= 100000:
            temp_magazine = magazine
            for r in ransom_note:
                if r not in temp_magazine:
                    return False
                else:
                    temp_magazine = temp_magazine.replace(r, '', 1)
            return True


print(Solution.can_construct(ransom_note='aa', magazine='aab'))
