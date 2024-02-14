#Introduction of Hyperbot
def introduction():
    print("Hello! My name is Hyperbot.")
    print("I was created in 2024.")

#Ask and save name of user
def name():
    print("Please, remind me your name.")
    user_name = input()
    print(f"What a great name you have, {user_name}!")
    return user_name

#Guess the users age
def age():
    print("Let me guess your age.")
    print("Enter the remainders of dividing your age by 3, 5 and 7.")
    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    user_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {user_age}; that's a good time to start programming!")
    return user_age

#Count
def count():
    print('Now I will prove to you that I can count to any number you want.')
    user_count_number = int(input())
    counter = 0
    while counter <= user_count_number:
        print(counter, end=' ! \n')
        counter += 1

#Simple quiz
def quiz():
    answer_correct = False
    print("Why do we use methods?", 
          "1. To repeat a statement multiple times.", 
          "2. To decompose a program into several small subroutines.", 
          "3. To determine the execution time of a program.",
          "4. To interrupt the execution of a program.",
          sep='\n')
    while answer_correct == False:
        user_answer = int(input())
        if user_answer == 2:
            answer_correct = True
        else:
            print("Please, try again.")

#Run functions
introduction()
u_name = name()
u_age = age()
count()
quiz()

#Bot completed
print('Congratulations, have a nice day!')