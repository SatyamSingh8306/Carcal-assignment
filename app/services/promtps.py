from langchain_core.prompts import PromptTemplate

template_str = """
You are a helpful assistant. Please search online for the Wimbledon men's singles final results for the years I give you.  

Return the data only related to this 
'''
    "year": YEAR,
    "champion": "CHAMPION_NAME",
    "runner_up": "RUNNER_UP_NAME",
    "score": "MATCH_SCORE",
    "sets": NUMBER_OF_SETS,
    "tiebreak": true_or_false
'''

Example for 2021:
'''
    "year": 2021,
    "champion": "Novak Djokovic",
    "runner_up": "Matteo Berrettini",
    "score": "6–7(4–7), 6–4, 6–4, 6–3",
    "sets": 4,
    "tiebreak": true
'''
Note: IF you haven't get any data from online they return null

GIVEN YEAR : {years}
"""

prompt = PromptTemplate(
    template=template_str,
    input_variables=["years"]
)

format_prompt = PromptTemplate(
    template="""
Reformat this data into the Wimbledon final JSON dictionary format. Return ONLY valid JSON without any markdown formatting or additional text:

{raw_data}

Return the result in this exact JSON format:
{{
    "champion": "CHAMPION_NAME",
    "runner_up": "RUNNER_UP_NAME", 
    "score": "SCORE_STRING",
    "sets": NUMBER_OF_SETS,
    "tiebreak": TRUE_OR_FALSE
}}
""",
    input_variables=["raw_data"]
)