from flask import Flask
import glob
from flask import send_file
app = Flask(__name__)


def filelist(dirname):
    filenames = glob.glob(dirname+'*')
    ret = []
    for filename in filenames:
        #ret.append(filename)
        tmp = filename[len(dirname):]
        #tmp = filename.replace(dirname,'')
        #tmp = tmp.replace('\\','')
        #tmp = tmp.replace('/','')
        ret.append(tmp)
    return ret
    #for filename in filenames:
        #filepath = os.path.join(dirname, filename)
        #ext = os.path.splitext(full_filename)[-1]
        #if ext == '.py': 

@app.route('/down/<file_name>')    
def downloadFile (file_name):
    path = "./download/"+file_name
    #if os.path.exists(path) == True:
    return send_file(path, as_attachment=True)
    #return ''

@app.route('/down')
def viewFile ():
    filenames = filelist('./download/')
    ret = 'Total : ' + str(len(filenames)) + '<br>'
    for filename in filenames:
        ret = ret + "<a href='/down/"+filename+"'>"+filename + "</a><br>"
    return ret


if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=5000,debug=True) 
    #app.run(port=5000,debug=True) 
