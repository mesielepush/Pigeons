from game import *

user = opening()
intro()
left_key, right_key = selection()
Session(left_key,right_key,user)
