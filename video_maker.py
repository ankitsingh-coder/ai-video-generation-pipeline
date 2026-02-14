from moviepy import ImageClip, AudioFileClip, concatenate_videoclips

def create_video(images, audio_file):
    audio = AudioFileClip(audio_file)

    clips = []
    duration_per_image = audio.duration / len(images)

    for img in images:
        clip = ImageClip(img).resized(height=720).with_duration(duration_per_image)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")
    video = video.with_audio(audio)

    video.write_videofile("final_video.mp4", fps=24)
