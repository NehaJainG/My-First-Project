#Sample hostel name "NEW ERA HOME"
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import csv
import mysql.connector as m


def clearframe():
   #destroy all widgets from middle frame
   for widget in middle.winfo_children():
       widget.destroy()
   return
   #this will clear frame and frame will be empty

def admsnform():
   clearframe()
   def submission():
      try:
         values=(Name.get(),Class.get(),Section.get(),dob.get(),Gender.get(),Address.get(),PGName.get(),Room.get(),Contact.get(),Email.get())
         query='(Name,Class,Section,Dob,Gender,Permanent_Address,ParentGuardian,Room_no,Contact,Email)'
         QUERY= 'INSERT INTO Students'+query+'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
         cur.execute(QUERY,values)
         mydb.commit()
         message=Label(middle, text="You are successfully given admission in the hostel",font=('Arial',14,'bold'))
         message.grid(row=14,column=0,columnspan=2)
         cur.execute("SELECT * FROM Students WHERE name='"+values[0]+"' ")
         d=cur.fetchall()
         id_=Label(middle, text='Your school id is: '+str(d[0][0])+" Keep it safely", font=("Arial",15))
         id_.grid(row=15,column=0,columnspan=2)
         Name.set('')
         dob.set('')
         Gender.set('')
         Class.set('')
         Section.set('')
         Address.set('')
         PGName.set('')
         Contact.set('')
         Room.set('')
         Email.set('')
      except:
         error=Label(middle,text='Incorrect format/Error, TRY AGAIN LATER',font=('Arial',14,'bold'))
         error.grid(row=14,column=0,columnspan=2)
      
   adfm=Label(middle, text="ADMISSION FORM : ", font=('Arial',19,'bold') )
   adfm.grid(row=0,column=0,columnspan=2)

   L_Name=Label(middle, text="Name: ", font=('Arial',16,'bold') )
   L_Name.grid(row=1,column=0,padx=20)
   E_Name=Entry(middle,font=('Arial',12,'bold'), textvariable=Name, width=28)
   E_Name.grid(row=1,column=1,padx=20)

   L_Class=Label(middle, text="Class: ", font=('Arial',16,'bold') )
   L_Class.grid(row=2,column=0,padx=20)
   E_Class=Entry(middle,font=('Arial',12,'bold'), textvariable=Class, width=28)
   E_Class.grid(row=2,column=1,padx=20)

   L_Dob=Label(middle, text="Date Of Birth: (yyyy-mm-dd)", font=('Arial',16,'bold') )
   L_Dob.grid(row=3,column=0,padx=20)
   E_Dob=Entry(middle,font=('Arial',12,'bold'), text='yyyy-mm-dd',textvariable=dob, width=28)
   E_Dob.grid(row=3,column=1,padx=20)

   L_Gender=Label(middle, text="Gender: ", font=('Arial',16,'bold') )
   L_Gender.grid(row=4,column=0,padx=20)
   E_Gender=ttk.Combobox(middle,font=('Arial',12,'bold'), textvariable=Gender, state='readonly',width=28)
   E_Gender['value']=('Select','M','F','O')
   E_Gender.current(0)
   E_Gender.grid(row=4,column=1,padx=20)

   L_Adrs=Label(middle, text="Permanent Address: ", font=('Arial',16,'bold') )
   L_Adrs.grid(row=5,column=0,padx=20)
   E_Adrs=Entry(middle,font=('Arial',12,'bold'), textvariable=Address, width=28)
   E_Adrs.grid(row=5,column=1)

   L_PName=Label(middle, text="Parent/Guardian Name: ", font=('Arial',16,'bold') )
   L_PName.grid(row=6,column=0,padx=20)
   E_PName=Entry(middle,font=('Arial',12,'bold'), textvariable=PGName, width=28)
   E_PName.grid(row=6,column=1,padx=20)

   L_Contact=Label(middle, text="Contact: ", font=('Arial',16,'bold') )
   L_Contact.grid(row=7,column=0,padx=20)
   E_Contact=Entry(middle,font=('Arial',12,'bold'), textvariable=Contact, width=28)
   E_Contact.grid(row=7,column=1,padx=20)

   L_Email=Label(middle, text="Email: ", font=('Arial',16,'bold') )
   L_Email.grid(row=8,column=0,padx=20)
   E_Email=Entry(middle,font=('Arial',12,'bold'), textvariable=Email, width=28)
   E_Email.grid(row=8,column=1,padx=20)

   note=L_Name=Label(middle, text=" **To be filled by school authorities** ", font=('Arial',13,'bold') , bg='green')
   note.grid(row=9,column=0,columnspan=2,padx=20)

   L_Section=Label(middle, text="Section: ", font=('Arial',16,'bold') )
   L_Section.grid(row=10,column=0,padx=20)
   E_Section=Entry(middle,font=('Arial',12,'bold'), textvariable=Section, width=28)
   E_Section.grid(row=10,column=1,padx=20)

   L_Room=Label(middle, text="Room No: ", font=('Arial',16,'bold') )
   L_Room.grid(row=11,column=0,padx=20)
   E_Room=Entry(middle,font=('Arial',12,'bold'), textvariable=Room, width=28)
   E_Room.grid(row=11,column=1,padx=20)

   Submit=Button(middle,font=('Arial',28,'bold'), text='SUBMIT', padx=10, fg='white',bg='blue',command=submission)
   Submit.grid(row=12,column=0,columnspan=2)

   Note=Label(middle, text="*Press SUBMIT after filling all details PROPERLY*", font=('Arial',13,'bold') )
   Note.grid(row=13,column=0,columnspan=2)
    
