import csv

# DENMARK

labels = []

remove_list = ["Individual_33_1997", "Individual_33_2007", "Individual_34_1997", 
              "Individual_34_2007", "Individual_35_1997", "Individual_35_2007", 
              "Individual_36_1997", "Individual_36_2007", "Individual_37_1997", 
              "Individual_37_2007", "Individual_38_1997", "Individual_38_2007", 
              "Individual_39_1997", "Individual_39_2007", "Individual_40_1997", 
              "Individual_40_2007", "Individual_41_1997", "Individual_41_2007", 
              "Individual_42_1997", "Individual_42_2007"]

with open('/data/gpfs/projects/punim1257/Group31/hzx/DENMARK_label_adjusted.csv', 'r') as labelfile:
    f_label = csv.reader(labelfile, delimiter=',')
    for line in f_label:
        if line[1] == "Zygosity":
            labels.append("zygosity")
        elif line[0] in remove_list:
            labels.append("NA")
        elif line[1] == "1":
            labels.append("MZ")
        elif line[1] == "2":
            labels.append("DZ")
        else:
            labels.append("NA")

with open('/data/gpfs/projects/punim1257/Group31/hzx/DENMARK_COMMON_V1.csv', 'r') as datafile, \
    open('/data/gpfs/projects/punim1257/Group31/hzx/DENMARK_ALL.csv', 'w') as outputfile:
    f_data = csv.reader(datafile, delimiter=',')
    f_write = csv.writer(outputfile, delimiter=',')
    count = -1
    for line in f_data:
        count += 1
        if count == 0:
            continue
        if labels[count-1] == 'NA':
            continue
        line.append(labels[count-1])
        f_write.writerow(line)
