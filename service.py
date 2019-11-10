#!/usr/bin/python

import json
import time

import falcon
from catboost import CatBoostClassifier
from catboost.datasets import titanic

PORT_NUMBER = 8080
start = time.time()

# load the model
clf = CatBoostClassifier()
clf.load_model('model')

# get test data
train, test = titanic()

# remove nans
train, test = train.fillna(-999), test.fillna(-999)
X = test.drop('PassengerId', axis=1)
X_count = X.shape[0]

end = time.time()
print("Loading time: {0:f} secs)".format(end - start))

# API Handler for Iris images
class Titanic(object):

    def on_get(self, req, resp, index):
        if index < X_count:
            y_pred = clf.predict(X)
            payload = {'index': index, 'predicted': y_pred[0]}
            resp.body = json.dumps(payload)
            resp.status = falcon.HTTP_200
        else:
            raise falcon.HTTPBadRequest(
                "Index Out of Range. ",
                "The requested index must be between 0 and {:d}, inclusive.".format(X_count - 1)
            )

# API Handler for API example message
class Intro(object):

    def on_get(self, req, resp):
        resp.body = '{"message": \
                    "This service verifies a model using the Titanic Test data set. Invoke using the form /Titanic/<index of ' \
                    'test sample>. For example, /titanic/24"}'
        resp.status = falcon.HTTP_200
