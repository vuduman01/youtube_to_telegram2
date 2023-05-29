import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from pytube import YouTube
from moviepy.editor import VideoFileClip,AudioFileClip

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def download_youtube(url):
    yt = YouTube(url)
    title = yt.title
    streams = yt.streams.filter(only_audio=True)
    best_stream = streams[1]
    best_stream.download()
    return title

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="hello, Vlad")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello")

async def audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = context.args[0]
    title = await download_youtube(message) 
    mp4_file = title + '.mp4'
    mp3_file = title + '.mp3'

    file_to_convert = AudioFileClip(mp4_file) 
    file_to_convert.write_audiofile(mp3_file)
    file_to_convert.close()
    await context.bot.send_audio(chat_id=update.effective_chat.id, audio=mp3_file)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = context.args[0]
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)





application = ApplicationBuilder().token('TOKEN').build()
    
start_handler = CommandHandler('start', start)
hello_handler = CommandHandler('hello', hello)
send_audio_handler = CommandHandler('audio', audio)
echo_handler = CommandHandler('echo', echo)

application.add_handler(start_handler)
application.add_handler(hello_handler)
application.add_handler(send_audio_handler)
application.add_handler(echo_handler)

    
application.run_polling()