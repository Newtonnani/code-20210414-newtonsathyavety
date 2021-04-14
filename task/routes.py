from flask import current_app as app
from flask import request, render_template, make_response, json

from .models import *
# flask.request.json


@app.route('/')
def index():
    return 'Index Page with all'


@app.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        json_data = request.json
        for data in json_data:
            gender = data.get('Gender')
            height_cm = data.get('HeightCm')
            weight_kg = data.get('WeightKg')
            try:
                bmi = Bmi(gender=gender,height_cm=int(height_cm),weight_kg=weight_kg)
                db.session.add(bmi)
                db.session.commit()
            except Exception as e:
                return(str(e)),400
        return "bmi details submited",200
    else:
        data = []
        if Bmi.query.all():
            for i in Bmi.query.all():
                obj = {}
                obj['gender'] = i.gender
                obj['height'] = i.height_cm
                obj['weight'] = i.weight_kg
                bmi_value = ((obj['weight'])/(obj['height']/100)**2)
                if round(bmi_value,2) <= 18.4:
                    obj['category'] = "Underweight"
                    obj['risk'] = "Malnutrition risk"
                elif 18.5 <= round(bmi_value,2) <= 24.9:
                    obj['category'] = "Normal weight"
                    obj['risk'] = "Low risk"
                elif 25 <= round(bmi_value,2) <= 29.9:
                    obj['category'] = "Overweight"
                    obj['risk'] = "Enhanced risk"
                elif 30 <= round(bmi_value,2) <= 34.9:
                    obj['category'] = "Moderately obese"
                    obj['risk'] = "Medium risk"
                elif 35 <= round(bmi_value,2) <= 39.9:
                    obj['category'] = "Severely obese"
                    obj['risk'] = "High risk"
                elif round(bmi_value,2) >= 40:
                    obj['category'] = "Very severely obese"
                    obj['risk'] = "Very high risk"
                else:
                    obj['category'] = "Not available bmi category for this"
                    obj['risk'] = "Not available risk for this"

                data.append(obj)
            return render_template("home_data.html",data=data)
        else:
            return render_template("home_data.html",data=data)