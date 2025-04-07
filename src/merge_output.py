import ffmpeg

input_video = "/assets/test_clip.mp4"
input_audio = "../outputs/processed_audio.wav"
output_video = "../outputs/cinemorph_output.mp4"

ffmpeg.input(input_video).output(input_audio).run(overwrite_output=True)

ffmpeg.output(
    ffmpeg.input(input_video).video,
    ffmpeg.input(input_audio).audio,
    output_video,
    vcodec='copy',
    acodec='aac',
    strict='experimental'
).run(overwrite_output=True)

print("Merged audio with video. Output saved.")