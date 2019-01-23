def main():
    challenge1()
    #Python Program that Create a function that has a loop that quits with q. If the user doesn't enter q, ask them to 
    # input another string.
    
    #problem1
    # while (True):
    #     userInput = input("Enter quit to exit")
    #     if userInput != "quit":
    #         print(input("Please Try Again"))
    #     elif (userInput.lower() == ("quit")):
    #         print("Thank You for quitting")
    #         break


    #Problem 2
    #Python Program that has two functions and pass in numbers to be added, multiplied and averaged together


#
# def exercise2():
#     print(exercise2_helper(5,3,5,"sum"))
#     print(exercise2_helper(5,3,5,"product"))
#     print(exercise2_helper(5,3,5,"AVG"))
#
#
# def exercise2_helper(num1, num2, num3, operation):
#
#     if operation == "sum":
#         return (num1+num2+num3)
#     elif operation == "product":
#         return (num1*num2*num3)
#     elif operation == "AVG":
#         return ((num1 + num2 + num3)//3)

    #Bonus1
def challenge1():
    playerOne = int(input("How many stars do you want to see"))
    for playerOne in range(1, playerOne + 1):
        print("* ")
        print("\r")








if __name__ == '__main__':
    main()
