def bubbleSort(list):
    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

def insertionSort(list):
   for index in range(1,len(list)):

     currentvalue = list[index]
     position = index

     while position>0 and list[position-1]>currentvalue:
         list[position]=list[position-1]
         position = position-1

     list[position]=currentvalue
