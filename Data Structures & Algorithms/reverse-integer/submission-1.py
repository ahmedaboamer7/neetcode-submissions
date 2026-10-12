class Solution:
    def reverse(self, x: int) -> int:
        temp = abs(x)
        if x>0: lenth = len(str(x))
        else : lenth = len(str(x))-1
        count = 10 ** (lenth-1)
        ans = 0
        while temp>0:
            ans += ((temp%10) * count)
            count//=10
            temp //= 10
        if x < 0:
            ans = -1 * ans
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        return ans