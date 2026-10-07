class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        boats = 0
        people.sort()
        n = len(people)
        left = 0
        right = n-1
        while left <= right:
            if people[left] + people[right] <= limit:
                boats+=1
                right -=1
                left +=1
            else:
                boats+=1
                right-=1
        return boats
