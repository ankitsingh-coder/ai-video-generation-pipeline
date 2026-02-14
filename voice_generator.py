import edge_tts
import asyncio

async def generate_voice(script, output_file="voice.mp3"):
    communicate = edge_tts.Communicate(script, "en-US-GuyNeural")
    await communicate.save(output_file)
[]