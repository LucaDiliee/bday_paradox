import streamlit as st
st.title("Birthday collision calculator")

st.write("hi user, tell me how many people you want in the class")

number = st.number_input("how many?")

from random import randint

if st.button("press me"):
    c = [randint(1,365) for _ in range(int(number))]

def generate_class(n):
   return [randint(1,365) for _ in range (n)]

def count(e,l):
   return sum([x == e for x in l])

def create_calendar(list_of_birthday):
   return [count(x,list_of_birthday) for x in range (1,366)]

class_requested = generate_class(int(number))

calendar_of_requested_class = create_calendar(class_requested)

def check_if_there_are_reps(list_of_birthdays):
   calendar = create_calendar(list_of_birthdays)
   return max(calendar) >= 2

experiments = [check_if_there_are_reps(generate_class(int(number))) for _ in range (1000)]

st.write("the probability to have repetition for the requested number of people is:", (sum(experiments)/1000))