def fee_class():
    clearframe()
    middlel=Frame(middle,width=500,height=450,padx=20,relief=RIDGE,bg="white",bd=6)
    middlel.pack(side=LEFT)
    middler=Frame(middle,width=500,height=450,padx=20,relief=RIDGE,bg="white",bd=6)
    middler.pack(side=RIGHT)
    def dis_fdetail(n):
       with open("fee.csv",'r') as file:
           data=csv.reader(file)
           for i in data:
               if i[0]==n:
                   tf,cf,rf,ff,tt=i[1:6]
                   L_tf= Label(middler, text="TUTION FEE: "+tf,font=('Arial',20,'bold'))
                   L_tf.grid()
                   L_cf= Label(middler, text="COMPUTER FEE: "+cf,font=('Arial',20,'bold'))
                   L_cf.grid()
                   L_rf= Label(middler, text="ROOM FEE: "+rf,font=('Arial',20,'bold'))
                   L_rf.grid()
                   L_ff= Label(middler, text="FOOD FEE: "+ff,font=('Arial',20,'bold'))
                   L_ff.grid()
                   L_tt= Label(middler, text="TOTAL: "+tt,font=('Arial',20,'bold'))
                   L_tt.grid() 
    l1= Label(middlel, text="FEE DETAILS FOR WHICH CLASS?",font=('Arial',20,'bold') )
    l1.grid(row=0,column=0,columnspan=2)
    Class3=Button(middlel, text='CLASS 03', padx=50,bg='white',command=lambda:dis_fdetail('3'))
    Class3.grid(row=1,column=0)
    Class4=Button(middlel, text='CLASS 04', padx=50,bg='white',command=lambda:dis_fdetail('4'))
    Class4.grid(row=1,column=1)
    Class5=Button(middlel, text='CLASS 05', padx=50,bg='white',command=lambda:dis_fdetail('5'))
    Class5.grid(row=2,column=0)
    Class6=Button(middlel, text='CLASS 06', padx=50,bg='white',command=lambda:dis_fdetail('6'))
    Class6.grid(row=2,column=1)
    Class7=Button(middlel, text='CLASS 07', padx=50,bg='white',command=lambda:dis_fdetail('7'))
    Class7.grid(row=3,column=0)
    Class8=Button(middlel, text='CLASS 08', padx=50,bg='white',command=lambda:dis_fdetail('8'))
    Class8.grid(row=3,column=1)
    Class9=Button(middlel, text='CLASS 09', padx=50,bg='white',command=lambda:dis_fdetail('9'))
    Class9.grid(row=4,column=0)
    Class10=Button(middlel, text='CLASS 10', padx=50,bg='white',command=lambda:dis_fdetail('10'))
    Class10.grid(row=4,column=1)
    Class11=Button(middlel, text='CLASS 11', padx=50,bg='white',command=lambda:dis_fdetail('11'))
    Class11.grid(row=5,column= 0)
    Class12=Button(middlel, text='CLASS 12', padx=50,bg='white',command=lambda:dis_fdetail('12'))
    Class12.grid(row=5,column=1)
    
