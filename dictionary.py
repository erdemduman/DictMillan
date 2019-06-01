import json
import requests 

class Dictionary:
    def __init__(self):
        self.__URL = "https://mydictionaryapi.appspot.com/" #https://github.com/meetDeveloper/googleDictionaryAPI

    def definition(self, inp):

        PARAMS = {'define':inp} 
        r = requests.get(url = self.__URL, params = PARAMS) 
  
        data = r.json()
        try:
            meaning = self.__parseJson(data)
        except:
            raise
    
        return meaning

    def __parseJson(self, data):
        
        defin = ""

        word = data[0]['word']
        phonetic = data[0]['phonetic']
        meaning = data[0]['meaning']
        
        defin += "word: " + str(word)
        defin += "\n"
        defin += "phonetic: " + str(phonetic)
        defin += "\n\n"

        count = 1
        letter = 'a'
        for k in meaning:
            defin += str(letter) + ") " + str(k)
            defin += "\n\n"
            letter = chr(ord(letter) + 1)
            count = 1
            for defList in meaning[k]:
                defin += "[" + str(count) + "]"
                defin += "\n"
                count += 1
                for k1,v1 in defList.items():
                    defin += str(k1) + ': '
                    if(k1 == 'definition' or k1 == 'example'):
                        defin += v1
                        defin += "\n"
                        
                    elif(k1 == 'synonyms'):
                        for i in range(0,len(defList[k1])):
                            if(i != len(defList[k1])-1):
                                defin += str(defList[k1][i]) + ", "
                            else:
                                defin += str(defList[k1][i]) + "."

                defin += "\n\n"
        
        return defin