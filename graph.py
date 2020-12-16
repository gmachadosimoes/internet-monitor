from matplotlib import pyplot as plt
import csv
from matplotlib import ticker as ticker

times = []
download = []
upload = []

with open('test.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        times.append(str(row[0]))
        download.append(str(row[1]))
        upload.append(str(row[2]))

print(times, "\n", download, "\n", upload)

plt.figure(30, 30)
plt.plot(times, download, label="download", color="r")
plt.plot(times, upload, label="upload", color="b")
plt.xlabel('time')
plt.ylabel('speed in Mb/s')
plt.title('internet speed')
plt.legend()
plt.savefig('test_graph.jpg', bbox_inches="tight")


