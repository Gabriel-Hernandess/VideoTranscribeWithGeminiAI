# Sistema de transcricao de videos em resumo com seus principais pontos utilizando o Gemini Ai.
# Desenvolvido por Gabriel Yanagawa Hernandes
# LinkedIn: https://www.linkedin.com/in/gabriel-hernandess/
# GitHub: https://github.com/Gabriel-Hernandess 

import yt_dlp
import speech_recognition as sr
import os
import subprocess
import google.generativeai as genai

genai.configure(api_key='SUA_API_KEY')
model = genai.GenerativeModel('gemini-pro')

# Função para baixar o vídeo em formato mp3
def baixar_video(link, caminho_arquivo='audio'):
    opcoes = {
        'format': 'bestaudio/best',
        'outtmpl': caminho_arquivo,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([link])
    
    return caminho_arquivo + '.mp3'


# Função para converter o mp3 em wav
def converter_mp3_para_wav(arquivo_mp3, arquivo_wav):
    subprocess.run(['ffmpeg', '-i', arquivo_mp3, '-ar', '16000', arquivo_wav])
    os.remove(arquivo_mp3)


# Função para transcrever o texto do vídeo
def transcrever(arquivo='audio.wav'):
    print('Transcrevendo vídeo, aguarde...')
    r = sr.Recognizer()

    audio_file = sr.AudioFile(arquivo)

    with audio_file as source:
        audio = r.record(source)

        try:
            texto = r.recognize_google(audio, language='pt-BR')
            query = f'Faça um resumo do seguinte texto e descreva seus principais pontos: {texto}'  
            response = model.generate_content(query)

            print(f'Texto transcrito: {texto}\nResposta: {response.text}')
        except sr.UnknownValueError:
            print("O reconhecimento de fala não conseguiu entender o áudio.")
        except sr.RequestError as e:
            print(f"Erro ao se conectar ao serviço de reconhecimento de fala: {e}")


# Coletar o link do vídeo inserido pelo usuário
while True:
    link = input('Digite o link do vídeo a ser transcrito: ')
    option = input(f'O vídeo {link} está correto? [1] SIM [2] NÃO: ')
    
    if option == '1':
        break


# Baixar o vídeo que o usuário quer processar a transcrição
try:
    print('Seu vídeo está sendo processado, aguarde...')
    caminho_arquivo_mp3 = baixar_video(link)

    if caminho_arquivo_mp3:
        caminho_arquivo_wav = 'audio.wav'
        converter_mp3_para_wav(caminho_arquivo_mp3, caminho_arquivo_wav)

        transcrever(caminho_arquivo_wav)
except Exception as e:
    print(f'Erro ao processar o vídeo: {e}')