import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation

df = pd.read_csv("city_populations.txt", usecols=['name', 'group', 'year', 'value'])
fig, ax = plt.subplots(figsize=(15, 8))

def draw_barchart(year):
    # Top 10 population
    dff = df[df['year'].eq(year)].sort_values(by='value', ascending=False).head(10)

    # Clear the axes.
    ax.clear()

    # Plot property
    dff = dff[::-1]

    # Color dictionary
    colors = {
        'India':'#adb0ff',
        'Europe':'#ffb3ff',
        'Asia':'#90d595',
        'Latin America':'#e48381',
        'Middle East':'#aafbff',
        'North America':'#f7bb5f',
        'Africa':'#eafb50'
    }

    group_lk = df.set_index('name')['group'].to_dict()

    # Add X and Y data
    ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])

    dx = dff['value'].max() / 200
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value-dx, i,     name,           size=14, weight=600, ha='right', va='bottom')
        ax.text(value-dx, i-.25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value+dx, i,     f'{value:,.0f}',  size=14, ha='left',  va='center')

    # Text location
    ax.text(1, 0.4, year, transform=ax.transAxes, size=46, ha='right')

    plt.box(False)

if __name__ == "__main__":
    animator = animation.FuncAnimation(fig, draw_barchart, frames=range(1968, 2019))


    # Display chart
    plt.show()

