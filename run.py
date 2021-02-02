import streamlit as st

from tech import read_impact_hour_data, read_cstk_data
from tech import ImpactHoursData, ImpactHoursFormula, Hatch, DandelionVoting
import panel as pn
pn.extension()

impact_hour_data_1, impact_hour_data_2 = read_impact_hour_data()

i = ImpactHoursData()
impact_data_view = pn.Row(i, i.impact_hours_accumulation)

st.bokeh(i.impact_hours_accumulation)