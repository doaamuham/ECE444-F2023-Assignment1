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


    def formatter(number):
        try:
            check = int(number)

        except:
            print("Please enter an integer, invalid input!")
        
        else:
            
            return bin(check), oct(check)
            

input = input("Please enter an integer: ")
num_binary = utils.formatter(input)
print(num_binary)