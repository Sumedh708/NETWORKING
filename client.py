import random, time as t, socket
from colorama import Fore
from threading import *
#establish connection
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='localhost'
port=1255
bold = '\033[1m'
boldstop = '\033[0m'
bl = bold + Fore.BLUE
g = bold + Fore.GREEN
c = bold + Fore.CYAN
y = bold + Fore.YELLOW
b = bold + Fore.BLACK
r = bold + Fore.RED
res = boldstop + Fore.RESET
try:
    s.connect((host,port))
    ipaddr=socket.gethostbyname(socket.gethostname())
    s.send(bytes(ipaddr,'utf-8'))
except ConnectionRefusedError:
    print(f'{r}Sorry couldnt connect to server!\n')
#Defining
def loading():
    print("Loading",end='')
    while boo:
        print('.',end='')
        t.sleep(1)
def pb():
    print('╟─────────────────────────────────────────────────')
def rtime(n):
    t.sleep(random.random()/n)
quotes = [ 'You don’t have to be extreme, just consistent.' , 'Fitness is not just about the body. It’s also about the mind and the spirit.' ,
           'Do something today that your future self will thank you for.', 'Your health is an investment, not an expense.' , 'The greatest wealth is health.'
             , 'The groundwork for all happiness is good health.' , 'A healthy outside starts from the inside.' , "Don't wish for a good body, work for it."
             , "It's not about being the best. It's about being better than you were yesterday." , "Invest in your health today to enjoy the benefits tomorrow."
             , "Make time for wellness now or make time for illness later." ]

summary = []
editedSummary = 0
summaryEnd = 0
#Asking user details
name='';age=0;gen='';heightCm=0;weight=0
load=Thread(target=loading);boo=True
def new():
    global name,age,gen,heightCm,weight,boo
    print(f"\n╔════════════════▌{g}WELCOME TO FITNESS MANAGER{res}▐════════════════\n║")
    print(f'║{bl} "{random.choice(quotes)}"{res} ')
    print(f"║\n║{g} Enter your details please:{res} ")
    name = input(f"║\n║{c} Enter your name:{res} ")
    age = int(input(f"║\n║{c} Enter your age:{res} "))
    gen = input(f"║\n║{c} Enter gender (M/F/O):{res} ").lower()
    heightCm = float(input(f"║\n║{c} Enter height(in cm):{res} "))
    weight = float(input(f"║\n║{c} Enter weight(in kg):{res} "))
    pb()
    load.start()
    s.send(bytes(name,'utf-8'))
    t.sleep(1)
    s.send(bytes(str(age),'utf-8'))
    t.sleep(1)
    s.send(bytes(gen,'utf-8'))
    t.sleep(1)
    s.send(bytes(str(int(heightCm)),'utf-8'))
    t.sleep(1)
    s.send(bytes(str(int(weight)),'utf-8'))
    t.sleep(1)
    boo=False
    print(f"║\n║{b} values sent to server{res} ")
    boo=True
    continu("new")
#Conversions
def take_data():
    ip=s.recv(1024).decode()
    name=s.recv(1024).decode()
    age=s.recv(1024).decode()
    age=int(age)
    gen=s.recv(1024).decode()
    heightCm=s.recv(1024).decode()
    heightCm=int(heightCm)
    weight=s.recv(1024).decode()
    weight=int(weight)
    return ip,name,age,gen,heightCm,weight
