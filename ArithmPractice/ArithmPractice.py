import tkinter as tk
import random as rn
import math as m
import time
from tkinter.ttk import Progressbar
 
"""
Border effects:
tk.FLAT
tk.SUNKEN
tk.RAISED
tk.GROOVE
tk.RIDGE
"""
 
## Create the main menu

class mainWindow:

    def __init__(self):

        self.createWidgets()
        self.runMain()
       
    def runMain(self):
        self.root.mainloop()

    def createWidgets(self):

        # Create window
        self.root = tk.Tk()
        self.root.title("ArithmPractice")
 
        # Widgets
 
        self.root.columnconfigure(0, weight = 1, minsize = 900)
        self.root.rowconfigure(1, weight = 1, minsize = 50)
 
        #Title
        self.frm_title = tk.Frame(self.root, height=600, relief = tk.RAISED, borderwidth = 6, bg = "#94DFEF")
        self.frm_title.grid(row=0,column=0,sticky="new")
        self.txt_title = tk.Label(self.frm_title, text = "Welcome to ArithmPractice!", font = ("Copperplate",44),bg = "#94DFEF")
        self.txt_title.pack(pady = 10)
 
        #Selection pane to choose operation to practice
        self.frm_body = tk.Frame(self.root,relief = tk.GROOVE, borderwidth = 9)
        self.frm_body.grid(row=1,column=0, sticky = "nsew")
 
        self.frm_body.columnconfigure(0, weight = 1, minsize = 300)
        self.frm_body.rowconfigure(0, weight = 1, minsize = 400)
 
        self.frm_select = tk.Frame(self.frm_body,bg = "#D5D5D5",relief=tk.RIDGE,borderwidth = 10)
        self.frm_select.pack(padx = 50, pady = 50)
 
        # Quiz parameter entry
        self.NQ_frm = tk.Entry(self.frm_select)
        self.NQ_frm.pack(padx = 20, pady = 20)
        self.NQ_lbl = tk.Label(self.NQ_frm, text = "Enter the number of questions to do:")
        self.NQ_lbl.grid(row=0,column=0)
        self.NQ_ent = tk.Entry(self.NQ_frm)
        self.NQ_ent.grid(row = 0, column = 1)
        self.NQ_ent.insert(0,"20")
        self.HN_lbl = tk.Label(self.NQ_frm,text="Enter the Highest Number:")
        self.HN_lbl.grid(row = 1, column = 0)
        self.HN_ent = tk.Entry(self.NQ_frm)
        self.HN_ent.insert(0,"100")
        self.HN_ent.grid(row = 1, column = 1)
        
        # Commands to increase or decrease time
        def minIncrease():
            try:
                current_val = int(self.min_ent.get())
            except:
                self.min_ent.delete(0,tk.END)
                self.min_ent.insert(0,"0")
                return
            self.min_ent.delete(0,tk.END)
            self.min_ent.insert(0,f"{current_val + 1}")

        def minDecrease():
            try:
                current_val = int(self.min_ent.get())
            except:
                self.min_ent.delete(0,tk.END)
                self.min_ent.insert(0,"0")
                return
            self.min_ent.delete(0,tk.END)
            self.min_ent.insert(0,f"{current_val - 1}")
       
        def secIncrease():
            try:
                current_val = int(self.sec_ent.get())
            except ValueError:
                self.sec_ent.delete(0,tk.END)
                self.sec_ent.insert(0,"0")
                return
            self.sec_ent.delete(0,tk.END)
            self.sec_ent.insert(0,f"{(current_val + 15)%60}") # The seconds entry will cycle from 0 to 60

        def secDecrease():
            try:
                current_val = int(self.sec_ent.get())
            except ValueError:
                self.sec_ent.delete(0,tk.END)
                self.sec_ent.insert(0,"0")
                return
            self.sec_ent.delete(0,tk.END)
            self.sec_ent.insert(0,f"{(current_val - 15)%60}")
 
        self.frm_timer = tk.Frame(self.NQ_frm)
        self.frm_timer.grid(row = 2, column = 1)
        self.Timer_lbl = tk.Label(self.frm_timer,text = "Timer")
        self.Timer_lbl.grid(row = 0, column = 0)
        self.timer_enable = tk.IntVar()
        self.timer_enable.set(0)
        self.Check_timer = tk.Checkbutton(self.frm_timer,variable = self.timer_enable, onvalue = 1, offvalue = 0)
        self.Check_timer.grid(row = 0, column = 1)
        self.Min_increase = tk.Button(self.frm_timer, command = minIncrease,text= u"\u2191")
        self.Min_increase.grid(row = 0, column = 2)
        self.Min_decrease = tk.Button(self.frm_timer, command = minDecrease,text=u"\u2193")
        self.Min_decrease.grid(row = 0, column = 4)
        self.min_ent = tk.Entry(self.frm_timer)
        self.min_ent.grid(row = 0, column = 3)
        self.min_ent.insert(0,"1")
        self.sec_increase = tk.Button(self.frm_timer, command = secIncrease,text= u"\u2191")
        self.sec_increase.grid(row = 0, column = 5)
        self.sec_ent = tk.Entry(self.frm_timer)
        self.sec_ent.grid(row = 0, column = 6)
        self.sec_ent.insert(0,"0")
        self.sec_decrease = tk.Button(self.frm_timer, command = secDecrease,text=u"\u2193")
        self.sec_decrease.grid(row = 0, column = 7)
 
 
        self.select_lbl = tk.Label(self.frm_select, text = "What do you want to practice?",bg = "#D5D5D5")
        self.select_lbl.pack(fill = tk.Y, side = "top",padx = 20, pady = 20)
 
        self.options_lstbox = tk.Listbox(self.frm_select, selectmode = "SINGLE")
        self.options_lstbox.insert(1,"Addition")
        self.options_lstbox.insert(2,"Subtraction")
        self.options_lstbox.insert(3,"Multiplication")
        self.options_lstbox.insert(4,"Division")
        self.options_lstbox.pack(pady = 10)
 
        self.go_frm = tk.Frame(self.frm_select,bg = "#D5D5D5")
        self.go_frm.pack()
 
        self.msg_lbl = tk.Label(self.go_frm, bg = "#D5D5D5")
        self.msg_lbl.grid(row = 1, column = 0)
 
        self.go_btn = tk.Button(self.go_frm,text = "Go",command=self.pressgo, bg = "#74DF63")
        self.go_btn.grid(row = 0, column = 0)

    ## Below are the commands used in the GUI

    def pressgo(self):
        """Adds functionality to the Go button"""
        NQentry = self.NQ_ent.get()
        HNentry = self.HN_ent.get()
        option_selected = tk.IntVar()
        option_selected = self.options_lstbox.curselection()
        try:
            # Get the parameters for the quiz
            N_questions = int(NQentry)
            HN = int(HNentry)
            yesGo = False
            #Get timer parameters
            mins = int(self.min_ent.get())
            secs = int(self.sec_ent.get())
          
            if N_questions <= 0 or HN <= 0 or mins < 0 or secs < 0:
                raise ValueError
            else:
                if option_selected == ():
                    self.msg_lbl["text"] = "Select an option"
 
                elif option_selected == (0,):
                    
                    Q = Quiz("Addition",N_questions,HN)
                    yesGo = True
 
                elif option_selected == (1,):
                    
                    Q = Quiz("Subtraction",N_questions,HN)
                    yesGo = True
 
                elif option_selected == (2,):
                    
                    Q = Quiz("Multiplication",N_questions,HN)
                    yesGo = True
 
                elif option_selected == (3,):
                    
                    Q = Quiz("Division",N_questions,HN)
                    yesGo = True

                else:
                    self.msg_lbl["text"] = "This is not available yet"

                if yesGo == True:

                    #Check if the timer option is enabled
                   
                    if self.timer_enable.get() == 1:
                
                        # Set the timer on the quiz
                        Q.setTimer(mins,secs)
                        
                    #self.root.destroy()
                    Q.runPractice()

                    
        except:
            self.msg_lbl["text"] = "Invalid entries."


