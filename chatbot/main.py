import openai

# use this on the .json data to format it. (terminal)
# openai tools fine_tunes.prepare_data -f ./datasets/municode_florida_west_palm_beach_chapter94_zoning_and_land_development_regulations.json

# authorize the api with the key from https://platform.openai.com/account/api-keys
openai.api_key = "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"

# create a fine tune model. (terminal)
# openai api fine_tunes.create -t ./datasets/municode_florida_west_palm_beach_chapter94_zoning_and_land_development_regulations.json -m davinci

# Enter a prompt and get an answer (called a completion).
openai.Completion.create(
    model="davinci:ft-personal-2023-07-14-10-54-52",
    prompt=input("Enter your prompt: "))

# Delete a fine-tune model.
# import openai
# openai.Model.delete("davinci:ft-personal-2023-07-14-10-54-52")
