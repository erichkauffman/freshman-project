from modGraphics import *
import tkinter
from tkinter import ttk
import random

class hangman: #creates buttons and text entry fields from tkinter
   def __init__(self, master):
       self.master = master
       self.var = ""
       self.text = ""

   def buttons(self): # creates easy and hard buttons
      master = self.master
      label = tkinter.ttk.Label(master, text = "Choose a difficulty")
      label.pack()
      buttonE = tkinter.ttk.Button(master, text = "Easy", command = self.chooseEasy)
      buttonE.pack()

      buttonH = tkinter.ttk.Button(master, text = "Hard", command = self.chooseHard)
      buttonH.pack()

   def chooseEasy(self): #if the user clicks easy, set var to "easy" and destroy window
       self.var = "easy"
       self.master.destroy()
       self.master.quit()

   def chooseHard(self):#if the user clicks easy, set var to "hard" and destroy window
       self.var = "hard"
       self.master.destroy()
       self.master.quit()

   def mode(self):
      master = self.master
      label = tkinter.ttk.Label(master, text = "Choose a mode")
      label.pack()
      buttonSig = tkinter.ttk.Button(master, text = "Singleplayer", command = self.chooseSig)
      buttonSig.pack()
      buttonMult = tkinter.ttk.Button(master, text = "Multiplayer", command = self.chooseMult)
      buttonMult.pack()

   def chooseSig(self):
      self.var = "single"
      self.master.destroy()
      self.master.quit()

   def chooseMult(self):
      self.var = "multi"
      self.master.destroy()
      self.master.quit()

   def enterWord(self):
      master = self.master
      label = tkinter.ttk.Label(master, text = "Enter a word")
      label.pack()
      entry = tkinter.ttk.Entry(master, width = 30, show = "*")
      entry.pack()
      enterButton = tkinter.ttk.Button(master, text = "Enter", command = lambda: self.enterFun(entry, label))
      enterButton.pack()

   def enterWordG(self):
      master = self.master
      label = tkinter.ttk.Label(master, text = "Enter your guess")
      label.pack()
      entry = tkinter.ttk.Entry(master, width = 30)
      entry.pack()
      enterButton = tkinter.ttk.Button(master, text = "Enter", command = lambda: self.enterFun(entry, label))
      cancelButton = tkinter.ttk.Button(master, text = "Cancel", command = self.chooseEasy)
      enterButton.pack()
      cancelButton.pack()

   def enterFun(self, widg, lab):
      master = self.master
      word = widg.get()
      if word.isalpha() and len(word) <= 15:
         self.text = word
         self.master.destroy()
         master.quit()
      elif len(word) > 15:
         lab.config(text = "The word must be 15 letters or less")
      else:
         lab.config(text = "The word must only have letters")

   def playAgain(self):
      master = self.master
      label = tkinter.ttk.Label(master, text = "Would you like to play again?")
      buttonY = tkinter.ttk.Button(master, text = "Yes", command = self.yesAgain)
      buttonN = tkinter.ttk.Button(master, text = "No", command = self.noAgain)
      label.pack()
      buttonY.pack()
      buttonN.pack()

   def yesAgain(self):
      master = self.master
      self.var = 0
      self.master.destroy()
      self.master.quit()

   def noAgain(self):
      master = self.master
      self.var = 1
      self.master.destroy()
      self.master.quit()
# END CLASS HANGMAN

def center_window(master, width = 300, height = 100):
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    master.geometry('%dx%d+%d+%d' % (width, height, x, y))

# creating parts for drawing
def creatHang():
    base = Rectangle(Point(80,160), Point(360,180))
    post = Rectangle(Point(210,180), Point(230,620))
    over = Rectangle(Point(120,620), Point(560,640))
    rope = Line(Point(520,620), Point(520,560))
    head = Circle(Point(520,530), 30)
    body = Line(Point(520,500), Point(520,390))
    lArm = Line(Point(520,470), Point(460,460))
    rArm = Line(Point(520,470), Point(580,460))
    lLeg = Line(Point(520,390), Point(470,280))
    rLeg = Line(Point(520,390), Point(570,280))
    parts = [base, post, over, rope, head, body, lArm, rArm, lLeg, rLeg]
    return parts

