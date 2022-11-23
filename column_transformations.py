import pandas as pd
import numpy as np
from scipy import stats


def filter_df_by_zscore(data_frame, column, zscore_threshold = 3):
	"""
	Inputs:
		data_frame: a pandas dataframe
		column: column in the dataframe to perform z-score filtering on
		zscore_threshold: absolute value z-score threshold over which records will be filtered
	Output:
		data_frame_filtered: pandas dataframe with records above z-score threshold excluded
	"""

	new_col_name = column + '_abs_z_score'
	data_frame[new_col_name] = np.abs(stats.zscore(data_frame[column]))

	data_frame_filtered = data_frame[data_frame[new_col_name] < zscore_threshold]

	return data_frame_filtered