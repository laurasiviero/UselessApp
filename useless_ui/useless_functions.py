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
 
 Date 17.03.2021
#*************************************************************************

The MIT License (MIT)

Copyright (c) 2021 laura siviero

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

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