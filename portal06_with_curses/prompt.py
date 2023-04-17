import sys, json, os, random, time
from pathlib import Path

#-------- shared utils access hack
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from shared import utils
# printers = utils.setupPrinters()

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

def loopSetup():
    q = random.choice(questions)
    responseSet = fetch_matched_responses(q)
    return {
        "question": q,
        "responses": responseSet
    }


def main(window):
    while(1): 
        os.system('clear')


if __name__ == "__main__":
    main()
