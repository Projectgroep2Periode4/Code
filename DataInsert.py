import mysql.connector, time, glob, os
from Bio.Blast import NCBIXML

Con = mysql.connector.connect(
    user="sql7242348",
    password="XhrqkulCnN",
    host="sql7.freemysqlhosting.net",
    database="sql7242348",
    port="3306")

def main(Con):
    Actie=Menu(Con)
    if Actie == 1:
        request_data(Con)
    elif Actie == 2:
        Insert_XML_Data(Con)
    elif Actie == 3:
        for i in ['READ1','READ2']:
            os.chdir("C:/Users/ygebo/Desktop/project/Code/BLASTS/"+i)
            for File in glob.glob("*.xml"): 
                Open_XML(File)
        print('_'*160)
    elif Actie == 4:
        print("Doei")
        time.sleep(3)
        exit()
    elif Actie == 0:
        insert_data(Con)
    else:
        Menu(Con)

def Menu(Con):
    print('\n1 -- Request Data\n2 -- Insert Data\n3 -- Open XML\n4 -- Exit')
    Actie=input("Voer actie in:\n--> ")
    if Actie == "":
        main(Con)
    Actie=int(Actie)
    return Actie
    
def request_data(Con):
    Cur=Con.cursor()
    Cur.execute("select * from blast")
    for line in Cur:
        print(line)
    Cur.close()
    Con.close()
    main(Con)

def insert_data(Con):
    Cur=Con.cursor()
    Des=input("Voer Description in: ")
    EVal=input("Voer E-Value in: ")
    QCov=input("Voer Query_cover in: ")
    BlID=input("Voer Blast_id in: ")
    Cur.execute("insert into blast (description,Evalue,query_cover,blast_id) value ('"+Des+"','"+EVal+"','"+QCov+"',"+BlID+")")
    Con.commit()
    main(Con)

def Open_XML(File):
    T="_"*160
    blast_record = NCBIXML.read(open(File))   
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            print(T)
            print ("Alignment")
            print ("Sequence  :", alignment.title)
            print ("Length    :", alignment.length)
            print ("E-value   :", hsp.expect)
            print ("Score     :", hsp.score)
            print ("Alignment:")
            print ('\tquery  :',hsp.query)
            print ('\t        ',hsp.match)
            print ('\tsubject:',hsp.sbjct)
    main(Con)

def Insert_XML_Data(Con):
    Cur=Con.cursor()
    DesS=[]
    EValS=[]
    QCovS=[]

    os.chdir("C:/Users/ygebo/Desktop/project/Code/BLASTS/READ1")
    for File in glob.glob("*.xml"):
        blast_record = NCBIXML.read(open(File))   
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                DesS.append(alignment.title.split("|"))
                EValS.append(hsp.expect)
                QCovS.append(hsp.score)

    os.chdir("C:/Users/ygebo/Desktop/project/Code/BLASTS/READ2")
    for File in glob.glob("*.xml"):
        blast_record = NCBIXML.read(open(File))   
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                DesS.append(alignment.title.split("|"))
                EValS.append(hsp.expect)
                QCovS.append(hsp.score)
    
    Length_Blasts=len(DesS)

    Tstart=time.time()
    for i in range(0,Length_Blasts):
        if str(DesS[i][4]).startswith(" 3'-5'"):
            Des=str(DesS[i][0])+"|"+str(DesS[i][1])+"|"+str(DesS[i][2])+"|"+str(DesS[i][3])+"|"+str(DesS[i][4]).replace(" >gi","").replace(" 3'-5'"," 3-5").replace("'","")
        else:
            Des=str(DesS[i][0])+"|"+str(DesS[i][1])+"|"+str(DesS[i][2])+"|"+str(DesS[i][3])+"|"+str(DesS[i][4]).replace(" >gi","").replace("'","")
        print(Des)
        Cur.execute("insert into blast (description,Evalue,query_cover,blast_id) value ('"+str(Des)+"',"+str(EValS[i])+","+str(QCovS[i])+","+str(i)+")")
    Con.Commit()
    Tend=time.time()
    print("\n-->",Length_Blasts,"Results committed in",int(round(Tend-Tstart)),"seconds\n") 

    Tstart=time.time()
    for i in range(0,Length_Blasts):
        print(DesS[i][1])
        Cur.execute("insert into fwrv (read_number,read_id) value ("+str(DesS[i][1])+","+str(i)+")")
    Con.Commit()
    Tend=time.time()
    print("\n-->",Length_Blasts,"Results committed in",int(round(Tend-Tstart)),"seconds\n")

    Tstart=time.time()
    OPP=[]
    ORG=[]
    Organisms=[]
    for i in range(0,Length_Blasts):
        OPP.append(DesS[i][4].split("["))
    for i in OPP:
        ORG.append(str(i[1:]).replace("] >gi","").split(" "))
    for i in ORG:
        TTT=str(i[0:2]).replace("[","").replace('"','').replace("]","").replace("'","").replace(",","")
        if TTT not in Organisms:
            Organisms.append(TTT)

    for i in range(0,len(Organisms)):
        print(Organisms[i])
        Cur.execute("insert into organism (organism,organism_id) value ('"+str(Organisms[i])+"',"+str(i)+")")
    Con.Commit()
    Tend=time.time()
    print("\n-->",len(Organisms),"Results committed in",int(round(Tend-Tstart)),"seconds\n")

main(Con)