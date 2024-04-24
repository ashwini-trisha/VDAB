from graphviz import Digraph
from IPython.display import Image

# Create a Digraph object
dot = Digraph()

# Define node attributes
dot.attr('node', shape='rectangle', style='filled', fillcolor='lightblue', fontname='Arial')
dot.attr('edge', fontname='Arial')

# Add nodes
dot.node('Start', label='Start')
dot.node('ReadData', label='Read revenue report data')
dot.node('CalcTotal', label='Calculate total revenue for each product')
dot.node('CalcPercentage', label='Calculate revenue percentage for each product')
dot.node('SortData', label='Sort revenue report by revenue percentage')
dot.node('CreateChart', label='Create bar chart of revenue percentages')
dot.node('ShowChart', label='Show bar chart')
dot.node('End', label='End')

# Add edges
dot.edge('Start', 'ReadData')
dot.edge('ReadData', 'CalcTotal')
dot.edge('CalcTotal', 'CalcPercentage')
dot.edge('CalcPercentage', 'SortData')
dot.edge('SortData', 'CreateChart')
dot.edge('CreateChart', 'ShowChart')
dot.edge('ShowChart', 'End')

# Specify the folder path to store the generated image
folder_path = 'C:\GOWTHAM\hackathon\static\images\\'

# Render the DOT code to a PNG file in the specified folder
dot.render(folder_path + 'RevenueReportFlowchart', format='png')

# Display the generated image
Image('RevenueReportFlowchart.png')
