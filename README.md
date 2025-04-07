# Cinemorph

AI-based audio panning using video scene analysis.

Steps:
1. Run object detection
2. Run audio panning
3. Merge final video ( ffmpeg -i detected_video.mp4 -i processed_audio.wav -c:v copy -map 0:v:0 -map 1:a:0 -shortest final_output.mp4 )

Need to improve recognition algorithm and audio timing.
