import pandas as pd
from collections import Counter

# Display the count
def print_array(result):
    for element, count in result.items():
        print(f'{element}')
    for element, count in result.items():
        print(f'{count}')

def get_analysis(df, column_name):
    values_circumstance = df[column_name].unique()
    circumstance_element_counts = Counter(df[column_name])
    result = {element: circumstance_element_counts.get(element, 0) for element in values_circumstance}
    print_array(result)
    print('**********')



df = pd.read_csv('MD.csv')
column_names = ['insert names here']
label_names = ['Insert names here']
label_names = ['Topic']
for name in label_names:
    print('Doing Analysis for:',  name)
    get_analysis(df, name)
