masa=int(input ("Podaj swoją masę ciała:\n"))
while (masa<0):
    masa=int(input ("Podaj swoją masę ciała:\n"))

wzrost=float(input ("Podaj swój wzrost w metrach:\n"))
while(wzrost<0):
    wzrost=float(input ("Podaj swój wzrost w metrach:\n")) #wzrost podajemy w metrach np.1.75

BMI=float (masa/(wzrost**2))

if (BMI<18.5):
    print("Niedowaga")
elif (BMI>=18.5) and (BMI<25):
    print("Norma")
elif ( BMI>=25) and (BMI<30):
    print("Nadwaga")
elif (BMI>=30) and (BMI<35):
    print("I stopień otyłości")
elif (BMI>=35) and (BMI<40):
    print("II stopień otyłości")
else:
    print("III stopień otyłości")
print("\nTwoje BMI wynosi: ", BMI)
