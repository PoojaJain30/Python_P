#Takes in a string and returns a matching string where every even letter is uppercase and every odd letter is lowercase. 
# The string only contains letters and considering input is string only.

def even_odd_char(stri):
    re_stri = []
    for i,ch in enumerate(stri):
        if i % 2 == 0:
            re_stri.append(ch.upper())
        else:
            re_stri.append(ch.lower())
    return ''.join(re_stri)


even_odd_char("mynameis")

####OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    name_re = []
    for i,c in enumerate(name):
        if i == 0 or i == 3:
            name_re.append(c.capitalize())
        else:
            name_re.append(c)
    return ''.join(name_re)
old_macdonald('macdonald')

####MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    li = text.split()
    li.reverse()
    return ' '.join(li)

master_yoda('I am home')

####ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    stri_1 = text.split()[0]
    stri_2 = text.split()[1]
    if stri_1[0] == stri_2[0]:
        return True
    else:
        return False
animal_crackers("my mane")

#better approch
def animal_crackers_1(text):
    name = text.split()
    return name[0][0] == name[1][0]

animal_crackers_1('Levelheaded llama')

####PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    li=[]
    for x,ch in enumerate(text):
        x=0
        while(x<3):
            li.append(ch)
            x = x+1
    return ''.join(li)

paper_doll('Hello')