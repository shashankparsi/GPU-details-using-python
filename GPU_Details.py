#Finding Out GPU details using python script on windows machine
import GPUtil
from tabulate import tabulate
print("="*126, "GPU Details", "="*126)
my_gpus=GPUtil.getGPUs()
gpu_details = []
for gpu in my_gpus:
    gpu_id=gpu.id  # get GPU ID
    gpu_name = gpu.name # get GPU Name
    gpu_load= f"{gpu.load * 100} %" # get GPU current load
    gpu_free_memory = f"{gpu.memoryFree} MB" # get GPU free memory
    gpu_used_memory = f"{gpu.memoryUsed} MB "# get GPU used memory
    gpu_total_memory = f"{gpu.memoryTotal} MB" # get GPU Total memory
    gpu_temperature = f"{gpu.temperature} °C "# get GPU temperature
    gpu_uuid = gpu.uuid # get GPU uuid
    gpu_display_active=f"{gpu.display_active}" # gpu display active status
    gpu_display_mode=f"{gpu.display_mode}" # gpu display mode
    gpu_driver_version=f"{gpu.driver}" # gpu driver version
    gpu_memory_util=f"{gpu.memoryUtil} %" # gpu memory utilization in %
    gpu_serial_number=f"{gpu.serial}" # get gpu serial number
    gpu_details.append((gpu_id,gpu_name,gpu_load,gpu_free_memory,gpu_used_memory,gpu_total_memory,gpu_temperature,gpu_uuid,gpu_display_active,gpu_display_mode,gpu_driver_version,gpu_memory_util,gpu_serial_number)) #appending details to list

print(tabulate(gpu_details, headers=("Id", "Name", "Load", "Free memory", "Used memory", "Total memory","Temperature", "uuid","Is GPU display active","GPU display Mode","GPU Driver Version","GPU memory Utilization","GPU serial number")))

