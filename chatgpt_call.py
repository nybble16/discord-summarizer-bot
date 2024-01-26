import openai

from async_lru_cache import AsyncLRUCache

cache = AsyncLRUCache()


async def call_openai_summarize(messages_context, messages_in_channel):
    print("Getting summary for: " + messages_in_channel)

    # return messages_in_channel

    completion = openai.ChatCompletion.create(
        # model="gpt-4-1106-preview",
        model="gpt-4",
        messages=[
            {
                "role": "assistant",
                "content": f"Poproszę Cię o streszcze rozmowy na czacie. Najpierw podam Ci kontekst rozmowy, abyś mógł w lepszy sposób zrozumieć o czym jest rozmowa, a potem napiszę kontynuację, o której streszczenie i zaznaczenie najważniejszych punktów Cię poproszę.\nOto kontekst: \n\n{'-' * 10}\n{messages_context}\n{'-' * 10}\n\n>>>A teraz proszę streść i pogrubiając najważniejsze elementy poniższej rozmowy:\n\n\n{messages_in_channel}"
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
