 
# Using readline()
import argparse

parser = argparse.ArgumentParser(description="Arguments for timne calculation")

parser.add_argument('-x', '--file_name', type = str, required=True , help= "Enter Line name clearly")

args = parser.parse_args()

fn = args.file_name

file1 = open(f'{fn}.txt', 'r')
count = 0
total_min = 0
total_sec = 0
 
while True:
    count += 1
    # Get next line from file
    line = file1.readline().strip()
    time1 = line[-7:]
    try:    
        minn = int(time1[0:2])
        total_min = total_min+minn
        secc = int(time1[-2:])
        total_sec = total_sec+ secc
        #print(f"Added +++++++++++++++++++++++++++ {minn} +++++++++++++++++++++ min {secc} sec")
        #print(f'Total is {int(total_min)} min {total_sec} sec')
    except Exception as e:
        pass
 
    # if line is empty
    # end of file is reached
    if not line:
        break

print(f'Total is {int(total_min/60)} hr {total_sec/60} min')
 
file1.close()