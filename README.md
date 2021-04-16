*************************************************************************

Useless App:

*************************************************************************

Description:
  - useless but hopefully beautiful;
  - app that changes its color and themes;
  - Tool for Maya;

*************************************************************************
 License: MIT https://github.com/laurasiviero/UselessApp/blob/main/LICENSE
 Author: Laura Siviero
         laura.seav@gmail.com
 
 FOR QUICK OVERVIEW:
 Vimeo : https://vimeo.com/537818552
 
 Date: 2021.04.17
*************************************************************************

Instructions:
   - Put the useless_ui folder in the folder: 
     C:\Users\YOU\Documents\maya\20XX\scripts
   - Extract everything in the same location;
   - Launch maya;
   - Copy the following line script editor, make sure to change the path in the next lines too:


  import sys

  USERPATH = r"C:\Users\YOU\Documents\maya\20XX\scripts\useless_ui"
  
  sys.path.append(USERPATH)

  import useless_ui
  useless_ui.useless_app(USERPATH)
 
 
 - Feel free to add the code to your shelf
 - Replace the default shelf icon with the appropriate one: useless_ui\shelf_icon
 - Have fun!
