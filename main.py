import os
import uuid
from pytube import YouTube
from flask import Flask, request, send_file,render_template

app = Flask(__name__)

@app.route('/home')
def hom():
    return render_template('index.html')
@app.route('/')
def strm():
    link = request.args.get('link')
    if link is None:
        return render_template('index.html')
    else: 
        pass
    try:
        print(link)
        obj = YouTube(link)
        yt = obj.streams.get_highest_resolution()

        unique_filename = str(uuid.uuid4()) + '.mp4'

        temp_directory = '/tmp'
        temp_file = os.path.join(temp_directory, unique_filename)

        yt.download(output_path=temp_directory, filename=unique_filename)

        return send_file(temp_file, as_attachment=True,download_name=obj.title)
    except Exception as e:
        return f'Error: {str(e)}'


if __name__ == '__main__':
    app.run(port=8080)
