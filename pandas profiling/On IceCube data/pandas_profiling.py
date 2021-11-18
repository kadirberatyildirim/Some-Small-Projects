
import pandas_profiling as pp
import numpy as np
import pandas as pd

path = 'Search_for_point_sources_with_first_year_of_IC86_data/'

df_tabulatedAeff = pd.read_csv(path + 'TabulatedAeff.csv')

tabulatedAeff_profile = pp.ProfileReport(df_tabulatedAeff)


