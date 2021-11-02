from flask import Flask
from flask import request, render_template
import platform
app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    running_processor = platform.processor()
#    running_on = platform.platform()
#    return 'Hey, we have Flask running on...' + str(running_on)+" "+str(running_processor)

@app.route('/', methods=['GET', 'POST'])
def index():
    running_processor = platform.processor()
    running_on = platform.platform()
    showme = str(running_on)+" "+str(running_processor)
    return render_template('index.html', post=showme)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