def IMG():
    clearframe()
    middlel=Frame(middle,width=500,height=450,padx=20,relief=RIDGE,bg="white",bd=6)
    middlel.pack(side=LEFT)
    middler=Frame(middle,width=500,height=450,padx=20,relief=RIDGE,bg="white",bd=6)
    middler.pack(side=RIGHT)
#---------------------------variable to store images for CAMPUS--------------------------------------------------------------------------------------
    C=["C:/Users/Akash/Neha/Desktop/campus1.jpeg",'C:/Users/Akash/Neha/Desktop/campus2.jfif','C:/Users/Akash/Neha/Desktop/campus3.jfif']
#---------------------------variable to store images for ROOM-----------------------------------------------------------------------------------
    R=["C:/Users/Akash/Neha/Desktop/room1.jpg",'C:/Users/Akash/Neha/Desktop/room2.jfif','C:/Users/Akash/Neha/Desktop/room3.jfif','C:/Users/Akash/Neha/Desktop/room4.jpg']
    CAMPUS=Button(middlel, text='CAMPUS IMAGES', padx=50,bg='white' ,command=lambda:display_img(C))
    CAMPUS.grid(row=1,column=0)
    ROOM=Button(middlel, text='ROOM IMAGES', padx=50,bg='white',command=lambda:display_img(R))
    ROOM.grid(row=2,column=0)

    def display_img(imgl_):
       global l_img
       img=[]
       for i in imgl_:
           img_ = ImageTk.PhotoImage(Image.open(i))
           img.append(img_)
       n=len(imgl_)
       l_img = Label(middler,image=img[0])
       l_img.grid(row=0, column=1)

       def forward(img_num):
           global l_img
           global b_forward
           global b_back
           l_img.grid_forget()
           l_img = Label(middler, image=img[img_num-1])
           b_forward = Button(middler, text=">>>", command=lambda: forward(img_num+1))
           b_back = Button(middler, text="<<<", command=lambda: back(img_num-1))
           if img_num == n:
               b_forward = Button(middler, text=">>>", state=DISABLED)
           l_img.grid(row=0, column=1)
           b_back.grid(row=0, column=0)
           b_forward.grid(row=0, column=2)

       def back(img_num):
           global l_img
           global b_forward
           global b_back
           l_img.grid_forget()
           l_img = Label(middler,image=img[img_num-1])
           b_forward = Button(middler, text=">>>", command=lambda: forward(img_num+1))
           b_back = Button(middler, text="<<<", command=lambda: back(img_num-1))
           if img_num == 1:
               b_back = Button(middler, text="<<<", state=DISABLED)
           l_img.grid(row=0, column=1)
           b_back.grid(row=0, column=0)
           b_forward.grid(row=0, column=2)
           
       b_back = Button(middler, text="<<<", command=back, state=DISABLED)
       b_forward = Button(middler, text=">>>", command=lambda: forward(2))
       b_back.grid(row=0, column=0)
       b_forward.grid(row=0, column=2)
       

