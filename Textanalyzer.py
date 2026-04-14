import re
import tkinter as tk
from tkinter import filedialog as fd

global text_area
global full_text
full_text = ""

def update_button_state(event=None):
    # This checks the text area and enables/disables the button
    content = text_area.get("1.0", tk.END)
    if content and len(content) >= 2:
        check_button.config(state=tk.NORMAL)
    else:
        check_button.config(state=tk.DISABLED)

def import_file():
    #Function imports a file (developed by the help of Google Gemini)
    title = "Select a file"
    filetypes = [("Text files", "*.txt"), ("All files", "*.*")]
    file_path = fd.askopenfilename(title=title, filetypes=filetypes)
    with open(file_path, 'r', encoding = "utf-8") as f:
        text = f.read()
        text_area.insert(tk.INSERT, text) 
        full_text = text_area.get("1.0", tk.END)
        print(full_text)
        update_button_state()

def paste_text():
    try:
        text_from_buffer = root.clipboard_get()
        text_area.insert(tk.INSERT, text_from_buffer) 
        full_text = text_area.get("1.0", tk.END)
        update_button_state()
    except tk.TclError:
        print("Clipboard is empty or doesn't contain text.")

class Textanalyzer():
    def __init__(self, text):
        self.text = text 
        self.palindrome = ""
        self.anagram = ()
        self.statistics = {}
    #separate the text into words
    def clean_text(self):
        all_words = self.text.lower().strip().split()
        clean_text = [re.sub(r"[\"“',.!-:;]","",t) for t in all_words]
        self.text = clean_text
    
    def find_longest_palindrome(self):
        s = ""
        for i in self.text:
            rev = i[::-1]
            if rev == i and len(i) > len(s):
                s = i
        self.palindrome = s
    
    def find_longest_anagram(self):
        anag1 = ""
        anag2 = ""
        s = ""
        #sort all the words and store them with 
        # the original word to identify anagrams
        sorted_org = [[],[]]
        for i in self.text:
            if len(i) < 3 or len(anag1) > len(i):
                continue
            cur = i
            s = ''.join(sorted(cur))
            if s in sorted_org[0]:
                for k,j in zip(sorted_org[0],sorted_org[1]) :
                    if k == s and j != cur :
                            anag2 = j
                            anag1 = cur
                            break
            if cur not in sorted_org[1] :
                sorted_org[0].append(s)
                sorted_org[1].append(cur)
        self.anagram = (anag1,anag2)
    
    def calculate_statistics(self):
        ans = {
            "word frequency" : [],
            "average word length" : 0,
            "consonant vowel ratio" : 0
        }
        # calculating word frequency
        freq = {}
        for i in self.text:
            if i not in freq.keys() and len(i) >= 3:
                freq[i] = 1
            elif len(i) >= 3:
                freq[i] += 1
        # Selection of top 5 values was modified with Google Gemini
        top_5_values = sorted(freq.items(), 
        key =  lambda x : x[1], reverse=True)[:5] 
        ans["word frequency"] = top_5_values
        # calculating the average word length
        word_num = len(self.text)
        total_char_count = sum(len(i) for i in self.text)
        ans["average word length"] = total_char_count / word_num
        # consonant vowel ratio
        vowels = "aeyuio"
        num_vowels = 0
        num_consonants = 0
        for i in self.text :
            for j in i :
                if j in vowels:
                    num_vowels += 1
                else :
                    num_consonants += 1
        ans["consonant vowel ratio"] = num_consonants / num_vowels
        self.statistics = ans


root = tk.Tk()
root.title("Star Animation Control Panel")
def solve():
    full_text = text_area.get("1.0", tk.END)

    a = Textanalyzer(full_text)
    #Canvas was implemented by the help of Google Gemini
    canvas_window = tk.Toplevel(root)
    canvas_window.title("Bar Chart Panel")
    canvas = tk.Canvas(canvas_window,width=500,height=400,bg="white")
    canvas.pack()
    
    #cleaning the text and calculating everything
    a.clean_text()
    a.calculate_statistics()
    a.find_longest_anagram()
    a.find_longest_palindrome()
    
    data = a.statistics["word frequency"]
    bar_width = 60
    bar_spacing = 20
    max_height = 300
    scale = max_height / (3 * data[1][1])

    x = 50
    for i in data:
        label = i[0]
        value = i[1]
        bar_height = value * scale
        canvas.create_rectangle(x,max_height - bar_height, 
                                x + bar_width, max_height, 
                                fill = "skyblue",outline="black")
        canvas.create_text(x + bar_width//2, max_height + 20, text = label)
        canvas.create_text(x + bar_width//2, max_height - bar_height - 10,
                            text=str(value))
        x += bar_width + bar_spacing
    
    new_window = tk.Toplevel(root)
    new_window.title("Other statistics panel")
    

    text_area2 = tk.Text(new_window, width=40, height=10, font=("Arial", 12))
    text_area2.pack(padx=10, pady=10)
    
    text_area2.insert(tk.INSERT,f"The longest anagrams are {a.anagram}\n")
    text_area2.insert(tk.INSERT,f"The longest palindromes are {a.palindrome}\n")
    text_area2.insert(tk.INSERT,f'''The average word length is 
                      {round(a.statistics["average word length"],3)}\n''')
    text_area2.insert(tk.INSERT,f'''The consonant and vowel ratio is 
                      {round(a.statistics["consonant vowel ratio"],3)}\n''')

import_button = tk.Button(root, text="Import File", command=import_file)
import_button.pack(pady=10)

paste_text_button = tk.Button(root, text="Paste Text", command = paste_text)
paste_text_button.pack(pady=10)

text_area = tk.Text(root, width=40, height=10, font=("Arial", 12))
text_area.pack(padx=10, pady=10)

check_button = tk.Button(root, text="Text Analysis", 
                         command = solve, state=tk.DISABLED) 
check_button.pack(pady=10)

#In order to track key release I used Google Gemini 
text_area.bind("<KeyRelease>", update_button_state)
text_area.bind("<ButtonRelease-1>", update_button_state)

root.mainloop()