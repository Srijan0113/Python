str="Hello <my> name <is> <siri>  is the <and>"
words=set()
start_of_word=-1

target_start="<"
target_end=">"

for i, char in enumerate(str):
     if char==target_start:        
        start_of_word=i
     if char==target_end and start_of_word!=-1:
        word=str[start_of_word:i+1]
        words.add(word)
        start_of_word=-1 #reset after finishing
print(words)    