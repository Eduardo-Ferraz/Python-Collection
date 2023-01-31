# Faça um programa que leia um texto digitado no terminal 
# e use dicionários para contar quantas vezes cada palavra aparece no texto. 
# As palavras devem ser usadas como 
# chaves do dicionário e as contagens como valor associado. 
# Assuma que não existem assentos nem símbolos diferentes de letras nos textos. 
# O programa não deve diferenciar maiúsculas e minúsculas 
# e as contagens devem ser exibidas com as palavras em ordem alfabética.

from collections import OrderedDict

def main():
    words = input().split()
    wordDict = {}

    for word in words:
        word = word.lower()
        if word in wordDict.keys():
            wordDict[word] += 1
        else:
            wordDict.update({word: 1})
    
    wordDictSorted = OrderedDict(sorted(wordDict.items()))

    # Outra forma de fazer:
    # myKeys = list(wordDict.keys())
    # myKeys.sort()
    # wordDictSorted = {i: wordDict[i] for i in myKeys}

    for key in wordDictSorted.keys():
        print(key, wordDictSorted[key])

if __name__ == '__main__':
    main()