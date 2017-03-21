
import random
numbers_generated = [0,0,0,0,0,0]

def main():
    pick_num = int(input("How many picks?"))
    count = 0
    while count < pick_num:
        for i in range(6):
            num = random.randint(1,45)
            if num in numbers_generated:
                num = random.randint(1,45)
            numbers_generated[i] = num
        numbers_generated.sort()
        print(numbers_generated)

        count += 1

main()