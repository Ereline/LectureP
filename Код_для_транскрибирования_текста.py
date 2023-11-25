# установка Whisper
! pip install git+https://github.com/openai/whisper.git
!pip install pytorch_lightning

import whisper

model = whisper.load_model("medium")
n = int(input("Нумерация аудио"))
for i in range(1,n):
  result = model.transcribe(f"audio{i}.mp3",language="ru")
  print(result["text"])
  t = open(f"{i}.txt", "w")
  t.write(result["text"])
  t.close()