def facilities():
    clearframe()
    label1= Label(middle, text="Facilities: ", font=('Arial',16,'bold') )      #Here you can type the facilities provided
    label2= Label(middle,text='''
Perfect routine translates into the fact that there is a scheduled wake-up time, a time when breakfast,lunch,and dinner are served,
adequate arrangements for studies, and on top of that there is enough space for physical and recreational activities too. Hygiene
is on the top listthe first thing that we look for is the hygienefactors that the hostel provides. Clean utensils for cooking the food,
serving them, clean washrooms, and cleanliness of the residential space are always checked on time and again.
Recreational rooms: “All work and no play, makes Jack a dull boy” – this goes without saying and the same applies to school kids.
The students cannot always engage in studies but must have the space of balancing and dividing his/her time to study, play and
spend time at recreational activities. There are dedicated rooms and a playground where the kids can meet at their leisure and
spend time playing outdoor or indoor games. This will help them fight boredom, homesickness, and other negatives if any.
First Aid facilities: Student health and emergency administration is another factor that is top a school’s hostel facility’s list. we always
ensure for the first aid facilities of our hostel that are provided during your child’s stay at the same. The first aid facilities ensure that
there are items that could take care of the child is suffering from fever, deep wounds, or minor injuries while they are engaged in
playing games or so on. Celebration of special occasions. The perk of staying in a hostel is that the children get a scope to spend
time with friends. It may so happen that special occasions like Diwali or any other religious festival fall during the school session when
the children happen to stay back at their schools. The facility of celebrating those occasions with peers will lift their mood and make
their stay at the place happier. The homely feeling goes a long way, again, to break their regular monotony and bond with their peers.
IMPORTANT POINTS TO NOTE: Under no circumstances the institution shall provide separate rooms for school students.   
Our hostel provides electricity 24/7 and there are security cameras in each hostel corridor to ensure utmost safety. Students are
provided with water cans for drinking. Each floor consists of separate restrooms for girls and boys. New era hostel provides 3 member
sharing room to 6 member sharing room for students according to their convenience but shall not be allowed to change or shift their
rooms according to their wish. Students are given enough space to do their laundry and the privacy of students is our utmost priority.
Parents are not allowed to enter the hostel premises. Students are not allowed to have a bulk amount of cash with them without their
respective warden's permission.''', font=('Arial',14),bg='white')
    label1.pack()
    label2.pack()
    
 #_main_    
mydb=m.connect(host="localhost",user="root",passwd='Nehajain#12', database="Hostel_Management")
cur=mydb.cursor()

