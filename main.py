import asyncio
from script_generator import generate_script
from voice_generator import generate_voice
from image_fetcher import fetch_images
from video_maker import create_video

topic = input("Enter topic: ")

print("Generating script...")
script = generate_script(topic)

print("Generating voice...")
asyncio.run(generate_voice(script))

print("Fetching images...")
images = fetch_images(topic)
if not images:
    print("Image fetching failed. Exiting gracefully.")
    exit()

print("Creating video...")
create_video(images, "voice.mp3")

print("🎉 Video created successfully: final_video.mp4")


