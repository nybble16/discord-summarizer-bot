import openai

from async_lru_cache import AsyncLRUCache

cache = AsyncLRUCache()


async def call_openai_summarize(messages_context, messages_in_channel):
    print("Getting summary for: " + messages_in_channel[:50])

    # return messages_in_channel

    completion = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {
                "role": "assistant",
                "content": f"Oto kontekst rozmowy na czacie: \n\n{'-' * 10}\n{messages_context}\n{'-' * 10}\n\n>>> Poniżej znajduje się kontynuacja, i tę kontynuację chciałbym abyś streścił znając powyższy kontekst: \n\n\n{messages_in_channel}"
            }
        ]
    )
    return completion.choices[0].message.content


async def get_summary(channel_context, channel_messages):
    key = (tuple(channel_context), tuple(channel_messages))
    cached_result = await cache.get(key)
    if cached_result is not None:
        return cached_result
    else:
        result = await call_openai_summarize(channel_context, channel_messages)
        await cache.set(key, result)
        return result
