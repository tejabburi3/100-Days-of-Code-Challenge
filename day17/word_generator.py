import pandas as pd
import random
data=pd.read_csv("a_to_z_words_programming_common.csv")
a=input("Enter a word or words : ").upper()
for letter in a:
  if not letter.isalpha():
    print("")
  else:
    l=(data[data['letter']==letter]['words']).to_list()
    if l:
      words= [w.strip() for w in l[0].split(",")]
      print(f"{letter }: {random.choice(words)}")
