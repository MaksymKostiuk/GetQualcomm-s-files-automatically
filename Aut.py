import subprocess

def adb_pull(source_path, destination_path):
    try:
        # Викликаємо команду adb pull
        subprocess.run(['adb', 'pull', source_path, destination_path], check=True)
        print(f"Successfully pulled {source_path} to {destination_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error pulling {source_path} to {destination_path}: {e}")

destination = input("Input the destination for your files")
# Задаємо шляхи для adb pull
source_path1 = "/sdcard/diag_logs"
destination_path1 = "%s/logs"%(destination)

source_path2 = "/sdcard/MIUI/debug_log"
destination_path2 = destination

source_path3 = "/sdcard/DCIM/ScreenRecorder"
destination_path3 = destination

# Викликаємо adb pull для кожного шляху
adb_pull(source_path1, destination_path1)
adb_pull(source_path2, destination_path2)
adb_pull(source_path3, destination_path3)
