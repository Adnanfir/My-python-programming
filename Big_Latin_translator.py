Sentence = input("Enter a sentence ")
words = Sentence.split()
new_words=[]
for word in words:
    if word[0].lower() in "aeiou":
        new_word=word + "yah"
        new_words.append(new_word)
    else:
        vowel_pos=0
        for letter in words:
            if letter.lower() not in "aeiou":
                vowel_pos=words.index(letter) 
                vowel_pos+=1
            else:
                break
        cons=word[:vowel_pos]
        the_rest=word[vowel_pos:]
        new_word=the_rest + cons + "ay"
        new_words.append(new_word)
output=" ".join(new_words)
print(output)
print(words)
