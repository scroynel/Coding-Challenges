'''
Have the function LetterCountI(str) take the str parameter being passed
and return the first word with the greatest number of repeated letters. For 
example: "Today, is the greatest day ever!" should return 'greatest' because
it has 2 e's (and 2 t's) and it comes before 'ever' which also has 2 e's. If
there are no words with repeating letters return -1. Words will be separated
by spaces.


Example:
	Input: "Hello apple pie"
	Output: Hello
	
	Input: "No words"
	Output: -1
'''

def LetterCountI(str):
    text = str.split()

    count = 0
    word = ''
    
    for i in range(len(text)):
        for j in range(len(text[i])):
            count_letter = 0
            for k in range(j+1, len(text[i])):
                if text[i][j] == text[i][k]:
                    count_letter += 1
            if count_letter > count:
                count = count_letter
                word = text[i]

    return word


print(LetterCountI("Hello apple pie"))
