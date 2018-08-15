#Making a basic Bokeh graph

#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare some data
x=[0,2,3,4,5,6]
y=[7,8,9,10,11,12]

#prepare the output file
output_file("Line.html")

#create a figure object
f=figure()

#create line plot
f.line(x,y)
show(f)
