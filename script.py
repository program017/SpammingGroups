import os
import csv
import pandas as pd

def SettingRoot():
    root=os.getcwd()
    #print(root)
    return root

def SetPirority(temp_projects):
    print("Enter Pirority of projects. 1 means highest")
    projects={}
    check={}
    for i in range(0,len(temp_projects)):
        temp=int(input('Enter for '+str(temp_projects[i])+':'))
        while(temp<=0 or temp>len(temp_projects) or temp in check):
            print("Invalid input. Try again")
            temp=int(input('Enter for '+str(temp_projects[i])+':'))
        check[temp]=0
        projects[temp_projects[i]]=temp
        #print(check,temp)
    return projects

def Arrange_by_pirority(modules,pirority):
    for i in modules:
        temp_old=modules[i]
        temp_new=[0 for i in range(0,len(pirority))]
        for items in temp_old:
            pirority_of_current=pirority[items]
            temp_new[pirority_of_current-1]=items
        while len(temp_new)!=len(temp_old):
            temp_new.remove(0)
        modules[i]=temp_new
    return modules


def SanityUpstream():
    print("Running Upstream Sanity Automation")
    print("*******************************************")
    print("Project currently in Upstream Sanity")
    modules={}
    temp_projects=[]
    for projects in os.listdir():
        if str(projects.split('.')[-1])!='xlsx':  #just checking for excel files
            #print(projects)
            pass
        else:
            data=pd.read_excel(projects)
            df=pd.DataFrame(data,columns=['Module','Stage 1'])
            df=df.dropna()
            df=df.loc[df['Stage 1'] == 'not updated']
            undone_module=df['Module'].tolist()
            for i in undone_module:
                if str(i) in modules:
                    temp=modules[str(i)]
                    temp.append(str(projects).split('.')[0])
                    modules[str(i)]=temp
                else:
                    modules[str(i)]=[str(projects).split('.')[0]]
            print(projects.split('.')[0])
            temp_projects.append(projects.split('.')[0])
    pirority=SetPirority(temp_projects)
    print("----------Module wise-----------")
    modules=Arrange_by_pirority(modules,pirority)
    for i in modules:
        print(i,modules[i])

def DeltaMerge():
    modules={}
    print("Running Delta Merge Automation")
    print("***************************************")
    print("Projects currently in Delta Merge Stage")
    temp_projects=[]
    for projects in os.listdir():
        if str(projects.split('.')[-1])!='xlsx':  #just checking for excel files
            #print(projects)
            pass
        else:
            data=pd.read_excel(projects)
            #print(data)
            df=pd.DataFrame(data,columns=['Part Module','Delta Status'])
            df=df.dropna()
            df=df.loc[df['Delta Status'] == 'Not Confirmed']
            #print(df)
            undone_module=df['Part Module'].tolist()
            for i in undone_module:
                if str(i) in modules:
                    temp=modules[str(i)]
                    temp.append(str(projects).split('.')[0])
                    modules[str(i)]=temp
                else:
                    modules[str(i)]=[str(projects).split('.')[0]]
            print(projects.split('.')[0])
            temp_projects.append(projects.split('.')[0])
    pirority=SetPirority(temp_projects)
    print("----------Module wise-----------")
    modules=Arrange_by_pirority(modules,pirority)
    for i in modules:
        print(i,modules[i])

def main():
    root=SettingRoot()
    choice=0
    while choice<1 or choice>3:
        print("Spam Automation")
        print("Enter Choice")
        print("1. Run Delta")
        print("2. Run Upstream")
        print("3. Exit")
        choice=int(input())
        if choice==1:
            deltamerge=root+"\DeltaMerge"
            os.chdir(deltamerge)
            DeltaMerge()
            os.chdir(root)
        elif choice==2:
            upstream=root+"\SanityUpstream"
            os.chdir(upstream)
            SanityUpstream()
            os.chdir(root)
        elif choice==3:
            print("Closing")
        else:
            print("Wrong choice. Enter Again")

if __name__=="__main__":
    main()
