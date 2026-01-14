import pandas as pd

df = pd.read_csv('data/bronze/metadata/grid_coordinates_all.csv')
print('Shape:', df.shape)
print('\nColumns:', df.columns.tolist())
print('\ncell_type value counts:')
print(df['cell_type'].value_counts())
print('\nFirst 5 land cells:')
print(df[df['cell_type']=='land'][['grid_id', 'centroid_lat', 'centroid_lon', 'cell_type']].head())
