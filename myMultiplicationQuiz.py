import random
import re
import time

quizLength = 10


def validateNumber(item):
    nonNumericRegex = re.compile(r'\D')
    if nonNumericRegex.search(item) == None:
        return True
    else:
        return False


def promptInt(prompt, tries=3, timeLimit=8):
    answer = None
    start = time.time()
    asking = True
    attempt = 1
    while asking:
        attempt += 1
        response = input(prompt)
        end = time.time()
        duration = int(end - start)

        if duration > timeLimit:
            print(
                f'Your response took longer than the time limit of {timeLimit} seconds.')
            asking = False
            break
        if attempt > tries:
            print(
                f'The number of attempts has exceeded the limit of {tries} tries')
            asking = False
            break

        answerIsValid = validateNumber(response)

        if answerIsValid == True:
            asking = False
            answer = int(response)
            break

    return answer


correct = 0
for i in range(quizLength):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = f'What is {num1} x {num2}?\n'
    answer = promptInt(prompt, timeLimit=2)
    if answer == num1*num2:
        correct += 1
        print('You got that correct!')
        time.sleep(1)

print(f'The final score is {correct}/{quizLength}')
