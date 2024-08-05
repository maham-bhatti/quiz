'''import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_dt import quiz_dt

root= tk.Tk()
root.title("Maham/s Quiz")
root.geometry('650x500')
style = Style(theme="flatly")

#configure the font size for ques and choice button
style.configure("TLabel", font =("Helvetica", 20))
style.configure("TButton", font =("Helvetica", 18))

def show_ques():
    ques = quiz_dt[curr_ques]
    label.config(text=ques["question"])

#display the choices on button
    choice = ques["choices"]
    for i in range(4):
        button[i].config(text = choice[i],state = 'normal')#reset button state
    #clear the feedback label & disable the next button
    choice_label.config(text="")
    next_button.config(state= "disable")
#func to check the ans and give us the feedback
def check_ans(choice):
    ques = quiz_dt[curr_ques]
    select_choice = button[choice].cget("text")
     #check if the selected choice matches the correct ans
    if select_choice == ques["answer"]:
        #update the score and display it
        global score
        score +=1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_dt)))
        choice_label.config(text="Correct!",fg="Green")
    else:
        choice_label.config(text="Incorrect!",fg="red")
    # diable all choices button & enable the next button
    for buttonss in button:
        buttonss.config(state='disable')
    next_button.config(state='normal')

#fun to move in the next ques    
def Next_ques():
    global curr_ques
    curr_ques += 1

    if curr_ques < len(quiz_dt):    
        #if there are more question show more ques
        show_ques()
    else:
        #if all ques are answered then display the final score 
        messagebox.showinfo("Quiz Completed", "Quiz completed! final score is: {}/{}".format(score, len(quiz_dt)))
        root.destroy()


#qs_label
label = ttk.Label(root, anchor="center", wraplength=500, padding=10 )
label.pack(pady=10)

#choice_btns
button = []
for i in range(4):
    button_1 = ttk.Button(root, command=lambda i=i: check_ans(i))
    button_1.pack(pady=10)
    button.append(button_1)

#feedback_label
choice_label = ttk.Label(root, anchor="center",padding=10)
choice_label.pack(pady=10)

score =0
score_label = ttk.Label(root, text = "Total Score is: 0/{}".format(len(quiz_dt)), anchor= "center",padding=10)
score_label.pack(pady=10)

next_button = ttk.Button(root, text = "Next", command=Next_ques,state='disable')

#current_question
curr_ques = 0

#show_question
show_ques()

root.mainloop()'''

import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_dt import quiz_dt

root = tk.Tk()
root.title("Maham's Quiz")
root.geometry('600x500')
style = Style(theme="flatly")

# Configure the font size for question and choice buttons
style.configure("TLabel", font=("Times New Roman", 25))
style.configure("TButton", font=("Times New Roman", 20))

def show_ques():
    ques = quiz_dt[curr_ques]
    label.config(text=ques["question"])

    # Display the choices on buttons
    choices = ques["choices"]
    for i in range(4):
        buttons[i].config(text=choices[i], state='normal')  # Reset button state

    # Clear the choice label and disable the next button
    choice_label.config(text="")
    next_button.config(state="disabled")

# Function to check the answer and give choice
def check_ans(choice):
    ques = quiz_dt[curr_ques]
    selected_choice = buttons[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == ques["answer"][0]:
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_dt)))
        choice_label.config(text="Correct!", foreground="green")
    else:
        choice_label.config(text="Incorrect!", foreground="red")

    # Disable all choice buttons and enable the next button
    for btn in buttons:
        btn.config(state='disabled')
    next_button.config(state='normal')

# Function to move to the next question
def next_ques():
    global curr_ques
    curr_ques += 1

    if curr_ques < len(quiz_dt):
        show_ques()
    else:
        # Display the final score if all questions are answered
        messagebox.showinfo("Quiz Completed", "Quiz completed! Final score is: {}/{}".format(score, len(quiz_dt)))
        root.destroy()

# Question label
label = ttk.Label(root, anchor="center", wraplength=500, padding=10)
label.grid(row=0, column=0)

# Choice buttons in a 2x2 grid
buttons = []
for i in range(4):
    button = ttk.Button(root, command=lambda i=i: check_ans(i))
    button.grid(row=i//2 + 1, column=i%2, padx=12, pady=12)
    buttons.append(button)

# Feedback label
choice_label = ttk.Label(root, anchor="center", padding=10)
choice_label.grid(row=3, column=0)

score = 0
score_label = ttk.Label(root, text="Score: 0/{}".format(len(quiz_dt)), anchor="center", padding=10)
score_label.grid(row=4, column=0, columnspan=2, pady=10)

next_button = ttk.Button(root, text="Next", command=next_ques, state='disabled')
next_button.grid(row=5, column=0, columnspan=2, pady=10)

curr_ques = 0
show_ques()

root.mainloop()


