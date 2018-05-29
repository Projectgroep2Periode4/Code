import xlrd

def main():
    Headers_For,Headers_Rev,Sequences_For,Sequences_Rev=Open_test()
    To_File(Headers_For,Headers_Rev,Sequences_For,Sequences_Rev)

def Open_test():
    Headers_For=[]
    Headers_Rev=[]
    Sequences_For=[]
    Sequences_Rev=[]
    workbook=xlrd.open_workbook('Course4_dataset_v03.xlsx')
    worksheet=workbook.sheet_by_name('groep2')
    worksheet=workbook.sheet_by_index(0)
    for i in range(0,100):
        Headers_For.append(worksheet.cell(i,0).value)
        Headers_Rev.append(worksheet.cell(i,3).value)
        Sequences_For.append(worksheet.cell(i,1).value)
        Sequences_Rev.append(worksheet.cell(i,4).value)

    return Headers_For,Headers_Rev,Sequences_For,Sequences_Rev

def To_File(Headers_For,Headers_Rev,Sequences_For,Sequences_Rev):
    Buffer=''
    Items=[]
    Headers_For2=[]
    T1=''
    Headers_Rev2=[]
    T2=''

    for Header in Headers_For:
        for k in Header:
            if k == "@":
                T1=T1+">"
            else:
                T1=T1+k
        Headers_For2.append(T1)
        T1=''

    for Header in Headers_Rev:
        for k in Header:
            if k == "@":
                T2=T2+">"
            else:
                T2=T2+k
        Headers_Rev2.append(T2)
        T2=''

    Gegevens=[Headers_For2,Headers_Rev2,Sequences_For,Sequences_Rev]
    for Lists in Gegevens:
        for item in Lists:
            Buffer+=item+','
        Items.append(Buffer)
        Buffer=''

    Data='<HF,'+Items[0]+'\n<HR,'+Items[1]+'\n<SF,'+Items[2]+'\n<SR,'+Items[3]
    with open('ParsedData.txt','w') as FileOut:
        FileOut.write(Data)

main()