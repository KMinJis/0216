def calcme(student_):
    student_['tot']=student_['kor']+student_['eng']+student_['math']
    student_['avg']=student_['tot']/3
    student_['grade']=None
    if student_['avg']>= 90 :  student_['grade'] ='A'
    elif student_['avg']>= 80 :  student_['grade'] ='B'
    elif student_['avg']>= 70 : student_['grade'] = 'C'
    elif student_['avg']>= 60 :  student_['grade'] = 'D'
    else : student_['grade'] = 'F'