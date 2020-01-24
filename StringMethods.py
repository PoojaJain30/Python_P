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