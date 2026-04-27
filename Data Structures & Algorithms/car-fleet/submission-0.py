class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(sorted(zip(position,speed), reverse=True))
        print(cars)
        stack = [(cars[0][0], cars[0][1])]
        fleetCount = 0

        for i in range (len(cars)):
            if (target - cars[i][0])/cars[i][1] <= (target - stack[-1][0])/stack[-1][1]:
                continue
            else:
                stack.append((cars[i][0], cars[i][1]))
        return len(stack)





