class Solution:
    def compress(self, chars: List[str]) -> int:
        slow = 0
        fast = 0
        length = 0
        count = 0
        
        if len(chars) <= 1:
            return len(chars)

        while fast < len(chars):

            if chars[slow] == chars[fast]:
                fast += 1
                count += 1

            elif chars[slow] != chars[fast] and count < 2:
                chars[length] = chars[slow]
                slow = fast
                length += 1
                count = 0

            else:
                chars[length] = chars[slow]
                length += 1
                countSTr = str(count)
                for ch in countSTr:
                    chars[length] = ch
                    length += 1
                count = 0
                slow = fast


        if count > 1:
            chars[length] = chars[slow]
            length += 1
            countSTr = str(count)
            for ch in countSTr:
                chars[length] = ch
                length += 1
        else:
            chars[length] = chars[slow]
            length += 1
        return length 