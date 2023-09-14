class utils:
    def reverse(number):
        try:
            int(number)

        except:
            print("Please enter an integer, invalid input!")

        else:
            converted = str(number)
            reversed = converted[::-1]
            return reversed


input = input("Please enter a number to reverse: ")
num = utils.reverse(input)
print(num)