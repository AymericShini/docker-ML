import seaborn
import sklearn
import joblib 
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.model_selection import train_test_split


def accuracy(preds, Y):
    return (preds == Y).sum() / len(Y)

iris = seaborn.load_dataset('iris')
df_iris = iris.copy()


Y = df_iris['species'].astype('category').cat.codes
X = df_iris.drop('species', axis='columns')

X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=0.3, stratify=Y,random_state=2)

rf = RF(n_estimators=35, max_depth=5)
rf.fit(X_train, y_train)

Y_pred = rf.predict(X_test)
print("My accuracy : ", accuracy(Y_pred, y_test)*100, "%")

joblib.dump(rf, 'modelIris.pkl')

