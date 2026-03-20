import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def plot_crime_trends(df, province_col='province', year_col='year', crime_col='total_crimes'):
    """Line chart of total crimes per year per province."""
    fig = px.line(df, x=year_col, y=crime_col, color=province_col,
                  title='Crime Trends by Province')
    return fig

def plot_unemployment_heatmap(df, province_col='province', year_col='year', unemp_col='unemployment_rate'):
    """Heatmap of unemployment rates by province and year."""
    pivot_df = df.pivot(index=province_col, columns=year_col, values=unemp_col)
    plt.figure(figsize=(10,6))
    sns.heatmap(pivot_df, annot=True, fmt=".1f", cmap="YlOrRd")
    plt.title("Unemployment Rate Heatmap")
    plt.tight_layout()
    plt.show()

def plot_loadshedding_trends(df, date_col='date', stage_col='stage', province_col='province'):
    """Interactive bar chart showing load-shedding stages over time."""
    fig = px.bar(df, x=date_col, y=stage_col, color=province_col,
                 title="Load-Shedding Frequency by Province")
    return fig
