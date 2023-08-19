def index() :

    weight = int(input("please send me your weight(kg) forexample=72 :"))
    height = float(input("please send me your height(m) forexample=1.77 :"))

    bmi = weight / (height * height)   
    print(f"your BMI is:{bmi}")
    if bmi<18 : 
     print (f"Severe underweight")

    elif 17 < bmi < 25:
     print (f"normal")

    elif bmi>24 :        
     print (f"Overweight")

    else :
     pass
index()