#create and draw spaces for letters
def creatSpac(word, win):
    for ik in range(len(word)):
        space = Line(Point(80 + 60 * ik, 70), Point(120 + 60 * ik, 70))
        space.draw(win)

#create and draw boxes for letters
def creatLetBox(win):
    for ik in range(6):
        for jk in range(4):
            letterBox = Rectangle(Point(620 + 80 * jk, 700 - 80 * ik), Point(660 + 80 * jk, 740 - 80 * ik))
            letterBox.draw(win)
    letterBox = Rectangle(Point(700, 220), Point(740, 260))
    letterBox.draw(win)
    letterBox = Rectangle(Point(780, 220), Point(820, 260))
    letterBox.draw(win)

#When a letter is clicked, it will guess that letter and remove it from graphics window
def chooseLet(win, used, letterList, click):
   while True:
      if click.getX() >= 620 and click.getX() <= 660 and click.getY() >= 700 and click.getY() <= 740 and "a" not in used:
         letSelect = "a"
         letterList[0].undraw()
         break
      if click.getX() >= 700 and click.getX() <= 740 and click.getY() >= 700 and click.getY() <= 740 and "b" not in used:
         letSelect = "b"
         letterList[1].undraw()
         break
      if click.getX() >= 780 and click.getX() <= 820 and click.getY() >= 700 and click.getY() <= 740 and "c" not in used:
         letSelect = "c"
         letterList[2].undraw()
         break
      if click.getX() >= 860 and click.getX() <= 900 and click.getY() >= 700 and click.getY() <= 740 and "d" not in used:
         letSelect = "d"
         letterList[3].undraw()
         break
      if click.getX() >= 620 and click.getX() <= 660 and click.getY() >= 620 and click.getY() <= 660 and "e" not in used:
         letSelect = "e"
         letterList[4].undraw()
         break
      if click.getX() >= 700 and click.getX() <= 740 and click.getY() >= 620 and click.getY() <= 660 and "f" not in used:
         letSelect = "f"
         letterList[5].undraw()
         break
      if click.getX() >= 780 and click.getX() <= 820 and click.getY() >= 620 and click.getY() <= 660 and "g" not in used:
         letSelect = "g"
         letterList[6].undraw()
         break
      if click.getX() >= 860 and click.getX() <= 900 and click.getY() >= 620 and click.getY() <= 660 and "h" not in used:
         letSelect = "h"
         letterList[7].undraw()
         break
      if click.getX() >= 620 and click.getX() <= 660 and click.getY() >= 540 and click.getY() <= 580 and "i" not in used:
         letSelect = "i"
         letterList[8].undraw()
         break
      if click.getX() >= 700 and click.getX() <= 740 and click.getY() >= 540 and click.getY() <= 580 and "j" not in used:
         letSelect = "j"
         letterList[9].undraw()
         break
      if click.getX() >= 780 and click.getX() <= 820 and click.getY() >= 540 and click.getY() <= 580 and "k" not in used:
         letSelect = "k"
         letterList[10].undraw()
         break
      if click.getX() >= 860 and click.getX() <= 900 and click.getY() >= 540 and click.getY() <= 580 and "l" not in used:
         letSelect = "l"
         letterList[11].undraw()
         break
      if click.getX() >= 620 and click.getX() <= 660 and click.getY() >= 460 and click.getY() <= 500 and "m" not in used:
         letSelect = "m"
         letterList[12].undraw()
         break
      if click.getX() >= 700 and click.getX() <= 740 and click.getY() >= 460 and click.getY() <= 500 and "n" not in used:
         letSelect = "n"
         letterList[13].undraw()
         break
      if click.getX() >= 780 and click.getX() <= 820 and click.getY() >= 460 and click.getY() <= 500 and "o" not in used:
         letSelect = "o"
         letterList[14].undraw()
         break
      if click.getX() >= 860 and click.getX() <= 900 and click.getY() >= 460 and click.getY() <= 500 and "p" not in used:
         letSelect = "p"
         letterList[15].undraw()
         break
      if click.getX() >= 620 and click.getX() <= 660 and click.getY() >= 380 and click.getY() <= 420 and "q" not in used:
         letSelect = "q"
         letterList[16].undraw()
         break
      if click.getX() >= 700 and click.getX() <= 740 and click.getY() >= 380 and click.getY() <= 420 and "r" not in used:
         letSelect = "r"
         letterList[17].undraw()
         break
      if click.getX() >= 780 and click.getX() <= 820 and click.getY() >= 380 and click.getY() <= 420 and "s" not in used:
         letSelect = "s"
         letterList[18].undraw()
         break
      if click.getX() >= 860 and click.getX() <= 900 and click.getY() >= 380 and click.getY() <= 420 and "t" not in used:
         letSelect = "t"
         letterList[19].undraw()
         break
      if click.getX() >= 620 and click.getX() <= 660 and click.getY() >= 300 and click.getY() <= 340 and "u" not in used:
         letSelect = "u"
         letterList[20].undraw()
         break
      if click.getX() >= 700 and click.getX() <= 740 and click.getY() >= 300 and click.getY() <= 340 and "v" not in used:
         letSelect = "v"
         letterList[21].undraw()
         break
      if click.getX() >= 780 and click.getX() <= 820 and click.getY() >= 300 and click.getY() <= 340 and "w" not in used:
         letSelect = "w"
         letterList[22].undraw()
         break
      if click.getX() >= 860 and click.getX() <= 900 and click.getY() >= 300 and click.getY() <= 340 and "x" not in used:
         letSelect = "x"
         letterList[23].undraw()
         break
      if click.getX() >= 700 and click.getX() <= 740 and click.getY() >= 220 and click.getY() <= 260 and "y" not in used:
         letSelect = "y"
         letterList[24].undraw()
         break
      if click.getX() >= 780 and click.getX() <= 820 and click.getY() >= 220 and click.getY() <= 260 and "z" not in used:
         letSelect = "z"
         letterList[25].undraw()
         break
      else:
         letSelect = ""
         break
   return letSelect

