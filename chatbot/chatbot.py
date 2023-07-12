import openai



# "Davinci" = $0.03/1,000 tokens 
# "Curie" = $0.003/1,000 tokens


openai

# use this on the .json data to format it when you get to the windows pc.
# openai tools fine_tunes.prepare_data -f <LOCAL_FILE>

# pip install openai with a virtual environment
key = "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"

# create a fine tune model
# openai api fine_tunes.create -t ./datasets/municode_florida_west_palm_beach_chapter94_zoning_and_land_development_regulations.json -m curie

# make sure it uploads. the cli will give updates

# use either python or openai cli to make a completion request

# python
openai.Completion.create(
    model="curie:ft-personal-2023-07-12-09-41-49",
    prompt="What is section 94-76?")

# openai cli
# openai api completions.create -m <FINE_TUNED_MODEL> -p <YOUR_PROMPT>


# delete a fine-tune model with either python or openai cli
# python
# import openai
# openai.Model.delete(FINE_TUNED_MODEL)

# openai cli
# openai api models.delete -i <FINE_TUNED_MODEL>


