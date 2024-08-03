import subprocess
import os

arduinoCLI = 'arduino-cli'
comando = 'version'

codePath = os.path.join(os.path.expanduser('~'), 'Documents', 'wandistudio', 'wandicode')
print(codePath)

arduinoVersion = f'{arduinoCLI} {comando}'

version = subprocess.run(arduinoVersion, shell=True)

arduinoCLI = 'arduino-cli'

nomeSketch = input('Digite nome do sketch: ')
comando = f'sketch new {nomeSketch}'

if not os.path.exists(nomeSketch):
    criarSketch = f'{arduinoCLI} {comando}'
    sketch = subprocess.run(criarSketch, shell=True)
    print('criado com sucesso')
else:
    print('já existe o sketch')

pasta = os.listdir()
print(pasta)
