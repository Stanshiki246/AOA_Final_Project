from SortingAlgo import Sorting
from datetime import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
from os import system
from time import sleep
from math import log
from PGFeatures import *
import pygame as pg
import sys
import csv
"""
Name: Stanley Tantysco, Isabella, Alessandro, and Michael Stanley Chinaza
Sorting words from E-book
"""
#Main Class Object
class Main:

    S=Sorting()#Call Sorting class object

    LibraryDict={1: 'A Friend of Caesar',2: 'Antonina',3: 'Aurellian',4: 'Beowulf',5: 'Beric the Briton', 6: 'Castle Richmond', 7: 'Chaldea',
                 8: 'Dead Men Tell No Tales', 9: 'Dorian Gray', 10: 'Friends, though divided A Tale of the Civil War', 11: 'Grimms', 12: 'Hereward',
                 13: 'History of Egypt, Chaldea, Syria, Babylonia, and Assyria in the Light of Recent',14: 'Hypatia', 15: 'Ivanhoe',16: 'Jekyll and Hyde',
                 17: 'Pagan and Christian Rome', 18: 'Peter Pan', 19: 'Sherlock Holmes', 20: 'Shirley', 21: 'Springhaven',22: 'St. Ronan Well',23: 'Sybil',
                 24: 'The Legends of King Arthur and His Knights', 25: 'The Story of Sigurd the Volsung and the Fall of the Niblungs', 26: 'The Tales of Two Cities',
                 27: 'Twilight Land', 28: 'Ulysses', 29: 'Wulf the Saxon', 30: 'Zenobia'}#List of Ebooks

    NameList=[]#List of Added Ebooks
    LineList=[]#List of Ebook Contents
    words={}#List of word counter sets
    OrderFlag=False#Sorting order flag
    oname=''#Sorting order name
    sortingname=''#Name of sorting method

    TimeList=[]#Elapsed Time List
    EbookList=[]#List of Added Files
    EbookDict={}#List of Added Files Contents
    MergeEbook={}#List of Added Files Contents to be Merge Sorted
    ShellEbook={}#List of Added Files Contents to be Shell Sorted
    HeapEbook={}#List of Added Files Contents to be Heap Sorted
    QuickEbook={}#List of Added Files Contents to be Quick Sorted
    FileDict={}#List of Elapsed Time each files
    CompDict={}#List of Average Complexity each files
    MergeDict={}#List of Merge Sorted Elapsed Time each files
    ShellDict={}#List of Shell Sorted Elapsed Time each files
    HeapDict={}#List of Heap Sorted Elapsed Time each files
    QuickDict={}#List of Quick Sorted Elapsed Time each files
    TopWords={}#List of 10 Most Common or Fewest Words


    setting_panel='menu'#panel changing flag
    OF_Num=1#default of maximum size file
    MF_Num=3#default of file numbers
    MF_Steps=1#starting number of multiple files
    Book_KB=0#starting number of added books size
    backtrigger=False#back button trigger flag
    array2dmode=True#word counter sets trigger flag


    #word counter sets sorting time measuring functions
    def Measure_2DShellsort(self,arr,reversed,baseon):
        start = dt.now()

        self.S.Shell_Sort_2D(arr,reversed,baseon)

        return dt.now()-start

    def Measure_2DMergesort(self,arr,reversed,baseon):
        start = dt.now()

        self.S.MergeSort_2D(arr,reversed,baseon)

        return dt.now()-start

    def Measure_2DQuicksort(self,arr,low,high,reversed,baseon):
        start = dt.now()

        self.S.QuickSort_2D(arr,low,high,reversed,baseon)

        return dt.now()-start

    def Measure_2DHeapsort(self,arr,reversed,baseon):
        start = dt.now()

        self.S.HeapSort_2D(arr,reversed,baseon)

        return dt.now()-start

    #words sorting time measuring functions
    def Measure_Shellsort(self,arr,reversed):
        start = dt.now()

        self.S.Shell_Sort(arr,reversed)

        return dt.now()-start

    def Measure_Mergesort(self,arr,reversed):
        start = dt.now()

        self.S.MergeSort(arr,reversed)

        return dt.now()-start

    def Measure_Quicksort(self,arr,low,high,reversed):
        start = dt.now()

        self.S.QuickSort(arr,low,high,reversed)

        return dt.now()-start

    def Measure_Heapsort(self,arr,reversed):
        start = dt.now()

        self.S.HeapSort(arr,reversed)

        return dt.now()-start

    #average time complexity of merge, quick, and heap sorting function
    def MQH_AvgComplexity(self,arr):
        return int(round(len(arr)*log(len(arr),10),3))

    #average time complexity of shell sorting function
    def S_AvgComplexity(self,arr):
        return int(round(len(arr)*(log(len(arr),10)**2),3))

    #read file into dictionary list of word counter function
    def Load_Ebook(self,filename):
        file=open('Data_Sets\\'+filename+'.txt','r',encoding='UTF-8')
        readword=file.read().split()
        self.words['the']=1
        for word in range(1,len(readword)):
            if self.array2dmode:
                token=readword[word].replace('.','').replace('\'','').replace(',','').replace('_','').replace(';','').replace('?','').replace('!','').replace('\"','')\
            .replace('(','').replace(')','').replace(':','').replace('/','').replace('[','').replace(']','').replace('\\','').replace('\ufeff','').replace('”','').replace('“','').lower()
            else:
                token=readword[word].replace('\ufeff','').replace('”','\"').replace('“','\"').lower()

            if token not in self.words:
                self.words[token]=1
            else:
                self.words[token]+=1
        file.close()
    #read file into lists of words or lists of word counter sets function
    def Load_Ebook_Into_Lists(self,filename):
        file=open('Data_Sets\\'+filename+'.txt','r',encoding='UTF-8')
        readword=file.read().split()
        self.words['the']=1
        for word in range(1,len(readword)):
            if self.array2dmode:
                token=readword[word].replace('.','').replace('\'','').replace(',','').replace('_','').replace(';','').replace('?','').replace('!','').replace('\"','')\
            .replace('(','').replace(')','').replace(':','').replace('/','').replace('[','').replace(']','').replace('\\','').replace('\ufeff','').replace('”','').replace('“','').lower()
            else:
                token=readword[word].replace('\ufeff','').replace('”','\"').replace('“','\"').lower()

            if token not in self.words:
                self.words[token]=1
            else:
                self.words[token]+=1

        file.close()
        if self.array2dmode:
            Wordarr=self.Add_WordCounter()
        else:
            Wordarr=self.Add_Word()
        self.words.clear()
        return Wordarr

    #list of word counter sets getter function
    def Add_WordCounter(self):
        return list(self.words.items())

    #list of words getter function
    def Add_Word(self):
        return list(self.words.keys())


    def WriteandRead_WordCounter(self,adict,bdict,num):
        #Show output in terminal and plotting
        with open('Data_Sets\SingleFile.csv','w') as SingleCSV:
            fieldnames=['Words','Counting']
            writer=csv.DictWriter(SingleCSV,fieldnames)
            writer.writeheader()
            for key,value in adict.items():
                writer.writerow({'Words': key,'Counting': value})
        SingleCSV.close()
        df = pd.read_csv('Data_Sets\SingleFile.csv',index_col='Words')
        if self.oname == 'Ascending':
            print('Top 10 Fewer Words with {} Sorting Algorithm from {} MB with {} word counter sets'.format(self.sortingname,num,len(list(bdict.items()))))
        elif self.oname == 'Descending':
            print('Top 10 Most Common Words with {} Sorting Algorithm from {} MB with {} word counter sets'.format(self.sortingname,num,len(list(bdict.items()))))
        print(df)

    #write and read csv file with average time complexity function
    def WriteandRead_CSV(self,filename,adict,bdict,cdict,loop,oname):
        with open('Data_Sets\\'+filename+'Sort.csv','w') as MultiFile:
            fieldnames=['File Size (MB)','Different Words','Running Time (ms)','Theoretical Average Complexity']
            writer=csv.DictWriter(MultiFile,fieldnames)
            writer.writeheader()
            for i in range(0,loop):
                if self.array2dmode:
                    writer.writerow({'File Size (MB)':i+1,'Word Counter Sets':len(adict[i+1]),'Running Time (ms)':bdict[i+1],'Theoretical Average Complexity':cdict[i+1]})
                else:
                    writer.writerow({'File Size (MB)':i+1,'Different Words':len(adict[i+1]),'Running Time (ms)':bdict[i+1],'Theoretical Average Complexity':cdict[i+1]})
        MultiFile.close()
        df = pd.read_csv('Data_Sets\\'+filename+'Sort.csv',index_col='File Size (MB)')
        if self.array2dmode:
            print('{} Sort Algorithm By Word Counter Sets in {} order'.format(filename,oname))
        else:
            print('{} Sort Algorithm By Words in {} order'.format(filename,oname))
        print(df)

    #write and read csv file without average time complexity function
    def WriteandRead_CSV_NoComp(self,filename,adict,bdict,loop,oname):
        with open('Data_Sets\\'+filename+'Sort.csv','w') as MultiFile:

            fieldnames=['File Size (MB)','Different Words','Running Time (ms)']
            writer=csv.DictWriter(MultiFile,fieldnames)
            writer.writeheader()
            for i in range(0,loop):
                if self.array2dmode:
                    writer.writerow({'File Size (MB)':i+1,'Word Counter Sets':len(adict[i+1]),'Running Time (ms)':bdict[i+1]})
                else:
                    writer.writerow({'File Size (MB)':i+1,'Different Words':len(adict[i+1]),'Running Time (ms)':bdict[i+1]})
        MultiFile.close()
        df = pd.read_csv('Data_Sets\\'+filename+'Sort.csv',index_col='File Size (MB)')
        if self.array2dmode:
            print('{} Sort Algorithm By Word Counter Sets in {} order'.format(filename,oname))
        else:
            print('{} Sort Algorithm By Words in {} order'.format(filename,oname))
        print(df)

    #sorted word counter plot function
    def PlottingSorting(self,Filename,oname):


        x,y=zip(*self.TopWords.items())#get x and y from dictionary list
        plt.plot(x,y,label='Words')
        plt.plot(x,y,'o')
        if oname == 'Ascending':
            plt.title('10 Fewest Words with {} Sorting Algorithm\nfrom {} MB with {} word counter sets'.format(self.sortingname,Filename,len(list(self.words.items()))))
        elif oname == 'Descending':
            plt.title('10 Most Common Words with {} Sorting Algorithm\nfrom {} MB with {} word counter sets'.format(self.sortingname,Filename,len(list(self.words.items()))))
        plt.xlabel('Words')
        plt.ylabel('Counting')
        plt.legend()
        df = pd.DataFrame(self.TopWords.items(),columns=['Words','Counting'])#get data for histogram
        df.plot.bar(x='Words',y='Counting',rot=0)
        if oname == 'Ascending':
            plt.title('10 Fewest Words with {} Sorting Algorithm\nfrom {} MB with {} word counter sets'.format(self.sortingname,Filename,len(list(self.words.items()))))
        elif oname == 'Descending':
            plt.title('10 Most Common Words with {} Sorting Algorithm\nfrom {} MB with {} word counter sets'.format(self.sortingname,Filename,len(list(self.words.items()))))
        plt.xlabel('Words')
        plt.ylabel('Counting')
        plt.show()
        plt.close()

    #multiple size files plot function
    def PlottingFile(self,name,oname):
        x1,y1=zip(*self.FileDict.items())#get x and y from dictionary list
        x2,y2=zip(*self.CompDict.items())#get x and y from dictionary list
        plt.plot(x1,y1,label=name+' Sort')
        plt.plot(x1,y1,'o')
        plt.plot(x2,y2,label=name+' Sort Complexity')
        plt.plot(x2,y2,'o')
        plt.title('{} Sort Algorithm By Words in {} order'.format(name,oname))
        plt.xlabel('Sizes (MB)')
        plt.ylabel('Running Times (ms)')
        plt.legend()

        df = pd.DataFrame({'Actual':list(self.FileDict.values()),'Theoretical':list(self.CompDict.values())},index=self.EbookList)#get data for histogram
        df.plot.bar(rot=0)
        plt.title('{} Sort Algorithm By Words in {} order'.format(name,oname))
        plt.xlabel('Sizes (MB)')
        plt.ylabel('Running Times (ms)')
        plt.show()
        plt.close()

    #multiple size files with all sorting methods plot function
    def PlottingFile_AllSorts(self,oname):
        x1,y1=zip(*self.MergeDict.items())#get x and y from dictionary list
        x2,y2=zip(*self.ShellDict.items())#get x and y from dictionary list
        x3,y3=zip(*self.HeapDict.items())#get x and y from dictionary list
        x4,y4=zip(*self.QuickDict.items())#get x and y from dictionary list
        plt.plot(x1,y1,label='Merge Sort')
        plt.plot(x1,y1,'o')
        plt.plot(x2,y2,label='Shell Sort')
        plt.plot(x2,y2,'o')
        plt.plot(x3,y3,label='Heap Sort')
        plt.plot(x3,y3,'o')
        plt.plot(x4,y4,label='Quick Sort')
        plt.plot(x4,y4,'o')
        plt.title('Sorting Algorithms By Words in {} order'.format(oname))
        plt.xlabel('Sizes (MB)')
        plt.ylabel('Running Times (ms)')
        plt.legend()

        df = pd.DataFrame({'Merge':list(self.MergeDict.values()),'Shell':list(self.ShellDict.values()),'Heap':list(self.HeapDict.values()),
                           'Quick':list(self.QuickDict.values())},
                          index=self.EbookList)#get data for histogram
        df.plot.bar(rot=0)
        plt.title('Sorting Algorithm By Words in {} order'.format(oname))
        plt.xlabel('Sizes (MB)')
        plt.ylabel('Running Times (ms)')
        plt.show()

        plt.show()
        plt.close()

    #reset all settings function
    def ResetAll(self):
        self.words.clear()
        self.TimeList.clear()
        self.EbookList.clear()
        self.EbookDict.clear()
        self.FileDict.clear()
        self.CompDict.clear()
        self.MergeEbook.clear()
        self.MergeDict.clear()
        self.ShellEbook.clear()
        self.ShellDict.clear()
        self.HeapEbook.clear()
        self.HeapDict.clear()
        self.QuickEbook.clear()
        self.QuickDict.clear()
        self.TopWords.clear()
        self.sortingname=''
        self.oname=''
        self.OrderFlag=False
        self.OF_Num=1
        self.MF_Num=3
        self.MF_Steps=1
        self.Book_KB=0
        self.array2dmode=True

    #book size rendering after ebook being clicked function (One File Case)
    def OF_KBRendering(self,B,success,error):
        if self.Book_KB < self.OF_Num*1024:
            if not B.Passed:
                self.Book_KB += int(B.kb_text)
                self.NameList.append(B.book)
                B.Passed = True
                B.Update()
            else:
                error.DrawText()
                pg.display.flip()
                pg.time.wait(1000)
        if self.Book_KB >= self.OF_Num*1024:
            self.OF_CreateSizeFile(self.OF_Num)
            success.DrawText()
            pg.display.flip()
            pg.time.wait(1000)
            self.setting_panel = 'OneFileType'

    #book size rendering after ebook being clicked function (Multiple Files Case)
    def MF_KBRendering(self,B,success,error):
        if self.Book_KB >= self.MF_Steps*1024 and self.MF_Steps < self.MF_Num:

            self.OF_CreateSizeFile(self.MF_Steps)
            self.NameList.append(str(self.MF_Steps))
            self.MF_Steps += 1

        if self.Book_KB < self.MF_Steps*1024:
            if not B.Passed:
                self.Book_KB += int(B.kb_text)
                self.NameList.append(B.book)
                B.Passed = True
                B.Update()
            else:
                error.DrawText()
                pg.display.flip()
                pg.time.wait(1000)

        if self.Book_KB >= self.MF_Num*1024:
            self.OF_CreateSizeFile(self.MF_Steps)
            success.DrawText()
            pg.display.flip()
            pg.time.wait(1000)
            self.setting_panel = 'MultiFileType'

    #create specific MB size file function
    def OF_CreateSizeFile(self,size):
        for name in self.NameList:
            file=open('Data_Sets\\'+name+'.txt','r')
            for line in file.read().split('\n'):
                self.LineList.append(line)
            file.close()
        newfile=open('Data_Sets\\'+str(size)+'.txt','w')
        for line in self.LineList:
            newfile.write(line+'\n')
        newfile.close()
        self.NameList.clear()
        self.LineList.clear()

    #clear terminal output function
    def clear(self):
        sleep(5)
        system('cls')
        #print('\n'*50)

    #Multiple Files Sorting result function
    def MF_SortEachFiles(self,loop):
        #Every lists get initial values
        for i in range(0,loop):
            FilenameIn=i+1
            self.FileDict[FilenameIn]=0
            self.CompDict[FilenameIn]=0
            self.MergeDict[FilenameIn]=0
            self.ShellDict[FilenameIn]=0
            self.HeapDict[FilenameIn]=0
            self.QuickDict[FilenameIn]=0
            self.EbookList.append(FilenameIn)
            self.EbookDict[FilenameIn]=[]
            self.MergeEbook[FilenameIn]=[]
            self.ShellEbook[FilenameIn]=[]
            self.HeapEbook[FilenameIn]=[]
            self.QuickEbook[FilenameIn]=[]

        #Every lists get its own values from files
        for book in self.EbookList:
            self.EbookDict[int(book)]=self.Load_Ebook_Into_Lists(str(book))
            self.MergeEbook[int(book)]=self.Load_Ebook_Into_Lists(str(book))
            self.ShellEbook[int(book)]=self.Load_Ebook_Into_Lists(str(book))
            self.HeapEbook[int(book)]=self.Load_Ebook_Into_Lists(str(book))
            self.QuickEbook[int(book)]=self.Load_Ebook_Into_Lists(str(book))

        #Merge sort with average time complexity
        if self.sortingname == 'Merge':
            for key,value in self.EbookDict.items():
                Elapsed=self.Measure_Mergesort(value,self.OrderFlag)
                self.FileDict[key]=Elapsed.microseconds
                self.CompDict[key]=self.MQH_AvgComplexity(value)
                print('Merge Sort Processing.... on File {} MB'.format(key))

            #Show output in terminal and plotting
            self.WriteandRead_CSV('Merge',self.EbookDict,self.FileDict,self.CompDict,loop,self.oname)
            self.PlottingFile(self.sortingname,self.oname)

        #Quick sort with average time complexity
        elif self.sortingname == 'Shell':
            for key,value in self.EbookDict.items():
                Elapsed=self.Measure_Shellsort(value,self.OrderFlag)
                self.FileDict[key]=Elapsed.microseconds
                self.CompDict[key]=self.S_AvgComplexity(value)
                print('Shell Sort Processing.... on File {} MB'.format(key))

            #Show output in terminal and plotting
            self.WriteandRead_CSV('Shell',self.EbookDict,self.FileDict,self.CompDict,loop,self.oname)
            self.PlottingFile(self.sortingname,self.oname)

        #Heap sort with average time complexity
        elif self.sortingname == 'Heap':
            for key,value in self.EbookDict.items():
                Elapsed=self.Measure_Heapsort(value,self.OrderFlag)
                self.FileDict[key]=Elapsed.microseconds
                self.CompDict[key]=self.MQH_AvgComplexity(value)
                print('Heap Sort Processing.... on File {} MB'.format(key))

            #Show output in terminal and plotting
            self.WriteandRead_CSV('Heap',self.EbookDict,self.FileDict,self.CompDict,loop,self.oname)
            self.PlottingFile(self.sortingname,self.oname)

        #Quick sort with average time complexity
        elif self.sortingname == 'Quick':
            for key,value in self.EbookDict.items():
                Elapsed=self.Measure_Quicksort(value,0,len(value)-1,self.OrderFlag)
                self.FileDict[key]=Elapsed.microseconds
                self.CompDict[key]=self.MQH_AvgComplexity(value)
                print('Quick Sort Processing.... on File {} MB'.format(key))

            #Show output in terminal and plotting
            self.WriteandRead_CSV('Quick',self.EbookDict,self.FileDict,self.CompDict,loop,self.oname)
            self.PlottingFile(self.sortingname,self.oname)

        #All sorting methods without average time complexity
        elif self.sortingname == '':
            for key,value in self.QuickEbook.items():
                Elapsed=self.Measure_Quicksort(value,0,len(value)-1,self.OrderFlag)
                self.QuickDict[key]=Elapsed.microseconds
                print('Quick Sort Processing.... on File {} MB'.format(key))

            for key,value in self.MergeEbook.items():
                Elapsed=self.Measure_Mergesort(value,self.OrderFlag)
                self.MergeDict[key]=Elapsed.microseconds
                print('Merge Sort Processing.... on File {} MB'.format(key))

            for key,value in self.ShellEbook.items():
                Elapsed=self.Measure_Shellsort(value,self.OrderFlag)
                self.ShellDict[key]=Elapsed.microseconds
                print('Shell Sort Processing.... on File {} MB'.format(key))

            for key,value in self.HeapEbook.items():
                Elapsed=self.Measure_Heapsort(value,self.OrderFlag)
                self.HeapDict[key]=Elapsed.microseconds
                print('Heap Sort Processing.... on File {} MB'.format(key))

            #Show output in terminal and plotting
            self.WriteandRead_CSV_NoComp('Merge',self.MergeEbook,self.MergeDict,loop,self.oname)
            self.WriteandRead_CSV_NoComp('Quick',self.QuickEbook,self.QuickDict,loop,self.oname)
            self.WriteandRead_CSV_NoComp('Heap',self.HeapEbook,self.HeapDict,loop,self.oname)
            self.WriteandRead_CSV_NoComp('Shell',self.ShellEbook,self.ShellDict,loop,self.oname)

            self.PlottingFile_AllSorts(self.oname)
        self.clear()#clear terminal output

    #One File Sorting result function
    def OF_SortEachLists(self):
        #Get datas from specific MB size file into word counter dictionary list
        self.Load_Ebook(str(self.OF_Num))

        WordArr=self.Add_WordCounter()#Get word counter sets

        #Merge sort on Word Counter
        if self.sortingname == 'Merge':
            Elapsed=self.Measure_2DMergesort(WordArr,self.OrderFlag,1)
            for i in range(0,10):
                self.TopWords[WordArr[i][0]]=WordArr[i][1]
            self.WriteandRead_WordCounter(self.TopWords,self.words,self.OF_Num)
            print('\nElapsed Time: ',Elapsed.microseconds,' ms')
            self.PlottingSorting(self.OF_Num,self.oname)
        #Quick sort on Word Counter
        elif self.sortingname == 'Shell':
            Elapsed=self.Measure_2DShellsort(WordArr,self.OrderFlag,1)
            for i in range(0,10):
                self.TopWords[WordArr[i][0]]=WordArr[i][1]
            self.WriteandRead_WordCounter(self.TopWords,self.words,self.OF_Num)
            print('\nElapsed Time: ',Elapsed.microseconds,' ms')
            self.PlottingSorting(self.OF_Num,self.oname)
        #Heap sort on Word Counter
        elif self.sortingname == 'Heap':
            Elapsed=self.Measure_2DHeapsort(WordArr,self.OrderFlag,1)
            for i in range(0,10):
                self.TopWords[WordArr[i][0]]=WordArr[i][1]
            self.WriteandRead_WordCounter(self.TopWords,self.words,self.OF_Num)
            print('\nElapsed Time: ',Elapsed.microseconds,' ms')
            self.PlottingSorting(self.OF_Num,self.oname)
        #Quick sort on Word Counter
        elif self.sortingname == 'Quick':
            Elapsed=self.Measure_2DQuicksort(WordArr,0,len(WordArr)-1,self.OrderFlag,1)
            for i in range(0,10):
                self.TopWords[WordArr[i][0]]=WordArr[i][1]
            self.WriteandRead_WordCounter(self.TopWords,self.words,self.OF_Num)
            print('\nElapsed Time: ',Elapsed.microseconds,' ms')
            self.PlottingSorting(self.OF_Num,self.oname)

        self.clear()#clear terminal output

    #Main Program function
    def MainRun(self):

        pg.init()#initialize pygame

        BG=BackGround()#call Background screen object
        screen=pg.display.set_mode((BG.width,BG.height))#Set width and height of screen
        pg.display.set_caption('E-Book Words Sorting')#Set caption of screen

        #Create Text and Buttons for menu interface
        OneFile=Button(screen,300,200,250,60,'Word Counter')
        MultiFile=Button(screen,300,270,300,60,'Sort Comparison')
        title=Text(60,'E-Book Words Sorting',(227,220,0),BG.color,425,100,screen)

        #Create Texts and Buttons for Specific Size of One File interface
        OF_SizeIncrement=Button(screen,550,200,50,60,'+')
        OF_SizeDecrement=Button(screen,150,200,50,60,'-')
        OF_SizeNum=Text(60,str(self.OF_Num),(227,220,0),BG.color,375,230,screen)
        OF_Next=Button(screen,330,400,110,60,'Next')
        OF_choice=Text(30,'Choose Size of File',(227,220,0),BG.color,375,100,screen)

        #Create Texts and Buttons for Numbers of File interface
        MF_SizeIncrement=Button(screen,550,200,50,60,'+')
        MF_SizeDecrement=Button(screen,150,200,50,60,'-')
        MF_SizeNum=Text(60,str(self.MF_Num),(227,220,0),BG.color,375,230,screen)
        MF_Next=Button(screen,330,400,110,60,'Next')
        MF_choice=Text(30,'Choose Number of Files',(227,220,0),BG.color,375,100,screen)

        #Create Texts for E-Book choices on One File interface
        OFFile_Text=Text(30,'File:',(227,220,0),BG.color,325,25,screen)
        OFMB_Text=Text(30,'MB',(227,220,0),BG.color,475,25,screen)
        OFNum_Text=Text(30,str(self.OF_Num),(227,220,0),BG.color,400,25,screen)
        OFtotal_text=Text(20,'Total KB:',(227,220,0),BG.color,325,60,screen)
        OFKBNum_Text=Text(20,str(self.Book_KB),(227,220,0),BG.color,400,60,screen)
        OFKB_text=Text(20,'KB',(227,220,0),BG.color,475,60,screen)

        #Create Texts for E-Book choices on Multiple Files interface
        MFFile_Text=Text(30,'File:',(227,220,0),BG.color,325,25,screen)
        MFMB_Text=Text(30,'MB',(227,220,0),BG.color,475,25,screen)
        MFNum_Text=Text(30,str(self.MF_Steps),(227,220,0),BG.color,400,25,screen)
        MFtotal_text=Text(20,'Total KB:',(227,220,0),BG.color,325,60,screen)
        MFKBNum_Text=Text(20,str(self.Book_KB),(227,220,0),BG.color,400,60,screen)
        MFKB_text=Text(20,'KB',(227,220,0),BG.color,475,60,screen)

        #Create List of E-books for E-book choice on both One File and Multiple Files interface
        B1=Book(50,150,screen,'1',self.LibraryDict)
        B2=Book(120,150,screen,'2',self.LibraryDict)
        B3=Book(190,150,screen,'3',self.LibraryDict)
        B4=Book(260,150,screen,'4',self.LibraryDict)
        B5=Book(330,150,screen,'5',self.LibraryDict)
        B6=Book(400,150,screen,'6',self.LibraryDict)
        B7=Book(470,150,screen,'7',self.LibraryDict)
        B8=Book(540,150,screen,'8',self.LibraryDict)
        B9=Book(610,150,screen,'9',self.LibraryDict)
        B10=Book(680,150,screen,'10',self.LibraryDict)
        B11=Book(50,250,screen,'11',self.LibraryDict)
        B12=Book(120,250,screen,'12',self.LibraryDict)
        B13=Book(190,250,screen,'13',self.LibraryDict)
        B14=Book(260,250,screen,'14',self.LibraryDict)
        B15=Book(330,250,screen,'15',self.LibraryDict)
        B16=Book(400,250,screen,'16',self.LibraryDict)
        B17=Book(470,250,screen,'17',self.LibraryDict)
        B18=Book(540,250,screen,'18',self.LibraryDict)
        B19=Book(610,250,screen,'19',self.LibraryDict)
        B20=Book(680,250,screen,'20',self.LibraryDict)
        B21=Book(50,350,screen,'21',self.LibraryDict)
        B22=Book(120,350,screen,'22',self.LibraryDict)
        B23=Book(190,350,screen,'23',self.LibraryDict)
        B24=Book(260,350,screen,'24',self.LibraryDict)
        B25=Book(330,350,screen,'25',self.LibraryDict)
        B26=Book(400,350,screen,'26',self.LibraryDict)
        B27=Book(470,350,screen,'27',self.LibraryDict)
        B28=Book(540,350,screen,'28',self.LibraryDict)
        B29=Book(610,350,screen,'29',self.LibraryDict)
        B30=Book(680,350,screen,'30',self.LibraryDict)
        bookchoice=Text(30,'Choose Books',(227,220,0),BG.color,375,100,screen)
        BList=[B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,B15,B16,B17,B18,B19,B20,B21,B22,B23,B24,B25,B26,B27,B28,B29,B30]

        #Create text notifications for E-book choice on both One File and Multiple Files interface
        success=Text(30,'Successful!',(255,0,0),BG.color,425,BG.height-150,screen)
        Passedtext=Text(30,'It is already added',(255,0,0),BG.color,425,BG.height-150,screen)

        #Create text notifications for Result interface
        BackError=Text(30,'Click Show button first',(255,0,0),BG.color,425,BG.height-150,screen)
        ShowError=Text(30,'You cannot click this button again',(255,0,0),BG.color,425,BG.height-150,screen)

        #Create Text and Buttons for Multiple Files type,order, and sorting name choice interface
        MWordAscend=Button(screen,0,100,260,60,'Merge Asc')
        MWordDescend=Button(screen,0,180,260,60,'Merge Desc')
        SWordAscend=Button(screen,265,100,260,60,'Shell Asc')
        SWordDescend=Button(screen,265,180,260,60,'Shell Desc')
        HWordAscend=Button(screen,530,100,260,60,'Heap Asc')
        HWordDescend=Button(screen,530,180,260,60,'Heap Desc')
        QWordAscend=Button(screen,200,260,260,60,'Quick Asc')
        QWordDescend=Button(screen,470,260,260,60,'Quick Desc')
        AWordAscend=Button(screen,200,340,250,60,'All Asc')
        AWordDescend=Button(screen,470,340,250,60,'All Desc')
        SOchoice=Text(30,'Choose Sorting Name and Order',(255,255,255),BG.color,400,50,screen)

        #Create Texts and Buttons for Result interface
        Result=Text(30,'Result is showed in Terminal and Plotting',(255,255,255),BG.color,400,100,screen)
        Clicking=Text(30,'by clicking Show button',(255,255,255),BG.color,400,150,screen)
        Back=Button(screen,325,BG.height-100,130,60,'Back')
        Show=Button(screen,325,BG.height-300,130,60,'Show')

        #Main looping
        while True:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()#quit program after clicking close window button
                if event.type == pg.MOUSEBUTTONDOWN:

                    mouse_x,mouse_y=pg.mouse.get_pos()#get position of mouse
                    #Collide position of buttons with position of mouse
                    OF_onclick = OneFile.rect.collidepoint(mouse_x,mouse_y)
                    MF_onclick = MultiFile.rect.collidepoint(mouse_x,mouse_y)

                    OF_SIonclick= OF_SizeIncrement.rect.collidepoint(mouse_x,mouse_y)
                    OF_SDonclick=OF_SizeDecrement.rect.collidepoint(mouse_x,mouse_y)
                    OF_SNonclick=OF_Next.rect.collidepoint(mouse_x,mouse_y)
                    MF_SIonclick=MF_SizeIncrement.rect.collidepoint(mouse_x,mouse_y)
                    MF_SDonclick=MF_SizeDecrement.rect.collidepoint(mouse_x,mouse_y)
                    MF_SNonclick=MF_Next.rect.collidepoint(mouse_x,mouse_y)

                    B1_onclick=B1.rect.collidepoint(mouse_x,mouse_y)
                    B2_onclick=B2.rect.collidepoint(mouse_x,mouse_y)
                    B3_onclick=B3.rect.collidepoint(mouse_x,mouse_y)
                    B4_onclick=B4.rect.collidepoint(mouse_x,mouse_y)
                    B5_onclick=B5.rect.collidepoint(mouse_x,mouse_y)
                    B6_onclick=B6.rect.collidepoint(mouse_x,mouse_y)
                    B7_onclick=B7.rect.collidepoint(mouse_x,mouse_y)
                    B8_onclick=B8.rect.collidepoint(mouse_x,mouse_y)
                    B9_onclick=B9.rect.collidepoint(mouse_x,mouse_y)
                    B10_onclick=B10.rect.collidepoint(mouse_x,mouse_y)
                    B11_onclick=B11.rect.collidepoint(mouse_x,mouse_y)
                    B12_onclick=B12.rect.collidepoint(mouse_x,mouse_y)
                    B13_onclick=B13.rect.collidepoint(mouse_x,mouse_y)
                    B14_onclick=B14.rect.collidepoint(mouse_x,mouse_y)
                    B15_onclick=B15.rect.collidepoint(mouse_x,mouse_y)
                    B16_onclick=B16.rect.collidepoint(mouse_x,mouse_y)
                    B17_onclick=B17.rect.collidepoint(mouse_x,mouse_y)
                    B18_onclick=B18.rect.collidepoint(mouse_x,mouse_y)
                    B19_onclick=B19.rect.collidepoint(mouse_x,mouse_y)
                    B20_onclick=B20.rect.collidepoint(mouse_x,mouse_y)
                    B21_onclick=B21.rect.collidepoint(mouse_x,mouse_y)
                    B22_onclick=B22.rect.collidepoint(mouse_x,mouse_y)
                    B23_onclick=B23.rect.collidepoint(mouse_x,mouse_y)
                    B24_onclick=B24.rect.collidepoint(mouse_x,mouse_y)
                    B25_onclick=B25.rect.collidepoint(mouse_x,mouse_y)
                    B26_onclick=B26.rect.collidepoint(mouse_x,mouse_y)
                    B27_onclick=B27.rect.collidepoint(mouse_x,mouse_y)
                    B28_onclick=B28.rect.collidepoint(mouse_x,mouse_y)
                    B29_onclick=B29.rect.collidepoint(mouse_x,mouse_y)
                    B30_onclick=B30.rect.collidepoint(mouse_x,mouse_y)

                    MWA_onclick=MWordAscend.rect.collidepoint(mouse_x,mouse_y)
                    MWD_onclick=MWordDescend.rect.collidepoint(mouse_x,mouse_y)
                    SWA_onclick=SWordAscend.rect.collidepoint(mouse_x,mouse_y)
                    SWD_onclick=SWordDescend.rect.collidepoint(mouse_x,mouse_y)
                    HWA_onclick=HWordAscend.rect.collidepoint(mouse_x,mouse_y)
                    HWD_onclick=HWordDescend.rect.collidepoint(mouse_x,mouse_y)
                    QWA_onclick=QWordAscend.rect.collidepoint(mouse_x,mouse_y)
                    QWD_onclick=QWordDescend.rect.collidepoint(mouse_x,mouse_y)
                    AWA_onclick=AWordAscend.rect.collidepoint(mouse_x,mouse_y)
                    AWD_onclick=AWordDescend.rect.collidepoint(mouse_x,mouse_y)

                    Back_onclick=Back.rect.collidepoint(mouse_x,mouse_y)
                    Show_onclick=Show.rect.collidepoint(mouse_x,mouse_y)

                    #Menu interface
                    if OF_onclick and self.setting_panel == 'menu':
                        self.array2dmode = True
                        self.setting_panel = 'OneFileSize'
                    elif MF_onclick and self.setting_panel == 'menu':
                        self.array2dmode = False
                        self.setting_panel = 'MultiFileSize'

                    #Input Maximum size of one file interface
                    elif OF_SIonclick and self.setting_panel == 'OneFileSize':
                        self.OF_Num += 1
                        OF_SizeNum.name=str(self.OF_Num)
                        OF_SizeNum.Update()
                    elif OF_SDonclick and self.setting_panel == 'OneFileSize':
                        if self.OF_Num > 1:
                            self.OF_Num -= 1
                            OF_SizeNum.name=str(self.OF_Num)
                            OF_SizeNum.Update()
                    elif OF_SNonclick and self.setting_panel == 'OneFileSize':
                        self.setting_panel = 'OneFileBook'
                        OFNum_Text.name=str(self.OF_Num)
                        OFNum_Text.Update()
                    #Input Numbers of File interface
                    elif MF_SIonclick and self.setting_panel == 'MultiFileSize':
                        self.MF_Num += 1
                        MF_SizeNum.name=str(self.MF_Num)
                        MF_SizeNum.Update()
                    elif MF_SDonclick and self.setting_panel == 'MultiFileSize':
                        if self.MF_Num > 3:
                            self.MF_Num -= 1
                            MF_SizeNum.name=str(self.MF_Num)
                            MF_SizeNum.Update()
                    elif MF_SNonclick and self.setting_panel == 'MultiFileSize':
                        self.setting_panel = 'MultiFileBook'

                    #E-Book choice interface for multiple files
                    elif B1_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B1,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B2_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B2,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B3_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B3,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B4_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B4,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B5_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B5,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B6_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B6,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B7_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B7,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B8_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B8,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B9_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B9,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B10_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B10,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B11_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B11,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B12_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B12,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B13_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B13,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B14_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B14,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B15_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B15,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B16_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B16,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B17_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B17,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B18_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B18,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B19_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B19,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B20_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B20,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B21_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B21,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B22_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B22,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B23_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B23,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B24_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B24,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B25_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B25,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B26_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B26,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B27_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B27,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B28_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B28,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B29_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B29,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    elif B30_onclick and self.setting_panel == 'MultiFileBook':
                        self.MF_KBRendering(B30,success,Passedtext)
                        MFKBNum_Text.name = str(self.Book_KB)
                        MFKBNum_Text.Update()
                        MFNum_Text.name = str(self.MF_Steps)
                        MFNum_Text.Update()
                    #E-Book choice interface for one file
                    elif B1_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B1,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B2_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B2,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B3_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B3,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B4_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B4,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B5_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B5,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B6_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B6,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B7_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B7,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B8_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B8,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B9_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B9,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B10_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B10,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B11_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B11,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B12_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B12,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B13_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B13,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B14_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B14,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B15_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B15,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B16_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B16,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B17_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B17,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B18_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B18,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B19_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B19,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B20_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B20,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B21_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B21,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B22_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B22,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B23_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B23,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B24_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B24,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B25_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B25,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B26_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B26,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B27_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B27,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B28_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B28,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B29_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B29,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()
                    elif B30_onclick and self.setting_panel == 'OneFileBook':
                        self.OF_KBRendering(B30,success,Passedtext)
                        OFKBNum_Text.name = str(self.Book_KB)
                        OFKBNum_Text.Update()

                    #sorting name and order choice interface
                    elif MWA_onclick and self.setting_panel == 'OneFileType':
                        self.oname = 'Ascending'
                        self.OrderFlag=False
                        self.sortingname='Merge'
                        self.setting_panel = 'OneFileResult'
                    elif MWD_onclick and self.setting_panel == 'OneFileType':
                        self.oname = 'Descending'
                        self.OrderFlag = True
                        self.sortingname='Merge'
                        self.setting_panel = 'OneFileResult'
                    elif SWA_onclick and self.setting_panel == 'OneFileType':
                        self.oname = 'Ascending'
                        self.OrderFlag=False
                        self.sortingname='Shell'
                        self.setting_panel = 'OneFileResult'
                    elif SWD_onclick and self.setting_panel == 'OneFileType':
                        self.oname = 'Descending'
                        self.OrderFlag = True
                        self.sortingname='Shell'
                        self.setting_panel = 'OneFileResult'
                    elif HWA_onclick and self.setting_panel == 'OneFileType':
                        self.oname = 'Ascending'
                        self.OrderFlag=False
                        self.sortingname='Heap'
                        self.setting_panel = 'OneFileResult'
                    elif HWD_onclick and self.setting_panel == 'OneFileType':
                        self.oname = 'Descending'
                        self.OrderFlag = True
                        self.sortingname='Heap'
                        self.setting_panel = 'OneFileResult'
                    elif QWA_onclick and self.setting_panel == 'OneFileType':
                        self.oname = 'Ascending'
                        self.OrderFlag=False
                        self.sortingname='Quick'
                        self.setting_panel = 'OneFileResult'
                    elif QWD_onclick and self.setting_panel == 'OneFileType':
                        self.oname = 'Descending'
                        self.OrderFlag = True
                        self.sortingname='Quick'
                        self.setting_panel = 'OneFileResult'

                    #sorting name and order choice interface
                    elif MWA_onclick and self.setting_panel == 'MultiFileType':
                        self.oname = 'Ascending'
                        self.OrderFlag=False
                        self.sortingname='Merge'
                        self.setting_panel = 'MultiFileResult'
                    elif MWD_onclick and self.setting_panel == 'MultiFileType':
                        self.oname = 'Descending'
                        self.OrderFlag = True
                        self.sortingname='Merge'
                        self.setting_panel = 'MultiFileResult'
                    elif SWA_onclick and self.setting_panel == 'MultiFileType':
                        self.oname = 'Ascending'
                        self.OrderFlag=False
                        self.sortingname='Shell'
                        self.setting_panel = 'MultiFileResult'
                    elif SWD_onclick and self.setting_panel == 'MultiFileType':
                        self.oname = 'Descending'
                        self.OrderFlag = True
                        self.sortingname='Shell'
                        self.setting_panel = 'MultiFileResult'
                    elif HWA_onclick and self.setting_panel == 'MultiFileType':
                        self.oname = 'Ascending'
                        self.OrderFlag=False
                        self.sortingname='Heap'
                        self.setting_panel = 'MultiFileResult'
                    elif HWD_onclick and self.setting_panel == 'MultiFileType':
                        self.oname = 'Descending'
                        self.OrderFlag = True
                        self.sortingname='Heap'
                        self.setting_panel = 'MultiFileResult'
                    elif QWA_onclick and self.setting_panel == 'MultiFileType':
                        self.oname = 'Ascending'
                        self.OrderFlag=False
                        self.sortingname='Quick'
                        self.setting_panel = 'MultiFileResult'
                    elif QWD_onclick and self.setting_panel == 'MultiFileType':
                        self.oname = 'Descending'
                        self.OrderFlag = True
                        self.sortingname='Quick'
                        self.setting_panel = 'MultiFileResult'
                    elif AWA_onclick and self.setting_panel == 'MultiFileType':
                        self.oname = 'Ascending'
                        self.OrderFlag=False
                        self.sortingname=''
                        self.setting_panel = 'MultiFileResult'
                    elif AWD_onclick and self.setting_panel == 'MultiFileType':
                        self.oname = 'Descending'
                        self.OrderFlag = True
                        self.sortingname=''
                        self.setting_panel = 'MultiFileResult'

                    #Result interface
                    elif Back_onclick and self.setting_panel == 'OneFileResult':
                        if self.backtrigger:
                            self.setting_panel = 'menu'
                            self.ResetAll()
                            OF_SizeNum.name=str(self.OF_Num)
                            OF_SizeNum.Update()
                            MF_SizeNum.name=str(self.MF_Num)
                            MF_SizeNum.Update()
                            OFNum_Text.name=str(self.OF_Num)
                            OFNum_Text.Update()
                            MFNum_Text.name=str(self.MF_Steps)
                            MFNum_Text.Update()
                            OFKBNum_Text.name=str(self.Book_KB)
                            OFKBNum_Text.Update()
                            MFKBNum_Text.name=str(self.Book_KB)
                            MFKBNum_Text.Update()
                            for i in BList:
                                i.Passed=False
                                i.Update()
                            self.backtrigger = False
                        else:
                            BackError.DrawText()
                            pg.display.flip()
                            pg.time.wait(1000)
                    elif Show_onclick and self.setting_panel == 'OneFileResult':
                        if not self.backtrigger:
                            self.OF_SortEachLists()
                            self.backtrigger = True
                        else:
                            ShowError.DrawText()
                            pg.display.flip()
                            pg.time.wait(1000)

                    elif Back_onclick and self.setting_panel == 'MultiFileResult':
                        if self.backtrigger:
                            self.setting_panel = 'menu'
                            self.ResetAll()
                            OF_SizeNum.name=str(self.OF_Num)
                            OF_SizeNum.Update()
                            MF_SizeNum.name=str(self.MF_Num)
                            MF_SizeNum.Update()
                            OFNum_Text.name=str(self.OF_Num)
                            OFNum_Text.Update()
                            MFNum_Text.name=str(self.MF_Steps)
                            MFNum_Text.Update()
                            OFKBNum_Text.name=str(self.Book_KB)
                            OFKBNum_Text.Update()
                            MFKBNum_Text.name=str(self.Book_KB)
                            MFKBNum_Text.Update()
                            for i in BList:
                                i.Passed=False
                                i.Update()
                            self.backtrigger = False
                        else:
                            BackError.DrawText()
                            pg.display.flip()
                            pg.time.wait(1000)
                    elif Show_onclick and self.setting_panel == 'MultiFileResult':
                        if not self.backtrigger:
                            self.MF_SortEachFiles(self.MF_Num)
                            self.backtrigger = True
                        else:
                            ShowError.DrawText()
                            pg.display.flip()
                            pg.time.wait(1000)

            #Interface panels
            if self.setting_panel == 'OneFileSize':
                screen.fill(BG.color)
                OF_SizeIncrement.draw_button()
                OF_SizeNum.DrawText()
                OF_SizeDecrement.draw_button()
                OF_Next.draw_button()
                OF_choice.DrawText()
            elif self.setting_panel == 'MultiFileSize':
                screen.fill(BG.color)
                MF_SizeIncrement.draw_button()
                MF_SizeNum.DrawText()
                MF_SizeDecrement.draw_button()
                MF_Next.draw_button()
                MF_choice.DrawText()
            elif self.setting_panel == 'menu':
                screen.fill(BG.color)
                title.DrawText()
                OneFile.draw_button()
                MultiFile.draw_button()
            elif self.setting_panel == 'OneFileBook':
                screen.fill(BG.color)
                bookchoice.DrawText()
                OFFile_Text.DrawText()
                OFNum_Text.DrawText()
                OFMB_Text.DrawText()
                OFtotal_text.DrawText()
                OFKBNum_Text.DrawText()
                OFKB_text.DrawText()
                for i in BList:
                    i.Draw()
            elif self.setting_panel == 'MultiFileBook':
                screen.fill(BG.color)
                bookchoice.DrawText()
                MFFile_Text.DrawText()
                MFNum_Text.DrawText()
                MFMB_Text.DrawText()
                MFtotal_text.DrawText()
                MFKBNum_Text.DrawText()
                MFKB_text.DrawText()
                for i in BList:
                    i.Draw()
            elif self.setting_panel == 'OneFileType':
                screen.fill(BG.color)
                SOchoice.DrawText()
                MWordAscend.draw_button()
                MWordDescend.draw_button()

                SWordAscend.draw_button()
                SWordDescend.draw_button()

                HWordAscend.draw_button()
                HWordDescend.draw_button()

                QWordAscend.draw_button()
                QWordDescend.draw_button()
            elif self.setting_panel == 'MultiFileType':
                screen.fill(BG.color)
                SOchoice.DrawText()
                MWordAscend.draw_button()
                MWordDescend.draw_button()

                SWordAscend.draw_button()
                SWordDescend.draw_button()

                HWordAscend.draw_button()
                HWordDescend.draw_button()

                QWordAscend.draw_button()
                QWordDescend.draw_button()

                AWordAscend.draw_button()
                AWordDescend.draw_button()

            elif self.setting_panel == 'OneFileResult':
                screen.fill(BG.color)
                Result.DrawText()
                Clicking.DrawText()
                Back.draw_button()
                Show.draw_button()

            elif self.setting_panel == 'MultiFileResult':
                screen.fill(BG.color)
                Clicking.DrawText()
                Result.DrawText()
                Back.draw_button()
                Show.draw_button()

            pg.display.flip()#blit anything based on interface panels
