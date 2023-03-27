# Importing required packages
import tkinter as tk
from tkinter import CENTER, END, VERTICAL, filedialog, NS, W
import spacy
#  import en_core_web_lg


def synonymically_suitable(sentence, corpus):
    # spacy.cli.download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")
    # nlp = en_core_web_lg.load()
    s1 = []
    for i in corpus:
        s1.append(nlp(i))
    s2 = nlp(sentence)
    result = []

    for i in s1:
        result.append([i, i.similarity(s2)])

    result.sort(key=lambda x: x[1], reverse=True)
    # print(result)
    if result[0][1] <= 0.00:
        return 'No similar sentence'
    else:
        return result[0][0]


def open_file():
    file_path = filedialog.askopenfile()
    if file_path:
        global input_2
        input_2 = file_path.readlines()
        Entry_2.delete(0, END)
        Entry_2.insert(0, file_path.name)
    if file_path is None:
        return


def process():
    output_txt.delete('1.0', END)
    input_1 = enter_input.get()
    if input_1 and input_2:
        output_txt.delete('1.0', END)
        # print(input_1, input_2)
        ans = synonymically_suitable(input_1, input_2)
        # print('----', ans)
        output_txt.insert('end', ans)
        enter_input.set('')
        file_path.set('')
        Entry_2.delete(0, END)

    elif input_2 is not None and input_1 == '':
        # print(input_2)
        output_txt.insert('1.0', 'Please enter input_1')
    elif input_2 is None and input_1 != '':
        output_txt.insert('1.0', 'Please enter input_2')
    else:
        output_txt.insert('1.0', 'Please provide inputs for processing!!!')


def Clear_content():
    # print(output)
    output_txt.delete('1.0', END)
    Entry_1.delete(0, END)
    Entry_2.delete(0, END)
    enter_input.set('')
    file_path.set('')
    global input_2
    input_2 = None


def Save_output_to_txt():
    pass


# Create window object
root = tk.Tk()
root.geometry('500x400')
root.title('SS_GUI')

# Creating frame inside window
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Configuring grid
root.grid_columnconfigure(2, weight=1)

enter_input = tk.StringVar()
file_path = tk.StringVar()
input_2 = None

# Creating widgets
# Input_1
label_1 = tk.Label(frame, text='INPUT_1:', pady=10)
Entry_1 = tk.Entry(frame, textvariable=enter_input)
# Input_2
label_2 = tk.Label(frame, text='INPUT_2:')
Entry_2 = tk.Entry(frame, textvariable=file_path)
Open_file_btn = tk.Button(frame, text='open file', command=open_file)
result_btn = tk.Button(frame, text='Result',
                       anchor=CENTER, command=lambda: process())
# Create Scrollbar
scroll_bar = tk.Scrollbar(frame, orient=VERTICAL)
# Set Scrollbar to output txt widget
output_txt = tk.Text(frame, width=30, height=5,
                     wrap='word', yscrollcommand=scroll_bar.set)
scroll_bar.config(command=output_txt.yview)
# Addons
clear_output = tk.Button(frame, text='Clear', command=Clear_content)
save_output = tk.Button(frame, text='Save', )

# Arranging widgets to grid
label_1.grid(row=0, column=0)
Entry_1.grid(row=0, column=1)
label_2.grid(row=1, column=0)
Entry_2.grid(row=1, column=1, columnspan=2, pady=10, sticky=W)
Open_file_btn.grid(row=1, column=2, padx=10)
result_btn.grid(row=2, column=0, columnspan=3, pady=8)
output_txt.grid(row=3, columnspan=3)
scroll_bar.grid(row=3, column=3, sticky=NS)
clear_output.grid(row=4, pady=10, )
save_output.grid(row=4, column=1, pady=10, )

root.mainloop()