class Quiz:
    def __init__(self,operation,NQ,HN):
 
        self.HN = HN
        self.LN = 1
        self.NQ = NQ
        self.QN = 1
        self.Ncorrect = 0
 
        self.operation = operation
 
        self.operation_dict = {"Addition":"+","Subtraction":"-","Multiplication":"x","Division":"/"}
 
        if self.operation == "Division":
            self.createWidgetsMain(isDivision=True)
        else:
            self.createWidgetsMain()
 
        self.n1,self.n2,self.ans = self.generateQuestion()
        self.Q_lbl["text"] = f"What is {self.n1} {self.operation_dict[self.operation]} {self.n2} ?"
 
        self.completed = False
        self.QuizComplete = False

        self.start_time = time.time()
        self.time_taken = 0
 
    # This button function checks if the answer entered is correct
    def checkAns(self):
        green = "#B4EB89"
        orange = "#F29E4C"

        if self.QuizComplete == True:
            self.Warn_lbl["text"] = "The quiz is complete, please press continue."
            return

        try:
            ansIN = int(self.Q_ent.get())
            if self.completed == False:
 
                if self.operation == "Division":
                    rem = self.n1 - self.ans*self.n2
                    remIN = int(self.rem_ent.get())
 
                    if rem == remIN and self.ans == ansIN:
 
                        self.Warn_lbl["text"] = "Correct."
                        self.Ncorrect += 1
                        self.Q_frm["bg"] = green
                    else:
                        self.Warn_lbl["text"] = f"Incorrect, the correct answer is {self.ans} remainder {rem}."
                        self.Q_frm["bg"] = orange
                else:
 
                    if ansIN == self.ans:
 
                        self.Warn_lbl["text"] = "Correct."
                        self.Ncorrect += 1
                        self.Q_frm["bg"] = green
                    else:
                        self.Warn_lbl["text"] = f"Incorrect, the correct answer is {self.ans}."
                        self.Q_frm["bg"] = orange
                self.completed = True
 
 
            else:
                self.Warn_lbl["text"] = "You have already completed the question, please continue."
 
        except ValueError:
            self.Warn_lbl["text"] = "Invalid input, please try again."
            self.Q_ent.delete(0,tk.END)


 
    def generateQuestion(self):
 
        num1 = rn.randint(self.LN,self.HN)
        num2 = rn.randint(self.LN,self.HN)
 
 
        if self.operation == "Addition":
            ans = num1+num2
 
        elif self.operation == "Multiplication":
            ans = num1*num2
        elif self.operation == "Subtraction":
            if num1 < num2:
                n1 = num1
                n2 = num2
                num1 = n2
                num2 = n1
            ans = num1-num2
 
        elif self.operation == "Division":
            if num1 < num2:
                n1 = num1
                n2 = num2
                num1 = n2
                num2 = n1
            ans = m.floor(num1/num2)
 
        return num1,num2,ans
 
 
 
    # This button function generates a new question
    def cont(self):
        
        if self.QN == self.NQ:
            self.Warn_lbl["text"] = f"You have completed the quiz, your score was {self.Ncorrect}/{self.NQ}. Continue to see detailed summary."
            self.time_taken = time.time() - self.start_time
            self.QuizComplete = True
            self.Progress_lbl["text"] = "Complete!"
 
        else:
            if self.completed == True:
                self.n1,self.n2,self.ans = self.generateQuestion()
                self.Q_lbl["text"] = f"What is {self.n1} {self.operation_dict[self.operation]} {self.n2}?"
                self.Warn_lbl["text"] = ""
                self.completed = False
                self.Q_ent.delete(0,tk.END)
                if self.operation == "Division":
                    self.rem_ent.delete(0,tk.END)
                self.Q_ent.focus_set()
                self.QN += 1
                self.Progress_lbl["text"] = f"Question {self.QN} of {self.NQ}"
                self.progress_bar["value"] = self.QN
                self.Q_frm["bg"] = "#E7E1A6"
 
            else:
                self.Warn_lbl["text"] = "You have not yet attempted the question."

        if self.QuizComplete == True:
            if self.QN > self.NQ:
                self.showStats()
            else:
                self.QN += 200

    def handle_enter(self,event):
        if self.Q_ent.get() != "":
            if self.completed == True:
                self.cont()
            else:
                self.checkAns()
 
    def createWidgetsMain(self,isDivision=False):
 
        #Create quiz window
        self.practiceWindow = tk.Tk()
        self.practiceWindow.title(f"{self.operation} Practice")
 
        #Make window not resizeable
        self.practiceWindow.resizable(0,0)
 
        ## Progress display ##
        #Container for progress display
        self.Progress_frm = tk.Frame(self.practiceWindow, height = 100, bg = "grey",relief=tk.RAISED)
        self.Progress_frm.pack(fill = tk.BOTH)
 
        # Progress counter
        self.Progress_lbl = tk.Label(self.Progress_frm,text=f"Question {self.QN} of {self.NQ}")
        self.Progress_lbl.grid(row = 0, column = 0, sticky = "e")
        # Progress bar
        self.progress_bar = Progressbar(self.Progress_frm, maximum = self.NQ, length = 800)
        self.progress_bar["value"] = self.QN
        self.progress_bar.grid(row = 0, column = 1,padx = 40)
 
        ## Question container ##
        self.Q_frm = tk.Frame(self.practiceWindow, bg = "#E7E1A6")
        self.Q_frm.pack(fill = tk.BOTH)
 
        self.Q_frm.columnconfigure(0,weight = 1, minsize = 900)
        self.Q_frm.rowconfigure(0,weight=1,minsize = 500)
 
        #Entry box for entering the answer
        self.Q_entfrm = tk.Frame(self.Q_frm)
        self.Q_entfrm.grid(row = 1, column = 0, padx = 50)
 
        self.Q_ent = tk.Entry(self.Q_entfrm)
        self.Q_ent.pack(side = tk.LEFT)
 
        # Additional remainder box for entering division answers
        if isDivision == True:
            self.rem_lbl = tk.Label(self.Q_entfrm,text="remainder")
            self.rem_ent = tk.Entry(self.Q_entfrm)
            self.rem_lbl.pack(side=tk.LEFT)
            self.rem_ent.pack(side=tk.LEFT)
 
 
        self.Q_lbl = tk.Label(self.Q_frm, font = ("monaco", 50), bg = "#96D9F9",relief=tk.GROOVE,borderwidth=20)
        self.Q_lbl.grid(row = 0, column = 0, pady = 30, padx = 60)
 
        self.Warn_lbl = tk.Label(self.Q_frm, bg = "#E7E1A6")
        self.Warn_lbl.grid(row=2,column = 0)
 
        #Buttons with functions
        self.submit_btn = cont_btn = tk.Button(self.Q_frm, text = "Submit", bg="grey", command = self.checkAns)
        self.submit_btn.grid(row = 1, column = 1)
 
        self.cont_btn = tk.Button(self.Q_frm, bg="grey",text = "Continue",command = self.cont)
        self.cont_btn.grid(row = 2, column = 1)
 
        # Continue with enter key
        self.practiceWindow.bind("<Key-Return>",self.handle_enter)

    def setTimer(self,minutes,seconds):

        #Create the timer widget under the progress frame

        self.mins_rem = minutes
        self.secs_rem = seconds
        
        self.time_lbl = tk.Label(self.Progress_frm,text = f"Time remaining: {self.mins_rem:02d} : {self.secs_rem:02d}")
        self.time_lbl.grid(row=0,column=2)
        

    def updateTime(self):

        try:
            if self.secs_rem == 0 and self.mins_rem == 0 or self.QuizComplete == True:
                self.QuizComplete == True
                return

            if self.secs_rem <= 0:
                self.mins_rem -= 1
                self.secs_rem = 60
        
            self.secs_rem -= 1

            self.time_lbl["text"] = f"Time remaining: {self.mins_rem:02d} : {self.secs_rem:02d}"

            self.practiceWindow.after(1000,self.updateTime)

        except:
            return

         

    def showStats(self):
        """Create widgets which display the outcomes of the quiz:
            * Score and time taken
            * 
            Exit button to return to the main menu"""

        minutes = m.floor(self.time_taken/60)
        seconds = m.floor(self.time_taken - 60*minutes)

        self.Q_frm.destroy()
        self.Progress_frm.destroy()

        self.stat_frm = tk.Frame(self.practiceWindow)
        self.stat_frm.pack(fill=tk.BOTH)

        self.time_lbl = tk.Label(self.stat_frm, text = f"You completed {self.NQ} questions of {self.operation} with the highest number {self.HN} in {minutes} minutes and {seconds} seconds.")
        self.time_lbl.pack()

        self.score_lbl = tk.Label(self.stat_frm, text = f"Your accuracy is: {self.Ncorrect}/{self.NQ} or {int(self.Ncorrect/self.NQ*100)}%")
        self.score_lbl.pack()

 
    def runPractice(self):

        try:
            self.practiceWindow.after(1000,self.updateTime)
        except:
            pass

        self.practiceWindow.mainloop()
        


def createMainWindow():
    window = mainWindow()
    
createMainWindow()

