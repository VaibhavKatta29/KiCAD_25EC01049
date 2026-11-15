import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_05 = pd.read_csv("L2_5V_model.txt", sep="\t")
data_09 = pd.read_csv("L2_9V_model.txt", sep="\t")

Vin_05 = data_05["Vin"]
Vout_05 = data_05["V(vout)"]

Vin_09 = data_09["Vin"]
Vout_09 = data_09["V(vout)"]

plt.figure(figsize=(8, 5))
plt.plot(Vin_05,Vout_05, label=r"VDD = 5V")
plt.plot(Vin_09,Vout_09, label=r"VDD = 9V")
plt.xticks(np.arange(0, 5.5, 0.5))
plt.xlabel("Input Voltage Vin")
plt.ylabel("Output Voltage Vout")
plt.title("L2: Vout vs Vin")
plt.legend()
plt.grid()
plt.show()

target = 5/2

# Find the first point where Vout becomes less than 2.5V for VDD = 5v
index_05 = np.where(Vout_05 <= target)[0][0]
# Two points surrounding Vout = 2.5V
x1_05 = Vin_05.iloc[index_05-1]
x2_05 = Vin_05.iloc[index_05]
y1_05 = Vout_05.iloc[index_05-1]
y2_05 = Vout_05.iloc[index_05]
# Linear interpolation
Vm_05 = x1_05 + (target-y1_05)*(x2_05-x1_05)/(y2_05-y1_05)
print("Switching threshold Vm for VDD = 5V:", Vm_05, "V")


# Find the first point where Vout becomes less than 2.5V for VDD = 9v
index_09 = np.where(Vout_09 <= target)[0][0]
# Two points surrounding Vout = 2.5V
x1_09 = Vin_09.iloc[index_09-1]
x2_09 = Vin_09.iloc[index_09]
y1_09 = Vout_09.iloc[index_09-1]
y2_09 = Vout_09.iloc[index_09]
# Linear interpolation
Vm_09 = x1_09 + (target-y1_09)*(x2_09-x1_09)/(y2_09-y1_09)
print("Switching threshold Vm for VDD = 9V:", Vm_09, "V")






### Using closest point method. 
# index = np.argmin(np.abs(Vout_05 - 2.5))

# print("Index =", index)
# print("Vin =", Vin_05.iloc[index])
# print("Vout =", Vout_05.iloc[index])

plt.figure(figsize=(8, 5))
plt.plot(Vin_05, Vout_05, label=r"VDD = 5V")
# Mark Vm
plt.axvline(Vm_05, color="red", linestyle="--", label="Vm for VDD = 5V")
plt.scatter(Vm_05, 2.5, color="red")

plt.plot(Vin_09, Vout_09, label=r"VDD = 5V")
plt.axvline(Vm_09, color="blue", linestyle="--", label="Vm for VDD = 9V")
plt.scatter(Vm_09, 2.5, color="red")

plt.axhline(2.5, color="green", linestyle="--", label="VDD/2")
plt.yticks(np.arange(0, 9.5, 1))
plt.xticks(np.arange(0, 5.5, 0.5))
plt.xlabel("Input Voltage Vin")
plt.ylabel("Output Voltage Vout")
plt.title("L4:Switching Threshold = Vm")
plt.legend()
plt.grid()
plt.savefig("L4_VTC.png", dpi=300)
plt.show()


