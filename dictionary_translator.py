##DICTIONARIES examples and workings

##SIMPLE translator with dictionaries


##D = {1: 'one', 'deus': 'two','pi':3.14159}
##D1 = D
##print D1
##D[1] = 'uno'
##print D1
##for k in D1.keys():
##    print k, '=', D1[k]


EtoF = {'bread': 'du pain', 'wine': 'du vin',\
        'eats':'mange','drinks':'bois',\
        'likes':'aime', 1:'un',\
        '6.00':'6.00'}
##print EtoF
##print EtoF.keys()
##print EtoF.keys
##del EtoF[1]
##print EtoF

def translateWord(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return word
    
def translate(sentence):
    translation = ''
    word =''
    for c in sentence:
        if c != ' ':  ## keep walking through until word is found.
            ##So walk along sentence until space is found
            word = word + c
        else:
            translation = translation + ' '\
                          + translateWord(word, EtoF)
            word = ''
    return translation[1:] + ' ' + translateWord(word, EtoF)

print translate('John eats bread')
print translate('Steve drinks wine')
print translate('John likes 6.00')
        