print("\t\t\tWELCOME TO THE NEW ERA HOME\n\n")
print("Login as: \n1.Student, \n2.Teacher, \n3.New entry")
c=int(input("Enter your choice(1/2/3) from above: "))
if c==1:
   cur.execute("SELECT * FROM Students")
   stdrec=cur.fetchall()
   c='y'
   while c=='y' or c=='Y':
       name=input("Enter your Full Name:")
       pswd=int(input("Enter Your Password:"))
       for x in stdrec:
           if x[0]==pswd and x[1].lower()==name.lower():
               print("Logined succesfully!!!")
               c='n'
               c2='y'
               while c2=='y' or c2=='Y':
                  print("\t\t\t**Menu:**\t\t\t \n1.View Details \n2.Update details \n3.Fee Details \n4.Exit")
                  c1=int(input("Select any one of the option from above(1/2/3/4): "))
                  if c1==1:
                      print("1. Your id: ",x[0])
                      print("2. Name: ",x[1])
                      print("3. Class: ",x[2])
                      print("4. Section: ",x[3])
                      print("5. Date of Birth: ",x[4])
                      print("6. Gender: ", x[5])
                      print("7. Permanent Address: ",x[6])
                      print("8. Parent/Guardian Name: ",x[7])
                      print("9. Room Number: ",x[8])
                      print("10. Contact: ",x[9])
                      print("11. Email id: ",x[10])

                  elif c1==2:
                      print("1. Name, \n2. Room No, \n3. Class,")
                      print("4. Section, \n5. Date of Birth, \n6. Gender,")
                      print("7. Permanent Address, \n8. Parent/Guardian Name,")
                      print("9. Contact, \n10. Email id. ")
                      ec='y'
                      while ec=='y' or ec=='Y':
                         option=int(input("What you want to update/edit: "))
                         if option==1:
                            Value=input("Enter Your Correct Name: ")
                            cur.execute("UPDATE students SET Name='"+Value+"' WHERE Id= "+ str(x[0]))
                         elif option==2:
                            Value=input("Enter Your Correct Room Number: ")
                            cur.execute("UPDATE students SET Room_no="+Value+"WHERE Id= "+ str(x[0]))
                         elif option==3:
                            Value=input("Enter Your Correct Class: ")
                            cur.execute("UPDATE students SET Class="+Value+"WHERE Id= "+ str(x[0]))
                         elif option==4:
                            Value=input("Enter Your Correct Section: ")
                            cur.execute("UPDATE students SET Section='"+Value+"' WHERE Id= "+ str(x[0]))
                         elif option==5:
                            Value=input("Enter Your Correct Date of Birth: ")
                            cur.execute("UPDATE students SET Dob='"+Value+"' WHERE Id= "+ str(x[0]))
                         elif option==6:
                            Value=input("Enter Your Correct Gender: ")
                            cur.execute("UPDATE students SET Gender='"+Value+"' WHERE Id= "+ str(x[0]))
                         elif option==7:
                            Value=input("Enter Your Correct Permanent Address: ")
                            cur.execute("UPDATE students SET Permanent_Address='"+Value+"' WHERE Id= "+ str(x[0]))
                         elif option==8:
                            Value=input("Enter Your Correct Parent/Guardian Name: ")
                            cur.execute("UPDATE students SET ParentGuardian='"+Value+"' WHERE Id= "+ str(x[0]))
                         elif option==9:
                            Value=input("Enter Your Correct Contact Number: ")
                            cur.execute("UPDATE students SET Contact="+Value+" WHERE Id= "+ str(x[0]))
                         elif option==10:
                            Value=input("Enter Your Correct Email Id: ")
                            cur.execute("UPDATE students SET Email='"+Value+"' WHERE Id= "+str(x[0]))
                         else:
                            print("Wrong Input!")
                         mydb.commit()
                         ec=input("Do you want to continue update(y/n): ") 

                  elif c1==3:
                      with open("fee.csv",'r') as file:
                         data=csv.reader(file)
                         for i in data:
                            if i[0]==str(x[2]):
                               tf,cf,rf,ff,tt=i[1:6]
                               print("Term Fee Amount:")
                               print("Tution fee: ",tf)
                               print("Computer fee: ",cf)
                               print("Room fee: ",rf)
                               print("Food fee: ",ff)
                               print("The Total Amount for the year= Rs.",tt)
                               break
                              
                  else:
                     break
                  c2=input("Do you want to continue(y/n): ")
               break
                  

           else:
              continue
           
       else:
            print("Incorrect Name or Password")
            c=input("Do you want to try again(y/n):")

elif c==2:
    cur.execute("SELECT * FROM Teacher")
    tearec=cur.fetchall()

    c='y'
    while c=='y' or c=='Y':
        name=input("Enter your Full Name:")
        pswd=int(input("Enter Your Password:"))
        for x in tearec:
            if x[0]==pswd and x[1].lower()==name.lower():               
               c2='y'
               while c2=='y' or c2=="Y":
                   print("Logined succesfully!!!")
                   c='n'
                   print("\t\t\t*********Menu:*********\t\t\t \n1.View Details \n2.Update details \n3.Exit")
                   c1=int(input("Select any one of the option from above(1/2/3): "))
                   if c1==1:
                      print("1. Your id: ",x[0])
                      print("2. Name: ",x[1])
                      print("3. Profession: ",x[2])
                      print("4. Contact: ",x[3])
                      print("5. Date of Birth: ",x[4])
                      print("6. Gender: ", x[5])
                      print("7. Permanent Address: ",x[6])
                      print("8. Email_id ",x[7])
                      print("9. Salary: ",x[8])
                   elif c1==2 :
                      print("1. Name, \n2. Profession,")
                      print("3. Contact, \n4. Date of Birth, \n5. Gender,")
                      print("6. Permanent Address, \n7. Email_id,")
                      
                      ec='y'
                      while ec=='y' or ec=='Y':
                         option=int(input("What you want to update/edit: "))
                         if option==1:
                            Value=input("Enter Your Correct Name: ")
                            cur.execute("UPDATE teacher SET Name='"+Value+"' WHERE Id= "+ str(x[0]))
                         elif option==2:
                            Value=input("Enter Your Profession: ")
                            cur.execute("UPDATE teacher SET Profession='"+Value+"' WHERE Id= "+ str(x[0]))
                         elif option==3:
                            Value=input("Enter Your Correct Contact Number: ")
                            cur.execute("UPDATE teacher SET Contact="+Value+" WHERE Id= "+  str(x[0]))
                         elif option==4:
                            Value=input("Enter Your Correct Date of Birth: ")
                            cur.execute("UPDATE teacher SET Dob='"+Value+"' WHERE Id= "+ str(x[0]))
                         elif option==5:
                            Value=input("Enter Your Correct Gender: ")
                            cur.execute("UPDATE teacher SET Gender='"+Value+"' WHERE Id= "+ str(x[0]))
                         elif option==6:
                            Value=input("Enter Your Correct Permanent Address: ")
                            cur.execute("UPDATE teacher SET Permanent_Address='"+Value+"'WHERE Id= "+ str(x[0]))
                         elif option==7:
                            Value=input("Enter Your Correct Email id: ")
                            cur.execute("UPDATE teacher SET Email_id='"+Value+"' WHERE Id= "+ str(x[0]))
                         else:
                            print("Wrong Input!")
                         mydb.commit()
                         print("UPDATION COMPLETED SUCCESSFULLY")
                         ec=input("Do you want to continue update(y/n): ")
                   else:
                      break
                   c2=input("Do you want to continue(y/n): ") 
               break   
            else:
               continue
           
        else:
            print("Incorrect Name or Password")
            c=input("Do you want to try again(y/n):")

            
             
