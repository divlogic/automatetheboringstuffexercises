import sys

def collatz(number):
    if number % 2 == 0:
        answer = number // 2
        print(answer)
        return answer
    else:
        answer = 3 * number + 1
        print(answer)
        return answer

try:
    while True:
        global number
        number = None
        print('Enter number:')
        while number == None:
            try:
                number = int(input())
            except ValueError:
                print('You must enter an integer.')

        while number != 1:
            number = collatz(number)

except KeyboardInterrupt:
    sys.exit()