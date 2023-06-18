import os
import uuid
from pytube import YouTube
from flask import Flask, request, send_file

app = Flask(__name__)


@app.route('/')
def strm():
    link = request.args.get('link')
    try:
        print(link)
        obj = YouTube(link)
        yt = obj.streams.get_lowest_resolution()

        unique_filename = str(uuid.uuid4()) + '.mp4'

        temp_directory = '/tmp'
        temp_file = os.path.join(temp_directory, unique_filename)

        yt.download(output_path=temp_directory, filename=unique_filename)

        return send_file(temp_file, as_attachment=True)
    except Exception as e:
        return f'Error: {str(e)}'


if __name__ == '__main__':
    app.run(port=8080)
