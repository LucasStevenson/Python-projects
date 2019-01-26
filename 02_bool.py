firstL = [False,True,True,None,True,None,None,False,False,None,True,False]

secondL = ["or","or","or","==","!=","==","and","==","!=","and","==","or"]

thirdL = [False,False,None,None,True,True,False,True,None,False,True,None]
#end of givens

for i in range(len(firstL)):
  finalL = (str(firstL[i])) + " " + (str(secondL[i])) + " " + (str(thirdL[i]))
  print (finalL + " => " + str(eval(finalL)))
