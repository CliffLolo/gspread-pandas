import gspread
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
goocleclient = gspread.service_account()

sheet = goocleclient.open("Product Data").worksheet("January")

# Load data into a pandas DataFrame
df = pd.DataFrame(sheet.get_all_records())