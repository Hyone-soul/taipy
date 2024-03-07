from taipy.gui import Gui
from data.data import data as dataset

from utils.graphs import bubble_chart_whole, treemap_whole

from pages.root import root_md
from pages.district.district import district_md

nepal = """
# **Nepal**{: .color-primary} Statistics

<br/>

<|layout|columns= 1 1 1 1|gap=100px|class_name=m1|

<|card|
**Total Population**{:.color-primary}
<|{total_population}|text|class_name=h2|>
|>

<|card|
**Total Male Population**{:.color-primary}
<|{total_male_population}|text|class_name=h2|>
|>

<|card|
**Total Female Population**{:.color-primary}
<|{total_female_population}|text|class_name=h2|>
|>

|>

<br/>

# Visualization in **Graphs**{:.color-primary}

<|layout|columns=1 1|class_name=m2|

<|{bubble_chart_whole_data}|chart|mode=markers|x=Total Male|y=Total Female|marker={bubble_chart_whole_marker}|text=Texts|>

<|{treemaps_data}|chart|type=treemap|labels=label|values=values|>

|>
"""


def getNepalStats():
    total_population = str(dataset['Total population'].sum())
    total_male_population = str(dataset['Total Male'].sum())
    total_female_population = str(dataset['Total Female'].sum())

    return total_population, total_male_population, total_female_population


total_population, total_male_population, total_female_population = getNepalStats()

bubble_chart_whole_data, bubble_chart_whole_marker, bubble_chart_whole_layout = bubble_chart_whole()

treemaps_data = treemap_whole()
pages = {
    "/": root_md,
    "district": district_md,
    "nepal": nepal,
    "map": "Map"
}

if __name__ == "__main__":
    Gui(pages=pages).run(title="From Taipy Quine Quest-007", use_reloader=True)
