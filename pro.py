import csv
import pandas as pd
import plotly.express as px
with open("Student Marks vs Days Present.csv") as file1:
   reader=csv.DictReader(file1)
   pro=px.scatter(reader, x="Marks In Percentage", y="Days Present")
   pro.show()
    
