from flask import jsonify, current_app
from flask import Blueprint
from sqlalchemy import func

from models.Names import Names

bp = Blueprint('routes', __name__)

@bp.route("/")
def index():
    return jsonify([
        {"response": current_app.config['HELLO_MESSAGE']},
        {"db_path": current_app.config['SQLALCHEMY_DATABASE_URI']}
    ])

@bp.route("/name")
def name():
    n = Names.query.order_by(func.random()).first()
    return jsonify({"names": "%s - %d" % (n.name, n.amount)})

@bp.route("/add_random")
def add_random():
    n = Names()
    n.fill_random()
    n.save()
    return jsonify({"added": "%s = %d" % (n.name, n.amount)})



# from flask import Flask, request, Response, render_template
# from io import BytesIO
# from gtts import gTTS
# from pydub import AudioSegment
# from googletrans import Translator
# import re



# @app.route('/create_mp3_from_words', methods=['POST', 'GET'])
# def create_mp3_from_words():
#     if request.method == 'POST':
#         form = request.form
#         if form:
#             text = form['words']
#             sentences = re.split(r'[.!?]', text)
#             sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

#             enter_language = form['enter_language']
#             destination_language = form['destination_language']

#             final_audio = None
#             translator = Translator()

#             for sentence in sentences:
#                 enter_audio_io = BytesIO()
#                 translated_audio_io = BytesIO()
#                 try:
#                     translated_text = translator.translate(sentence, src=enter_language, dest=destination_language).text

#                     tts_enter = gTTS(sentence, lang=enter_language)
#                     tts_enter.write_to_fp(enter_audio_io)

#                     tts_dest = gTTS(translated_text, lang=destination_language)
#                     tts_dest.write_to_fp(translated_audio_io)

#                 except Exception as e:
#                     # print the exception to command
#                     print("An error occurred:", e)
#                 enter_audio_io.seek(0)
#                 translated_audio_io.seek(0)

#                 enter_audio = AudioSegment.from_file(enter_audio_io, format="mp3")
#                 translated_audio = AudioSegment.from_file(translated_audio_io, format="mp3")
#                 empty_segment_duration_multiplier = len(sentence) // 10
#                 duration = 1000 * empty_segment_duration_multiplier
#                 if duration < 2001:
#                     duration = 2500
#                 if duration > 7000:
#                     duration = 7000
#                 empty_segment = AudioSegment.silent(duration=duration)
#                 if final_audio:
#                     final_audio += enter_audio + translated_audio + empty_segment
#                 else:
#                     final_audio = enter_audio + translated_audio + empty_segment

#             audio_io = BytesIO()
#             final_audio.export(audio_io, format="mp3")
#             audio_io.seek(0)

#             response = Response(audio_io.getvalue(), content_type='audio/mp3')
#             response.headers['Content-Disposition'] = 'attachment; filename="generated.mp3"'
#             return response

#     return render_template('mp3translations.html')
