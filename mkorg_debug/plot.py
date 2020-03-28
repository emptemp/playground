import matplotlib.pyplot as plt
import re


channel1 = []
channel2 = []

with open("sine_flang_noise.csv", "r") as o:
    for line in o.readlines():
        if line.startswith("T"):
            print("nothing")
        else:
            reg_ch = re.findall("Ch (.)", line)
            reg_val = re.findall("'(.*)'", line)
            if reg_ch and reg_val:
#                print("{}: {}".format(reg_ch[0], reg_val[0]))
                if int(reg_ch[0]) == 1:
                    if reg_val[0].isdigit():
#                        print("{}: {}".format(reg_ch[0], reg_val[0]))
                        a = int(reg_val[0])
                        if a > 0x8000:
                            a = -1*(0xFFFF-a)
                        channel1.append(a)
                    else:
                        channel1.append(0)
                elif int(reg_ch[0]) == 2:
                    if reg_val[0].isdigit():
                        a = int(reg_val[0])
                        if a > 0x8000:
                            a = -1*(0xFFFF-a)
                        channel2.append(a)
                    else:
                        channel2.append(0)

o.close()

#print(channel1)
plt.plot(channel1)
plt.plot(channel2)
plt.show()
