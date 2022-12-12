sentence = input("Please enter a sentence:").strip().lower()
words = sentence.split()
output = []
for w in words:
    if w[0] in "aeiou":
        #w[0] = w[0] + "yay"
        output.append(w+"yay")
    else:
        vowel_pos = 0
        for l in w:
            if l not in "aeiou":
                vowel_pos += 1
            else:
                break
        const = w[:vowel_pos]
        res =w[vowel_pos:]
        output.append(res+const+"ay")

print(" ".join(output))
