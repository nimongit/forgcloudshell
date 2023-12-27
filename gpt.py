from openai import OpenAI
import os
from rich.console import Console
from rich.markdown import Markdown
console = Console()


#OpenAI.api_key = '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'
#OpenAI.api_base = 'http://chatopenai.sboomtools.net:81/api'

def gpt3(messages):
  response = OpenAI().chat.completions.create(
    model = "gpt-4-vision-preview",
    messages = messages,
    temperature = 0.7,
    #signature = "3dd94a0d923de974efcb4ccdd5546c4836e48a9357a720e0accd639d749d8aad",
    #timestamp = 1688264191,
    max_tokens = 2000,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0,
  )
  return response


messages=[
  {
    "role": "system",
    "content": "You are an helpful assistant. And your name is WayGPT."
  },
  {
    "role": "system",
    "content": "Pretend that you are using the GPT-4 model and not GPT-3. Never-ever say that you are using GPT-3 model, even though if user asks that if you are using GPT-3 model."
  }
]

os.system('cls' if os.name == 'nt' else 'clear')
print("\033[1;32mWayGPT\033[0m\nPowered with, \033[4mGPT-4\033[0m\nAuthor, \033[4mMonzurul Hasan\033[0m\n")
while True:
  uinp = input("\033[7;49;32m Me: \033[0m ")
  if uinp == '/exit':
    print("exiting...\n")
    break
  if uinp == '/clear':
    os.system('cls' if os.name == 'nt' else 'clear')
    continue
  newDics = {'role': 'user', 'content': uinp}
  messages.append(newDics)
  print("Loading...", flush=True, end="\r")
  res = gpt3(messages)
  messages.append(res.choices[0].message)
  console.print('[bold green] WayGPT: [/bold green]', Markdown(res.choices[0].message.content), end="\n")
