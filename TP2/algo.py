import sklearn
import joblib
import pandas as pd

from stop_words import get_stop_words

from sklearn.pipeline import make_pipeline
from sklearn.multiclass import OneVsRestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

datalabel = pd.read_csv(r"./labels.csv")
df_dataLabel = datalabel.copy()

df_dataLabel = df_dataLabel.drop(['Unnamed: 0'], axis= 1)
df_dataLabel = df_dataLabel.dropna()

clf = make_pipeline(
    TfidfVectorizer(stop_words=get_stop_words('en')),
    OneVsRestClassifier(SVC(kernel='linear', probability=True))
)

clf = clf.fit(X=df_dataLabel['tweet'], y=df_dataLabel['class'])

joblib.dump(clf, 'model.pkl')