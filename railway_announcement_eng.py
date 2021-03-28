import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

# pip install pyaudio, pydub, pandas, gTTS

def textToSpeech(text, filename):
    myText = str(text)
    language = 'en'
    myobj = gTTS(text=myText, lang=language, slow=True)
    myobj.save(filename)

# this function returns pydub audio_segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3("railway.mp3")
    # 1.generate "May i have your attention"
    start = 66000
    finish = 70000
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_eng.mp3", format="mp3")

    # 2. train number and name

    # 3. generate "from"
    start = 76000
    finish = 77100
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_eng.mp3", format="mp3")

    # 4. from city

    # 5. generate "to"
    start = 78000
    finish = 78900
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_eng.mp3", format="mp3")

    # 6. to city

    # 7. generate "via"
    start = 80000
    finish = 80900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_eng.mp3", format="mp3")

    # 8. via city

    # 9. generate "arriving shortly on platform number"
    start = 83000
    finish = 86500
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_eng.mp3", format="mp3")

    # 10. platform number

    # 11. generate end tune
    start = 87200
    finish = 88000
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_eng.mp3", format="mp3")

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2. generate - train number and name
        textToSpeech(item['train_no']+" "+item['train_name'], '2_eng.mp3')
        # 4. generate - from city
        textToSpeech(item['from'], '4_eng.mp3')
        # 6. generate - to city
        textToSpeech(item['to'], '6_eng.mp3')
        # 8. generate - via city
        textToSpeech(item['via'], '8_eng.mp3')
        # 10. generate - platform number
        textToSpeech(item['platform'], '10_eng.mp3')
        # merging audios
        audios = [f"{i}_eng.mp3" for i in range(1, 12)]
        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}_eng.mp3", format="mp3")


if __name__ == '__main__':
    print("generating skeleton...")
    generateSkeleton()
    print("Now generating announcement...")
    generateAnnouncement("announce.xls")