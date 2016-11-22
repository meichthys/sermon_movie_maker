#!/Users/Matt/Development/ENVS/sermon_movie_maker/bin/python
from mutagen.mp3 import MP3
import settings
import os


def main():

    image = str(raw_input("Enter full path of image file: ")).strip()
    audio_file_name = str(raw_input("Enter full path of mp3 file: ")).strip()
    output_file_name = str(raw_input("Enter desired name of output file: "))
    audio_length = MP3(audio_file_name).info.length
    title = str(raw_input("Enter title of sermon: "))
    speaker = str(raw_input("Enter speaker of sermon: "))
    date = str(raw_input("Enter date of sermon: "))

    os.system("""ffmpeg -y -loop 1 -i "{image}"\
              -i "{audio_file_name}"\
              -t {audio_length} -pix_fmt yuv420p \
              -vf "drawtext=fontcolor={text_color}:\
                   fontfile={font_file_path}:\
                   text='{title}\n{speaker}\n{date}':\
                   fontsize={font_size}:\
                   alpha={text_alpha}:\
                   x={horizontal_position}:y={vertical_position}:\
                   box={box}:\
                   boxborderw={box_boarder_width}:\
                   boxcolor={box_color},\
                   scale={scale_width}:-2"\
              "{output_location}/{output_file_name}{video_output_type}"\
              """.format(audio_file_name=audio_file_name,
                         box=settings.box,
                         box_boarder_width=settings.box_boarder_width,
                         box_color=settings.box_color,
                         date=date,
                         font_file_path=settings.font_file_path,
                         font_size=settings.font_size,
                         horizontal_position=settings.horizontal_position,
                         image=image,
                         audio_length=audio_length,
                         output_file_name=output_file_name,
                         output_location=settings.output_location,
                         scale_width=settings.scale_width,
                         speaker=speaker,
                         text_alpha=settings.text_alpha,
                         text_color=settings.text_color,
                         title=title,
                         vertical_position=settings.vertical_position,
                         video_output_type=settings.video_output_type
                         )
              )


if __name__ == "__main__":
    main()
