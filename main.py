"""Converts static jpg + mp3 into an mp4"""
import os

from imagesoup import ImageResult, ImageSoup
from PIL import Image
from mutagen.mp3 import MP3

import settings


def main():
    '''Runs Sermon Movie Maker'''
    # Get Input
    image = input("Enter full path of image file or search term: ").strip().replace("\\", "")
    if not os.path.isfile(image):
        results = ImageSoup().search(image, aspect_ratio='wide', image_size="800x600+")
        result = 0
        not_ready = True
        while not_ready:
            img = ImageResult(results[result].URL)
            img.reduce(720)
            img.to_file("upload_image")
            img.show()
            not_ready = input(" \
                OPTIONS: \n \
                -------- \n \
                Press ENTER to use the displayed image. \n \
                Press 1 then ENTER to see the next image. \n \
                ")
            result += 1
        image = "upload_image"
    audio_file_name = input("Enter full path of mp3 file: ").strip().replace("\\","")
    output_file_name = input("Enter desired name of output file: ")
    audio_length = MP3(audio_file_name).info.length
    title = input("Enter title of sermon: ")
    speaker = input("Enter speaker of sermon: ")
    date = input("Enter date of sermon: ")

    title_path = f"{os.path.realpath('')}/text/title.txt"
    speaker_path = f"{os.path.realpath('')}/text/speaker.txt"
    date_path = f"{os.path.realpath('')}/text/date.txt"
    image_path = f"{os.path.realpath('')}/image/image.jpg"

    # Save Text & create containing folder if it doesn't exist
    os.makedirs(os.path.dirname(title_path), exist_ok=True)
    with open(title_path, 'w') as title_file:
        title_file.write(title + "\n")
    with open(speaker_path, 'w') as speaker_file:
        speaker_file.write(speaker + "\n")
    with open(date_path, 'w') as date_file:
        date_file.write(date)

    # Resize Image & create containing folder if it doesn't exist
    resized_image = Image.open(image)
    resized_image.thumbnail([1280, 1280])
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    resized_image.save(image_path)

    # Run conversion
    os.system(f"""ffmpeg -y -loop 1 -i "{image}"\
              -i "{audio_file_name}"\
              -t {audio_length} -pix_fmt yuv420p \
              -vf "drawtext=fontcolor={settings.text_color}:\
                   fontfile={settings.font_file_path}:\
                   textfile='{title_path}':\
                   fontsize={settings.font_size}:\
                   bordercolor={settings.border_color}:\
                   borderw={settings.border_width}:\
                   alpha={settings.text_alpha}:\
                   x={settings.horizontal_position}:y={settings.vertical_position}-text_h:\
                   box={settings.box}:\
                   boxborderw={settings.box_border_width}:\
                   boxcolor={settings.box_color},\
                  drawtext=fontcolor={settings.text_color}:\
                   fontfile={settings.font_file_path}:\
                   textfile='{speaker_path}':\
                   fontsize={settings.font_size}:\
                   bordercolor={settings.border_color}:\
                   borderw={settings.border_width}:\
                   alpha={settings.text_alpha}:\
                   x={settings.horizontal_position}:y={settings.vertical_position}:\
                   box={settings.box}:\
                   boxborderw={settings.box_border_width}:\
                   boxcolor={settings.box_color},\
                  drawtext=fontcolor={settings.text_color}:\
                   fontfile={settings.font_file_path}:\
                   textfile='{date_path}':\
                   fontsize={settings.font_size}:\
                   bordercolor={settings.border_color}:\
                   borderw={settings.border_width}:\
                   alpha={settings.text_alpha}:\
                   x={settings.horizontal_position}:y={settings.vertical_position}+text_h:\
                   box={settings.box}:\
                   boxborderw={settings.box_border_width}:\
                   boxcolor={settings.box_color},\
                  scale={settings.scale_width}:-2"\
              "{settings.output_location}/{output_file_name}{settings.video_output_type}"\
              """
              )

    #Remove image file if downloaded to local directory
    if os.path.isfile(image):
        os.remove(image)

if __name__ == "__main__":
    main()
