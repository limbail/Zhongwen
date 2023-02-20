import speech_recognition as sr
import pinyin
from translate import Translator
import pandas as pd

outputfile = "./data/output.csv"

df = pd.read_csv(outputfile)

def zh_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        with open("audio_file.wav", "wb") as file:
            file.write(audio.get_wav_data())
    try:
        zhchar = r.recognize_google(audio, language="zh-cmn-Hans-CN")
        print('hanzi: {}'.format(zhchar))
        print('pinyin: {}'.format(pinyin.get(zhchar)))
        translator= Translator(from_lang='zh' ,to_lang="es")
        translation = translator.translate("{}".format(zhchar))
        print('spanish: {}'.format(translation))
        variable = input('want to save?: ')

        if variable == 'y':
            #with open("audio_file.wav", "wb") as file: # for trancribe later (pending)
            #audiofile = file.write(audio.get_wav_data())
            #    file.flush()
            #    file.close()
            data = {
                'hanzi': [zhchar],
                'pinyin': [pinyin.get(zhchar)],
                'spanish': [translation],
            }
            df = pd.DataFrame(data)
            df.to_csv(outputfile, mode='a', index=False, header=False)
            print("Data appended successfully.")

    except sr.UnknownValueError:
        print("Google Speech Recognition not understand a fuck")
    except sr.RequestError as e:
        print("Maybe Google Speech Recognition service is fucked; {0}".format(e))

if __name__ == "__main__":
    while True:
        zh_recognition()
