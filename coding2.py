#!/usr/bin/env python
# -*- coding: utf-8 -*-

          
  # COMS3203 DISCRETE MATHEMATICS
  # CODING ASSIGNMENT 2
  # YOUR NAME: Larissa Tyree
  # YOUR UNI: lbt2116
import math 
from random import randint

            
#Returns the GCD of two integers using Euclid's algorithm. 
#Also prints out theintermediate steps for Euclid's Algorithm on num1 
#and num2.
            
                #Parameters:
                #num1 (int): First number for the GCD
                #num2 (int): Second number for the GCD
                
                #Returns:
                   # int: GCD of num1 and num2'''
            
def euclid(num1, num2): 
                
            
             
             print(" GCD(",num1,",", num2,")", "=", end = '')
             while num2:               
                num1, num2 = num2, num1%num2
                print(" GCD(",num1,",", num2,")", "=", end = '')
                
             print(num1)
             return num1
          
#Returns a list of prime numbers up to (and including) 
#a certain input integer, n.
                
                #Parameters:n (int): The target number to generate primes up to.
                #Returns:list: List of all prime numbers <= n.'''
                
def prime_gen(n):  
                
                  
                #USING SETS
                edge = round(math.sqrt(n)) #set a boundary as squareroot of n
                set1, set2 = set(), set() #create two sets             
                
                if(n==2): #edge case 
                  return n 
                
                if(n<2): #edge case 
                  return  "No primes <2" # 1 is not prime 
            
                for x in range(2, n):
                    set1.add(x) # add all greater than 2 to set1
            
                for g in range(2, n): #from 2 to n 
                    #from i to sqrt of n
                    for i in range(1, edge): 
                        #if n contains a multiple of i, it is not prime
                        nonPrime= g * (i+1) #add new primes 
                        set2.add(nonPrime)
                        
                        if (nonPrime) in set2:
                            continue #prime already in set2, don't add again
                        
                set1 -= set2 #delete non-primes from set1
                sortedset= sorted(set1) #sort the set of primes 
            
                return sortedset #return a list of all primes <=n 
            
                         
 #Returns a boolean value (True or False) depending on whether 
 #the input n is prime.
  
 #Parameters:
 #n (int): The target integer to check primality.
               
 #Returns:
 #boolean: True if n is prime, False if n is not prime.'''
                            
def prime_check_trial(n):  
                # WRITE YOUR CODE HERE    return prime 
                # boolean True or False depending on prime or not
                
                if n< 2 or n % 2 == 0:
                    return False #not prime 
                
                if n == 2:
                    return True   #2 is prime          
            
                # see if n is divisible by a number from 
                # two to sqrt of n               
                for i in range(2, int(math.sqrt(n))):
                    if n % i == 0:
                        return False #if divisible, not prime 
                return True # e;se is prime 

                

                   
                    
def prime_check_sieve(n):  
                    # WRITE YOUR CODE HERE    return prime 
                    # boolean True or False depending on prime or not
                    
                    
                #modified code from above    
                #USING SETS 
                edge = round(math.sqrt(n)) #set a boundary as squareroot of n
                set1, set2 = set(), set() #create two sets             
                
                if(n==2): #edge case 
                  return True
                
                if(n<2): #edge case 
                  return  False # 1 is not prime 
            
                for x in range(2, n*n):
                    set1.add(x) # add all greater than 2 to set1
            
                for g in range(2, n+2): #from 2 to n 
                    #from i to sqrt of n
                    for i in range(1, edge): 
                        #if n contains a multiple of i, it is not prime
                        nonPrime= g * (i+1) #add new primes 
                        set2.add(nonPrime)                                        
                        
                set1 -= set2 #delete non-primes from set1
                sortedset= sorted(set1) #sort the set of primes 
                
                if n in sortedset:
                    return True #n is prime, return true 
                else:
                    return False #n is not prime, return false 
            
                           
                    
                        
   
def prime_check_fermat(n):  
                        # WRITE YOUR CODE HERE    return prime
                        # boolean True or False depending on prime or not
                        #If p is a prime number, then for any integer a,
                        #the number a^p−a is an integer multiple of p.
                        
                        #use 3 as the random a
                        #** used for power of integer
                        if (3 ** n - 3) % n == 0:
                            return True 
                        else:
                            return False # not a multiple of p, not prime 
                        
                        
                        
                        
                        
                    
#Returns a list of two prime integers that sum up to n
#Parameters:
# n (int): The target even integer to check Goldbach's 
#Conjecture for.
#Returns:
#list: A list of length 2 containing 2 ints
#that sum up to n.'''
                        
