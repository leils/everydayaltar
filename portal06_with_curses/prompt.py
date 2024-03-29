import sys, json, os, random, time, curses, termios
import argparse
from pathlib import Path

maxPrintConnectionTries = 10

#-------- modes and arg parsing 
parser = argparse.ArgumentParser("simple_example")
parser.add_argument("--waitForPrinter", help="`True` to enter wait loop if printers not found", default="false")

args = parser.parse_args()
waitForPrinter = (args.waitForPrinter.lower() == 'true') 

#-------- Required for curses
class EchoControl(object):
    def __init__(self, disable=True):
        self.fd = sys.stdin.fileno()
        self._echo_on = termios.tcgetattr(self.fd)
        self._echo_off = termios.tcgetattr(self.fd)
        self._echo_off[3] = self._echo_off[3] & ~termios.ECHO

    def enable(self):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self._echo_on)

    def disable(self):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self._echo_off)

    def __enter__(self):
        self.disable()
        return self

    def __exit__(self, *args):
        self.enable()

echoDisabled = EchoControl()
echoEnabled = EchoControl(True)

#-------- shared utils access hack
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from shared import utils

printersAvailable = False

if waitForPrinter:
    tries = 0
    while (not printersAvailable): 
        try:
            printers = utils.setupPrinters()
            printersAvailable = True
        except: 
            print('Printer connection failed. Press ctrl+c to exit program.')
            tries += 1
            if (tries > maxPrintConnectionTries):
                print("Reach max tries, shutting down.")
                exit()
            time.sleep(3)
else: 
    try:
        printers = utils.setupPrinters()
        printersAvailable = True
    except:
        pass

#-------- JSON file loads for questions & responses
sharedPath = path + '/shared'
source_filename = os.path.join(sharedPath, 'source.json')
data_filename = os.path.join(sharedPath, "data.json")
source_data = json.load(open(source_filename))

prompts = source_data['prompts']
questions = source_data['questions']
responses = json.load(open(data_filename))

def fetch_matched_responses(q):
    if q in responses:
        chosen_responses = []
        if len(responses[q]) >= 2:
            chosen_responses = random.sample(responses[q], 2)
        else: #there's only 1 response
            chosen_responses = responses[q]
            chosen_responses.extend([""])
    else:
        utils.print_slow('No other responses found. Check again later, maybe someone will stop by and share.\n')
        chosen_responses = ["", ""]

    return chosen_responses

def questionLoopSetup():
    q = random.choice(questions)
    responseSet = fetch_matched_responses(q)
    return {
        "question": q,
        "responses": responseSet
    }

def main():
    respondingToQuestions = False

    while(1):
        os.system('clear')
        input(prompts['wakeup']) # Wait for wakeup
        os.system('clear')

        utils.print_slow(prompts['intro_message'])
        input()
        respondingToQuestions = True

        while(respondingToQuestions):
            questionSet = questionLoopSetup()
            formattedResponses = utils.formatArrayForMultiPrint(questionSet['responses'])

            os.system('clear')
            if printersAvailable:
               utils.printInCycle(formattedResponses, printers[1::-1])
            else:
                print(questionSet['question'])
                for response in formattedResponses:
                    print('  ', '\n    '.join(reversed(response)))
                    print('')
                print("Press enter to continue")
                input()

            utils.print_slow(prompts['ask_to_share'])

            termios.tcflush(sys.stdin, termios.TCIOFLUSH) # the suppressed echoes need to be flushed
            response = curses.wrapper(utils.inputBox, questionSet['question'])
            formattedResponse = "".join(x.strip() for x in response.split("\n"))
            os.system('clear')

            utils.print_slow(prompts['outro_message'])
            utils.print_slow(prompts['add'])

            if printersAvailable:
                printers[2].print(utils.textWrapped(formattedResponse))
                formattedQuestion = utils.textWrapped(questionSet['question']).splitlines()
                utils.printInvertedToAll(formattedQuestion, printers)
            else:
                print(formattedResponse)
                time.sleep(1)

            utils.write_to_file(formattedResponse, data_filename, questionSet['question'])

            with echoEnabled:
                if not utils.yn_timed(prompts['continue']):
                    respondingToQuestions = False

        utils.print_slow(prompts['sleep'])
        time.sleep(1)

if __name__ == "__main__":
    with echoDisabled:
        main()
