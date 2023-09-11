import os 
os.system ("clear ")

print('Hello World')
user_name = input(" please enter your surname ")
print()
print (" welcome," +user_name)
print("this is simple calculator , the group no.3 project , Description in the code .")
print ("credit by :") 
print ("           ahmed mousa")
print ("           omar ahmed ")
print ("           manar elshiekh ")
print ("           ahmed samy ")
print ("           marwan samy ") 
print ("           mohamed abo zied ")




print(input("press enter to continue"))
print()
import math
print ("please choose the calculator you want : ") 
print("basic calculator (B) , sientific calculator (S) or Constants (C) ?  (CAPITAL)")
# basic معناها اله بسيطة و sientific معناها اله علميه و constants معناها ثوابت
# معلش شغال ع الكمبيوتر فمينفعش اكتب الكود بالعربي
bsc = (input())
print()
# اي قيمه غلط يقفل البرنامج
if bsc == "B" :
    print("choose calculation ( + - x / )")
    cal = (input())
    print()
    if cal == "+" :
        a = (float(input("first number : ")))
        b = (float(input("second number : ")))
        print(a + b)
    if cal == "-" :
        c = (float(input("first number : ")))
        d = (float(input("second number : ")))
        print(c - d)
    if cal == "x" :
        e = (float(input("first number : ")))
        f = (float(input("second number : ")))
        print(e * f)
    if cal == "/" :
        g = (float(input("first number : ")))
        h = (float(input("second number : ")))
        print(g / h)
if bsc == "C" :
    print("pi = 3.14159")
    print("e = 2.71828")
    print("gold value = 1.6")
    print("M = 5.97 x 10^24 KG")
    print("R = 6.38 x 10^6 m")
    print("N(a) = 6.02 x 10^23 Mol")
    print("G = 6.67 x 10^-11")
    print("c = 299792458 m/s")
    print()
if bsc == "S" :
    print("choose calculation (log , log10 , power , sqrt , sin , cos , tan , degrees , radians )")
# الى مش فاهم log و log10 معناهم اللوغاريتم الطبيعي و العشري و power معناها الأس و sqrt معناها الجزر التربيعي و sin , cos , tan معناهم بالترتيب جا و جتا و ظا و degrees تحويل الزاوية من دائري للدرجات و radians العكس
# الدوال المثلثية لازم تتكتب بالراديان و value يعني قيمة
# للنسخ حدد القيمة و اضعط كليك يمين و للصق اضغط كليك يمين تاني و القيم تقربها انت للواحد الصحيح
    sc = (input())
    print()
    if sc == "log" :
        log = (float(input("put a value : ")))
        print(math.log(log))
    if sc == "log10" :
        log10 = (float(input("put a value : ")))
        print(math.log10(log10))
    if sc == "power" :
        power = (float(input("put a value : ")))
        print(power * power)
    if sc == "sqrt" :
        sqrt = (float(input("put a value : ")))
        print(math.sqrt(sqrt))
    if sc == "sin" :
        sin = (float(input("put a value (in radian) : ")))
        print(math.sin(sin))
    if sc == "cos" :
        cos = (float(input("put a value (in radian) : ")))
        print(math.cos(cos))
    if sc == "tan" :
        tan = (float(input("put a value (in radian) : ")))
        print(math.tan(tan))
    if sc == "degrees" :
        degrees = (float(input("put a value (in radian) : ")))
        print(math.degrees(degrees))
    if sc == "radians" :
        radians = (float(input("put a value (in degress) : ")))
        print(math.radians(radians))
        
        
print("press enter to exit or type (C) to continue ")
d = input()
if d == "C" :
    print ("please choose the calculator you want : ") 
    print("basic calculator (B) , sientific calculator (S) or Constants (C) ?  (CAPITAL)")
    # basic معناها اله بسيطة و sientific معناها اله علميه و constants معناها ثوابت
# معلش شغال ع الكمبيوتر فمينفعش اكتب الكود بالعربي    
    bsc = (input())
    print()
# اي قيمه غلط يقفل البرنامج    
    if bsc == "B" :
        print("choose calculation ( + - x / )")
        cal = (input())
        print()
        if cal == "+" :
            a = (float(input("first number : ")))
            b = (float(input("second number : ")))
            print(a + b)
        if cal == "-" :
            c = (float(input("first number : ")))
            d = (float(input("second number : ")))
            print(c - d)
        if cal == "x" :
            e = (float(input("first number : ")))
            f = (float(input("second number : ")))
            print(e * f)
        if cal == "/" :
            g = (float(input("first number : ")))
            h = (float(input("second number : ")))
            print(g / h)
    if bsc == "C" :
        print("pi = 3.14159")
        print("e = 2.71828")
        print("gold value = 1.6")
        print("M = 5.97 x 10^24 KG")
        print("R = 6.38 x 10^6 m")
        print("N(a) = 6.02 x 10^23 Mol")
        print("G = 6.67 x 10^-11")
        print("c = 299792458 m/s")
        print()
    if bsc == "S" :
        print("choose calculation (log , log10 , power , sqrt , sin , cos , tan , degrees , radians )")
