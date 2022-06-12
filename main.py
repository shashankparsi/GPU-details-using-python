import platform
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
from IPython import get_ipython
import psutil
from timeit import default_timer as timer
import xlsxwriter
from xlsx2html import xlsx2html
import GPUtil
import torch
start = timer()
system = platform.uname()
print(f"system : {system.system}")
print(f"Node: {system.node}")
print(f"Release : {system.release}")
print(f"Processor : {system.processor}")
print(f"Version: {system.version}")
print(f"Machine: {system.machine}")
cores = psutil.cpu_count()
print(f"CPU cores : {cores}")
system_memory = psutil.virtual_memory()
print(system_memory)
print(f"Total Memory : {system_memory[0]}")
print(f"Available Memory : {system_memory[1]}")
print(f"Memory Percentage used: {system_memory[2]}")
print(f"Memory used:{system_memory[3]}")
print(f"Memory free : {system_memory[4]}")
print("CPU time for execution:",timer()-start)


data = pd.DataFrame({"Memory Details":["Total Memory","Available Memory","Memory Percentage used","Memory used","Memory used"],"Values":[system_memory[0],system_memory[1],system_memory[2],system_memory[3],system_memory[4]]})
writer = pd.ExcelWriter("system_info.xlsx",engine="xlsxwriter")

data.to_excel(writer,sheet_name="sheet1",index=False)
writer.save()

reader=pd.read_excel("system_info.xlsx")
print(reader)

xlsx2html("C:\\Users\parsi\PycharmProjects\pythonProject\Data_analysis\system_info.xlsx","C:\\Users\parsi\PycharmProjects\pythonProject\Data_analysis\system_info.html")

GPUtil.showUtilization()
