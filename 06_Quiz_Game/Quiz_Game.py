# Mini quiz game

# Creation of a dicctionary with the questions, every of which is another dictionary with the questions and answers
quiz_questions = {
    'question1':{
    'question' : 'Which is the capital of Spain?', 
    'answer': 'Madrid'
    },
    'question2':{
    'question' : 'Which is the capital of Germany?', 
    'answer': 'Berlin'
    },
    'question3':{
    'question' : 'Which is the capital of Italy?', 
    'answer': 'Roma'
    },
    'question4':{
    'question' : 'Which is the capital of France?', 
    'answer': 'Paris'
    },
    'question5':{
    'question' : 'Which is the capital of Portugal?', 
    'answer': 'Lisbon'
    },
    'question6':{
    'question' : 'Which is the capital of Switzerland?', 
    'answer': 'Bern'
    },
    'question7':{
    'question' : 'Which is the capital of Austria?', 
    'answer': 'Vienna'
    }
}

# Variable to save the score
score = 0

# For loop to ask every of the questions and ask for an answer
for key, value in quiz_questions.items():
    print(value['question'])
    answer = input('Answer?: ')

# If statement to check if the answer is correct and add 1 to the score 
if answer.lower() == value['answer'].lower():
    print('Correct')
    score += 1
    print(f'Your score is: {score}')
    print("")
    print("")
else: # Else statement in case the answer is not correct
    print('NOOOOOO!')
    print(f'The answer is: {value['answer']}')
    print(f'Your score is {score}')
    print("")
    print("")

print(f'You got {score} out of 7 questions correctly')
print(f'Your percentage is {score/7 * 100}%')
