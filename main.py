import plotly.graph_objects as go
import pandas

debt_table = pandas.read_csv("debt.csv")

plot = go.Figure(go.Scatter(
    x = debt_table["Record Date"],
    y = debt_table["Debt Held by the Public"],
    hovertemplate = "Date: %{x}<br>Debt: %{y:$,.0f}",
))

plot.update_layout(
    title = "Federal Debt Over Time",
    xaxis_title = "Date",
    yaxis_title = "Total Federal Debt",
)

plot.show()
