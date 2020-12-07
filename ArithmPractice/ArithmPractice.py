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
 
class Timer:
    def __init(self,countdown_duration):
        self.start_time = time.time()
        self.current_time = self.start_time
        self.duration = countdown_duration
    def get_time_elapsed(self):
        self.current_time = time.time()
        return self.current_time - self.start_time
    def is_ended(self):
        return self.get_time_elapsed() >= self.duration
 
 
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

    def showStats(self):
        """Create widgets which display the outcomes of the quiz:
            * Score and time taken
            * 
            Exit button to return to the main menu"""

        self.Q_frm.destroy()
        self.Progress_frm.destroy()

        self.stat_frm = tk.Frame(self.practiceWindow)
        self.stat_frm.pack(fill=tk.BOTH)

        self.time_lbl = tk.Label(self.stat_frm, text = f"You completed {self.NQ} questions of {self.operation} with the highest number {self.HN} in "+"{:.2f} seconds.".format(self.time_taken))
        self.time_lbl.pack()

        self.score_lbl = tk.Label(self.stat_frm, text = f"Your accuracy is: {self.NQ}/{self.Ncorrect} or {int(self.NQ/self.Ncorrect*100)}%")
        self.score_lbl.pack()

 
    def runPractice(self):
        self.practiceWindow.mainloop()
        runMain()
 






def runMain():
 
    # Create window
    root = tk.Tk()
    root.title("ArithmPractice")
 
    # Widgets
 
    root.columnconfigure(0, weight = 1, minsize = 900)
    root.rowconfigure(1, weight = 1, minsize = 50)
 
    #Title
    frm_title = tk.Frame(root, height=600, relief = tk.RAISED, borderwidth = 6, bg = "#94DFEF")
    frm_title.grid(row=0,column=0,sticky="new")
    txt_title = tk.Label(frm_title, text = "Welcome to ArithmPractice!", font = ("Copperplate",44),bg = "#94DFEF")
    txt_title.pack(pady = 10)
 
    #Selection pane to choose operation to practice
    frm_body = tk.Frame(root,relief = tk.GROOVE, borderwidth = 9)
    frm_body.grid(row=1,column=0, sticky = "nsew")
 
    frm_body.columnconfigure(0, weight = 1, minsize = 300)
    frm_body.rowconfigure(0, weight = 1, minsize = 400)
 
    frm_select = tk.Frame(frm_body,bg = "#D5D5D5",relief=tk.RIDGE,borderwidth = 10)
    frm_select.pack(padx = 50, pady = 50)
 
    # Quiz parameter entry
    NQ_frm = tk.Entry(frm_select)
    NQ_frm.pack(padx = 20, pady = 20)
    NQ_lbl = tk.Label(NQ_frm, text = "Enter the number of questions to do:")
    NQ_lbl.grid(row=0,column=0)
    NQ_ent = tk.Entry(NQ_frm)
    NQ_ent.grid(row = 0, column = 1)
    NQ_ent.insert(0,"20")
    HN_lbl = tk.Label(NQ_frm,text="Enter the Highest Number:")
    HN_lbl.grid(row = 1, column = 0)
    HN_ent = tk.Entry(NQ_frm)
    HN_ent.insert(0,"100")
    HN_ent.grid(row = 1, column = 1)
 
    def minIncrease():
        return
    def minDecrease():
        return
    def secIncrease():
        return
    def secDecrease():
        return
 
    frm_timer = tk.Frame(NQ_frm)
    frm_timer.grid(row = 2, column = 1)
    Timer_lbl = tk.Label(frm_timer,text = "Timer")
    Timer_lbl.grid(row = 0, column = 0)
    Check_timer = tk.Checkbutton(frm_timer)
    Check_timer.grid(row = 0, column = 1)
    Min_increase = tk.Button(frm_timer, command = minIncrease,text= u"\u2191")
    Min_increase.grid(row = 0, column = 2)
    Min_decrease = tk.Button(frm_timer, command = minDecrease,text=u"\u2193")
    Min_decrease.grid(row = 0, column = 4)
    min_ent = tk.Entry(frm_timer,width = 2)
    min_ent.grid(row = 0, column = 3)
    min_ent.insert(0,"1")
    sec_increase = tk.Button(frm_timer, command = secIncrease,text= u"\u2191")
    sec_increase.grid(row = 0, column = 5)
    sec_ent = tk.Entry(frm_timer,width = 2)
    sec_ent.grid(row = 0, column = 6)
    sec_ent.insert(0,"0")
    sec_decrease = tk.Button(frm_timer, command = secDecrease,text=u"\u2193")
    sec_decrease.grid(row = 0, column = 7)
 
 
    select_lbl = tk.Label(frm_select, text = "What do you want to practice?",bg = "#D5D5D5")
    select_lbl.pack(fill = tk.Y, side = "top",padx = 20, pady = 20)
 
    options_lstbox = tk.Listbox(frm_select, selectmode = "SINGLE")
    options_lstbox.insert(1,"Addition")
    options_lstbox.insert(2,"Subtraction")
    options_lstbox.insert(3,"Multiplication")
    options_lstbox.insert(4,"Division")
    options_lstbox.pack(pady = 10)
 
    go_frm = tk.Frame(frm_select,bg = "#D5D5D5")
    go_frm.pack()
 
    msg_lbl = tk.Label(go_frm, bg = "#D5D5D5")
    msg_lbl.grid(row = 1, column = 0)
 
    def pressgo():
        NQentry = NQ_ent.get()
        HNentry = HN_ent.get()
        option_selected = tk.IntVar()
        option_selected = options_lstbox.curselection()
        try:
            N_questions = int(NQentry)
            HN = int(HNentry)
            if N_questions <= 0 or HN <= 0:
                raise ValueError
            else:
                if option_selected == ():
                    msg_lbl["text"] = "Select an option"
 
                elif option_selected == (0,):
                    root.destroy()
                    Q = Quiz("Addition",N_questions,HN)
                    Q.runPractice()
 
                elif option_selected == (1,):
                    root.destroy()
                    Q = Quiz("Subtraction",N_questions,HN)
                    Q.runPractice()
 
                elif option_selected == (2,):
                    root.destroy()
                    Q = Quiz("Multiplication",N_questions,HN)
                    Q.runPractice()
 
                elif option_selected == (3,):
                    root.destroy()
                    Q = Quiz("Division",N_questions,HN)
                    Q.runPractice()
                else:
                    msg_lbl["text"] = "This is not available yet"
        except:
            msg_lbl["text"] = "Invalid entries."
 
 
    go_btn = tk.Button(go_frm,text = "Go",command=pressgo, bg = "#74DF63")
    go_btn.grid(row = 0, column = 0)
 
    root.mainloop()
 
runMain()
