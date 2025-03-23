def greet():
    bot_name = input("What is my name?" )
    creation_year = int(input("What year was I created? "))
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {creation_year}.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print("Let me guess your age.")
    three_into_age = int(input("How many times would 3 go into your age? "))
    five_into_age = int(input("How many times would 5 go into your age? "))
    seven_into_age = int(input("How many times would 7 go into your age? "))
    age = (three_into_age * 70 + five_into_age * 21 + seven_into_age * 15) % 105
    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input("What number would you like me to count to? "))
    current_number = 0
    while current_number <= num:
        print(current_number, '!')
        current_number += 1

def end():
    print('Congratulations, have a nice day!')

def test():
    print("Let's test your programming knowledge.")
    print("1. To repeat a statement multiple times.")
    print("2. To compare conditional statements.")
    print("3. To output statements to the console.")
    print("4. To  decompose a program into several small subroutines.")
    user_answer = int(input("Which one do you think is correct? "))

    while user_answer != 1:
            print("Wrong answer!, try again.")
            user_answer = int(input("Which one do you think is correct? "))
    print("Correct!")

greet()
remind_name()
guess_age()
count()
test()
end()
