import firebase_admin
from firebase_admin import credentials
from firebase_admin import  db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://face-verification-f48a9-default-rtdb.firebaseio.com/'
})

ref=db.reference('Students')

data={
    "22124002":
            {
                "name":"Adit Khare",
                "course":"BSBE",
                "batch":"2026",
                "email":"adit_k@bt.iitr.ac.in"
            },
    "22124004":
        {
            "name": "Aiman Khan",
            "course": "BSBE",
            "batch": "2026",
            "email": "aiman_k@bt.iitr.ac.in"
        },
    "22124006":
        {
            "name": "Aman Yadav",
            "course": "BSBE",
            "batch": "2026",
            "email": "aman_y@bt.iitr.ac.in"
        },
    "22124007":
        {
            "name": "Amit Kothari",
            "course": "BSBE",
            "batch": "2026",
            "email": "amit_k@bt.iitr.ac.in"
        }
}

for key,value in data.items():
    ref.child(key).set(value)
