import re
class Textanalyzer():
    def __init__(self, text):
        self.text = text 

    def clean_text(self):
        for i in self.text :
            Text = i.strip().split()
        clean_text = [re.sub(r"[,.!-:;]","",t) for t in Text]
        return clean_text
    def find_longest_palindrome(self):
        s = ""
        for i in self.text:
            rev = i[::-1]
            if rev == i and len(i) > len(s) :
                s = i
        return s
    #sort all the words to identify anagrams
    def find_longest_anagram(self):
        s = ""
        sorted_org = [[],[]]
        for i in self.text:
            s = sorted(i)
            if s in sorted_org[0]:
                    
            sorted_org[0].append(s)
            sorted_org[1].append(i)

with open("Text.txt", "r") as f:
    file = f.readlines()
    a = Textanalyzer(file)
    print(a.clean_text())
    
