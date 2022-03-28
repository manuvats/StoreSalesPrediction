import pickle
from featureTransform import featureTransform


def predictSales(iweight, ivisibility, imrp, outlet_yrs, lowfat, nonedible, regular, tier1, tier2, tier3, high,
                 medium, small, grocery, supermarket1, supermarket2, supermarket3, drinks, food, noncons, modelfile):
    try:
        loaded_model = pickle.load(open(modelfile, 'rb'))  # loading the model file from the storage

        #feat = featureTransform(iid, ifat, oestd_yr, osize, oloc, otype)
        # predictions using the loaded model file
        prediction = loaded_model.predict(
            [[iweight, ivisibility, imrp, outlet_yrs, lowfat, nonedible, regular, tier1, tier2, tier3, high, medium,
              small, grocery, supermarket1, supermarket2, supermarket3, drinks, food, noncons, modelfile]]
        )
        print('The predicted sales of this item is ', prediction)
    except Exception as e:
        raise Exception(f"(predict): Something went wrong in predicting sales\n" + str(e))

'''def predictSales(iid, iweight, ifat, ivisibility, imrp, oestd_yr, oloc, otype, osize, modelfile):
    try:
        loaded_model = pickle.load(open(modelfile, 'rb'))  # loading the model file from the storage

        feat = featureTransform(iid, ifat, oestd_yr, osize, oloc, otype)
        # predictions using the loaded model file
        prediction = loaded_model.predict(
            [[iweight, ivisibility, imrp, feat.outletYrs(), feat.fatContent()['lowfat'],
              feat.fatContent()['nonedible'], feat.fatContent()['regular'], feat.outletLocation()['tier1'],
              feat.outletLocation()['tier2'], feat.outletLocation()['tier3'], feat.outletSize()['high'],
              feat.outletSize()['medium'], feat.outletSize()['small'], feat.outletType()['grocery'],
              feat.outletType()['supermarket1'], feat.outletType()['supermarket2'], feat.outletType()['supermarket3'],
              feat.itemType()['drinks'], feat.itemType()['food'], feat.itemType()['nonconsum']]]
        )
        print('The predicted sales of this item is ', prediction)
    except Exception as e:
        raise Exception(f"(predict): Something went wrong in predicting sales\n" + str(e))'''