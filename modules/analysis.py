import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

class Analysis:
    def __init__(self, path):
        self.db_path = path

    def load_data(self, table_name):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query(f'select * from {table_name}', conn)
        conn.close()
        return df

    def analyze_students_per_major(self):
        students_df = self.load_data('Students')
        students_per_major = students_df.groupby('Major').size().reset_index(name='Count')
        gender_ratio_per_major = students_df.groupby(['Major', 'Gender']).size().unstack().fillna(0)
        gender_ratio_per_major['Total'] = gender_ratio_per_major['Female'] + gender_ratio_per_major['Male']
        return students_per_major, gender_ratio_per_major

    def analyze_results_comparison(self):
        students_df = self.load_data('Students')
        results_comparison = students_df.groupby('Major')['test_score'].describe()
        return results_comparison

    def analyze_age_vs_test_scores(self):
        students_df = self.load_data('Students')
        age_test_score_corr = students_df[['Age', 'test_score']].corr().iloc[0, 1]
        return age_test_score_corr

    def analyze_regional_distribution_vs_test_scores(self):
        students_df = self.load_data('Students')
        region_test_scores = students_df.groupby('Region')['test_score'].describe()
        return region_test_scores

    def plot_students_per_major(self, students_per_major):
        plt.figure(figsize=(10, 5))
        plt.bar(students_per_major['Major'], students_per_major['Count'], color=['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red'])
        plt.title('Number of Students per Major')
        plt.xlabel('Major')
        plt.ylabel('Number of Students')
        plt.xticks(rotation=45, ha='right')
        plt.show()

    def plot_gender_ratio_per_major(self, gender_ratio_per_major):
        plt.figure(figsize=(10, 5))
        bar_width = 0.35
        index = range(len(gender_ratio_per_major))
        plt.bar(index, gender_ratio_per_major['Female'], bar_width, label='Female', color='violet')
        plt.bar(index, gender_ratio_per_major['Male'], bar_width, label='Male', color='indigo', bottom=gender_ratio_per_major['Female'])
        plt.xlabel('Major')
        plt.ylabel('Number of Students')
        plt.title('Gender Distribution per Major')
        plt.xticks(index, gender_ratio_per_major.index, rotation=45, ha='right')
        plt.legend()
        plt.tight_layout()
        plt.show()