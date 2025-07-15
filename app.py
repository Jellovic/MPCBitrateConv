import re
import os
import zipfile
from pydub import AudioSegment
from flask import Flask, send_file, request, render_template, redirect, flash

app = Flask(__name__)
app.secret_key = 'my_secret_key'

def clear_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

def mpc_filename(original):
    base, _ = os.path.splitext(original)
    base = re.sub(r'[^A-Za-z0-9]', '_', base)
    base = base.upper()[:8]
    return base + ".WAV"

def mpc_audioconvert(audio):
    audio = audio.set_frame_rate(44100)
    audio = audio.set_sample_width(2)
    return audio  

def get_unique_mpc_filename(base_folder, original):
    base, _ = os.path.splitext(original)
    base = re.sub(r'[^A-Za-z0-9]', '_', base)
    base = base.upper()[:8]
    filename = base + ".WAV"
    counter = 1
    while os.path.exists(os.path.join(base_folder, filename)):
        filename = f"{base[:7]}{counter}.WAV"
        counter += 1
    return filename

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')    

    if request.method == 'POST':


        #clean the folders
        clear_folder('processed_folder')
        clear_folder('unzip_folder')

        #save files in the form
        u_upload = request.files.get("user_files")

        #if single file
        if u_upload and u_upload.filename.endswith(('.wav', '.snd', '.mp3')):
            
            # create a AudioSegment Object from files in the form 
            audio = AudioSegment.from_file(u_upload)

            #CONVERT IT FOR MPC2000XL

            
            audio = mpc_audioconvert(audio)

            # Export as 16-bit, 44.1kHz WAV
            output_filename = mpc_filename(u_upload.filename)
            audio.export(os.path.join('processed_folder', output_filename), format="wav")

            #'Success' user feedback
            flash("Successfully processed your audio file")


            return redirect('/')

        if u_upload and u_upload.filename.endswith('.zip'):

            #we know it's folder, we need to unzip it to a dedicated somewhere we can access later on
            with zipfile.ZipFile(u_upload.stream, 'r') as zip_ref:
                zip_ref.extractall('unzip_folder')

            #Loop the folder to enter subfolders
            for root, dirs, files in os.walk('unzip_folder'):
                #loop the subfolder to convert audio files and export them to processed_folder
                for file in files:

                    #only audio files that were found in the zip
                    if file.endswith(('.wav', '.snd', '.mp3')):
                        filepath = os.path.join(root, file)
                        audio = AudioSegment.from_file(filepath)
                        audio = mpc_audioconvert(audio)
                        output_filename = get_unique_mpc_filename('processed_folder', file)
                        audio.export(os.path.join('processed_folder', output_filename), format="wav")

            #'Success' user feedback      
            flash("Successfully processed your audio files")


            return redirect('/')
            

    #if incompatible file
    return render_template('typeerrorscreen.html')


#downloading the files    
@app.route('/download/processed', methods=['GET'])

def download_processed():
        files = os.listdir('processed_folder')
        #if returning a batch of files
        if len(files) > 1:
                #zip it
                with zipfile.ZipFile('processed_folder.zip', 'w') as zipf:
                    for file in files:
                        filepath = os.path.join('processed_folder', file)
                        zipf.write(filepath, arcname=file)       
                #send it
                return send_file('processed_folder.zip', as_attachment=True)

        #if returning single file
        elif len(files) == 1:        
            return send_file(os.path.join('processed_folder', files[0]), as_attachment=True)
        else:
            return render_template('nofiles.html')
    

if __name__ == '__main__':
    app.run(debug=True)
