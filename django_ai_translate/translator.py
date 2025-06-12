import asyncio
from tqdm import tqdm
from .settings import AI_TRANSLATOR, AI_CLIENT as client, AI_ASYNC_CLIENT as async_client

def translate_text(text, 
                         target_language, 
                         model=AI_TRANSLATOR['MODEL'], 
                         prompt_text=AI_TRANSLATOR['PROMPT_TEXT']):
    prompt = f"{prompt_text} {target_language}:\n\n{text}"
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content.strip()



async def async_translate_text(text,
                          target_language,
                          model=AI_TRANSLATOR['MODEL'],
                          prompt_text=AI_TRANSLATOR['PROMPT_TEXT']):
    prompt = f"{prompt_text} {target_language}:\n\n{text}"
    
    if AI_TRANSLATOR['ENGINE'] == 'anthropic':
        # Use async context manager for streaming
        async with async_client.messages.stream(
            max_tokens=4096,
            model=model,
            messages=[{"role": "user", "content": prompt}]
        ) as stream:
            content = ""
            async for chunk in stream:
                if hasattr(chunk, 'delta') and hasattr(chunk.delta, 'text'):
                    content += chunk.delta.text
                elif hasattr(chunk, 'content_block') and hasattr(chunk.content_block, 'text'):
                    content += chunk.content_block.text
            return content.strip()
    else:
        response = await async_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            timeout=600.0  # 10 minutes timeout
        )
        return response.choices[0].message.content.strip()

async def translate_in_batches(entries, target_language, batch_size=100):
    for i in tqdm(range(0, len(entries), batch_size), desc="Translating", total=len(entries) // batch_size):
        batch = entries[i:i + batch_size]
        tasks = [async_translate_text(entry.msgid, target_language) for entry in batch]
        translations = await asyncio.gather(*tasks)
        for entry, translation in zip(batch, translations):
            entry.msgstr = translation