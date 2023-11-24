
s1={
    "time":30,
    "flag":True,
    "accident":False,
    "vehicle_count":88,
    "emergency":False,
    "occur":0

}
s2={
    "time":30,
    "flag":False,
    "accident":False,
    "vehicle_count":0,
    "emergency":False,
    "occur":0

}
s3={
    "time":30,
    "flag":False,
    "accident":False,
    "vehicle_count":0,
    "emergency":False,
    "occur":0
}
s4={
    "time":30,
    "flag":False,
    "accident":False,
    "vehicle_count":0,
    "emergency":False,
    "occur":0

}

# creating the list of above dctionary elements 
lane=[s1,s2,s3,s4]

# mimnimum function to find the m first occurance 
def minimum():
      min=10
      index=0
      for i in lane:
           if(i.occur<min and i.occur != 0):
                 min=i.occur
                 index=i
                 i.occur=0
                 
      return index           
# accident function(what will happen if accident occures)
def accident_occures(x):
    sos=False
    while (x.accident == True):
                s1.flag , s2.flag , s3.flag , s4.flag = False
                sos=True

# ambulance function
def emergency_occures(count):
      em_count=0 # Emergency vehicle count
      min=None   # first occurence of Emergency vehicle 
      curr = None
      tempCount = 0
      for x in lane:
            if(x.emergency==True):
                  em_count=em_count+1
                  x.occur=em_count
                  curr = x
    # find the lane in which ambulance occures first in sorted order  
      occur=[]
      for i in range(len(lane)):
            min=minimum()
            occur[i]=min 
      
    # now finding the flag whose value is true
      for i in lane:
            if(i.flag==True):
                  current_lane=i
      if (occur[0] != 0 ):
            if (current_lane != occur[0]):
                  if (count > 10):
                       for x in lane:
                             if (x != occur[0]):
                                   tempCount = count
                                   x.flag = False
                                   occur[0].flag = True
      else:
           #Regular cycle   
           pass                           
                        
# signal manuplating if the no of vehicles in greator then therashhold capacity of the vechils

def deadtraffic():
      for i in lane:
            if(i["vehicle_count"]>70):
                  i["time"]+=10
                  

# Signal controlling function
                        
def signal_control():
    for x in lane:
        count=x["time"]
        while (count >= 0 and x["flag"]==True):
            # if accident occures
            accident_occures(x)

            #Emergency Vehicle Call 
            emergency_occures(count)
            count=count-1    

