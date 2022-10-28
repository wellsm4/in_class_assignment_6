import plotly.express as px
import pandas

data_frame = pandas.read_csv("./kaggle/country_data.csv")

data_frame["xp_per_hr"] = data_frame["XP"] / data_frame["Hours"]

fig = px.scatter(x=data_frame["Players"], y=data_frame["xp_per_hr"])
fig.show()

corr_matrix = data_frame.corr()
fig2 = px.imshow(corr_matrix, text_auto = "True")
fig2.show()