from flask import Flask, render_template, request, jsonify # type: ignore

import google.generativeai as genai # type: ignore

genai.configure(api_key='AIzaSyAsGsXh91wkfhdg3dOY7CsFPb9w3G3Ilog')

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_speech', methods=['POST'])
def handle_speech():
    data = request.json
    convo.send_message('''for the input generate flow chart for revenue system  process we get  the code:
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
                   
folder_path = 'C:\GOWTHAM\hackathon\static\images'

# Render the DOT code to a PNG file in the specified folder
dot.render(folder_path + 'image', format='png')

# Display the generated image
Image('image.png')
similarly provide code for '''+data['transcript'] +''',dont forget to import necessary libraries,provide only the code dont include the word python and the symbol ``` in the output''')
    try:
      exec(convo.last.text)
    except Exception as e:
      print("improper prompt cannot create proper flow diagram:", e)
    diagram_filename="\static\imagesimage.png"

    return jsonify({'transcript':convo.last.text,'diagram_filename': diagram_filename})
    
if __name__ == '__main__':
    app.run(debug=True)
