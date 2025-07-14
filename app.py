from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == 'POST':
        #if single file

        #if multiple files

        #if incompatible file
        
        return render_template('index.html')

    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