elif c==3:
    print("You are WELCOME to New Era Home. Get to know about all the details from new window ")
    pname=input("Enter Parent\Guardian name: ")
    sname=input("Enter Student name: ")
    Class=int(input("Enter your class currently(3-12 classes only): "))
    if Class>13 or Class<2 :
        print("We dont provide service for your class.")
        
    root=Tk()
    root.title("hostel")
    root.geometry("1250x700")
    Name=StringVar()
    Gender=StringVar()
    dob=StringVar()
    Contact=StringVar()
    Address=StringVar()
    Room=StringVar()
    Email=StringVar()
    Section=StringVar()
    Class=StringVar()
    PGName=StringVar()
#----------------------------------------------------------------Top Frames and it's buttons---------------------------------------------------------------------------
    top=Frame(root,width=1000,height=150,padx=20,relief=RIDGE,bg="white",bd=4)
    top.grid()
    l1= Label(top,font=('Arial',16,'bold'), text="WHAT DO YOU WANT TO VIEW?")
    l1.grid(row=0,column=0, columnspan=4)
    admission=Button(top,font=('Arial',14,'bold'),text='ADMISSION FORM', padx=50,bg='white' ,width=11,height=2,command=admsnform)
    admission.grid(row=1,column=0)
    fee=Button(top, font=('Arial',14,'bold'),text='FEE', padx=50,bg='white' ,width=11,height=2,command=fee_class)
    fee.grid(row=1,column=1)
    image=Button(top, font=('Arial',14,'bold'),text='HOSTEL IMAGES', padx=50,bg='white',width=11,height=2, command=IMG)
    image.grid(row=1, column=2)
    facility= Button(top,font=('Arial',14,'bold'),text='FACILITIES',padx=50,bg='white',width=11,height=2,command=facilities)
    facility.grid(row=1,column=3)
#------------------------------------------------------------------Middle Frame and its functions-------------------------------------------------------------------
    middle=Frame(root,width=1000,height=450,padx=20,relief=RIDGE,bg="white",bd=4)
    middle.grid()
    #Functions defined will be executed in the middle frame
#-------------------------------------------------------------------------------Exit in Bottom Frame-------------------------------------------------------------------------------
    bottom=Frame(root,width=1000,height=50,padx=20,relief=RIDGE,bg="white",bd=4)
    bottom.grid()
    exit_=Button(bottom,font=('Arial',14,'bold'), text='EXIT THE MENU', fg='black',bg='red',width=90, command=root.destroy)
    exit_.pack()
    root.mainloop()


   
else:
    print("Wrong Input!!!!")

print("*********************************** THANK YOU ***************************************")

