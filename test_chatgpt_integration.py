import pytest
import openai
import json

# Load the test scenarios
with open('test_scenarios.json') as f:
    test_scenarios = json.load(f)

# Define a function to send a prompt to ChatGPT-4
def send_prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # Replace with the correct model name
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.0
    )
    return response['choices'][0]['message']['content']

# Parametrize the test to run for each scenario
@pytest.mark.parametrize("scenario", test_scenarios)
def test_chatgpt_response(scenario):
    prompt = scenario['prompt']
    expected_result = scenario['expected_result']
    
    response = send_prompt(prompt)
    print(f"Response: {response}")  # This will print the response to the console
    
    assert expected_result in response, f"Expected '{expected_result}' to be in the response but got '{response}'"

if __name__ == "__main__":
    pytest.main()
