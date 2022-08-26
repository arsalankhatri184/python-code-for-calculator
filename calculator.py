print("%%%%%%%%%%%%%%%%%% Calculator %%%%%%%%%%%%%%%%%%%%%")
while True:
    in1=float(input("Enter First Value : "))
    in2=float(input("Enter First Value : "))
    print("%%%%%%%%%%%%%%%%%% Operators %%%%%%%%%%%%%%%%%%%%%%\n")
    list=["Addition (+)","Subtraction (-)","Multiplication (x)","Dividsion (/)","Exponent (ex)\n"]
    print(*list,sep="\n")
    print("Note: Enter input again if you are choosing Exponent\n")
    print("Enter Any One Operator")
    op=input()
    if op=="+":
        Sum=in1+in2
        print("Sum of 2 numbers is ",Sum,"\n")
        print("%%%%%%%%%%%%%%%%%% END %%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
    elif op=="-":
        Sub=in1-in2
        print("Sbtract of 2 numbers is ",Sub,"\n")
        print("%%%%%%%%%%%%%%%%%% END %%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
    elif op=="*" or op=="x" or op=="X":
        Mul=in1*in2
        print("Mul of 2 numbers is ",Mul,"\n")
        print("%%%%%%%%%%%%%%%%%% END %%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
    elif op=="/":
        if in2==0:
            print("The denominator is 0\n\n")
            print("%%%%%%%%%%%%%%%%%% END %%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
        else:
            Div=in1/in2
            print("Division of 2 numbers is %.3f"%Div,"\n")
            print("%%%%%%%%%%%%%%%%%% END %%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
    elif op=="ex" or op=="Ex":
        in1=float(input("Enter Base Value : "))
        in2=float(input("Enter Exponent Value : "))
        ex=in1**in2
        print("Your Exponent Value is %.2f"%ex,"\n")
        print("%%%%%%%%%%%%%%%%%% END %%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
    else:
        print("Please Enter Correct Operator\nTry Again\n")
        print("%%%%%%%%%%%%%%%%%% END %%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
        
