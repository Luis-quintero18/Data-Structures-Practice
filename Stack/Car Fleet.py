"""
Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

Output: 3
"""

def carFleet(target, position, speed) -> int:
        # Create a new list of cars sorted in descending order based on position
        cars = sorted(zip(position, speed), reverse=True)
        print(cars)

        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            stack.append(time)
            print(stack)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                  stack.pop()
            print(f" After Pop: {stack}")

        return len(stack)

print(carFleet(10, [4,1,0,7], [2,2,1,1]))