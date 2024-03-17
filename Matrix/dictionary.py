import pandas as pd

adj_matrix = pd.read_csv('adjacency_matrix_adult_diseases.csv')

symptom_disease = {}

for symptom in adj_matrix.sum()[adj_matrix.sum() == 1].index:
    disease = adj_matrix.loc[adj_matrix[symptom] == 1].iloc[0, 0]
    symptom_disease[symptom] = disease

print(symptom_disease)