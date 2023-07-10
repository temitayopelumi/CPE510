import tkinter as tk
import nltk

# Define the grammar
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> N | Det N
    VP -> V | V NP
    N -> 'Mother' | 'father' | 'child' | 'parent'
    V -> 'sleeping' | 'runs' | 'jumps' | 'raining' | 'is' | 'chased'| 'saw'| 'crying' | 'likes' | 'singing'
    Det -> 'The' | 'A' | 'It' | 'the' 
""")

# Create a parser
parser = nltk.RecursiveDescentParser(grammar)
# Create the GUI
window = tk.Tk()

# Create a label
label = tk.Label(text="Enter a sentence:")
label.pack()

# Create an entry box
entry = tk.Entry()
entry.pack()


def check_grammar():
    sentence = entry.get()
    words = sentence.split()
    try:

        parser.parse(words)
        text_box.insert("end", "The sentence is grammatically correct.")
    except:
        text_box.insert("end", "The sentence is grammatically incorrect.")


# Create a button
button = tk.Button(text="Check Grammar", command=check_grammar)
button.pack()

# Create a text box
text_box = tk.Text()
text_box.pack()
# Create a function to check the grammar of a sentence

# Start the GUI
window.mainloop()