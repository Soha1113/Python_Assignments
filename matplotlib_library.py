#import matplotlib
import matplotlib.pyplot as plt

#simple line plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.show()

#multiple line plot
x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [15, 25, 35, 45]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.legend()
plt.title("Multiple Line Plot")
plt.show()

#bar chart
names = ["AI", "ML", "DL"]
values = [50, 70, 40]

plt.bar(names, values)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Bar Chart")
plt.show()

#horizontal bar chart
plt.barh(names, values)
plt.title("Horizontal Bar Chart")
plt.show()

#scatter plot
x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.show()

#histogram
data = [10, 20, 20, 30, 40, 40, 40, 50]

plt.hist(data)
plt.title("Histogram")
plt.show()

#pie chart
labels = ["AI", "ML", "DL"]
sizes = [40, 35, 25]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()

#area plot
x = [1, 2, 3, 4]
y = [3, 5, 7, 9]

plt.fill_between(x, y)
plt.title("Area Plot")
plt.show()

#stack plot
x = [1, 2, 3, 4]
y1 = [3, 4, 5, 6]
y2 = [1, 2, 3, 4]

plt.stackplot(x, y1, y2)
plt.title("Stack Plot")
plt.show()

#subplots
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("Plot 2")

plt.show()

#grid and limits
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)
plt.grid(True)
plt.xlim(1, 4)
plt.ylim(0, 50)
plt.show()

#saving a plot
x = [1, 2, 3]
y = [5, 10, 15]

plt.plot(x, y)
plt.title("Saved Plot")
plt.savefig("plot.png")
plt.show()

#clearing and closing plots
plt.plot([1, 2, 3], [4, 5, 6])
plt.clf()     # Clear figure
plt.close()   # Close plot