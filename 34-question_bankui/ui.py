THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class Quizui:
    
    def __init__(self,quiz_brain:QuizBrain):#makes that object is of type Quizbrain
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizller")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.score_label=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)
        
        self.canvas=Canvas(width=300,height=250,bg="white")
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.question_text=self.canvas.create_text(150,125,width=280,text="SOME TExt",fill=THEME_COLOR,font=("Arial",20,"italic"))
        
        true_img=PhotoImage(file="D:/python/udemy/34/images/true.png")
        false_img=PhotoImage(file="D:/python/udemy/34/images/false.png")
        self.get_next_question()
        self.true_b=Button(image=true_img,highlightthickness=0,command=self.check1)
        self.flase_b=Button(image=false_img,highlightthickness=0,command=self.check2)
        self.true_b.grid(row=2,column=0)
        self.flase_b.grid(row=2,column=1)
        
        self.window.mainloop()
    
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(self.canvas,bg="white")
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have finished the quiz")    
        
    def check1(self):
        self.get_feedback(self.quiz.check_answer("True"))
        
        
    def check2(self):
        self.get_feedback(self.quiz.check_answer("False"))
        
        
         
    def get_feedback(self,is_right):
        if is_right:
            self.canvas.config(self.canvas,bg="green")
        else:
            self.canvas.config(self.canvas,bg="red")    
        self.window.after(1000,self.get_next_question)        