import psutil
from psutil import cpu_percent
import psutil 
def get_system():
    cpu_percent=psutil.cpu_percent(interval=1)
    memory_percent=psutil.virtual_memory().percent
    disk_percent=psutil.disk_usage("C:\\").percent
    cpu_threshold=10
    status = " HIGH CPU " if cpu_percent>cpu_threshold else "HEALTHY"
    return {
        "cpu_percentage":cpu_percent,
        "memory_percent ":memory_percent,
        "disk_percent":disk_percent,
        "system_status":status,
        "cpu_threshold":cpu_threshold,  
    }