import sys, json, os, random, time, curses
from pathlib import Path

#-------- shared utils access hack
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from shared import utils

printersAvailable = False
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
                print(formattedResponses)
                input() 

            utils.print_slow(prompts['ask_to_share'])

            response = curses.wrapper(utils.inputBox, questionSet['question'])
            os.system('clear')
            
            if printersAvailable:
                printers[2].print(utils.textWrapped(response))
            else: 
                print(response)
                time.sleep(1)

            utils.print_slow(prompts['outro_message'])
            utils.print_slow(prompts['add'])

            if printersAvailable: 
                printers[2].print(utils.textWrapped(response))
                formattedQuestion = utils.textWrapped(questionSet['question']).splitlines()
                utils.printInvertedToAll(formattedQuestion, printers)

            utils.write_to_file(response, data_filename, questionSet['question'])

            if not utils.yes_or_no(prompts['continue']): 
                respondingToQuestions = False

        utils.print_slow(prompts['sleep'])
        time.sleep(1)

if __name__ == "__main__":
    main()
