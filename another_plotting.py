import altair as alt
import altair_viewer
import pandas as pd
from labels import *
from data_tratement import *
from Stadistics import *

def plotting_line_altair(data, x_axis, y_axis, lit_min = 0, lit_max = 0,  Eca = 0,switch_limit_manual = True):
    scatter = (
        alt.Chart(data)
        .mark_line()
        .encode(
            x=alt.X(x_axis, title="Fecha"),
            y=alt.Y(y_axis, title=rename_colum[y_axis])

        ).properties(width=600,height=400)
        .interactive()
    )

    return scatter.to_html()


