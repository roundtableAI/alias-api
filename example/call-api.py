import requests
import os
from dotenv import load_dotenv
load_dotenv()

def run_fetch(questions, question_histories, responses, survey_id, participant_id, API_KEY):
    # Make body of request
    body = {
        'questions': questions,
        'question_histories': question_histories,
        'responses': responses,
        'survey_id': survey_id,
        'api_key': API_KEY,
        'participant_id': participant_id,
    }
    # Make request
    response = requests.post('https://roundtable.ai/.netlify/functions/alias-v01', json=body)
    # Check response
    if response.status_code == 200:
        return response.json()
    else:
        # Get the body of the response and print
        response_body = response.json()
        print('Error: ', response_body)

# Example Usage
if __name__ == "__main__":
    questions = {
        'q-1': "Tell me about yourself",
        'q-2': 'How do you choose which shampoo to buy?',
    }
    question_histories = {
        'q-1': [{"s":"M","t":0},{"s":"My","t":196},{"s":"My ","t":328},{"s":"My n","t":494},{"s":"My na","t":589},{"s":"My nam","t":665},{"s":"My name","t":781},{"s":"My name ","t":833},{"s":"My name i","t":935},{"s":"My name is","t":1005},{"s":"My name is ","t":1053},{"s":"My name is M","t":1238},{"s":"My name is Ma","t":1343},{"s":"My name is Mat","t":1454},{"s":"My name is Matt","t":1594},{"s":"My name is Matt ","t":1658},{"s":"My name is Matt a","t":1738},{"s":"My name is Matt an","t":1802},{"s":"My name is Matt and","t":1890},{"s":"My name is Matt and ","t":1954},{"s":"My name is Matt and I","t":2111},{"s":"My name is Matt and I ","t":2236},{"s":"My name is Matt and I l","t":3256},{"s":"My name is Matt and I lo","t":4149},{"s":"My name is Matt and I l","t":4815},{"s":"My name is Matt and I li","t":5039},{"s":"My name is Matt and I lik","t":5216},{"s":"My name is Matt and I like","t":5291},{"s":"My name is Matt and I like ","t":5382},{"s":"My name is Matt and I like t","t":5479},{"s":"My name is Matt and I like to","t":5533},{"s":"My name is Matt and I like to ","t":5670},{"s":"My name is Matt and I like to c","t":6180},{"s":"My name is Matt and I like to co","t":6311},{"s":"My name is Matt and I like to cod","t":6415},{"s":"My name is Matt and I like to code","t":6500}],
        'q-2': [{"s":"I","t":0},{"s":"I ","t":163},{"s":"I g","t":209},{"s":"I ge","t":295},{"s":"I gen","t":421},{"s":"I gene","t":472},{"s":"I gener","t":543},{"s":"I genera","t":615},{"s":"I general","t":672},{"s":"I generall","t":812},{"s":"I generally","t":955},{"s":"I generally ","t":1137},{"s":"I generally j","t":1279},{"s":"I generally ju","t":1465},{"s":"I generally jus","t":1546},{"s":"I generally just","t":1628},{"s":"I generally just ","t":1703},{"s":"I generally just b","t":1959},{"s":"I generally just bu","t":2038},{"s":"I generally just buy","t":2159},{"s":"I generally just buy ","t":2328},{"s":"I generally just buy w","t":2505},{"s":"I generally just buy wh","t":2569},{"s":"I generally just buy wha","t":2705},{"s":"I generally just buy what","t":2828},{"s":"I generally just buy whate","t":2945},{"s":"I generally just buy whatev","t":3146},{"s":"I generally just buy whateve","t":3271},{"s":"I generally just buy whatever","t":3361},{"s":"I generally just buy whatever'","t":3455},{"s":"I generally just buy whatever's","t":3572},{"s":"I generally just buy whatever's ","t":3651},{"s":"I generally just buy whatever's c","t":3765},{"s":"I generally just buy whatever's ch","t":3880},{"s":"I generally just buy whatever's che","t":3966},{"s":"I generally just buy whatever's chea","t":4054},{"s":"I generally just buy whatever's cheap","t":4151},{"s":"I generally just buy whatever's cheape","t":4246},{"s":"I generally just buy whatever's cheapes","t":4337},{"s":"I generally just buy whatever's cheapest","t":4421},{"s":"I generally just buy whatever's cheapest.","t":4512},{"s":"I generally just buy whatever's cheapest..","t":4668},{"s":"I generally just buy whatever's cheapest...","t":4817}],
    }
    responses = {
        'q-1': "My name is Matt and I like to code",
        'q-2': "I generally just buy whatever's cheapest...",
    }

    survey_id = 'shampoo_survey_v4'

    participant_id = 'p_1'

    API_KEY = os.getenv("ROUNDTABLE_API_KEY")

    fetch_results = run_fetch(questions, question_histories, responses, survey_id, participant_id, API_KEY)

    print(fetch_results)