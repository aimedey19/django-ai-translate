import asyncio
from tqdm import tqdm
from .settings import AI_TRANSLATOR, AI_CLIENT as client, AI_ASYNC_CLIENT as async_client

def translate_text(text, 
                         target_language=AI_TRANSLATOR['LANGUAGE'], 
                         model=AI_TRANSLATOR['MODEL'], 
                         prompt_text=AI_TRANSLATOR['PROMPT_TEXT']):
    prompt = f"{prompt_text} {target_language}:\n\n{text}"
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


async def async_translate_text(text, 
                         target_language=AI_TRANSLATOR['LANGUAGE'], 
                         model=AI_TRANSLATOR['MODEL'], 
                         prompt_text=AI_TRANSLATOR['PROMPT_TEXT']):
    prompt = f"{prompt_text} {target_language}:\n\n{text}"
    response = await async_client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content.strip()



async def translate_in_batches(entries, target_language, batch_size=100):
    for i in tqdm(range(0, len(entries), batch_size), desc="Translating"):
        batch = entries[i:i + batch_size]
        tasks = [async_translate_text(entry.msgid, target_language) for entry in batch]
        translations = await asyncio.gather(*tasks)
        for entry, translation in zip(batch, translations):
            entry.msgstr = translation
            
