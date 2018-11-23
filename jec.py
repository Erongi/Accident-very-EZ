import pandas as pd
import pygal as pg
def main():
    df = pd.read_excel('data.xlsx', sheet_name='Query_fetival')
    tag = 'อายุ'
    bar_chart = pg.Bar()
    bar_chart.add(tag, df[tag])
    bar_chart.render_to_file('bar_chart.svg')
main()
