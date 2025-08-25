import plotly.express as px

def generate_chart(df):
    # Simple logic to choose chart type
    if df.shape[1] >= 2:
        return px.bar(df, x=df.columns[0], y=df.columns[1])
    else:
        return px.histogram(df, x=df.columns[0])
