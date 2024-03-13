maths=int(input("Enter the marks of the math (out of 100):"))
science=int(input("Enter the marks of the science (out of 100):"))
computer=int(input("Enter the marks of the computer (out of 100):"))
gujarati=int(input("Enter the marks of the gujarati (out of 100):"))
sanskrit=int(input("Enter the marks of the sanskrit (out of 100):"))

marks=(maths+science+ computer+gujarati+sanskrit)/5

if marks>=90:
    print("RESULT: Pass & Grade: A")
elif marks>=80:
    print("RESULT: Pass & Grade: B")
elif marks>=70:
    print("RESULT: Pass & Grade: C")
elif marks>=50:
    print("RESULT: Pass & Grade: D")
elif marks>=35:
    print("RESULT: Pass & Grade: E")
else :
    print("RESULT: FAIL")