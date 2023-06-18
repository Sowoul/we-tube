from flask import Flask, request
from pytube import YouTube

app = Flask(__name__)


@app.route('/')
def strm():
    link = request.args.get('link')
    try:
        print(link)
        obj = YouTube(link)
        yt = obj.streams.get_lowest_resolution()
        yt.download()
        return f'<b>Succesfully downloaded : </b>{obj.title}'
    except Exception as e:
        return f'Error: {str(e)}'


if __name__ == '__main__':
    app.run(port=8080)
    pass