#create letters
def creatLet():
   a = Text(Point(640, 720), "a")
   b = Text(Point(720, 720), "b")
   c = Text(Point(800, 720), "c")
   d = Text(Point(880, 720), "d")
   e = Text(Point(640, 640), "e")
   f = Text(Point(720, 640), "f")
   g = Text(Point(800, 640), "g")
   h = Text(Point(880, 640), "h")
   i = Text(Point(640, 560), "i")
   j = Text(Point(720, 560), "j")
   k = Text(Point(800, 560), "k")
   l = Text(Point(880, 560), "l")
   m = Text(Point(640, 480), "m")
   n = Text(Point(720, 480), "n")
   o = Text(Point(800, 480), "o")
   p = Text(Point(880, 480), "p")
   q = Text(Point(640, 400), "q")
   r = Text(Point(720, 400), "r")
   s = Text(Point(800, 400), "s")
   t = Text(Point(880, 400), "t")
   u = Text(Point(640, 320), "u")
   v = Text(Point(720, 320), "v")
   w = Text(Point(800, 320), "w")
   x = Text(Point(880, 320), "x")
   y = Text(Point(720, 240), "y")
   z = Text(Point(800, 240), "z")

   alphaList = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
   return alphaList

def again():
   pRoot = tkinter.Tk()
   center_window(pRoot)
   app4 = hangman(pRoot)
   app4.playAgain()
   pRoot.mainloop()
   return app4.var

