'''
#*************************************************************************

                            Useless:

#*************************************************************************
Description: - useless but hopefully beautiful;
             - app that changes its color and themes;
             - UI functions.

#*************************************************************************

 Author: Laura Siviero
         laura.seav@gmail.com
 
 License: MIT https://github.com/laurasiviero/UselessApp/blob/main/LICENSE
 
 Date 2021.04.17

#*************************************************************************
'''



import sys
import maya.cmds as cmds

# *************************************************************************
# FUNCTIONS:
# *************************************************************************


def change_theme(theme, USERPATH):

    PATH_ICONS = USERPATH + r"\icon"
    sys.path.append(USERPATH)
    sys.path.append(PATH_ICONS)

    theme_color = [0.286, 0.286, 0.286]
    analogue_color = [0.2, 0.2, 0.2]
    complementary_color = [0.792, 0.195, 0.203]
    theme_code = ""

    # THEME VALUES:
    # *********************************************************************
    if theme == "day":
        theme_color = [0.63, 0.80, 0.85]
        analogue_color = [1, 0.98, 0.9]
        complementary_color = [0.96, 0.58, 0.11]
        theme_code = "theme01_"

    elif theme == "night":
        theme_color = [0.03, 0.14, 0.25]
        analogue_color = [0.1, 0.29, 0.45]
        complementary_color = [0.12, 0.44, 0.65]
        theme_code = "theme02_"

    # User Settings parameter:
    # ***************************************************
    elif theme == "user":
        cmds.colorEditor()
        if cmds.colorEditor(query=True, rgb=True):
            r, g, b = cmds.colorEditor(query=True, rgb=True)
        else:
            cmds.warning("Process Delete")

        # distribute colors:
        # *******************************
        if r + g + b <= 0.4:
            theme_color = [r, g, b]
            analogue_color = [(r + 0.1) * 2, (g + 0.1) * 2, (b + 0.1) * 2]
            complementary_color = [(r + 0.1) * 4, (g + 0.1) * 4, (b + 0.1) * 4]
            theme_code = "theme04_"

        elif r + g + b >= 2.4:
            theme_color = [r * 0.7, g * 0.7, b * 0.7]
            analogue_color = [r * 0.8, g * 0.8, b * 0.8]
            complementary_color = [r * 0.55, g * 0.55, b * 0.55]
            theme_code = "theme03_"

        else:
            theme_color = [r / 2, g / 2, b / 2]
            analogue_color = [r, g, b]
            complementary_color = [r * 2, r * 2, r * 2]
            theme_code = "theme03_"

    # CHANGE BUTTONS THEME:
    # ********************************************************************
    buttons = ["button_day", "button_night", "button_user", "button_default",
               "useless_stuff_button", "useless_random_button",
               "useless_credits", "useless_number"]

    for button in buttons:
        path_icon = cmds.iconTextButton(button, query=True, image=True)

        if path_icon:
            icon = path_icon.split("\\")[-1]
            if "theme" in icon:
                icon = icon.replace("theme", "")[3:]
            cmds.iconTextButton(button, edit=True, backgroundColor=analogue_color,
                                image=PATH_ICONS + "\\" + theme_code + icon)

        else:
            cmds.iconTextButton(button, edit=True,
                                backgroundColor=analogue_color)

    # CHANGE OTHER UI ELEMENTS:
    # ********************************************************************
    separators = ["theme_separator", "title_separator", "stuff_separator",
                  "buttons_separator", "end_separator"]

    for separator in separators:
        cmds.separator(separator, query=True, backgroundColor=True)
        cmds.separator(separator, edit=True,
                       backgroundColor=complementary_color)

    # CHANGE MAIN WINDOW UI ELEMENTS:
    # ********************************************************************
    cmds.formLayout("useless_form_layout", query=True,
                    backgroundColor=True)
    cmds.formLayout("useless_form_layout", edit=True,
                    backgroundColor=theme_color)
