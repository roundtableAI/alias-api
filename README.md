# Roundtable Alias API

This repository contains details on using the [Roundtable](https://roundtable.ai) Alias API for survey bot and fraud detection.

## Setup

Roundtable Alias tracks behavior on open-ended survey questions and identifies potential fraudulent or bot-like responses. 
Our reccomended use of the API consists of two steps: (1) adding our [Javascript tracker](tracking-script.js) to any pages of your survey that have open-ended questions, and (2) passing the data generated by this script to our API for scoring. If needed, however, you can skip step (1) and just pass the participant's responses to each question.

## Getting Started

Follow these steps to use the Alias API:

1. **Set up Javascript Tracker (optional):** Our [Javascript tracker](tracking-script.js) generates a history of every change made for each open-ended textbox. To use this tracker, replace the value of the `textbox_id` variable at the top of the script with the HTML id of the relevant textbox and then store the generated `question_history`. You can also specify the max number of characters the parsed `question_history` should take before it stops tracking (by default, this is set to 25,000). Note that as is, the script only works if there is one textbox per page. **Also note that the script will need to be modified if participants can go "back" to edit their question.**
2. **Generate an API key:** Sign up at [https://roundtable.ai/sign-up](https://roundtable.ai/sign-up), and then navigate to your [account](https://roundtable.ai/account). Here you can generate API keys as needed.
3. **Collect data and format:** Run your survey, storing the `question_history` for each participant and each open-ended question they complete, and structure the data to make API calls as described below. Note that our API *only* takes data from open-ended questions.
4. **Call the API** Call the API using our endpoint at `https://roundtable.ai/.netlify/functions/alias-v01`. **Note: We reccomend waiting at least 5 seconds between each API call as we work to scale**.

## API Endpoints

### `POST /alias-v01`

This endpoint analyzes survey responses to detect fraudulent activity. The API only takes data from one participant---you must make a separate API call for each participant. After a successful API call is made, the data from that call is stored in our database as a response. This allows us to detect duplicate responses if two calls are made with identical responses but different values for `participant_id`.

#### Request Parameters:

- `questions` (Object) [Required]: Contains the survey questions. Each key is the id of the question, and the values are the text of the open-ended survey questions as shown to the participant.
- `question_histories` (Object) [Optional]: Records the changes made by the participant while answering the survey. Each key is the id of the quesiton, and the value is the array of changes generated by our [Javascript tracker](tracking-script.js).
- `responses`: (Object) [Required]: Records the participant's final responses to each question.
- `survey_id` (String) [Required]: A unique identifier for the survey.
- `participant_id` (String) [Required]: A unique identifier for the participant.
- `api_key` (String) [Required]: API key for authentication.

#### Response:

- `error` (Boolean): Indicates if there was an error in processing the request.
- `flagged` (Boolean): Indicates if any fraudulent activity was detected. If true, we reccomend reviewing the participant's responses.
- `num_checks_failed` (Integer): Number of checks that failed.
- `checks` (Object): Details of specific checks and their outcomes.

### Example Usage

To call our API, pass the request parameters in a serialized JSON array to our endpoint. Here's a simple example:

```python
import requests
import json

url = 'https://roundtable.ai/.netlify/functions/alias-v01'

# Data to be sent in the request
data = {
    "questions": {...},  # Replace with your questions object
    "question_histories": {...},  # Replace with your change history object or leave empty
    "responses:": {...},  # Replace with an object with the participant's final responses
    "survey_id": "survey123",
    "participant_id": "participant123",
    "api_key": "your-api-key"
}

# Make the POST request
response = requests.post(url, json=data)

# Parse the response
if response.status_code == 200:
    print("Success:", response.json())
else:
     # Get the body of the response and print
     response_body = response.json()
     print('Error: ', response_body)
```

A more detailed script with examples for each value is shown in [call-api.py](example/call-api.py).