#Main
def main():
   print("Hi!")
   dic = open("/Users/erichkauffman/Code/Python/FinalProject/dictionary.txt", "r")
   dRoot = tkinter.Tk() #create mode buttons
   center_window(dRoot)
   app6 = hangman(dRoot)
   app6.mode() #ask mode
   dRoot.mainloop()
   mode = app6.var
   root = tkinter.Tk() #create difficulty buttons
   center_window(root)
   app = hangman(root)
   app.buttons()#ask difficulty
   root.mainloop()
   diff = app.var
   if mode == "multi":
      mRoot = tkinter.Tk() #create word entry window
      center_window(mRoot)
      app1 = hangman(mRoot)
      app1.enterWord()#ask for word
      mRoot.mainloop()
      word = app1.text
      word = word.lower()
      dic.close()
   if mode == "single":
      dicList = []
      for i in dic:
         dicList.append(i)
      wordMod = dicList[random.randrange(0, len(dicList))]
      word = wordMod[0: len(wordMod) - 1]
      dic.close()
   win = GraphWin("Hangman", 1000, 750) #create graphics window
   win.setCoords(0, 0, 1000, 750)
   creatSpac(word, win) #draws spaces
   parts = creatHang() #creates hangman parts (doesn't draw them)
   creatLetBox(win) #draws boxes for letters
   alphaPoint = creatLet() #creates letters
   for let in alphaPoint:
       let.setSize(24)
       let.draw(win) #draws letters
   rect = Rectangle(Point(130, 55), Point(250, 15)) #draws guess box
   rect.draw(win)
   guess = Text(Point(190, 35), "guess")
   guess.setSize(24)
   guess.draw(win)
   count = 0 #set accumulator to zero (used to determine win or loss)
   used = "" #sets guess storage to empty string
   canclChk = ""#used for comparing for canceling a guess
   while True:
       for ik in range(len(word)): #check if user has guessed all letters in word
           if word[ik] not in used:
               break
           elif len(word) - 1 == ik:
               count = 11
       if count == 11: #player wins
           won = Text(Point(350, 715), "You Won!")
           clkExit = Text(Point(350, 680), "Click to Exit")
           won.setSize(24)
           won.draw(win)
           clkExit.draw(win)
           for ik in range(len(word)):
              drawLet = Text(Point(100 + 60 * ik, 80), word[ik])
              drawLet.setSize(24)
              drawLet.draw(win)
           break
       if count == 10: #player loses
           won = Text(Point(350, 715), "You Lost!")
           clkExit = Text(Point(350, 680), "Click to Exit")
           won.setSize(24)
           won.draw(win)
           clkExit.draw(win)
           for ik in range(len(word)):
              drawLet = Text(Point(100 + 60 * ik, 80), word[ik])
              drawLet.setSize(24)
              drawLet.draw(win)
           break
       while True:
          click = win.getMouse() #click on window
          if click.getX() >= 130 and click.getX() <= 250 and click.getY() >= 15 and click.getY() <= 55: #if click is on guess button
             gRoot = tkinter.Tk()# create text entry field for guess
             center_window(gRoot)
             app3 = hangman(gRoot)
             app3.enterWordG()
             gRoot.mainloop()
             canclChk = app3.var
             if app3.var == "easy":
                break
             if app3.text.lower() == word:
                count = 11 # if guess is correct, set to win condition
             else:
                count = 10 # if guess is incorrect, set to lose condition
             break
          else:
             letter = chooseLet(win, used, alphaPoint, click) #user guesses letter
             if letter == "":# if user clicks, but not on a box, re-loop
                continue
             break
       if count == 10 or count == 11 or canclChk == "easy": #checks if condition has been set by guess button
          canclChk = ""
          continue
       used = used + letter #add letter to the letters guessed
       if letter in word: #check if letter is in word
           for ik in range(len(word)):
               if letter == word[ik]: #checking where to display guessed letter
                   drawLet = Text(Point(100 + 60 * ik, 80), letter)
                   drawLet.setSize(24)
                   drawLet.draw(win)
       else: # if guessed letter is not in the word, draw next peice of hangman
           if diff == "easy": #if easy, draw 1 piece and increment condition by 1
               parts[count].draw(win)
               count += 1
           else:
               parts[count].draw(win)#if hard, draw 2 pieces and condition by 2
               parts[count + 1].draw(win)
               count += 2
   win.getMouse()
   win.close()

if __name__ == "__main__":
   game = 0
   while game == 0:
      main()
      game = again()
