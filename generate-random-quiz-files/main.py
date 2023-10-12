import random
import os
from dict import capitals

def generate_random_quiz_files():
    # Create a directory to store quiz and answer key files
    if not os.path.exists('quizzes'):
        os.mkdir('quizzes/')
    if not os.path.exists('quizzes/questions'):
        os.makedirs('quizzes/questions')
    if not os.path.exists('quizzes/answers'):
        os.makedirs('quizzes/answers')
        
    # Generate 35 quiz files.
    for quizNum in range(35):
        # Create the quiz and answer key files.
        # add other comments
        pass
        

if __name__ == '__main__':
    generate_random_quiz_files()
    
