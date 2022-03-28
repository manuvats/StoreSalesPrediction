# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS, cross_origin
#from featureTransform import featureTransform
from predict import predictSales
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            item_id=str(request.form['item_id'])
            item_weight = float(request.form['item_weight'])
            item_fat_content = str(request.form['item_fat_content'])
            item_visibility = float(request.form['item_visibility'])
            item_mrp = float(request.form['item_mrp'])
            outlet_estd_yr = float(request.form['outlet_estd_yr'])
            outlet_size = str(request.form['outlet_size'])
            outlet_loc = str(request.form['outlet_loc'])
            outlet_type = str(request.form['outlet_type'])

            filename = 'model.pkl'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage

            #transforming input vars
            #feat = featureTransform(item_id, item_fat_content, outlet_estd_yr, outlet_size, outlet_loc, outlet_type)

            # predictions using the loaded model file
            prediction = predictSales(item_id, item_weight, item_fat_content, item_visibility, item_mrp,
                                       outlet_estd_yr, outlet_loc, outlet_type, outlet_size, filename)
            #prediction = predictSales(
            #    [[item_weight, item_visibility, item_mrp, feat.outletYrs(), feat.fatContent()['lowfat'],
            #      feat.fatContent()['nonedible'], feat.fatContent()['regular'], feat.outletLocation()['tier1'],
            #      feat.outletLocation()['tier2'], feat.outletLocation()['tier3'], feat.outletSize()['high'],
            #      feat.outletSize()['medium'], feat.outletSize()['small'], feat.outletType()['grocery'],
            #      feat.outletType()['supermarket1'], feat.outletType()['supermarket2'], feat.outletType()['supermarket3'],
            #      feat.itemType()['drinks'], feat.itemType()['food'], feat.itemType()['noncons'], filename]])

            # showing the prediction results in a UI
            return render_template('results.html',prediction=prediction)

        except Exception as e:
            raise Exception(f"(predict): Something went wrong in predicting sales\n" + str(e))
            #return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app
