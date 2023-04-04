from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        with open('DCnewpickle', 'rb') as r:
            model = pickle.load(r)

        SALEYEAR = request.form['SALEYEAR']
        WARD = request.form['WARD']
        ASSESSMENT_NBHD = request.form['ASSESSMENT_NBHD']
        STYLE = request.form['STYLE']
        STRUCT = request.form['STRUCT']
        EXTWALL = request.form['EXTWALL']
        INTWALL = request.form['INTWALL']
        ROOF = request.form['ROOF']
        GRADE = request.form['GRADE']
        CNDTN = request.form['CNDTN']
        NUM_UNITS = float(request.form['NUM_UNITS'])
        BLDG_NUM = float(request.form['BLDG_NUM'])
        ROOMS = float(request.form['ROOMS'])
        BEDRM = float(request.form['BEDRM'])
        BATHRM = float(request.form['BATHRM'])
        HF_BATHRM = float(request.form['HF_BATHRM'])
        KITCHENS = float(request.form['KITCHENS'])
        FIREPLACES = float(request.form['FIREPLACES'])
        AC = request.form['AC']
        HEAT = request.form['HEAT']
        LANDAREA = request.form['LANDAREA']
        GBA = request.form['GBA']
        AYB = float(request.form['ageAYB'])
        SALEMONTH = request.form['SALEMONTH']
        YR_RMDL = request.form['binYR_RMDL']
        EYB = request.form['binEYB']

        input_df = pd.DataFrame({
            'SALEYEAR': [SALEYEAR],
            'WARD': [WARD],
            'ASSESSMENT_NBHD': [ASSESSMENT_NBHD],
            'STYLE': [STYLE],
            'STRUCT': [STRUCT],
            'EXTWALL': [EXTWALL],
            'INTWALL': [INTWALL],
            'ROOF': [ROOF],
            'GRADE': [GRADE],
            'CNDTN': [CNDTN],
            'NUM_UNITS': [NUM_UNITS],
            'BLDG_NUM': [BLDG_NUM],
            'ROOMS': [ROOMS],
            'BEDRM': [BEDRM],
            'BATHRM': [BATHRM],
            'HF_BATHRM': [HF_BATHRM],
            'KITCHENS': [KITCHENS],
            'FIREPLACES': [FIREPLACES],
            'AC': [AC],
            'HEAT': [HEAT],
            'LANDAREA': [LANDAREA],
            'GBA': [GBA],
            'ageAYB': [AYB],
            'SALEMONTH': [SALEMONTH],
            'binYR_RMDL': [YR_RMDL],
            'binEYB': [EYB]
        })

        predict_price = model.predict(input_df)[0]
        print("Predicted price:", predict_price)
        return render_template('hasil.html', pred_price=predict_price, saleyear=SALEYEAR, ward=WARD, 
        assessment_nbhd=ASSESSMENT_NBHD, style=STYLE, struct=STRUCT, extwall=EXTWALL, intwall=INTWALL, 
        roof=ROOF, grade=GRADE, cndtn=CNDTN, num_units=NUM_UNITS, bldg_num=BLDG_NUM, rooms=ROOMS, bedrm=BEDRM, 
        bathrm=BATHRM, hf_bathrm=HF_BATHRM, kitchens=KITCHENS, fireplaces=FIREPLACES, ac=AC, heat=HEAT, 
        landarea=LANDAREA, gba=GBA, ayb=AYB, salemonth=SALEMONTH, yr_rmdl=YR_RMDL, eyb=EYB)

        # return render_template('hasil.html', pred_price=predict_price)

    # If request method is GET, return the form
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