def check_goldbach(n):    
                    # WRITE YOUR CODE HERE    return primes
                    # two prime numbers that sum up to n
                    
                    # Return if number is not even  
                    # or less than 3 
                    
                    #generate list of primes using  Sieve of Eratosthenes
                    #method from above   
                    primes = prime_gen(n) 
                    
                    
                    if (n <= 2):  #edge case                     
                        return "Invalid Input, must be > 2 for Goldbach"
                  
                    
                    x = 0; # iterate through prime_gen(n)
                    while (primes[x]):  #while there are primes in list 
                          
                        # calculate the difference 
                        difference = n - primes[x] 
                  
                        # see if difference is a prime number too                      
                        if difference in primes:                              
                            # return n as two primes       
                            return [primes[x], difference]
                        x += 1 
                  
     



### DO NOT TURN IN AN ASSIGNMENT WITH ANYTHING BELOW HERE MODIFIED ###
if __name__ == '__main__':  
                    print("#######################################")   
                    print("Welcome to Coding 2: Prime Numbers!")   
                    print("#######################################")    
                    print()   
                    print("---------------------------------------")   
                    print("PART A: Euclid's Algorithm")   
                    print("---------------------------------------") 
                    euclid_test_1 = [(2^4*3^4*5^2*13^4*49), (2^2*5^4*7^4*11^2*3^3)]   
                    print("Test Case 1: GCD of", euclid_test_1[0],
                          "and", euclid_test_1[1]) 
                    print("Test Case 1 Steps: ")   
                    student_ans = euclid(euclid_test_1[0], euclid_test_1[1])   
                    print("Test Case 1 (Your Answer):", student_ans)  
                    print("Test Case 1 (Correct Answer):", 21)   
                    print("Test Case 1:", ("# PASSED! #" if student_ans == 21 
                                           else "# INCORRECT #"))   
                    print()    
                    euclid_test_2 = [1071, 462] 
                    print("Test Case 2: GCD of", euclid_test_2[0], 
                          "and", euclid_test_2[1])  
                    print("Test Case 2 Steps: ")   
                    student_ans = euclid(euclid_test_2[0], euclid_test_2[1])    
                    print("Test Case 2 (Your Answer):", student_ans)   
                    print("Test Case 2 (Correct Answer):", 21)    
                    print("Test Case 2:", ("# PASSED! #" if student_ans == 21 
                                           else "# INCORRECT #"))  
                    print()    
                    euclid_test_3 = [85523, 3212]    
                    print("Test Case 3: GCD of", euclid_test_3[0], "and",
                          euclid_test_3[1])    
                    print("Test Case 3 Steps: ")    
                    student_ans = euclid(euclid_test_3[0], euclid_test_3[1])
                    print("Test Case 3 (Your Answer):", student_ans)    
                    print("Test Case 3 (Correct Answer):", 1)    
                    print("Test Case 3:", ("# PASSED! #" if student_ans == 1  
                                           else "# INCORRECT #"))    
                    print("---------------------------------------")    
                    print("PART B: Prime Number Generation")    
                    print("---------------------------------------")    
                    prime_gen_test_1 = 42    
                    prime_gen_test_1_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                                            31, 37, 41]    
                    print("Test Case 1: Prime Numbers Up To:", prime_gen_test_1)    
                    print("Test Case 1 (Your Answer):", prime_gen(prime_gen_test_1))    
                    print("Test Case 1 (Correct Answer):", prime_gen_test_1_ans)    
                    print("Test Case 1:", ("# PASSED! #" if 
                                           prime_gen(prime_gen_test_1) == 
                                           prime_gen_test_1_ans 
                                           else "# INCORRECT #"))    
                    print()    
                    prime_gen_test_2 = 314    
                    prime_gen_test_2_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                                            31, 37, 41, 43,    
                        47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 
                        107, 109, 113, 127,
                        131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
                        191, 193, 197, 199,
                        211, 223, 227, 229, 233, 239, 241, 251, 257,
                        263, 269, 271, 277, 281, 283,
                        293, 307, 311, 313]    
                    print("Test Case 2: Prime Numbers Up To:", prime_gen_test_2)    
                    print("Test Case 2 (Your Answer):", prime_gen(prime_gen_test_2))    
                    print("Test Case 2 (Correct Answer):", prime_gen_test_2_ans)    
                    print("Test Case 2:", ("# PASSED! #" if 
                                           prime_gen(prime_gen_test_2) == 
                                           prime_gen_test_2_ans  else "# INCORRECT #"))    
                    print()    
                    prime_gen_test_3 = 884    
                    prime_gen_test_3_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
                            31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                            89, 97, 101, 103, 107, 109, 
                            113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
                            179, 181, 191, 193, 197,
                            199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263,
                            269, 271, 277, 281, 283,
                            293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
                            367, 373, 379, 383, 389,
                            397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457,
                            461, 463, 467, 479, 487, 
                            491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
                            571, 577, 587, 593, 599, 
                            601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
                            661, 673, 677, 683, 691,
                            701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769,
                            773, 787, 797, 809, 811, 
                            821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881,
                            883]    
                    print("Test Case 3: Prime Numbers Up To:", prime_gen_test_3)    
                    print("Test Case 3 (Your Answer):", prime_gen(prime_gen_test_3))    
                    print("Test Case 3 (Correct Answer):", prime_gen_test_3_ans)    
                    print("Test Case 3:", ("# PASSED! #" if prime_gen(prime_gen_test_3)
                                           == prime_gen_test_3_ans  else "# INCORRECT #"))    
                    print("---------------------------------------")   
                    print("PART C: Primality Testing")    
                    print("---------------------------------------")    
                    primality_test_1 = 8                 
                    primality_test_1_ans = False    
                    print("Test Case 1: Check Primality For:", primality_test_1)    
                    print("Test Case 1 (Your Trial Division Answer):",
                          prime_check_trial(primality_test_1))    
                    print("Test Case 1 (Your Sieve Answer):", prime_check_sieve(primality_test_1))    
                    print("Test Case 1 (Your Fermat's Little Theorem Answer):",
                          prime_check_fermat(primality_test_1))    
                    print("Test Case 1 (Correct Answer):", primality_test_1_ans)    
                    print("Test Case 1:", ("# PASSED! #" if 
                                           prime_check_trial(primality_test_1) == 
                            prime_check_sieve(primality_test_1) == 
                            prime_check_fermat(primality_test_1)
                            == primality_test_1_ans else "# INCORRECT #"))    
                    print()   
                    primality_test_2 = 482    
                    primality_test_2_ans = False    
                    print("Test Case 2: Check Primality For:", primality_test_2)    
                    print("Test Case 2 (Your Trial Division Answer):",
                          prime_check_trial(primality_test_2))    
                    print("Test Case 2 (Your Sieve Answer):", prime_check_sieve(primality_test_2))    
                    print("Test Case 2 (Your Fermat's Little Theorem Answer):",
                          prime_check_fermat(primality_test_2))    
                    print("Test Case 2 (Correct Answer):", primality_test_2_ans)    
                    print("Test Case 2:", ("# PASSED! #" if prime_check_trial(primality_test_2)
                            == prime_check_sieve(primality_test_2) ==
                            prime_check_fermat(primality_test_2)
                        == primality_test_2_ans else "# INCORRECT #"))    
                    print()   
                    primality_test_3 = 853    
                    primality_test_3_ans = True    
                    print("Test Case 3: Check Primality For:", primality_test_3)    
                    print("Test Case 3 (Your Trial Division Answer):",
                          prime_check_trial(primality_test_3))    
                    print("Test Case 3 (Your Sieve Answer):", prime_check_sieve(primality_test_3))    
                    print("Test Case 3 (Your Fermat's Little Theorem Answer):",
                          prime_check_fermat(primality_test_3))    
                    print("Test Case 3 (Correct Answer):", primality_test_3_ans)    
                    print("Test Case 3:", ("# PASSED! #" if prime_check_trial(primality_test_3) ==
                            prime_check_sieve(primality_test_3) == 
                            prime_check_fermat(primality_test_3) == 
                            primality_test_3_ans else "# INCORRECT #"))   
                    print("---------------------------------------")    
                    print("PART D: Goldbach's Conjecture")    
                    print("---------------------------------------")    
                    goldbach_test_1 = 8    
                    goldbach_test_1_ans = [3, 5]    
                    student_ans = check_goldbach(goldbach_test_1)    
                    print("Test Case 1: 2 Primes For:", goldbach_test_1)    
                    print("Test Case 1 (Your Answer):", check_goldbach(goldbach_test_1))    
                    print("Test Case 1 (A Correct Answer):", goldbach_test_1_ans)    
                    print("Test Case 1:", ("# PASSED! #" if student_ans[0] +
                                           student_ans[1] == goldbach_test_1 
                                           else "# INCORRECT #"))    
                    print()    
                    goldbach_test_2 = 482    
                    goldbach_test_2_ans = [3, 479]    
                    student_ans = check_goldbach(goldbach_test_2)    
                    print("Test Case 2: 2 Primes For:", goldbach_test_2)    
                    print("Test Case 2 (Your Answer):", check_goldbach(goldbach_test_2))    
                    print("Test Case 2 (A Correct Answer):", goldbach_test_2_ans)    
                    print("Test Case 2:", ("# PASSED! #" if student_ans[0] +
                                           student_ans[1] == goldbach_test_2  
                                           else "# INCORRECT #"))    
                    print()    
                    goldbach_test_3 = 1152    
                    goldbach_test_3_ans = [23, 1129]    
                    student_ans = check_goldbach(goldbach_test_3)    
                    print("Test Case 3: 2 Primes For:", goldbach_test_3)    
                    print("Test Case 3 (Your Answer):", check_goldbach(goldbach_test_3))    
                    print("Test Case 3 (A Correct Answer):", goldbach_test_3_ans)    
                    print("Test Case 3:", ("# PASSED! #" if student_ans[0] +
                                           student_ans[1] == goldbach_test_3 
                                           else "# INCORRECT #"))    
                    print("---------------------------------------")
                        
                        
                        
                        
                        