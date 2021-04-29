print(" *********** Enter the details **************** ")
f_name=input("First Name: ")
m_name=input("Middle Name (if) : ")
l_name=input("Last Name: ")
address=input("Address: ")
pincode=input("Pincode: ")
blood_group=input("Blood group: ")
age=input("Age: ")
contact_no=input("Contact Number: ")
add_contact_no=input("Additional Contact Number: ")
resident_contact_no=input("Residential Contact No. : ")
dept=input("Department: ")
dept_code=input("Department Code: ")
emp_id=input("Employeed Id: ")

blood_group_list=('A+' or 'A−' or 'B+' or 'B−' or 'AB+' or 'O+ ' or 'O−' or 'AB−')
while True:
    # Naming_Part 
    if (f_name.isalpha()) and l_name.isalpha() and (m_name.isalpha())==True:
        if(len(f_name)<=15) and (len(m_name)<=15) and (len(l_name)<=15)==True:
            pass
    elif ((f_name.isalpha()) and l_name.isalpha() and (m_name==""))==True:
        if(len(f_name)<=15) and (len(l_name)<=15)==True:
            pass
            
    elif ((f_name=="") or (f_name.isalpha()==False))==True:
        f_name=input("First Name: ")

    elif (l_name=="") or (l_name.isalpha()==False)==True:
        l_name=input("Last Name: ")
    
    # Age
    if age.isdigit()==True:
        age_limit=int(age)
        if (age_limit>=20) and (age_limit<=60):
            pass
        elif (age_limit>60) and (age_limit<20):
            age=input("Age: ")
    
    #Contact_feilds
    if (contact_no.isdigit() and add_contact_no.isdigit() and resident_contact_no.isdigit())==True:
        if (len(contact_no)==10)==False:
            contact_no=input("Contact Number: ")
        elif (len(add_contact_no)==10)==False:
            add_contact_no=input("Additional Contact Number: ")
        elif (len(resident_contact_no)==10)==False:
            resident_contact_no=input("Residential Contact No. : ")
        elif ((len(resident_contact_no)) and (len(add_contact_no)) and (len(contact_no))==10)==True:
            pass
    elif contact_no.isdigit()==False:
        contact_no=input("Contact Number: ")
    elif add_contact_no.isdigit()==False:
        add_contact_no=input("Additional Contact Number: ")
    elif resident_contact_no.isdigit()==False:
        resident_contact_no=input("Residential Contact No. : ")
    
    #Blood Group
    if (blood_group==blood_group_list)==True:
        pass
    elif ((blood_group=="") and (blood_group!=blood_group_list))==True:
        blood_group=input("Blood group: ")
    
     #address

    if (len(address)<=100)==True:
        pass
    elif (address=="")==True:
        address=input("Address: ")

    if pincode.isalnum()==True:
        if (len(pincode)<=6)==True:
            pass
    elif ((pincode.isalnum()==False) or (pincode==""))==True:
        pincode=input("Pincode: ")
    
    #dept
    
    if dept.isalpha()==True:
        if(len(dept)<=30)==True:
           pass
    elif ((dept.isalpha()==False) or (dept==""))==True:
        dept=input("Department: ")

    #dept_code

    if dept_code.isalnum()==True:
        if(len(dept_code)==6)==True:
            pass
    elif ((dept_code.isalnum()==False) or (dept_code==""))==True:
        dept=input("Department Code: ")
    
    #emp_id
    if emp_id.isdigit()==True:
        if(len(emp_id)==6)==True:
           pass
    elif ((emp_id.isdigit()==False) or (emp_id==""))==True:
        dept_code=input("Employee Id: ")
    
    if (add_contact_no and resident_contact_no and contact_no and blood_group and address and pincode and dept and dept_code and emp_id and f_name and l_name and age)!="":
        print("\n #### Result ###")
        print("First Name: {}".format(f_name))
        print("Middle Name: {}".format(m_name))
        print("Last Name: {}".format(l_name))
        print("Address: {}".format(address))
        print("Pincode: {}".format(pincode))
        print("Blood group: {}".format(blood_group))
        print("Age: {}".format(age))
        print("Contact No: {}".format(contact_no))
        print("Additional Contact No: {}".format(add_contact_no))
        print("Resident Contact No: {}".format(resident_contact_no))
        print("Department: {}".format(dept))
        print("Department Code: {}".format(dept_code))
        print("Employee Id:  {}".format(emp_id))
        break
