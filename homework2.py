#write a  python program too find the age of yourself with the help of functions
def calculateAge():
    birthYear:int = 2007
    currentYear:int = 2024
    currentAge:int = currentYear - birthYear
    print(currentAge)
calculateAge()

#calculate the area of rectangle
def calculateAreaRectangle():
    lenght:int = 5
    width:int= 10
    area:int = lenght * width
    print(area)
calculateAreaRectangle()

#calculate the area of a cube
def calculateAreaCube():
    lenghtSide:int = 10
    formula:int = 6 * (lenghtSide)**2
    print(formula)
calculateAreaCube()

#calculate the area of a circle 
def calculateAreaCircle():
    radiusCircle:int = 5
    pie:int = 3.1416
    area:int = pie * (radiusCircle) ** 2
    print(area)
calculateAreaCircle()

#calculate the percentage of a student
def calculatePercentage():
    totalMarks:int = 570
    obtainedMarks:int = 517
    percentage:int = (obtainedMarks / totalMarks) * 100
    print("Your percentage is",percentage,"%")
calculatePercentage()

#convert temp from celsius to farenhiet and vice versa
def tempInCelsius():
    tempFarenhit:int = 45
    tempCelsius:int = (tempFarenhit * 5/9) - 32
    print(tempCelsius)
def tempInFarenhit():
    tempInCelsius:int = 45
    tempInFarenhit:int = (tempInCelsius * 9/5) + 32
    print(tempInFarenhit)
tempInCelsius()
tempInFarenhit()

#convert seconds into minutes and vice versa
def inMinutes():
    a:int = 120
    inMinutes:int = a / 60
    print(inMinutes)
def inSeconds():
    a:int = 120
    inSeconds:int = a * 60
    print(inSeconds)
inMinutes()
inSeconds()

#calculate the volume of a cylinder with the help of a python program
def calculateVolume():
    heightCylinder:int = 5.5
    radiusCylinder:int = 3.5
    pie:int = 3.1416
    volume:int = pie * (radiusCylinder)**2 * heightCylinder
    print(volume)
calculateVolume()

#write a python program to find the BMI of a person
def calculateBMI():
    weight:int = 80
    height:int = 1.5
    secondHeight:int = height * height
    bmiPerson:int = weight / secondHeight
    print(bmiPerson) 
calculateBMI()
