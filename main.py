from pytube import YouTube
from flask import Flask, request, send_file
import os
app = Flask(__name__)


@app.route('/')
def strm():
    link = request.args.get('link')
    try:
        print(link)
        obj = YouTube(link)
        yt = obj.streams.get_lowest_resolution()
        yt.download('static')
        return send_file(f"{os.getcwd()}\static\{obj.title}.mp4", as_attachment=True)
    except Exception as e:
        return f'Error: {str(e)}'


if __name__ == '__main__':
    app.run(port=8080)
