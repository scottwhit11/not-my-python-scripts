# reverse_number.py

user_input=int(input("Enter the number to reverse: "))
_rev=0
while(user_input>0):
  dig=user_input%10
  _rev=_rev*10+dig
  user_input=user_input//10
print("The reversed number is :",_rev)

  #To execute from the terminal, run the following code:
  #python3 reverse_number.py