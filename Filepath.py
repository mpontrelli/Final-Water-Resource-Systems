# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 10:58:31 2018

@author: Marshall
"""

Filepath = "C:\\Users\\Marshall\\Box Sync\\Spring_2018\\Research\\Mexico City\\19sep17\\"
filename = ["AE0220170919181440.txt" , "AL0120170919181440.txt" , "AO2420170919181440.txt" ,
            "AP6820170919181440.txt", "AU1120170919181440.txt" , "AU4620170919181440.txt"]
for i in range(len(filename)):
    ffilename=filename[i]
    Filename = Filepath + ffilename
    print(Filename)