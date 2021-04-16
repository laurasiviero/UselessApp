'''
#*************************************************************************

                            Useless:

#*************************************************************************
Description: - useless but hopefully beautiful;
             - app that changes its color and themes;
             - button functions.

#*************************************************************************

 Author: Laura Siviero
         laura.seav@gmail.com
 
 License: MIT https://github.com/laurasiviero/UselessApp/blob/main/LICENSE
 
 Date 2021.04.17

#*************************************************************************
'''

import maya.cmds as cmds
import random
import webbrowser


def set_idle():
    print("\n*****************************************")
    print("****************  STUFF:  ***************")
    print("*****************************************")
    cmds.warning('Is something happened? Nope, sorry')


def show_credits():
    print("\n*****************************************")
    print("***********  INTRICATE STUFF:  **********")
    print("*****************************************")
    webbrowser.open("https://it.linkedin.com/in/laura-siviero")


def get_random_quotes(): 
    quotes = ["42 is the answer to everything",
              "Be yourself; everyone else is already taken.",
              "Be nice to nerds. You may end up working for them. We all could.",
              "Creativity is knowing how to hide your sources",
              "Never memorize something that you can look up.",
              "Two wrongs don't make a right, but they make a good excuse.",
              "I like work: it fascinates me. I can sit and look at it for hours.",
              "Never let your sense of morals prevent you from doing what is right.",
              "Time flies like an arrow; fruit flies like a banana.",
              "My tastes are simple: I am easily satisfied with the best.",
              "I suppose I'll have to add the force of gravity to my list of enemies.",
              "If writers wrote as carelessly as some people talk, then adhasdh asdglaseuyt[bn[ pasdlgkhasdfasdf.",
              "Don't Panic.",
              "Today was good. Today was fun. Tomorrow is another one.",
              "Wisdom comes from experience. Experience is often a result of lack of wisdom."]

    index = random.randint(0, len(quotes[:-1]))
    print ("\n")
    cmds.warning(quotes[index])


def pick_numbers():
    user_number = cmds.intSliderGrp("useless_number_slider", query=True, value=True)
    cmds.warning ("You chose " + str(user_number) + ", such a great pick!")