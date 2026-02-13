import re
class Textanalyzer():
    def __init__(self, text):
        self.text = text 
    #separate the text into words
    def clean_text(self):
        all_words = [word for line in self.text for word in line.strip().split()]
        clean_text = [re.sub(r"[\"“',.!-:;]","",t) for t in all_words]
        self.text = clean_text
    
    def find_longest_palindrome(self):
        s = ""
        for i in self.text:
            rev = i[::-1]
            if rev == i and len(i) > len(s):
                s = i
        return s
    
    #sort all the words to identify anagrams
    def find_longest_anagram(self):
        anag1 = ""
        anag2 = ""
        s = ""
        sorted_org = [[],[]]
        for i in self.text:
            if len(i) < 3 or len(anag1) > len(i):
                continue
            cur = i.lower()
            s = ''.join(sorted(cur, key=str.lower))
            if s in sorted_org[0]:
                for k,j in zip(sorted_org[0],sorted_org[1]) :
                    if k == s and j != cur :
                            anag2 = j
                            anag1 = cur
                            break
            if cur not in sorted_org[1] :
                sorted_org[0].append(s)
                sorted_org[1].append(cur)
        return (anag1,anag2)
    
    def calculate_statistics(self):
        ans = {
            "word frequency" : {},
            "average word length" : 0,
            "consonant vowel ratio" : 0,
            "common_endings" : {}
        }
        # calculating word frequency
        freq = {}
        for i in self.text:
            if i not in freq.keys() and len(i) >= 3:
                freq[i] = 1
            elif len(i) >= 3:
                freq[i] += 1
        top_10_values = sorted(freq.items(), key =  lambda x : x[1], reverse=True)[:10]
        ans["word frequency"] = top_10_values
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
        # calculating common endings
        freq_common_endings = {}
        for i in self.text:
            if len(i) <= 3:
                continue
            ending = i[-3:] 
            if ending not in freq_common_endings.keys():
                freq_common_endings[ending] = 1
            else :
                freq_common_endings[ending] += 1
        top_10_endings = sorted(freq_common_endings.items(), key =  lambda x : x[1], reverse=True)[:10]
        ans["common_endings"] = top_10_endings
        return ans

with open("Text.txt", "r", encoding="utf-8") as f:
    
    file = f.readlines()
    
    a = Textanalyzer(file)
    
    #cleaning the text
    a.clean_text()
    
    #calculating the statistics
    print(f"The longest palindrome in the text is: {a.find_longest_palindrome()}")
    print(f"The longest anagrams in the text is: {a.find_longest_anagram()}")
    print(a.calculate_statistics())

    
    