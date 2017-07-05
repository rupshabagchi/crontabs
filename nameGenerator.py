"""
Generates a random firstname and lastname. Helps while coming up with names for building web pages and dashboards
"""
import random, string

vowels='aeiou'
consonants='bcdfghjklmnpqrstvwxzy'


starting_with=input("Name starting with?")
name_length=input("length of name?")

def generate_name():
    i=2
    name=starting_with+random.choice(vowels)
    while i < (name_length):
        i+=1
        name=name+random.choice(string.ascii_lowercase)
    return name

for i in range(2):
    print(generate_name())
