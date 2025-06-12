from django.conf import settings

AI_TRANSLATOR = getattr(settings, 'AI_TRANSLATOR', {
    'ENGINE': '',
    'API_KEY': '',
    'MODEL': '',
    'PROMPT_TEXT': "You are a web application translator. Don't ouput thinking. Don't add anything else than result. Translate the following text to "
})

if AI_TRANSLATOR['ENGINE'] == 'groq':
    from groq import Groq, AsyncGroq
    client = Groq(api_key=AI_TRANSLATOR['API_KEY'])
    async_client = AsyncGroq(api_key=AI_TRANSLATOR['API_KEY'])

if AI_TRANSLATOR['ENGINE'] == 'openai':
    from openai import AsyncOpenAI, OpenAI
    client = OpenAI(api_key=AI_TRANSLATOR['API_KEY'])
    async_client = AsyncOpenAI(api_key=AI_TRANSLATOR['API_KEY'])

if AI_TRANSLATOR['ENGINE'] == 'together':
    from together import Together, AsyncTogether
    client = Together(api_key=AI_TRANSLATOR['API_KEY'])
    async_client = AsyncTogether(api_key=AI_TRANSLATOR['API_KEY'])

if AI_TRANSLATOR['ENGINE'] == 'anthropic':
    from anthropic import Anthropic, AsyncAnthropic
    client = Anthropic(api_key=AI_TRANSLATOR['API_KEY'])
    async_client = AsyncAnthropic(api_key=AI_TRANSLATOR['API_KEY'])


AI_CLIENT = client
AI_ASYNC_CLIENT = async_client
