from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import signalPreprocessing
import pickle
import os
import warnings
app = Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS']='Content-Type'
warnings.filterwarnings('ignore')
model = pickle.load(open('model.pickle','rb'))
a = os.path.abspath('/Users/vincenttran/Document/Cours Efrei/MasterCamp/SignalTreatment/virufy-data-main/clinical/segmented/totalMerged/neg-0421-091-cough-m-47-7.mp3')

@app.route('/signal')
def signal():
    audio = request.args.get('audio') if request.args.get('audio') else None
    print(audio)
    if audio != None:
        [maxmfcc, stdmfcc, maxmagspec, meanmagspec, maxfreqmagspec, maxfreqreg, maxfreqfft] = signalPreprocessing.signalPreprocess(audio)
        print(maxmfcc, stdmfcc, maxmagspec, meanmagspec, maxfreqmagspec, maxfreqreg, maxfreqfft)
        return jsonify({
            "maxmfcc":float(maxmfcc),
            "stdmfcc":float(stdmfcc),
            "maxmagspec":float(maxmagspec),
            "meanmagspec":float(meanmagspec),
            "maxfreqmagspec":int(maxfreqmagspec),
            "maxfreqreg":int(maxfreqreg),
            "maxfreqfft":int(maxfreqfft)
        })
    else:
        return 'audio undefined'

@app.route('/model')
def predmodel():
    smoker = float(request.args.get('smoker') if request.args.get('smoker') else -1)
    medhist = float(request.args.get('medhist') if request.args.get('medhist') else -1)
    symp = float(request.args.get('symp') if request.args.get('symp') else -1)
    maxmfcc = float(request.args.get('maxmfcc') if request.args.get('maxmfcc') else -1)
    stdmfcc = float(request.args.get('stdmfcc') if request.args.get('stdmfcc') else -1)
    maxmagspec = float(request.args.get('maxmagspec') if request.args.get('maxmagspec') else -1)
    meanmagspec = float(request.args.get('meanmagspec') if request.args.get('meanmagspec') else -1)
    maxfreqmagspec = float(request.args.get('maxfreqmagspec') if request.args.get('maxfreqmagspec') else -1)
    maxfreqreg = float(request.args.get('maxfreqreg') if request.args.get('maxfreqreg') else -1)
    maxfreqfft = float(request.args.get('maxfreqfft') if request.args.get('maxfreqfft') else -1)

    final_features = ([[smoker,medhist,symp,maxmfcc, stdmfcc, maxmagspec, meanmagspec, maxfreqmagspec, maxfreqreg, maxfreqfft]])
    prediction = model.predict(final_features)

    return jsonify({"prediction": str(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)