import os
import  cv2

import firebase_admin
from firebase_admin import credentials
from firebase_admin import  db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://face-verification-f48a9-default-rtdb.firebaseio.com/',
    'storageBucket':'face-verification-f48a9.appspot.com'
})

folderPath='Facial Recognition with liveness detection/application_data/verification_image'
pathList=os.listdir(folderPath)
# print(pathList)
imgList=[]
IdsList=[]

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    IdsList.append(path.split('.')[0])
print(IdsList)
