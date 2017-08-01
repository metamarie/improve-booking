import psycopg
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
import os

# connect to redshift
user = os.environ['REDSHIFT_USERNAME']
password = os.environ['REDSHIFT_PASSWORD']
rs_host = os.environ['DEV_REDSHIFT_URL']

conn = psycopg2.connect(dbname = 'dev_redshift', user = user, password = password, host = rs_host)

cur = conn.cursor()

## query a random 100k searches from the logs
cur.execute(
    """ SELECT * FROM search_logs
            WHERE length(raw_text) > 0
            AND raw_text NOT LIKE 'test%'
            AND s_timestamp::date >= timestamp '2016-07-15 00:00:00'
            AND destination NOT IN ('/404.html', '/help-center.html')
            ORDER BY random()
            LIMIT 100000;
    """
)

## load data from this query
data = cur.fetchall()
df = pd.DataFrame.from_records(data)

## train the baseline model
classif = OneVsRestClassifier(estimator=SVC(random_state=0))
y = preprocessing.MultiLabelBinarizer().fit_transform(df['completed'])
classifier = classif.fit(df, df['completed'])
