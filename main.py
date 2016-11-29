#!/Users/Matt/Development/ENVS/sermon_movie_maker/bin/python
from mutagen.mp3 import MP3
import settings
import os
from PIL import Image


def main():

    image = str(raw_input("Enter full path of image file: ")).strip()
    audio_file_name = str(raw_input("Enter full path of mp3 file: ")).strip()
    output_file_name = str(raw_input("Enter desired name of output file: "))
    audio_length = MP3(audio_file_name).info.length
    title = str(raw_input("Enter title of sermon: "))
    speaker = str(raw_input("Enter speaker of sermon: "))
    date = str(raw_input("Enter date of sermon: "))

    with open(os.path.dirname(os.path.realpath(__file__)) +
              "/text/title.txt", 'wb') as title_file:
        title_file.write(title + "\n")
    with open(os.path.dirname(os.path.realpath(__file__)) +
              "/text/speaker.txt", 'wb') as speaker_file:
        speaker_file.write(speaker + "\n")
    with open(os.path.dirname(os.path.realpath(__file__)) +
              "/text/date.txt", 'wb') as date_file:
        date_file.write(date)

    resized_image = Image.open(image)
    resized_image.thumbnail([1280, 1280])
    resized_image.save(os.path.dirname(os.path.relpath(__file__)) +
                       '/image/image.jpg')

    os.system("""ffmpeg -y -loop 1 -i "{image}"\
              -i "{audio_file_name}"\
              -t {audio_length} -pix_fmt yuv420p \
              -vf "drawtext=fontcolor={text_color}:\
                   fontfile={font_file_path}:\
                   textfile='{title}':\
                   fontsize={font_size}:\
                   bordercolor={border_color}:\
                   borderw={border_width}:\
                   alpha={text_alpha}:\
                   x={horizontal_position}:y={vertical_position}-text_h:\
                   box={box}:\
                   boxborderw={box_border_width}:\
                   boxcolor={box_color},\
                  drawtext=fontcolor={text_color}:\
                   fontfile={font_file_path}:\
                   textfile='{speaker}':\
                   fontsize={font_size}:\
                   bordercolor={border_color}:\
                   borderw={border_width}:\
                   alpha={text_alpha}:\
                   x={horizontal_position}:y={vertical_position}:\
                   box={box}:\
                   boxborderw={box_border_width}:\
                   boxcolor={box_color},\
                  drawtext=fontcolor={text_color}:\
                   fontfile={font_file_path}:\
                   textfile='{date}':\
                   fontsize={font_size}:\
                   bordercolor={border_color}:\
                   borderw={border_width}:\
                   alpha={text_alpha}:\
                   x={horizontal_position}:y={vertical_position}+text_h:\
                   box={box}:\
                   boxborderw={box_border_width}:\
                   boxcolor={box_color},\
                  scale={scale_width}:-2"\
              "{output_location}/{output_file_name}{video_output_type}"\
              """.format(audio_file_name=audio_file_name,
                         border_color=settings.border_color,
                         border_width=settings.border_width,
                         box=settings.box,
                         box_border_width=settings.box_border_width,
                         box_color=settings.box_color,
                         date=os.path.dirname(os.path.realpath(__file__)) +
                         "/text/date.txt",
                         font_file_path=settings.font_file_path,
                         font_size=settings.font_size,
                         horizontal_position=settings.horizontal_position,
                         image=os.path.dirname(os.path.realpath(__file__)) +
                         "/image/image.jpg",
                         audio_length=audio_length,
                         output_file_name=output_file_name,
                         output_location=settings.output_location,
                         scale_width=settings.scale_width,
                         speaker=os.path.dirname(os.path.realpath(__file__)) +
                         "/text/speaker.txt",
                         text_alpha=settings.text_alpha,
                         text_color=settings.text_color,
                         title=os.path.dirname(os.path.realpath(__file__)) +
                         "/text/title.txt",
                         vertical_position=settings.vertical_position,
                         video_output_type=settings.video_output_type
                         )
              )


if __name__ == "__main__":
    main()
