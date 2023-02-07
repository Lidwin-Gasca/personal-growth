from moviepy.editor import ImageSequenceClip, AudioFileClip
import os



def generate_timelapse(images_folder, speed, song=None):
    images = [os.path.join(images_folder, f) for f in os.listdir(images_folder) if f.endswith(".jpg")]
    clip = ImageSequenceClip(images, fps=speed)
    if song:
        audio = AudioFileClip(song)
        clip = clip.set_audio(audio)
    clip.write_videofile(os.path.join(images_folder, "timelapse.mp4"), preset='1080p')






from flask import Flask, request

app = Flask(__name__)

@app.route("/generate_timelapse", methods=["POST"])
def create_timelapse():
    images_folder = request.form.get("images_folder")
    speed = float(request.form.get("speed"))
    song = request.form.get("song")
    generate_timelapse(images_folder, speed, song)
    return "Timelapse generated successfully"

if __name__ == "__main__":
    app.run(debug=True)
