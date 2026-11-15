import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
data_05 = pd.read_csv("L2_5V_model.txt", sep="\t")
Vin_05 = data_05["Vin"]
Vout_05 = data_05["V(vout)"]
data_ltspice = pd.read_csv("S7.txt",sep = "\t")
Vin_ltspice = data_ltspice["Vin"]
Vout_ltspice = data_ltspice["Vout"]
plt.plot(Vin_05/5,Vout_05/5,label=r"KiCAD VTC")
plt.plot(Vin_ltspice/1.1,Vout_ltspice/1.1,label=r"LTspice VTC")
plt.xticks(np.arange(0, 1.1, 0.1))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.xlabel("Normalized Input VoltageVIN/VDD")
plt.ylabel("Normalized Output Voltage VOUT/VDD")
plt.title("L5: Normalized VTC - KiCAD v/s LTspice")
plt.legend()
plt.grid()
plt.show()