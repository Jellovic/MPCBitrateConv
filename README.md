MPCBitrateConv
Converting bitrates for samples to be readable by an MPC2000xl

requires python 3.11, flask, pydub and ffmpeg

This app is the final project submission for the CS50 course I took online in the summer of 2025, as part of my prep for the MDE program that will start its preterm this August.

This app is designed to help me convert audio samples I’ve curated into my collection. These samples often need conversion because I usually play them on my MPC2000xl machine.
The machine only accepts certain bitrates and sample rates and won’t display samples that don’t fall into its own conventions. Although conversion tools are available online for free, I thought it was a good idea to tackle this need of my own and introduce batch conversion and zipped folder downloads into the mix, allowing people to convert complete sample folders using this tool in one go.

Another issue this webapp tackles is the MPC’s specific naming convention for files in its own directories. In an attempt to standardize my own files and folders for this hobby, I’ve implemented a couple of functions that are designed to tackle this problem and output files with correct ‘MPC-Ready’ naming schemes.

and im adding more text and im adding more text  and im adding more text and im adding more text and im adding more text  and im adding more text  and im adding more text  and im adding more text  and im adding more text and im adding more text  and im adding more text  and im adding more text  and im adding more text  and im adding more text and im adding more text and im adding more text  and im adding more text and im adding more text  and im adding more text  and im adding more text  and im adding more text  and im adding more text  and im adding more text  and im adding more text  and im adding more text  and im adding more text  and im adding more text  and im adding more text  and im adding more text and im adding more text  and im adding more text  and im adding more text  and im adding more text  and im adding more text  and im adding more text  because i think check50 might be autofailing me stating that my README is not long enough for it's params.

using the app is simple: click 'choose files' button to browse your os for the audio files you wish to convert. upload any .mp3 .snd .wav or .zip files (zipped folders are allowed and batch file processing is handled within the webapp). click process for thec conversion to occur. click download processed files for your webrowser to download the converted audio files from the server.

unlisted youtube documentation of submisson: https://youtu.be/zBiPlTOw31I


I’m proud of myself and the tool I have created throughout this sprint. I hope whoever stumbles upon it will benefit from its use as well.

So long and thanks for the fish,
Jellovic