# import os
# import openai
# from config import apikey
#
# openai.api_key = apikey
#
# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Write an email to my boss for resignation?",
#   temperature=0.7,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
#
# print(response)
# '''
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "logprobs": null,
#       "text": "\n\nSubject: Resignation\n\nDear [Name],\n\nI am writing to inform you of my intention to resign from my current position at [Company]. My last day of work will be [date].\n\nI have enjoyed my time at [Company], and I am grateful for the opportunity to work here. I have learned a great deal during my time in this position, and I am grateful for the experience.\n\nIf I can be of any assistance during this transition, please do not hesitate to ask.\n\nThank you for your understanding.\n\nSincerely,\n[Your Name]"
#     }
#   ],
#   "created": 1683815400,
#   "id": "cmpl-7F1aqg7BkzIY8vBnCxYQh8Xp4wO85",
#   "model": "text-davinci-003",
#   "object": "text_completion",
#   "usage": {
#     "completion_tokens": 125,
#     "prompt_tokens": 9,
#     "total_tokens": 134
#   }
# }
# '''
# from openai import OpenAI
# from config import apikey
#
# # openai.api_key = apikey
# # Set your OpenAI API key
# api_key = apikey
# OpenAI.api_key = api_key
#
# # Create an instance of the OpenAI class
# client = OpenAI()
#
# response = client.Completion.create(
#     engine="gpt-3.5-turbo-instruct-0914",
#     prompt="write an email to my boss for my resignation?",
#     temperature=0.7,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )

# This code is for v1 of the openai package: pypi.org/project/openai
# from openai import OpenAI
# client = OpenAI()
#
# response = client.completions.create(
#   model="gpt-3.5-turbo-instruct-0914",
#   prompt="write a letter to my boss for my resignation",
#   temperature=1,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )

# working code

# This code is for v1 of the openai package: pypi.org/project/openai

# from openai import OpenAI
# api_key = "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"
#
# # Create an instance of the OpenAI class and pass the API key
# client = OpenAI(api_key=api_key)
#
# # client = OpenAI()
#
# response = client.completions.create(
#   model="gpt-3.5-turbo-instruct-0914",
#   prompt="write a letter to my boss for my resignation",
#   temperature=1,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
#
# print(response)
#
# '''
# choices=[
# CompletionChoice
# (
#            finish_reason='length', index=0,
#            logprobs=None,
#            text='\n[Your Name]\n[Address]\n[City, State ZIP Code]\n[Email]\n[Today’s Date]\n\n[Employer’s Name]\n[Company Name]\n[Address]\n[City, State ZIP Code]\n\nDear [Employer’s Name],\n\nI am writing this letter to inform you that I have decided to resign from my position as [Position] at [Company Name]. After much consideration and careful thought, I have come to the conclusion that it is time for me to pursue new opportunities and challenges.\n\nI want to express my heartfelt gratitude for the support, trust, and guidance you have provided during my time at [Company Name]. It has been a pleasure working with such a dedicated and professional team. I have learned a great deal and will always cherish the experiences I have gained while working here.\n\nPlease consider this letter as my two weeks’ notice, as per the company’s policy. I will ensure that I complete all my current projects and assist in finding and training my replacement during this time. I am committed to ensuring a smooth transition for both the company and my team.\n\nI am thankful for the opportunities that have been given to me during my tenure at [Company Name]. I am proud to have been a part of such a successful and reputable organization, and I am'
# )
# ],
# created=1699772985,
# model='gpt-3.5-turbo-instruct-0914',
# object='text_completion',
# system_fingerprint=None,
# usage=CompletionUsage(completion_tokens=256, prompt_tokens=9, total_tokens=265))
# '''
#
# # Completion(id='cmpl-8JytFOn91mBuD3d8ewUNqlHY1r36j',

# WORKS SOMETIMES

# This code is for v1 of the openai package: pypi.org/project/openai
# from openai import OpenAI
#
# api_key = "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"
# client = OpenAI(api_key=api_key)
#
# response = client.completions.create(
#   model="text-davinci-003",
#   prompt="write a letter to my mother about my health",
#   temperature=1,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
#
# print(response)
#
# '''
# Completion(id='cmpl-8K2TfaZrQRIT26nbeFiaaJ17VUmcT',
#  choices=[
#   CompletionChoice
#   (
#      finish_reason='stop',
#      index=0,
#      logprobs=None,
#      text="\n\nDear Mom,\n\nI hope this letter finds you well. I wanted to take the time to thank you for always being there for me and worrying about my health.\n\nLately, I've been feeling really great. I'm taking better care of myself, giving myself time to rest and recuperate when needed and I'm really seeing the results. Eating better, sleeping better, and just overall feeling a lot healthier has been a game changer.\n\nI also wanted to thank you for encouraging me to put my health first. Last time I visited you, you gave me some really valuable advice about taking the time to get plenty of sleep, eat well, and exercise regularly. It's been an invaluable part of this health journey.\n\nI'm so grateful for you and all the times you've supported me. Your love and concern is always felt and appreciated.\n\nLove,\nYour Son"
#   )
#   ],
#   created=1699786775,
#   model='text-davinci-003',
#   object='text_completion',
#   system_fingerprint=None,
#   usage=CompletionUsage(
#   completion_tokens=187,
#   prompt_tokens=9,
#   total_tokens=196
#   ),
#   warning='This model version is deprecated. Migrate before January 4, 2024 to avoid disruption of service. Learn more https://platform.openai.com/docs/deprecations')
# '''

# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
api_key = "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"
client = OpenAI(api_key=api_key)

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="write a letter to my mother about my health",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

'''
Completion(
  id='cmpl-8K2iOKG1lyRI46hTc3QWWGdaGIgbQ', 
  choices=[
  CompletionChoice(
    finish_reason='length', 
    index=0, 
    logprobs=None, 
    text="\n\n[Your Name]\n[Address]\n[City, State ZIP Code]\n[Date]\n\nDear Mom,\n\nI hope this letter finds you in good health and spirits. I have been thinking a lot about you lately and I miss you dearly. It has been a while since we last spoke, so I wanted to take this opportunity to update you on my health.\n\nAs you know, I have been struggling with some health issues for a few weeks now. I have been experiencing frequent headaches and fatigue which have been affecting my daily activities. After some medical tests, the doctors have diagnosed me with migraines and have prescribed me some medication to manage the pain.\n\nI have been taking the medication as prescribed and I am happy to say that my headaches have reduced significantly. However, I am still feeling a bit tired and the doctors have advised me to take some rest and follow a healthy diet to regain my strength.\n\nI am also trying to incorporate some physical activity into my daily routine to improve my overall well-being. I have started going for morning walks and I must say, the fresh air and exercise have been doing wonders for my mood and energy levels.\n\nI understand that you must be worried about me, but please don't be. I am taking good care of myself and I have the support"
    )
  ],
 created=1699787688, 
 model='gpt-3.5-turbo-instruct', 
 object='text_completion', 
 system_fingerprint=None, 
 usage=CompletionUsage(completion_tokens=256, prompt_tokens=9,
 total_tokens=265)
)
'''
