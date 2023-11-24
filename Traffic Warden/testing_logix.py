import multiprocessing0 as mu
import detection0 as d0
import detection1 as d1
import detection2 as d2
import detection3 as d3
import time as t1
import os
import SOS_calls as so
# emergency0=d0.emergency()
# # deadtraffic0=d0.pretrainde()
# accident0=d0.accident()
emergency1=d1.emergency()
# # deadtraffic1=d1.pretrainde()
accident1=d1.accident()
emergency2=d2.emergency()
# # deadtraffic2=d2.pretrainde()
accident2=d2.accident()
emergency3=d3.emergency()
# # deadtraffic3=d3.pretrainde()
accident3=d3.accident()

s1={"name":"up",
    "time":5,
    "flag":False,
    "accident":False,
    "vehicle_count":0,
    "emergency":True,
    "occur":0
}
s2={"name":"Down",
    "time":5,
    "flag":False,
    "accident":False,
    "vehicle_count":90,
    "emergency":emergency1,
    "occur":0

}
s3={"name":"Right",
    "time":5,
    "flag":False,
    "accident":False,
    "vehicle_count":0,
    "emergency":emergency2,
    "occur":0
}
s4={"name":"Left",
    "time":5,
    "flag":False,
    "accident":accident3,
    "vehicle_count":0,
    "emergency":emergency3,
    "occur":0
}
lane=[s1,s2,s3,s4]
# signal control 
if(s1["accident"]==True or s2["accident"]==True or s3["accident"]==True or s3["accident"]==True):
       so.calling() 

def signal_control():
    sos=False
    for x in lane:
        x["flag"]=True
        # print(x["name"],"is GREEN")
        count=x["time"]
        y=x    

        print(x["name"],"is GREEN")
        t1.sleep(0.5)
        # resuming the normal signal for the normal cycle

        while (count > 0 and x["flag"]==True ):
            # if accident occures  

            accident_occures(x,sos)

            #Emergency Vehicle Call 
            for i in lane:
                 if(i['emergency']==True):
                      x["flag"]=False
                      print(x["name"]," is RED")
                      t1.sleep(0.5)
                      emergency_occures(i)
                 else:
                      x["flag"]=True 

            if(x["accident"]==False):
                print("00:",count)
                count=count-1
                t1.sleep(1)
                os.system("cls")
            else:
                 x["flag"]=False
                #  so.calling()
                 print(x["name"]," signal is closed due to accident")
                     
            if(count==0):
                 x["flag"]=False 
                 print(x["name"],"is RED")  
                 t1.sleep(0.5)  
            #if dead traffic occures at any of tha lanes
            deadtraffic()
# if accident occures
def accident_occures(x,sos):
        for i in lane:
                 if(i["accident"]== True):
                  s1["accident"]=True
                  s2["accident"]=True
                  s3["accident"]=True
                  s4["accident"]=True
                    
    # sos==True

# if emergency vehicle is detected at any of the lane
def emergency_occures(y):
     present_state=y
     temp_count=30
     occur=[]
     em_count=0
     for x in lane:
        if(x["emergency"]==True):
                  em_count=em_count+1
                  x["occur"]=em_count
                  occur.append(x)
   # print the emergency queue which should give the first priority
     y=0    
     for x in occur:
          y=y+1
     print("the total no of emergencies foud is = ",y)     
   # now finding which lane should be open at the time
     for x in occur:
          temp=0
          print(x["name"],"is GREEN")
        #   t1.sleep(0.5)
          for i in lane:
                temp_count=30
                if(i==x):
                    print("emergency clearing  at ",i["name"]," lane ")
                    t1.sleep(4)
                    while(x["emergency"]==True and temp_count > 0):
                          i["flag"]=True
                          temp_count=temp_count-1
                          print("00:",temp_count)
                          t1.sleep(0.1)
                          os.system("cls")
                if(temp_count==0):
                     i["emergency"]=False
                else:
                    pass              
     occur=[]
     print("after clear")
     for i in lane:
        i["occur"]=0
        # print(x["name"],"is RED")
     print(x["name"]," is RED") 
     print(s1["name"]," is green ") 
     t1.sleep(0.5)
     return present_state
                

# signal manuplating if the no of vehicles in greator then therashhold capacity of the vechils

def deadtraffic():
      for i in lane:
            if(i["vehicle_count"]>70):
                  i["time"]+=10

def main():
    pass
if __name__== "__main__":
    signal_control()
#     temp_count=30
#     occur=[]
#     em_count=0
#     for x in lane:
#         if(x["emergency"]==True):
#                   em_count=em_count+1
#                   x["occur"]=em_count
#                   occur.append(x)
#                 #   x["occur"]=0
#    # print the emergency queue which should give the first priority
#     for x in occur:
#           print(x["occur"])
#    # now finding which lane should be open at the time
#     for x in occur:
#           temp=0
#           print(x)
#           for i in lane:
#                 temp_count=30
#                 if(i==x):
#                     while(x["emergency"]==True and temp_count > 0):
#                           i["flag"]=True
#                           temp_count=temp_count-1
#                           print(temp_count)
#                 if(temp_count==0):
#                      i["emergency"]=False
#                 else:
#                     pass              
#     occur=[]
#     print("after clear")
#     for x in lane:
#         x["occur"]=0
#         print(x)
    

                      
                           
    
                           
             
          

