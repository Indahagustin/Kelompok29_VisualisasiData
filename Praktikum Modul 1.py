import streamlit as st

# Judul aplikasi
st.title("Praktikum Modul 1 - Visualisasi Data")

# Header untuk identitas kelompok
st.header("Kelompok 29")

# Subheader untuk daftar anggota
st.subheader("Anggota Kelompok:")

# Plain text untuk nama dan NIM
st.text("1. Amirullah - 0110222106")
st.text("2. Indah Agustin - 0110222250")
st.text("3. Miftahul Jannah - 0110222101")

# Caption sebagai keterangan tambahan
st.caption("Mata Kuliah: Visualisasi Data | Semester 7")


# Basic text output
st.write("Hello")
st.write("World!!!!!")


# Displaying different text formats
st.write('World!!!!')
st.title("This is our Title")
st.header("""This is our Header""")
st.subheader("""This is our Sub-header""")
st.caption("""This is our Caption""")

# Displaying Plain Text
st.text("Hi,\nPeople\t!!!!!!!!!")
st.text('Welcome to')
st.text(""" Streamlit's World""")

# Displaying Markdown
st.markdown("# Hi,\n# ***People*** \t!!!!!!!!!!")
st.markdown('## Welcome to')
st.markdown("""### Streamlit's World""")

# Displaying LaTeX
st.latex(r'''cos^2\theta = 1 - 2sin^2\theta''')
st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")
st.latex(r'''\frac{\partial u}{\partial t} = h^2 \left( \frac{\partial^2 u}{\partial x^2} 
+ \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right)''')

# Displaying Python Code
st.subheader("""Python Code""")
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

# Display Java Code
st.subheader("Java Code")
st.code("""public class GFG {
    public static void main(String args[])
        {
        System.out.println("Hello World");
    }
}""", language='javascript')
st.subheader("""JavaScript Code""")
st.code("""<p id="demo"></p>
<script>
try {
adddlert("Welcome guest!")
}
catch(err) {
    document.getElementById("demo").innerHTML = err.message;
}
</script>""")

import streamlit as st
import pandas as pd
import numpy as np
#defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))
st.dataframe(df)

import streamlit as st
import pandas as pd
import numpy as np
#defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))

#Highlighting minimum value objects
st.dataframe(df.style.highlight_min(axis=0))

import streamlit as st
import pandas as pd
import numpy as np
#defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))
#defining data in table
st.table(df)

import streamlit as st
#Defining Metrics
st.metric(label="Temperature", value="31 °C", delta="1.2 °C" )

import streamlit as st
#Defining Columns(3)
c1, c2, c3 = st.columns(3)
# Defining Metrics
c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric(label="Population", value="123 Billions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Customers", value=100, delta=10, delta_color="off")
st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456", "-1132649")

import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))
# defining multiple arguments in write function
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nWrite is Super function")

# importing Necessary Libraries
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

# Defining random Values for Chart
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b'])
# Defining Chart
chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b'])

# Defining Chart in write() function
st.write(chart)

# Math calculations with no functions defined
"Adding 5 & 4 =", 5+4

# Displaying Variable 'a' and its value
a = 5
'a', a

# Markdown with Magic
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""

# Dataframe using magic
import pandas as pd
df = pd.DataFrame({'col': [1,2]})
'dataframe', df

# Magic working on Charts
import matplotlib.pyplot as plt
import numpy as np
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
# Magic chart
"chart", chart

import streamlit as st
st.write("Displaying an Images")
# Displaying Image by specifying path
st.image("D:/GreenSeaTurtle-2.jpg")
# Image Courtesy by unsplash
st.write("Image Courtesy: unsplash.com")

import streamlit as st
# Image Courtesy
st.write("Diplaying Multiple Images")
# Listing out animal images
animal_images = [
'D:/animal1.jpg',
'D:/animal2.jpg',
'D:/animal3.jpg',
'D:/animal4.jpg',
]

# Displaying Multiple images with width 150
st.image(animal_images, width=150)
# Image Courtesy
st.write("Image Courtesy: Unplash")

import streamlit as st
import base64

# Function to set Image as Background
def add_local_background_image(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Image Courtesy: unsplash")
    st.markdown(
    f"""
    <style>
    .stApp {{
    background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
    background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

st.write("Background Image")
# Calling Image in function
add_local_background_image('D:/animal1.jpg')

import streamlit as st
from PIL import Image

original_image = Image.open("D:/animal1.jpg")
# Display Original Image
st.title("Original Image")
st.image(original_image)

# Resizing Image to 600*400
resized_image = original_image.resize((600, 400))
# Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)

import streamlit as st
st.title('Creating a Button')
# Defining a Button
button = st.button('Click Here')
if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')

import streamlit as st
st.title('Creating Radio Buttons')
# Defining Radio Button
gender = st.radio(
"Select your Gender",
('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")

import streamlit as st
st.title('Creating Checkboxes')
st.write('Select your Hobbies:')
# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

import streamlit as st
st.title('Creating Dropdown')
# Creating Dropdown
hobby = st.selectbox('Choose your hobby: ',
('Books', 'Movies', 'Sports'))

import streamlit as st
st.title('Multi-Select')
# Defining Multi-Select with Pre-Selection
hobbies = st.multiselect(
'What are your Hobbies',
['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
['Reading', 'Playing'])

import streamlit as st
st.title("Download Button")
# Creating Download Button
down_btn = st.download_button(
label="Download Image",
data=open("D:/animal1.jpg", "rb"),
file_name="tiger.jpg",
mime="image/jpg"
)
st.download_button(
label="Download CSV",
data=open("D:/avocado.csv", "rb"),
file_name='data.csv',
mime='csv',
)
import streamlit as st
import time
st.title('Progress Bar')
# Defining Progress Bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')

import streamlit as st
import time
st.title('Spinner')
# Defining Spinner
with st.spinner('Loading....'):
    time.sleep(5)
st.write('Hello Data Scientists')

import streamlit as st
st.title("Text Box")
# Creating Text box
name = st.text_input("Enter your Name")
st.write("Your Name is ", name)

import streamlit as st
# Creating Text Area
input_text = st.text_area("Enter your Review")
# Printing entered text
st.write("""You entered: \n""",input_text)

import streamlit as st
# Create number input
st.number_input("Enter your Number")

import streamlit as st
# Create number input
num = st.number_input("Enter your Number", 0, 10, 5, 2)
st.write("Min. Value is 0, \n Max. value is 10")
st.write("Default Value is 5, \n Step Size value is 2")
st.write("Total value after adding Number entered with step value is:", num)

import streamlit as st
st.title("Time")
# Defining Time Function
st.time_input("Select Your Time")

import streamlit as st
st.title("Date")
# Defining Date Function
st.date_input("Select Date")

import streamlit as st
import datetime
st.title("Date")
# Defining Time Function
st.date_input("Select Your Date", value=datetime.date(1989, 12, 25),
min_value=datetime.date(1987, 1, 1),
max_value=datetime.date(2005, 12, 1))

import streamlit as st
st.title("Select Color")
# Defining color picker
color_code = st.color_picker("Select your Color")
st.header(color_code)

import streamlit as st
import pandas as pd
st.title("CSV Data")
data_file = st.file_uploader("Upload CSV",type=["csv"])
details = st.button("Check Details")
if details:
    if data_file is not None:
        file_details = {"file_name":data_file.name, "file_type":data_file.type,
                        "file_size":data_file.size}
        st.write("File details")
        st.dataframe(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")

import streamlit as st
my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')

st.write(a)