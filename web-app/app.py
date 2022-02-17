import uvicorn
from fastapi import FastAPI
from vehicle import mileage
import pickle
import numpy as np

app=FastAPI()
@app.get("/")
def read_main():
    return {"message": "Hello World from main app"}


@app.post("/predict")
def predict(data:mileage):
	data=data.dict()
	horsepower = data["horsepower"]
	acceleration = data["acceleration"]
	year = data["year"]
	origin =data["origin"]
	if origin==1:
		origin_2=0
		origin_3=0
	elif origin==2:
		origin_2=1
		origin_3=0
	elif origin==3:
		origin_2=0
		origin_3=1
	else:
		pass
	cylinders = data["cylinders"]
	if cylinders==3:
		cylinders_4=0
		cylinders_5=0
		cylinders_6	=0
		cylinders_8=0
	elif cylinders==4:
		cylinders_4=1
		cylinders_5=0
		cylinders_6	=0
		cylinders_8=0
	elif cylinders==5:
		cylinders_4=0
		cylinders_5=1
		cylinders_6	=0
		cylinders_8=0
	elif cylinders==6:
		cylinders_4=0
		cylinders_5=0
		cylinders_6	=1
		cylinders_8=0
	elif cylinders==8:
		cylinders_4=0
		cylinders_5=1
		cylinders_6	=0
		cylinders_8=1
	else:
		pass

	print(horsepower,acceleration,year,origin_2,origin_3,cylinders_4,cylinders_5,cylinders_6,cylinders_8)
	model = pickle.load(open("model.pkl", "rb"))
	pred=model.predict([[horsepower,acceleration,year,origin_2,origin_3,cylinders_4,cylinders_5,cylinders_6,cylinders_8]])
	print(pred)
	result=np.exp(pred[0])

	return {
		'the mileage of the vehicle would be' : result
	}

if __name__=='Main':
	uvicorn.run()