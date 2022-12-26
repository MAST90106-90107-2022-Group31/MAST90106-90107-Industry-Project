import csv

# AMDTSS

labels = []

with open('/data/gpfs/projects/punim1257/Group31/hzx/AMDTSS_label.csv', 'r') as labelfile:
    f_label = csv.reader(labelfile, delimiter=',')
    for line in f_label:
        if line[1] == "zygostiy":
            labels.append("zygosity")
        else:
            labels.append(line[1])

with open('/data/gpfs/projects/punim1257/Group31/hzx/AMDTSS_COMMON_V1.csv', 'r') as datafile, \
    open('/data/gpfs/projects/punim1257/Group31/hzx/AMDTSS_ALL.csv', 'w') as outputfile:
    f_data = csv.reader(datafile, delimiter=',')
    f_write = csv.writer(outputfile, delimiter=',')
    count = -1
    for line in f_data:
        count += 1
        if count == 0:
            continue
        if labels[count-1] == 'Sister':
            continue
        line.append(labels[count-1])
        f_write.writerow(line)
