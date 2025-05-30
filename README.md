![GitHub release (latest by date)](https://img.shields.io/github/v/release/OWNER/REPO) <br>
Speech is the fastest modern interface. as such, I'm more interested in developing chatbots than I am in GUIs.

test
This chatbot is a python-OpenAI API. It fine-tunes the existing Davinci LLM (large language model) to include data from the West Palm Beach, FL section of Municode (development code). 400 lines of prompt-completion pairs were formatted to .json and given to OpenAI. OpenAI charges for this service. So, I've deactivated the authorization keys. After training, the model is able to answer municode related questions with a 35% accuracy.

While the accuracy of this project is too low to be useful, it was a success. I gained experience with the fine-tuning process. Chatbots can replace GUIs as the major interface method. Their value is speed. So, chatbots seems necessary on the path to create city generating programs.

## Directions

-   Go to /building_code_consultant/chatbot/
-   Run `python3 main.py` in terminal.
-   Enter chatbot questions.

## Dependencies

-   Python3
-   Openai

## Features To Come

-   Higher answer accuracy
-   GPT 3.5/4 integration
-   3d model awareness
-   Omniverse support
-   larger datasets than just West Palm Beach, FL
-   autonomy (ability to execute functions)
