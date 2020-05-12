import os
import csv
import pandas as pd

def SettingRoot():
    root=os.getcwd()
    print(root)
    return root
    
def SanityUpstream():
    print("Running Upstream Sanity Automation")
    print("*******************************************")
    print("Project currently in Upstream Sanity")
    modules={}
    count=0
    number_of_projects=0
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
            count+=1
            print(projects.split('.')[0])
    print("----------Module wise-----------")
    for i in modules:
        print(i,modules[i])
        
def DeltaMerge():
    modules={}
    print("Running Delta Merge Automation")
    print("***************************************")
    print("Projects currently in Delta Merge Stage")
    count=0
    number_of_projects=0
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
            count+=1
            print(projects.split('.')[0])
    print("----------Module wise-----------")
    for i in modules:
        print(i,modules[i])
        
def main():
    root=SettingRoot()
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
    else:
        print("Closing")

if __name__=="__main__":
    main()