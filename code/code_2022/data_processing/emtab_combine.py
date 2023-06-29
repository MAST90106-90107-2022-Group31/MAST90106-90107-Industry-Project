import csv

# EMTAB

labels = []

with open('/data/gpfs/projects/punim1257/Group31/hzx/EMTAB_label.csv', 'r') as labelfile:
    f_label = csv.reader(labelfile, delimiter=',')
    for line in f_label:
        if line[9] == "Characteristics[twin zygosity]":
            labels.append("zygosity")
        if line[9] == "dizygotic":
            labels.append("DZ")
        elif line[9] == "monozygotic":
            labels.append("MZ")
        else:
            labels.append("NA")

with open('/data/gpfs/projects/punim1257/Group31/hzx/EMTAB_COMMON.csv', 'r') as datafile, \
    open('/data/gpfs/projects/punim1257/Group31/hzx/EMTAB_ALL.csv', 'w') as outputfile:
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
