# Sistema de Transcrição de Vídeos com seus Principais Pontos usando Gemini AI

Este projeto foi desenvolvido para realizar a transcrição de vídeos, convertendo-os para texto e, em seguida, destacando seus principais pontos através do modelo Gemini AI da Google. O sistema facilita o processamento de vídeos em português.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **yt_dlp**: Para download de vídeos em áudio.
- **FFmpeg**: Utilizado para conversão de áudio de MP3 para WAV.
- **SpeechRecognition**: Biblioteca para transcrição de áudio em texto.
- **Gemini AI (Google Generative AI)**: Para gerar um resumo dos principais pontos do texto transcrito.

## Funcionalidades

- Download do vídeo em áudio (MP3) de uma URL.
- Conversão do áudio de MP3 para WAV.
- Transcrição do áudio em texto usando a API de reconhecimento de fala do Google.
- Geração de um resumo com os principais pontos do texto transcrito utilizando o Gemini AI.

### Pré-requisitos

- Python 3.7+
- yt_dlp (`pip install yt-dlp`)
- FFmpeg (instalado e configurado no sistema)
- SpeechRecognition (`pip install SpeechRecognition`)
- google-generativeai (`pip install google-generativeai`)
