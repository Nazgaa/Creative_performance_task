import re
palindromes = []
with open("Text.txt", "r") as f:
    texts = []
    for i in f:
        Text = i.strip().split()
    clean_text = [re.sub(r"[,.!-:;]","",t) for t in Text ]
for i in clean_text :
    rvr = i[::-1].lower()
    if rvr == i.lower():
        palindromes.append(i)
print(f"The palindromes in the text were {palindromes}")