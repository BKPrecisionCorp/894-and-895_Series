import time
import visa
rm=visa.ResourceManager()
li=rm.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which device?: ")
vi=rm.open_resource(li[int(choice)])
vi.timeout = 2000

print(vi.query("*idn?"))

print("Linear sweep (because it's easier)")
try:
    start = int(input("Start frequency (Hz): "))
    points = int(input("Number of points: "))
    step = int(input("Frequency step (Hz): "))
except:
    print("input not a number probably")
    exit()
    
if (start + points*step) > 1000000:
    print("Frequency step and points too large (start + step*points) > 1000000 - exiting (sorry)")
    exit()

print("Function - ",vi.query("func:imp?"))
for i in range(int(points)):
    freq = int(start) + int(step)*i
    cmd = "freq "+str(freq)
    vi.write(cmd)
    resp = str(freq)+","+vi.query("fetch?") 
    print(resp)
