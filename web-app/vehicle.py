from pydantic import BaseModel

class mileage(BaseModel):
	horsepower: float
	acceleration :  float
	year : int	
	origin : int	
	cylinders : int


