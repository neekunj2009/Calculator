
def main():
 
 print("Select An operator From bellow")
 print('''
 + ADD
 - SUBTRACT
 * MULTIPY
 / DIVIDE 
 ''')
 num1=int(input("Enter the Value 1:"))
 num2=int(input("Enter the Value 2:"))
 opr=input("Enter The Operator")

 if opr== "+":
    print(num1+num2)
 elif opr== "-":
    print(num1-num2)    
 elif opr== "*":
    print(num1*num2)
 elif opr== "/":
    print(num1/num2)
 else:
    print("INVALID OPERATOR")

 Restart= str(input("Do you want to Reuse it "))

 if Restart == "yes":
    main()
 elif Restart == "no":
  exit()
main()