def continu(l):
    global summary,summaryEnd
    global name,age,gen,heightCm,weight,boo
    if l=="old":
        load.start()
        ip,name,age,gen,heightCm,weight=take_data()
        boo=False
    while True:
        #Looped conversions :
        boo=True
        if gen.lower() == 'm':
            gender = "Male"
            fatOfSex = 1
        elif gen.lower() == 'f':
            gender = "Female"
            fatOfSex = 0
        elif gen.lower() == 'o':
            gender = "Other"
            fatOfSex = 1
        heightM = heightCm/100
        bmi = weight / (heightM ** 2)
        bmi = round (bmi,2)
        fatPercent = (1.2 * (weight / (heightM ** 2))) + (0.23 * age) - (10.8 * fatOfSex) - 5.4
        fatPercent = round (fatPercent,2)
        fatMass = (weight/100) * fatPercent
        fatMass = round (fatMass,2)
        fatFreeMass = (weight - fatMass)
        if gen == 'm' or gen == 'o':
            bmr = 88.36 + (13.39 * weight) + (4.79 * heightCm) - (5.67 * age)
        elif gen == 'f':
            bmr = 447.59 + (9.24 * weight) + (3.09 * heightCm) - (4.33 * age)

        #Menu
        rtime(4)
        print(f"║\n║{g} What do you want to do today :{res}\n║{g} (type the option number){res} ")
        rtime(4)
        print(f"║\n║{y} 1.Calculate Bmi.{res} ")
        rtime(4)
        print(f"║ {y}2.Calculate Body fat percentage.{res} ")
        rtime(4)
        print(f"║ {y}3.Calculate calorie intake.{res} ")
        rtime(4)
        print(f"║ {y}4.Calculate BMR.{res} ")
        rtime(4)
        print(f"║ {y}5.Sleep health.{res} ")
        rtime(4)
        print(f"║ {y}6.Edit Details.{res} ")
        rtime(4)
        print(f"║ {y}7.Show Details.{res} ")
        rtime(4)
        print(f"║ {y}8.New entry.{res} ")
        rtime(4)
        print(f"║ {y}9.Stop{res} ")
        pb()
        menuInput = input(f"║ {c}Enter here:{res} ")
        pb()

        #Bmi
        if menuInput == '1':
            summary.append("bmi")
            print(f"║\n║{g} Your details:{res} ")
            print(f"║{y}Your BMI is: {res}{bmi}")
            if bmi < 18.5:
                bmiStatus = "Underweight"
                print(f"║{y} You're a bit underweight. Make sure to check summary for help.{res} ")
            elif 18.5 <= bmi < 24.9:
                bmiStatus = "Normal"
                print(f"║{y} Your BMI is normal.{res} ")
            elif 25 <= bmi < 29.9:
                bmiStatus = "Overweight"
                print(f"║{y} You're a bit overweight. Make sure to check summary for help.{res} ")
            else:
                print(f"║{y} You're Obese. Make sure to check summary for help.{res} ")
            pb()
        #Body fat
        elif menuInput == '2':
            summary.append("body fat")
            print(f"║\n║{g} Your fat percentage is :{res} {fatPercent}% (Approx)")
            print(f"║{y} Fat in your body :{res} {fatMass}kg (Approx)")
            print(f"║{y} Body weight without fat :{res} {fatFreeMass}kg (Approx)")
            pb()
        #Calorie calculator
        elif menuInput == '3':
            summary.append("calorie")
            calDict = {'apple':52,'apple juice':113,'banana':89,'banana shake ':260,
                   'orange':47,'orange juice':112,'muskmelon':186,'muskmelon juice':44,                                                                                                                                 'watermelon':86,'watermelon juice':90,'sandwich':500,'salad':98,
                   'carrot juice':39,'beetroot juice':52,'pomegranate juice':136,'papaya':275,'papaya juice':142,'milk':103,'chocolate milk':209,
                   'ice cream':253,'coke':150,'green tea':2,'coffee':1,'egg':78,'omlette':94,'fried rice':228,'burger':354,'fries':345,'pizza':285
                   ,'idli' : 58,'dosa' : 168,'pongal' : 320,'vada' : 135
                   }
                  # 'roti':,'chapati':,'egg':,'chicken':,'lays':,'samosa':,}
            print(f"║\n║{g} What did you eat today?{res}\n║{g} (Type stop to stop){res} ")
            tempCal = []
            calSum = 0
            while True:
                food = input(f"║\n║{c} Item :{res} ").lower()
                if food != 'stop':
                    if food in calDict:
                        quantity = int(input (f"║{c} Quantity :{res} "))
                        tempCal += quantity * [food]
                        rtime(2)
                        print(f"║{b} Item accepted.{res} ")
                    else:
                        print(f"║{r}Item currently not in database.{res} ")
                else:
                    break
            for i in tempCal:
                calSum += calDict[i]
            print(f"║\n║{y} Your total is:{res} {calSum}cal(Approx)")
            print("║\n║{y} Check if it is enough for you in the summary.{res} ")
            pb()
        #Calculating BMR
        elif menuInput == '4':
            summary.append("bmr")
            print(f"║\n║{g} Okay lets calculate BMR :{res} \n║{g}(amount of energy(in cal) your body requires to function well){res} ")
            print(f"\n║{g} Activeness list :{res} \n║{g} (type the option number){res} ")
            print(f"║\n║{y} 1.Sedentary (You have little to no exercise){res} ")
            print(f"║{y}2.Lightly active (You have 1-3 days of exercise a week){res} ")
            print(f"║{y}3.Moderately active (You have 3-5 days of exercise a week){res} ")
            print(f"║{y}4.Very active (You exercise everyday.){res} ")
            print(f"║{y}5.Extra active (Heavy exercise or physical job everyday.)")
            activeness = input (f"║\n║{c} How active are you on the basis of this list?:{res} ")
            if activeness == '1':
                act = 1.2
            elif activeness == '2':
                act = 1.375
            elif activeness == '3':
                act = 1.55
            elif activeness == '4':
                act = 1.725
            elif activeness == '5':
                act = 1.9
            else:
                print(f"║{r} Enter the right value.{res} ")
            bmr = round (bmr,2)
            print(f"║\n║{y} Your Bmr (required calories per day) is :{res} {round(bmr * act,2)}cal")
            pb()
        #Sleep health
        elif menuInput == '5':
            summary.append("sleep")
            print(f"║\n║{g} Okay lets check upon your sleep!{res} ")
            sleep = float(input(f"║\n║{c} How many hours of sleep do you get per day?:{res} "))
            if age <= 2 :
                if sleep < 11:
                    print(f"║{r} You need to get more sleep.{res} ")
                    sleepStatus = 1
                elif sleep > 14:
                    print(f"║{y} You're getting more sleep than required.{res} ")
                    sleepStatus = 2
                else:
                    print(f"║{g} You're getting enough sleep{res} ")
                    sleepStatus = 3
            elif age <= 5:
                if sleep < 9:
                    print(f"║{r} You need to get more sleep.{res} ")
                    sleepStatus = 1
                elif sleep > 12:
                    print(f"║{y} You're getting more sleep than required.{res} ")
                    sleepStatus = 2
                else:
                    print(f"║{g} You're getting enough sleep{res} ")
                    sleepStatus = 3
            elif age <= 13:
                if sleep < 8:
                    print(f"║{r} You need to get more sleep.{res} ")
                    sleepStatus = 1
                elif sleep > 10:
                    print(f"║{y} You're getting more sleep than required.{res} ")
                    sleepStatus = 2
                else:
                    print(f"║{g} You're getting enough sleep{res} ")
                    sleepStatus = 3
            elif age <= 17:
                if sleep < 6:
                    print(f"║{r} You need to get more sleep.{res} ")
                    sleepStatus = 1
                elif sleep > 9:
                    print(f"║{y} You're getting more sleep than required.{res} ")
                    sleepStatus = 2
                else:
                    print(f"║{g} You're getting enough sleep{res} ")
                    sleepStatus = 3
            elif age <= 100:
                if sleep < 7:
                    print(f"║{r} You need to get more sleep.{res} ")
                    sleepStatus = 1
                elif sleep > 8:
                    print(f"║{y} You're getting more sleep than required.{res} ")
                    sleepStatus = 2
                else:
                    print(f"║{g} You're getting enough sleep{res} ")
                    sleepStatus = 3
            pb()
        #Editing Details
        elif menuInput == '6':
            editedSummary = 1
            print(f"║\n║{g} What do you want to edit?{res} ")
            print(f"║\n║{y} 1.Name{res} ")
            print(f"║{y} 2.Age{res} ")
            print(f"║{y} 3.Gender{res} ")
            print(f"║{y} 4.Height{res} ")
            print(f"║{y} 5.Weight{res} ")
            pb()
            editChoice = int(input(f"║\n║{c} Enter here:{res} "))
            pb()
            if editChoice == 1:
                newName = input(f"║{c} Enter name:{res} ")
                name = newName
            elif editChoice == 2:
                newAge = int(input(f"║{c} Enter age:{res}"))
                age = newAge
            elif editChoice == 3:
                newGen = input(f"║{c} Enter gender (m/f/o):{res} ")
                gen = newGen
            elif editChoice == 4:
                newHeightCm = int(input(f"║{c} Enter height:{res} "))
                heightCm = newHeightCm
            elif editChoice == 5:
                newWeight = int(input(f"║{c} Enter weight:{res} "))
                weight = newWeight
            pb()
            print(f"║\n║{b} Details updated.{res} ")
            pb()
        #Displaying details
        elif menuInput == '7':
            print(f"║{g} Displaying details{res} ")
            t.sleep(1.0)
            print(f"║{b}Please wait ",end='')
            for i in range(3):
                print(".",end='')
                t.sleep(0.45)
            print(res+' ')
            pb()
            print(f"║\n║{g} Your details are:{res} ")
            print(f"║\n║{y} Name :{res} {name}")
            print(f"║{y} Age :{res} {age}")
            print(f"║{y} Gender :{res} {gender}")
            print(f"║{y} Height :{res} {heightCm}cm - {heightM}m")
            print(f"║{y} Weight :{res} {weight}kg")
            print(f"║\n║{g} Summary :{res} ")
            if 'bmi' in summary:
                print(f"║\n║{y}Your bmi is :{res} {bmi}")
                if bmi < 18.5:
                    print(f"║{r} You're a bit underweight. Here are some things you can do to gain weight:{res} ")
                    print(f"║{y} -Eat smaller, frequent meals throughout the day{res} \n║{y} rather than relying on three large meals.{res} ")
                    print(f"║{y} -Include calorie-dense snacks in your diet, such as{res} \n║{y} nuts, seeds, dried fruits, and peanut butters.{res} ")
                    print(f"║{y} -Maintain a calorie surplus and Increase your protein intake.{res} ")
                    print(f"║{y} -Incorporate strength training exercises into your fitness routine.{res} \n║{y} Helps build muscle mass, contributing to overall weight gain.{res} ")
                elif 18.5 <= bmi < 24.9:
                    print(f"║{y} Your BMI is normal.{res} \n║{y} Stick to your diet and stay healthy and do what you're doing{res} \n║{y} and never forget your good habits!.{res} ")
                elif 25 <= bmi < 29.9:
                    print(f"║{r} You're a bit overweight.{res} \n║{y} Here are some things you can do to lose weight:{res} ")
                    print(f"║{y} -Maintain a coloric deficit by consuming fewer colories{res} \n║ {y}than your body needs while having a balanced diet.{res} ")
                    print(f"║{y} -Exercise regularly and try incorporating more cardiovascular exercises{res} \n║{y} that can help you burn calories.{res} ")
                    print(f"║{y} -Drink plenty of water throughout the day.{res} ")
                    print(f"║{y} -Pay attention to what and how much you. Avoid junk food.{res} ")
                    print(f"║{y} -Ensure you get enough quality sleep each night.{res} ")
                else:
                    print(f"║{r} You're Obese.But do not worry.Here are some things you should do: {res} ")
                    print(f"║{y} -Consult healthcare professionals, including a doctor, dietitian, or nutritionist.{res} \n║{y} They can assess your overall health, identify potential underlying causes of obesity{res} \n║{y} and help create a personalized plan.{res} ")
                    print(f"║{y} -Focus on a balanced and nutritious diet with a variety of{res} \n║{y} fruits, vegetables, whole grains, lean proteins, and healthy fats.{res} \n║{y} Control portion sizes to avoid overeating.{res} ")
                    print(f"║{y} -Incorporate regular physical activity into your routine,{res} \n║{y} aiming for at least 150 minutes of moderate-intensity aerobic exercise per week.{res} ")
                    print(f"║{y} -Get adequate sleep, as lack of sleep can impact hormones that{res} \n║{y} regulate hunger and stress.Reduce sedentary behavior by{res} \n║{y} incorporating more movement into your daily life.{res} ")
                    print(f"║{y} Overall do not worry as this can be cured with the help of medications and healthcare professionals.{res} \n║{y} Seek support from healthcare professionals, and consider working with{res} \n║{y} a registered dietitian or weight management specialist for personalized guidance.{res} ")
            if 'body fat' in summary:
                print(f"║\n║{y} Your fat percentage is :{res} {fatPercent}% (Approx)")
                print(f"║{y} Fat in your body :{res} {fatMass}kg (Approx)")
                print(f"║{y} Body weight without fat :{res} {fatFreeMass}kg (Approx)")
            if 'bmr' in summary:
                print(f"║\n║{y} Your calorie requirement per day according to your lifestyle is:{res} {round(bmr * act,2)}")
            if 'calorie' in summary:
                print(f"║\n║{y} Your calorie intake today accoring to your input was :{res} {calSum}")
                if calSum < bmr:
                    print(f"║{y} According to your bmr you are recommended intake some more calories.{res} \n║{y} Here are some calorie efficient food you can intergrate into your diet:{res} ")
                    print(f"║{y} -Bananas{res} \n║{y} -Milk{res} \n║{y} -Yogurt{res} \n║{y} -Cheese{res} \n║{y} -Oats{res} \n║{y} -Dried fruits{res} \n║{y} -Nuts and Nut butters{res} \n║{y} -Avacados{res} ")
                if calSum > bmr:
                    print(f"║\n║{y} According to your Bmr you are in a calorie surplus.{res} ")
                    if bmiStatus == "Underweight":
                        print(f"║{r} This is good for you as your Bmi results show you are underweight and need to gain weight.{res} \n║{y} Calorie surplus can help you gain weight, Keep Up!!.{res} ")
                    if bmiStatus == "Overweight":
                        print(f"║{r} According to your Bmi results you are overweight and need to lose weight to stay healthy.{res} \n║A{y} calorie surplus will result in you gaining more weight.{res} \n║{y} Controlling your calorie intake is recommended.{res} ")
                    if bmiStatus == "Normal":
                        print(f"║{y} As have an adequate Bmi result, good amount of exercises and working out{res} \n║{y} combined with the calorie surplus will lead to good muscle growth but,{res} \n║{y} if left unmonitored without exercise it will lead to weight gain.{res} ")
            if 'sleep' in summary:
                if sleepStatus == 1:
                    print(f"║\n║{r} You have to sleep more. Here are some tips:{res} ")
                    print(f"║{y} -Establish a Consistent Sleep Schedule.{res} ")
                    print(f"║{y} -Limit Exposure to Screens Before Bed.{res} ")
                    print(f"║{y} -Get Regular Exercise.{res} ")
                    print(f"║{y} -Manage Stress.{res} ")
                    print(f"║{y} -Limit Fluid Intake Before Bed{res} ")
                    print(f"║{y} -Seek Professional Help if you feel like you have a sleeping disorder.{res} ")
                if sleepStatus == 2:
                    print(f"║\n║{r} You have to sleep less. Sleeping more isnt good bcs:{res} ")
                    print(f"║{y} -Oversleeping can disrupt your body's natural circadian rhythms,{res} \n║{y} leading to difficulty falling asleep at night and waking up in the morning.{res} ")
                    print(f"║{y} -Chronic oversleeping can be a symptom of certain sleep disorders,{res} \n║{y} such as hypersomnia or sleep apnea.{res} ")
                    print(f"║{y} -Prolonged periods of inactivity during excessive sleep{res} \n║{y} can contribute to joint and back pain.{res} ")
                    print(f"║{y} -Too much sleep may lead to a feeling of grogginess or 'sleep inertia'.{res} ")
                if sleepStatus == 3:
                    print(f"║\n║{g} You have a perfect sleep status. Keep up the routines and stay healthy.{res} ")
            if summary == []:
                    print(f"║\n║{b} No previous records.{res} ")
            pb()
            print(f"║\n║{g} What do you want to do next?{res} ")
            print(f"║{y} 1.Back to menu{res} ")
            print(f"║{y} 2.New entry{res} ")
            print(f"║{y} 3.Exit{res} ")
            pb()
            summaryEnd = int(input(f"║{c} Enter here:{res} "))
            pb()
            if summaryEnd == 1:
                print(f"║\n║{b} Returning to menu.{res} ")
                t.sleep(2.0)
                pb()
        #New entry
        elif menuInput == '8' or summaryEnd == 2:
            print(f"║{g} Enter the new entry{res} ")
            newName = input(f"║\n║{c} Name:{res} ")
            newAge = int(input(f"║{c} Age:{res} "))
            newGen = input(f"║{c} Gender(m/f/o) :{res} ")
            newHeightCm = float(input(f"║{c} Height:{res} "))
            newWeight = float(input(f"║{c} Weight:{res} "))
            name = newName
            age = newAge
            gen = newGen
            hcm = newHeightCm
            weight = newWeight
            summary = []
            print(f"║{y} New entry taken and previous records cleared.{res} ")
            pb()
        #Break
        elif menuInput == '9' or summaryEnd ==3:
            print(f"║\n║{g} Thank you for your support.{res} \n║{g} Please use again!{res} ")
            print("╚═════════════════════════════════════════════════")
            break
        else:
            print(f"║{r}Invalid choice try again.{res} ")
            q=input(f"║{y}Press enter to continue.{res} ",end=' ')
            pb()
#check weather old or new person
status=s.recv(1024).decode()
print(status)
if status=="continue":
    continu("old")
elif status=="new":
    try:
        new()
    except ConnectionRefusedError:
        print(f'{r}Sorry couldnt connect to server!\n')
