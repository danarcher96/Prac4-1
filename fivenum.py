
numbers = []
def main():
    for i in range(4):
        userNum = input("Enter a number: ")
        numbers.append(userNum)

    print("The first number is", numbers[0])
    print("The last numbers is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))

main()

