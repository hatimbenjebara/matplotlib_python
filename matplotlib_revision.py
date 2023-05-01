import matplotlib.pyplot as plt
#example1 : creating a simple line
#sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
#create the plot
plt.plot(x,y)
#add labels and title
plt.xlabel("X axis label")
plt.ylabel("Y axis label")
plt.title("title of the plot")
#display the plot
plt.show()
#example2 : creating bar chart
#sample data 
x = ["A", "B", "C", "D"]
y = [20, 35, 30, 25]
#create the bar chart using the sample data 
plt.bar(x,y)
#Add labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar chart")
#display the plot
plt.show()
#Example3: creating a scatter plot 
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
#create the plot 
plt.scatter(x,y)
#Add labels and title
plt.xlabel("X axis label")
plt.ylabel("Y axis label")
plt.title("Scatter plot")
#display the plot
plt.show()
#plot function
#Example 4 : simple plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("simple plot")
plt.show()
#Example 5: plot with out line 
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, "o")
plt.title("plot with out line")
plt.show() 
#example 6: 
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker="*")
plt.title("changing marker")
plt.show()
#Example 7: 
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(y, "o:r")
plt.title("plot changing ")
plt.show()
#Example 8:
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(y, marker="o", ms=20, mec="r", mfc="b")
plt.title("plot after changin characters")
plt.show()
#example 9:
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(y, linestyle = "dotted", color = "red", linewidth = "10")
plt.title("plot using new characters")
plt.show()
#example 10:
font1 = {"family": "serif", "color": "blue", "size":20}
font2= {"family": "serif", "color": "darkred", "size":15}
plt.plot(x, y)
plt.xlabel("Average Pulse", fontdict=font1)
plt.ylabel("Calorie Burnage", fontdict=font2)
plt.title("sport watch data", fontdict=font1 , loc ="Left") #by default loc= center
plt.show()
#Example 11 :
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x,y)
plt.grid() 
plt.grid(axis ="x") 
plt.grid(axis= "y")
plt.title("plot grid")
plt.show()
#Example 12: 
#plot1 
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.subplot(1,2,1) # the figure has 1 row, 2 columns and this is the first plot
plt.plot(x,y)
plt.title("title figure 1")# title for first figure
#plot2 
x = [2, 4, 6, 8, 10]
y = [2, 4, 6, 8, 10]
plt.subplot(1,2,2) # the figure has  row, 2 columns and this is plot is the second plot
plt.plot(x,y)
plt.title("title of figure 2") # title for the second figure 
plt.suptitle("title of figue") # suptitle() to give title of entire figure
plt.show() 
#Example 13: 
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.scatter(x,y)
plt.show()
#Example 14: 
#day one 
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
plt.scatter(x1,y1)
#day two 
x2 = [2, 4, 6, 8, 10]
y2 = [2, 4, 6, 8, 10]
plt.scatter(x2,y2 , c= y2 , cmap="viridis" , s = 100, alpha=0.5)
plt.colorbar()
plt.show()
#Example 15: 
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.bar(x,y)
plt.show()
# Example 16: 
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.barh(x,y)
plt.show()
#example 17: 
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.hist(x) 
plt.show()
#example 18: 
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.hist(x, bins=y) # change y to bins=y to specify the bin edges
plt.show()
#Example 19
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.pie(y)
plt.show()
#example 20: 
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
label_name = ["A", "B", "C", "D", "E"] # add labels for each data point
plt.pie(y, labels= label_name) # specify the correct variable name for the labels
plt.title("Pie chart")
plt.show()
#example 21: 
import matplotlib.pyplot as plt
label_name = ["A", "B", "C", "D", "E"] 
size = [20, 25, 35, 14, 6]
colors= ["red", "pink", "yellow", "orange", "purple"]
plt.pie(size, labels= label_name, colors= colors, startangle=90)
plt.title("pie chart with colors")
plt.show()











