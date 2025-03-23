def greet(bot_name, birth_year):
    bot_name = input("What is my name?" )
    creation_year = int(input("What year was I created? "))
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {creation_year}.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input("What is your age divided by 3? "))
    rem5 = int(input("What is your age divided by 5? "))
    rem7 = int(input("What is your age divided by 7? "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input("What number would you like me to count to? "))
    current_number = 0
    while current_number <= num:
        print(current_number, '!')
        current_number += current_number

def end():
    print('Congratulations, have a nice day!')

def test():
    print("Let's test your programming knowledge.")
    question = int(input("What are loops used for? Enter the Answer Number: "))
    answer1 = "1. To repeat a statement multiple times.\n2. To decompose a program into several small subroutines.\n3. To determine the execution time of a program.\n4. To interrupt the execution of a program."
    answer2 = "2. To compare conditional statements."
    answer3 = "3. To output statements to the console."
    answer4 = "4. To  decompose a program into several small subroutines."
    if question == 1:
        end()
    else:
        print("Please, try again.")

greet()
remind_name()
guess_age()
count()
test()
end()
