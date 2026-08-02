# 讓使用者分別輸入身高(cm)及體重(kg)後，進一步計算出其身體質量指數(BMI值)，並根據下表輸出該BMI值及其分級。例如輸入身高為160公分、體重50公斤，則輸出：BMI值為19.53(顯示至小數第二位)，屬正常範圍。
# BMI公式是以體重（公斤）除以身高（公尺）的平方。

h=int(input("請輸入身高(cm):"))
w=int(input("請輸入體重(kg):"))
BMI=w/(h/100)**2
print("身體質量指數BMI值為",BMI,end=" ")

if BMI<18.5:
    print("體重過輕")
elif BMI>=18.6 and BMI<24:
    print("體重正常")
elif BMI>=24 and BMI<27:
    print("體重過重")
elif BMI>=27 and BMI<30:
    print("輕度肥胖")
elif BMI>=30 and BMI<35:
    print("中度肥胖")
elif BMI>=35:
    print("重度肥胖")                    