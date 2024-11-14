from gtts import gTTS
from pydub import AudioSegment

# Text to convert to speech
text = "give me debt or equity ratio and revenue from 2005 onwards for each company and Category"

# Generate speech
tts = gTTS(text=text, lang='en')
tts.save("C:/Users/NChunduri/Downloads/give_me_debt_or_equity_ratio.mp3")

#Read .mp3 file and convert to  .wav file
AudioSegment.converter = 'C:/Users/NChunduri/Downloads/ffmpeg-7.0.2-essentials_build/ffmpeg-7.0.2-essentials_build/bin/ffmpeg.exe'
sound = AudioSegment.from_mp3("C:/Users/NChunduri/Downloads/give_me_debt_or_equity_ratio.mp3")
sound.export("C:/Users/NChunduri/Downloads/give_me_debt_or_equity_ratio.wav", format="wav")
print("Audio file generated and saved as C:/Users/NChunduri/Downloads/give_me_debt_or_equity_ratio.wav")

