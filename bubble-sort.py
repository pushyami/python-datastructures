import random
def bubblesort(k):
    for i in range(len(k)-1):
        for j in range(i+1,len(k)):
            if k[j] <= k[i]:
                temp = k[j]
                k[j]=k[i]
                k[i]=temp

        print "Iteration: ",i," : ",k

    return k





def main():

    k = []

    for i in range(0,10):
        x = random.randint(1,10)
        k.append(x)

    print "Input array: ",k
    k = bubblesort(k)
    print "Sorted array: ",k

main()
