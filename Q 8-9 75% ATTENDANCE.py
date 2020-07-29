"""8.A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
Answer

9.Modify the above question to allow student to sit if he/she has medical cause. 
Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly."""

CH=int(input("Enter number of classes held: "))
CA=int(input("Enter number of classes attended: "))
PER=(CA/CH)*100
print("Percentage of classes attend: ",PER)

if(PER<75):
    print("\n-------------NOT ALLOWED TO SIT IN EXAM :( -------------\n")
else:
    print("\n----------------ALLOWED TO SIT IN EXAM :)--------------\n")




if(PER<75):
    Medical=input("Does he/she has Medical cause? \nAnswer in Y or N only: ")

    if(Medical=="Y"):
        print("\n----------------ALLOWED TO SIT IN EXAM :)--------------\n")

    if(Medical=="N"):
        print("\n-------------NOT ALLOWED TO SIT IN EXAM :)--------------\n") 

    else:
        print("Wrong Answer")   




     
    

       
      

