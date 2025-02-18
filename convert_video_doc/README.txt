README - Conversor de Vídeo para Documento

Descrição

Este projeto tem como objetivo extrair o áudio de um vídeo do YouTube, converter para texto e salvar o resultado em um documento. O sistema é desenvolvido em Python e utiliza bibliotecas especializadas para download de vídeos, conversão de áudio e transcrição.

Dependências Necessárias

Antes de executar o script, instale as seguintes dependências:

1. Instalar o Python (se não estiver instalado)

Baixe e instale a versão mais recente do Python:https://www.python.org/downloads/

Durante a instalação, marque a opção "Add Python to PATH".

2. Instalar as bibliotecas Python necessárias

Abra um terminal (CMD ou PowerShell) e execute:

pip install yt-dlp ffmpeg-python speechrecognition pydub

3. Instalar o FFmpeg

O FFmpeg é necessário para processar o áudio.

Baixe o FFmpeg em: https://www.gyan.dev/ffmpeg/builds/

Extraia os arquivos e copie a pasta para C:\ffmpeg

Adicione C:\ffmpeg\bin ao PATH do Windows:

Pressione Win + R e digite sysdm.cpl

Acesse a aba Avançado > Variáveis de Ambiente

No campo Variáveis do Sistema, selecione Path e clique em Editar

Adicione C:\ffmpeg\bin e clique em OK

Reinicie o computador

Teste se a instalação está correta abrindo o Prompt de Comando e digitando:

ffmpeg -version
ffprobe -version

Se aparecer informações sobre o FFmpeg, a configuração está correta.

Como Executar o Script

Abra um terminal (CMD ou PowerShell) e navegue até a pasta do projeto:

cd C:\temp\convert_video_doc

Execute o script com o seguinte comando:

python convert_viedo_doc.py

=============================================================================================
python.exe .\convert_viedo_doc.py
Digite o link do vídeo do YouTube: https://www.youtube.com/watch?v=sV5EqoVQUtM
Baixando o áudio...
[youtube] Extracting URL: https://www.youtube.com/watch?v=sV5EqoVQUtM 
[youtube] sV5EqoVQUtM: Downloading webpage 
[youtube] sV5EqoVQUtM: Downloading tv client config 
[youtube] sV5EqoVQUtM: Downloading player af7f576f 
[youtube] sV5EqoVQUtM: Downloading tv player API JSON 
[youtube] sV5EqoVQUtM: Downloading ios player API JSON 
[youtube] sV5EqoVQUtM: Downloading m3u8 information 
[info] sV5EqoVQUtM: Downloading 1 format(s): 251 
[download] downloads\audio.webm has already been downloaded 
[download] 100% of    3.43MiB
[ExtractAudio] Destination: downloads\audio.mp3 
Deleting original file downloads\audio.webm (pass -k to keep) 
Transcrevendo o áudio...
100%|███████████████████████████████████████| 139M/139M [00:16<00:00, 9.07MiB/s]
Salvando transcrição...
Transcrição salva em: transcription.docx
===============================================================================================

O script irá solicitar o link do vídeo do YouTube. Digite o link e pressione Enter.

O sistema irá:

Baixar o áudio do vídeo

Converter o áudio para texto

Salvar o texto em um arquivo

O arquivo de saída será salvo na pasta outputs/ com o nome do vídeo.

Solução de Problemas

Erro: ffmpeg not found

Se o erro indicar que o ffmpeg não foi encontrado:

Confirme que C:\ffmpeg\bin está no PATH do sistema.

Execute:

where ffmpeg

Se não retornar um caminho válido, adicione manualmente C:\ffmpeg\bin ao PATH.

Erro: yt-dlp: DownloadError: ERROR: Postprocessing: ffmpeg not found

Execute o comando abaixo para instalar corretamente:

pip install --upgrade yt-dlp

Caso persista, tente rodar o script com o parâmetro:

python convert_viedo_doc.py --ffmpeg-location "C:/ffmpeg/bin/"

Outros Problemas

Caso encontre algum outro erro, reinicie o computador e verifique se todas as dependências estão corretamente instaladas.

Autor

Criado por Renato Barros
Profissão: Engenheiro de Software e Oracle 


python.exe .\convert_viedo_doc.py
Digite o link do vídeo do YouTube: https://www.youtube.com/watch?v=sV5EqoVQUtM
Baixando o áudio...
[youtube] Extracting URL: https://www.youtube.com/watch?v=sV5EqoVQUtM 
[youtube] sV5EqoVQUtM: Downloading webpage 
[youtube] sV5EqoVQUtM: Downloading tv client config 
[youtube] sV5EqoVQUtM: Downloading player af7f576f 
[youtube] sV5EqoVQUtM: Downloading tv player API JSON 
[youtube] sV5EqoVQUtM: Downloading ios player API JSON 
[youtube] sV5EqoVQUtM: Downloading m3u8 information 
[info] sV5EqoVQUtM: Downloading 1 format(s): 251 
[download] downloads\audio.webm has already been downloaded 
[download] 100% of    3.43MiB
[ExtractAudio] Destination: downloads\audio.mp3 
Deleting original file downloads\audio.webm (pass -k to keep) 
Transcrevendo o áudio...
100%|███████████████████████████████████████| 139M/139M [00:16<00:00, 9.07MiB/s]
Salvando transcrição...
Transcrição salva em: transcription.docx