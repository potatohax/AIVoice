from voicevox import Client
import asyncio

#field variables
speaker = 20; #check voicevox_speakers.json for speakers list


async def voiceConversion(inputText):
    async with Client() as client:
        audio_query = await client.create_audio_query(
            inputText, speaker = speaker
        )
        with open("sound/aivoice.wav", "wb") as f:
            f.write(await audio_query.synthesis(speaker = speaker))


if __name__ == "__main__":
    asyncio.run(voiceConversion())

