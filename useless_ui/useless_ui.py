'''
#*************************************************************************

                            Useless App:

#*************************************************************************
Description: - useless but hopefully beautiful;
             - app that changes its color and themes;
             - UI Modules.

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

import sys
import maya.cmds as cmds

import useless_theme_functions as uth
import useless_functions as ufx


# *************************************************************************
# UI:
# *************************************************************************


def useless_app(USERPATH):

    PATH_ICONS = USERPATH + r"\icon"
    sys.path.append(USERPATH)
    sys.path.append(PATH_ICONS)
    print("directories have been updated")

    ui_title = "Useless App"
    theme_color = [0.286, 0.286, 0.286]
    analogue_color = [0.2, 0.2, 0.2]
    complementary_color = [0.792, 0.195, 0.203]

    # DELETE if it already exists:
    if cmds.window(ui_title, exists=True):
        cmds.deleteUI(ui_title)

    window = cmds.window(ui_title, title="USELESS APP",
                         backgroundColor=theme_color,
                         resizeToFitChildren=True)

    # ************************************************************************
    # LAYOUT
    # ************************************************************************

    cmds.formLayout("useless_form_layout", backgroundColor=theme_color,
                    numberOfDivisions=100)
    theme_column = cmds.columnLayout("theme_column", adjustableColumn=True,
                                     rowSpacing=5)

    # THEME PANEL:
    # ************************************************************************
    theme_title = cmds.text("Change Theme:",
                            font="boldLabelFont", align="left")

    cmds.separator("theme_separator", backgroundColor=complementary_color,
                   style="none", height=3)

    cmds.iconTextButton("button_day", style='iconOnly',
                        image=PATH_ICONS + r'\day_icon.png',
                        backgroundColor=analogue_color,
                        command="useless_ui.uth.change_theme('day', USERPATH)")

    cmds.iconTextButton("button_night", style='iconOnly',
                        image=PATH_ICONS + r'\night_icon.png',
                        backgroundColor=analogue_color,
                        command="useless_ui.uth.change_theme('night', USERPATH)")

    cmds.iconTextButton("button_user", style='iconOnly',
                        image=PATH_ICONS + r'\user_icon.png',
                        backgroundColor=analogue_color,
                        command="useless_ui.uth.change_theme('user', USERPATH)")

    cmds.iconTextButton("button_default", style='iconOnly',
                        image=PATH_ICONS + r'\default_icon.png',
                        backgroundColor=analogue_color,
                        command="useless_ui.uth.change_theme('default', USERPATH)")
    cmds.setParent("..")

    # APP COLUMN:
    #************************************************************************
    app_column = cmds.columnLayout(adjustableColumn=True, rowSpacing=5)

    cmds.text("This is the space for the title:",
              font="boldLabelFont", align="center")
    cmds.separator("title_separator", backgroundColor=complementary_color,
                   style="none", height=3)
    cmds.text("This is the place where it should be the most powerful tool ever made",
              font="boldLabelFont", align="center")
    cmds.text("Sorry, I don't have to create it for this contest",
              font="boldLabelFont", align="center")
    cmds.separator("stuff_separator", backgroundColor=complementary_color,
                   style="none", height=3)

    # BUTTONS:
    cmds.rowLayout(numberOfColumns=2, adjustableColumn1=True)
    cmds.iconTextButton("useless_stuff_button", label="Set Idle",
                        width=190, style="textOnly",
                        backgroundColor=analogue_color,
                        command="useless_ui.ufx.set_idle()")
    cmds.iconTextButton("useless_random_button", label="I feel lucky",
                        style="textOnly",
                        width=190,
                        backgroundColor=analogue_color,
                        command='useless_ui.ufx.get_random_quotes()')
    cmds.setParent("..")

    cmds.columnLayout(adjustableColumn=True, rowSpacing=5)

    cmds.iconTextButton("useless_credits", label="CREDITS!",
                        style="textOnly",
                        width=190,
                        backgroundColor=analogue_color,
                        command='useless_ui.ufx.show_credits()')
    cmds.separator("buttons_separator", backgroundColor=complementary_color,
                   style="none", height=3)
    cmds.setParent("..")
    # SLIDERS:
    cmds.rowLayout(numberOfColumns=2, adjustableColumn1=True)

    cmds.intSliderGrp("useless_number_slider", field=True, label='Numbers',
                      value=0, min=0, max=10,
                      columnWidth=(1, 50),
                      columnAlign=[(1, "left"), (2, "left")])

    cmds.iconTextButton("useless_number", label="Pick it out!",
                        style="textOnly",
                        width=80,
                        backgroundColor=analogue_color,
                        command='useless_ui.ufx.pick_numbers()')
    cmds.setParent("..")
    cmds.separator("end_separator", backgroundColor=complementary_color,
                   style="none", height=3)

# MAIN LAYOUT:
# *********************************************************************
    cmds.formLayout("useless_form_layout", edit=True,
                    attachForm=[(theme_column, 'left', 5),
                                (app_column, 'right', 10)],
                    attachControl=[(app_column, 'left', 10, theme_column)])

    cmds.showWindow(window)
