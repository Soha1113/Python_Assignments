def medical_diagnosis ():
    print("welcome to the diagnostic system")
    fever = input("do you have a cough (yes/no)").lower()
    cough = input("do you have cough (yes/no)").lower()
    fatigue =input("do you have a cough (yes/no)").lower()
    if fever == "yes" and cough == "yes":
        print ("possible flu or covid-19")
    elif fatigue==  "yes":
        print ("possible stress")
    else:
        print("you are perfectly fine")
        medical_diagnosis()