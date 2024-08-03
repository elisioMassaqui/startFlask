import subprocess
import os

arduinoCLI = 'arduino-cli'
comando = 'version'
codePath = os.path.join(os.path.expanduser('~'), 'Documents', 'wandistudio', 'wandicode')
print(codePath)
arduinoVersion = f'{arduinoCLI} {comando}'
arduinoCLI = 'arduino-cli'

def arduinoV():
    version = subprocess.run(arduinoVersion, capture_output=True)
    saidaVersion = f'{version.stdout}'
    print(saidaVersion)
    return saidaVersion