import serial
import numpy as np
import pandas as pd

data = pd.read_csv("status.csv")
print(data.head(5))

from sklearn import preprocessing
ley = preprocessing.LabelEncoder()
X = data.drop(columns=['zona'])
y = data['zona'].values
y = ley.fit_transform(y)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

from sklearn.svm import SVC

clf = SVC(gamma=0.01, C=10)
clf.fit(X,y)

arduino = serial.Serial("/dev/ttyUSB0", timeout=1, baudrate=9600)

while True:
	a = arduino.readline().decode("utf-8").strip('\n').strip('\r').encode('ascii','ignore')
	if(a!=''):
		temp = a.split(';')
		print(temp)
		jarak = int(temp[0])
		micro = int(temp[1])
		milli = int(temp[2])

		new = np.array([[jarak, micro, milli]])
		print(new)
		new = scaler.transform(new)
		res = clf.predict(new)
		print(ley.inverse_transform(res))

		checkA = False
		checkB = False
		checkC = False

		if (jarak < 26):
			checkA = True
		if (micro < 1476):
			checkB = True
		if (milli < 2):
			checkC = True

		if(checkA and checkB and checkC):
			arduino.write('a')
