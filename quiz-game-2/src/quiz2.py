''' In this program, instead of having a fixed set of questions and 
answers entered within the code, nations and their capitals are 
sourced from a dataset using Pandas. Using random functions, a random nation and 
its capital will be chosen for the quiz.'''

import pandas as pd
import random, time, os

# Setting the Working Directory
os.chdir(r'quiz-game-2/src')
# print(os.getcwd())

""" 
# Pleasantries
print("Welcome to Geopolitical Quiz!!!")
print("Would you like to participate in this quiz? ")
play = input().lower()

if play not in ['yes', 'y', '1']:
    quit()
 """
# Sourcing data from given dataset - country-list.csv
df = pd.read_csv("../data/country-list.csv")

print(df.columns)
# 5 questions were given in this quiz

q_data = df.sample(n = 5, replace = False)

print(q_data['country'])