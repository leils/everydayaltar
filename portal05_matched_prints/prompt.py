import sys, json, os, random, time
from pathlib import Path

#-------- shared utils access hack
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from shared import utils
printers = utils.setupPrinters()

#-------- JSON file loads for questions & responses
sharedPath = path + '/shared'
source_filename = os.path.join(sharedPath, 'source.json')
data_filename = os.path.join(sharedPath, "data.json")
source_data = json.load(open(source_filename))

prompts = source_data['prompts']
questions = source_data['questions']
responses = json.load(open(data_filename))

def fetch_matched_responses(q): 
    global responses

    utils.print_slow('Resurfacing others\' responses ...\n')
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

def main():
    while(1): 
        os.system('clear')
        input(prompts['wakeup'])
        os.system('clear')
        print(prompts['divider'])
        
        utils.print_slow(prompts['intro_message'])
        input()
        q = random.choice(questions)
        utils.print_slow(q + "\n")

        responseSet = fetch_matched_responses(q)
        formattedResponses = utils.formatArrayForMultiPrint(responseSet)
        utils.printToAll([prompts['divider']], printers)
        utils.printInCycle(formattedResponses, printers[1::-1]) # print retrieved responses to left and middle printers

        utils.print_slow(prompts['ask_to_share'])

        print(prompts['divider'])
        response = input()
        print(prompts['divider'])
        utils.print_slow(prompts['outro_message'])

        print("Adding your words to the archive ...")
        # PRINT TO THE THIRD PRINTER
        printers[2].print(utils.textWrapped(response))

        formattedQuestion = utils.textWrapped(q).splitlines()
        utils.printToAll(formattedQuestion, printers)

        utils.write_to_file(response, data_filename, q)
        utils.print_slow(prompts['sleep'])

        time.sleep(5)

if __name__ == "__main__":
    main()
