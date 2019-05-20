# your co#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    total={}
    l=len(patient_medical_speciality_list)
    m=0
    i=1
    while(i<l):
        total[patient_medical_speciality_list[i]]=0
        i=i+2
    i=1    
    while(i<l):
        total[patient_medical_speciality_list[i]]=total[patient_medical_speciality_list[i]]+1
        i=i+2    
    for j in total:
        if(m<=total[j]):
            m=total[j]
            speciality=medical_speciality[j]
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