# الى مش فاهم log و log10 معناهم اللوغاريتم الطبيعي و العشري و power معناها الأس و sqrt معناها الجزر التربيعي و sin , cos , tan معناهم بالترتيب جا و جتا و ظا و degrees تحويل الزاوية من دائري للدرجات و radians العكس    
# الدوال المثلثية لازم تتكتب بالراديان و value يعني قيمة    
# للنسخ حدد القيمة و اضعط كليك يمين و للصق اضغط كليك يمين تاني و القيم تقربها انت للواحد الصحيح    
        sc = (input())
        print()
        if sc == "log" :
            log = (float(input("put a value : ")))
            print(math.log(log))
        if sc == "log10" :
            log10 = (float(input("put a value : ")))
            print(math.log10(log10))
        if sc == "power" :
            power = (float(input("put a value : ")))
            print(power * power)
        if sc == "sqrt" :
            sqrt = (float(input("put a value : ")))
            print(math.sqrt(sqrt))
        if sc == "sin" :
            sin = (float(input("put a value (in radian) : ")))
            print(math.sin(sin))
        if sc == "cos" :
            cos = (float(input("put a value (in radian) : ")))
            print(math.cos(cos))
        if sc == "tan" :
            tan = (float(input("put a value (in radian) : ")))
            print(math.tan(tan))
        if sc == "degrees" :
            degrees = (float(input("put a value (in radian) : ")))
            print(math.degrees(degrees))
        if sc == "radians" :
            radians = (float(input("put a value (in degress) : ")))
            print(math.radians(radians))




    print("press enter to exit or type (C) to continue ")
    f = input()
    if f == "C" :
        print ("please choose the calculator you want : ") 
        print("basic calculator (B) , sientific calculator (S) or Constants (C) ?  (CAPITAL)")
        # basic معناها اله بسيطة و sientific معناها اله علميه و constants معناها ثوابت
# معلش شغال ع الكمبيوتر فمينفعش اكتب الكود بالعربي        
        bsc = (input())
        print()
# اي قيمه غلط يقفل البرنامج        
        if bsc == "B" :
            print("choose calculation ( + - x / )")
            cal = (input())
            print()
            if cal == "+" :
                a = (float(input("first number : ")))
                b = (float(input("second number : ")))
                print(a + b)
            if cal == "-" :
                c = (float(input("first number : ")))
                d = (float(input("second number : ")))
                print(c - d)
            if cal == "x" :
                e = (float(input("first number : ")))
                f = (float(input("second number : ")))
                print(e * f)
            if cal == "/" :
                g = (float(input("first number : ")))
                h = (float(input("second number : ")))
                print(g / h)
        if bsc == "C" :
            print("pi = 3.14159")
            print("e = 2.71828")
            print("gold value = 1.6")
            print("M = 5.97 x 10^24 KG")
            print("R = 6.38 x 10^6 m")
            print("N(a) = 6.02 x 10^23 Mol")
            print("G = 6.67 x 10^-11")
            print("c = 299792458 m/s")
            print()
        if bsc == "S" :
            print("choose calculation (log , log10 , power , sqrt , sin , cos , tan , degrees , radians )")
# الى مش فاهم log و log10 معناهم اللوغاريتم الطبيعي و العشري و power معناها الأس و sqrt معناها الجزر التربيعي و sin , cos , tan معناهم بالترتيب جا و جتا و ظا و degrees تحويل الزاوية من دائري للدرجات و radians العكس        
# الدوال المثلثية لازم تتكتب بالراديان و value يعني قيمة        
# للنسخ حدد القيمة و اضعط كليك يمين و للصق اضغط كليك يمين تاني و القيم تقربها انت للواحد الصحيح        
            sc = (input())
            print()
            if sc == "log" :
                log = (float(input("put a value : ")))
                print(math.log(log))
            if sc == "log10" :
                log10 = (float(input("put a value : ")))
                print(math.log10(log10))
            if sc == "power" :
                power = (float(input("put a value : ")))
                print(power * power)
            if sc == "sqrt" :
                sqrt = (float(input("put a value : ")))
                print(math.sqrt(sqrt))
            if sc == "sin" :
                sin = (float(input("put a value (in radian) : ")))
                print(math.sin(sin))
            if sc == "cos" :
                cos = (float(input("put a value (in radian) : ")))
                print(math.cos(cos))
            if sc == "tan" :
                tan = (float(input("put a value (in radian) : ")))
                print(math.tan(tan))
            if sc == "degrees" :
                degrees = (float(input("put a value (in radian) : ")))
                print(math.degrees(degrees))
            if sc == "radians" :
                radians = (float(input("put a value (in degress) : ")))
                print(math.radians(radians))

print(input("press enter to exit"))



















