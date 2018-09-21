#Question 14 in Python
import time

dictionary = dict()

maxterms = 0
startnumMAX = 0

def collatz(n):
    global dictionary, maxterms, startnumMAX
    termcounter = 0
    startingnum = n
    
    while True:
        #checks dictionary for number which is paired with
        #the number of terms from n to 1
        if n in dictionary:
            #adds the number of terms from n to 1 to the running
            #sum of terms 
            termcounter = termcounter + dictionary.get(n)
            n = 1
        #if n is not already in the dictionary, update n and
        #add another term to termcounter
        else:
            if n % 2 == 0:
                n = n / 2
            else:
                n = (3 * n) + 1
            termcounter = termcounter + 1
        #when 1 has been reached...
        if n == 1:
            #...see if the number of terms in this sequence is the 
            #greatest number of terms in any sequence, if so, update maxterms
            if termcounter > maxterms:
                maxterms = termcounter
                startnumMAX = startingnum
            dictionary[startingnum] = termcounter
            break


start_time = time.time()
for x in range(1, 1000000):
    collatz(x)

print(startnumMAX)
#print(dictionary[str(startnumMAX)])
print(time.time() - start_time)