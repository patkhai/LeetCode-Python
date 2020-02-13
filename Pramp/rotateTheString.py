def rotateTheString(originalString, direction, amount):

    lengthS = len(originalString)
    for rotate in amount: 
        if direction == 1: #rotate right 
            originalString = originalString[lengthS - 1] + originalString[0:lengthS-1]
        else: #rotate left
            originalString = originalString[1:lengthS] + originalString[0]
    
    return originalString 

s = "hurart"
print(rotateTheString(s,[0,1],[4,1]))


def RotateMe(text,mode=0,steps=1):
  # Takes a text string and rotates
  # the characters by the number of steps.
  # mode=0 rotate right
  # mode=1 rotate left
  length=len(text)
 
  for step, i in enumerate(steps):
  # repeat for required steps
 
    if mode==0:
      # rotate right
      text=text[length-1] + text[0:length-1]
    else:
      # rotate left
      text=text[1:length] + text[0]
 
  return text

s = "hurart"
print(RotateMe(s,[0,1],[4,1]))