import xlrd

def main():
    Headers_For,Headers_Rev,Sequences_For,Sequences_Rev,FastQs_For,FastQs_Rev=Open_test()
    To_File(Headers_For,Headers_Rev,Sequences_For,Sequences_Rev,FastQs_For,FastQs_Rev)

def Open_test():
    Headers_For=[]
    Headers_Rev=[]
    Sequences_For=[]
    Sequences_Rev=[]
    FastQs_For=[]
    FastQs_Rev=[]
    workbook=xlrd.open_workbook('Course4_dataset_v03.xlsx')
    worksheet=workbook.sheet_by_name('groep2')
    worksheet=workbook.sheet_by_index(0)
    for i in range(0,100):
        Headers_For.append(worksheet.cell(i,0).value)
        Headers_Rev.append(worksheet.cell(i,0).value)
        Sequences_For.append(worksheet.cell(i,1).value)
        Sequences_Rev.append(worksheet.cell(i,4).value)
        FastQs_For.append(worksheet.cell(i,2).value)
        FastQs_Rev.append(worksheet.cell(i,5).value)

    return Headers_For,Headers_Rev,Sequences_For,Sequences_Rev,FastQs_For,FastQs_Rev

def To_File(Headers_For,Headers_Rev,Sequences_For,Sequences_Rev,FastQs_For,FastQs_Rev):
    Data='HF\t'+str(Headers_For)+'\n\nHR\t'+str(Headers_Rev)+'\n\nSF\t'+str(Sequences_For)+'\n\nSR\t'+str(Sequences_Rev)+'\n\nFF\t'+str(FastQs_For)+'\n\nFR\t'+str(FastQs_Rev)
    with open('ParsedData.txt','w') as FileOut:
        FileOut.write(Data)

main()