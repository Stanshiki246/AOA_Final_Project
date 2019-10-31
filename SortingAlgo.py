"""
Name: Stanley Tantysco, Isabella, Alessandro, and Michael Stanley Chinaza
Sorting words from E-book
"""
#Sorting Method Class Object
class Sorting:
    #2D Merge function
    def Merge_2D(self,a,L,R,reversed,t):
        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            #checking whether order is ascending or descending
            if reversed:
                #sorting a set of data
                if L[i][t] > R[j][t]:
                    a[k] = L[i]
                    i+=1
                else:
                    a[k] = R[j]
                    j+=1
                k+=1
            else:
                #sorting a set of data
                if L[i][t] < R[j][t]:
                    a[k] = L[i]
                    i+=1
                else:
                    a[k] = R[j]
                    j+=1
                k+=1

        # Checking if any element was left
        while i < len(L):
            a[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            a[k] = R[j]
            j+=1
            k+=1

    #2D Merge Sort function
    def MergeSort_2D(self,a,reversed,t):
        if len(a) >1:
            mid = len(a)//2 #Finding the mid of the array
            L = a[:mid] # Dividing the array elements
            R = a[mid:] # into 2 halves

            self.MergeSort_2D(L,reversed,t) # Sorting the first half
            self.MergeSort_2D(R,reversed,t) # Sorting the second half

            self.Merge_2D(a,L,R,reversed,t)

    #2D Partition getter function
    def Partition_2D(self,a,low,high,reversed,t):
        pivot = a[low][t]
        i=low
        j=high

        while True:
            #checking whether order is ascending or descending
            if reversed:
                #sorting a set of data
                while a[i][t] > pivot:
                    i += 1
                while a[j][t] < pivot:
                    j -= 1
            else:
                #sorting a set of data
                while a[i][t] < pivot:
                    i += 1
                while a[j][t] > pivot:
                    j -= 1
            if i < j:
                a[i],a[j]=a[j],a[i]
                i += 1
                j -= 1
            else:
                return j
    #2D Quick Sort function
    def QuickSort_2D(self,a,low,high,reversed,t):
        if low < high:
            pi = self.Partition_2D(a,low,high,reversed,t)

            self.QuickSort_2D(a,low,pi,reversed,t)
            self.QuickSort_2D(a,pi+1,high,reversed,t)

    #2D Max Heap function
    def MaxHeap_2D(self,a,i,n,t):
        largest=i
        l=2*i+1
        r=2*i+2
        #sorting a set of data
        if l < n  and a[l][t] > a[largest][t]:
            largest = l
        else:
            largest = i
        #sorting a set of data
        if r < n and a[r][t] > a[largest][t]:
            largest = r

        if largest != i:
            a[i],a[largest]=a[largest],a[i]
            self.MaxHeap_2D(a,largest,n,t)

    #2D Min heap function
    def MinHeap_2D(self,a,i,n,t):
        smallest=i
        l=2*i+1
        r=2*i+2
        #sorting a set of data
        if l < n and a[l][t] < a[smallest][t]:
            smallest = l
        else:
            smallest = i
        #sorting a set of data
        if r < n and a[r][t] < a[smallest][t]:
            smallest = r

        if smallest != i:
            a[i],a[smallest]=a[smallest],a[i]
            self.MinHeap_2D(a,smallest,n,t)

    #2D Heap Sort function
    def HeapSort_2D(self,a,reversed,t):
        numoflist=len(a)

        for i in range(numoflist,-1,-1):
            #checking whether order is ascending or descending
            if reversed:
                self.MinHeap_2D(a,i,numoflist,t)
            else:
                self.MaxHeap_2D(a,i,numoflist,t)

        for i in range(numoflist-1,0,-1):
            #checking whether order is ascending or descending
            if reversed:
                a[i],a[0]=a[0],a[i]
                self.MinHeap_2D(a,0,i,t)
            else:
                a[i],a[0]=a[0],a[i]
                self.MaxHeap_2D(a,0,i,t)


    #2D Shell Sort function
    def Shell_Sort_2D(self,arr,reversed,t):
        n = len(arr)
        gap = n // 2

        while gap > 0:

            for i in range(gap,n):

                temp = arr[i]

                j=i
                #checking whether order is ascending or descending
                if reversed:
                    #sorting a set of data
                    while j >= gap and arr[j-gap][t] < temp[t]:
                        arr[j]=arr[j-gap]
                        j -= gap
                else:
                    #sorting a set of data
                    while j >= gap and arr[j-gap][t] > temp[t]:
                        arr[j] = arr[j-gap]
                        j -= gap

                arr[j] = temp

            gap //= 2
    #Merge function
    def Merge(self,a,L,R,reversed):
        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            #checking whether order is ascending or descending
            if reversed:
                #sorting data
                if L[i] > R[j]:
                    a[k] = L[i]
                    i+=1
                else:
                    a[k] = R[j]
                    j+=1
                k+=1
            else:
                #sorting data
                if L[i] < R[j]:
                    a[k] = L[i]
                    i+=1
                else:
                    a[k] = R[j]
                    j+=1
                k+=1

        # Checking if any element was left
        while i < len(L):
            a[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            a[k] = R[j]
            j+=1
            k+=1

    #Merge Sort function
    def MergeSort(self,a,reversed):
        if len(a) >1:
            mid = len(a)//2 #Finding the mid of the array
            L = a[:mid] # Dividing the array elements
            R = a[mid:] # into 2 halves

            self.MergeSort(L,reversed) # Sorting the first half
            self.MergeSort(R,reversed) # Sorting the second half

            self.Merge(a,L,R,reversed)

    #Partition getter function
    def Partition(self,a,low,high,reversed):
        pivot = a[low]
        i=low
        j=high

        while True:
            #checking whether order is ascending or descending
            if reversed:
                #sorting data
                while a[i] > pivot:
                    i += 1
                while a[j] < pivot:
                    j -= 1
            else:
                #sorting data
                while a[i] < pivot:
                    i += 1
                while a[j] > pivot:
                    j -= 1
            if i < j:
                a[i],a[j]=a[j],a[i]
                i += 1
                j -= 1
            else:
                return j
    #Quick Sort function
    def QuickSort(self,a,low,high,reversed):
        if low < high:
            pi = self.Partition(a,low,high,reversed)

            self.QuickSort(a,low,pi,reversed)
            self.QuickSort(a,pi+1,high,reversed)

    #Max Heap function
    def MaxHeap(self,a,i,n):
        largest=i
        l=2*i+1
        r=2*i+2
        #sorting data
        if l < n  and a[l] > a[largest]:
            largest = l
        else:
            largest = i
        #sorting data
        if r < n and a[r] > a[largest]:
            largest = r

        if largest != i:
            a[i],a[largest]=a[largest],a[i]
            self.MaxHeap(a,largest,n)

    #Min heap function
    def MinHeap(self,a,i,n):
        smallest=i
        l=2*i+1
        r=2*i+2
        #sorting data
        if l < n and a[l] < a[smallest]:
            smallest = l
        else:
            smallest = i
        #sorting data
        if r < n and a[r] < a[smallest]:
            smallest = r

        if smallest != i:
            a[i],a[smallest]=a[smallest],a[i]
            self.MinHeap(a,smallest,n)

    #Heap Sort function
    def HeapSort(self,a,reversed):
        numoflist=len(a)

        for i in range(numoflist,-1,-1):
            #checking whether order is ascending or descending
            if reversed:
                self.MinHeap(a,i,numoflist)
            else:
                self.MaxHeap(a,i,numoflist)

        for i in range(numoflist-1,0,-1):
            #checking whether order is ascending or descending
            if reversed:
                a[i],a[0]=a[0],a[i]
                self.MinHeap(a,0,i)
            else:
                a[i],a[0]=a[0],a[i]
                self.MaxHeap(a,0,i)


    #Shell Sort function
    def Shell_Sort(self,arr,reversed):
        n = len(arr)
        gap = n // 2

        while gap > 0:

            for i in range(gap,n):

                temp = arr[i]

                j=i
                #checking whether order is ascending or descending
                if reversed:
                    #sorting data
                    while j >= gap and arr[j-gap] < temp:
                        arr[j]=arr[j-gap]
                        j -= gap
                else:
                    #sorting data
                    while j >= gap and arr[j-gap] > temp:
                        arr[j] = arr[j-gap]
                        j -= gap

                arr[j] = temp

            gap //= 2
