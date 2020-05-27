# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:07:04 2020

@author: Liam
"""
import matplotlib.pyplot as plt

def gridCoverage(m,n): # Complexity: O(n*m)
  
    if((m==0)|(n==0)):
        print("Invalid argument fed. Please feed positive integers.")
        
    
    gradients=[]
    grad=0
    points=0
    for i in range(0,m):
        for j in range(0,n):
            indicator1=True      #Indicator for checking if gradient already exists.
            indicator2=True      #Indicator for checking if the point has been separately processed.
            if(grad==0):
                indicator1=False
                
            if((i==0)&(j==0)):   #Takes care of (0,0) coordinate.
                points=points+1
                indicator2=False
                
            if((i==1)&(j==0)):   #Takes care of (1,0) coordinate.
                points=points+1
                indicator2=False  
            elif((i==0)&(j==1)): #Takes care of (0,1) coordinate.
                points=points+1
                indicator2=False
            elif((i==0)|(j==0)): #Excludes all other points along x and y axes.
                indicator2=False
            
                
            #Calculate gradient once special cases are taken care of
            if(indicator2==True):
                grad=i/j
            
            if(i==1&j==1):
                points=points+1
                gradients.append(grad)
                indicator2=False
                continue
                
            for gradient in gradients:
                if(grad==gradient):
                    indicator1=False
                    break
                elif(grad!=gradient):
                    indicator1=True
                    
            if(indicator1==True):
                gradients.append(grad)
                points=points+1
                
    percentCover=points/(m*n)*100
    return percentCover

def plotPercentage(m): # Complexity: O(m^3) Be prepared for long waits for large
                       # choices of m.
    x=[]
    y=[]
    for i in range(1,m):
        x.append(i)
        y.append(gridCoverage(i,i))
    
    plt.plot(x,y)
    plt.xlabel="Number of points on edge of square"
    plt.ylabel="Percentage of square that is covered from (0,0)."
    plt.show()

def main():
    m=200
    plotPercentage(m)
    
    
main()
