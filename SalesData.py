import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import sys
class SalesData(object):
    def __init__(self, dataset):
        self.dataset = dataset

    #4
    def eliminate_duplicates(self):
            if not self.dataset is None:
               df = pd.DataFrame(self.dataset)
               df.drop_duplicates(inplace=True)
               self.dataset = df
    #5
    def calculate_total_sales(self):
        total = self.dataset.groupby('Product')['Total'].sum()
        return total

    #6
    def calculate_total_sales_per_month(self):
        self.dataset['Month'] = pd.to_datetime(self.dataset['Date']).dt.month
        total_sales_per_month = self.dataset.groupby('Month')['Total'].sum()
        return total_sales_per_month

    #7
    def identify_best_selling_product(self):
        total_sales_per_product = self.dataset.groupby('Product')['Total'].sum()
        best_selling_product = total_sales_per_product.idxmax()
        return best_selling_product




    #8
    def identify_month_with_highest_sales(self):
        self.dataset['Month'] = pd.to_datetime(self.dataset['Date']).dt.month
        total_sales_per_month=self.dataset.groupby('Month')['Total'].sum()
        highest_sales_month=total_sales_per_month.idxmax()
        return highest_sales_month

    def identify_worst_selling_product(self):
        total_sales_per_product = self.dataset.groupby('Product')['Total'].sum()
        worst_selling_product = total_sales_per_product.idxmin()
        return worst_selling_product

    def average_sales_per_months(self):
        self.dataset['Date'] = pd.to_datetime(self.dataset['Date'])
        self.dataset['Month'] = self.dataset['Date'].dt.month
        sales_per_months = self.dataset.groupby('Month')['Total'].sum()
        average_sales_per_months = sales_per_months.mean()
        return average_sales_per_months


    #9
    def analyze_sales_data(self):
        best_selling_product = self.identify_best_selling_product()
        month_with_highest_sales = self.identify_month_with_highest_sales()
        result = {
            'best_selling_product': best_selling_product,
            'month_with_highest_sales': month_with_highest_sales,
        }
        return result

    #10
    def add_additional_values(self):

        self.calculate_total_sales()
        worst_selling_product = self.identify_worst_selling_product()
        average = self.average_sales_per_months()
        analysis_results = self.analyze_sales_data()
        analysis_results['minimest_selling_product'] = worst_selling_product
        analysis_results['average_sales'] = average
        return analysis_results


    #11
    def calculate_cumulative_sales(self):
        self.dataset['Date'] = pd.to_datetime(self.dataset['Date'])
        self.dataset['Month'] = self.dataset['Date'].dt.month
        cumulative_sales = self.dataset.groupby(['Product', 'Month'])['Quantity'].sum().groupby(level=0).cumsum()
        return cumulative_sales
    #12
    def add_90_values_column(self):
        self.dataset['discount'] = self.dataset['Total']*0.9

    #13
    def bar_chart_category_sum(self):

        quantity_per_product = self.dataset.groupby('Product')['Quantity'].sum()


        quantity_per_product.plot(kind='bar', ylabel='Sum of Quantities', xlabel='Product', title='Sum of Quantities Sold for Each Product')
        plt.show()

    #14
    def calculate_mean_quantity(self):
        total_array = self.dataset['Total'].values
        mean = np.mean(total_array)
        median = np.median(total_array)
        second_max = np.partition(total_array, -2)[-2]
        return mean, median, second_max
    #15
    def filter_by_sellings_or(self):
        if self.data is None:
            print("Data is empty")
            return
        condition = (self.dataset['Quantity'] > 5) | (self.dataset['Quantity'] == 0)
        filtered_data = self.dataset[condition]
        return filtered_data

    #15
    def filter_by_sellings_and(self):
        if self.dataset is None:
            print("Data is empty")
            return
        condition = (self.dataset['Price'] > 300) & (self.dataset['Quantity'] < 2)
        filtered_data = self.dataset[condition]
        return filtered_data

    #16
    def divide_by_2(self):
        self.dataset['BlackFridayPrice'] = self.dataset['Price'].div(2)

    #17
    def calculate_stats(self, columns=None):
        if columns is None:
            columns = self.data.columns

        stats = {}

        for col in columns:
            if col in self.data.columns:
                col_data = self.data[col]
                if col_data.dtype.kind in 'biufc':  # Check if data type is numeric
                    col_stats = {
                        'max': col_data.max(),
                        'sum': col_data.sum(),
                        'abs': col_data.abs().sum(),
                        'cumulative_max': col_data.cummax()
                    }
                    stats[col] = col_stats

        return stats


    #19
    def categorize_prices(self):
        self.dataset['Price category'] = pd.cut(self.dataset['Price'], bins=[-float('inf'), 50, 100, float('inf')],
                                       labels=['cheap', 'medium', 'expensive'])
        return self.dataset


#matplotlib
    def plot_total_sales_pie_chart(self):
        total_sales = self.calculate_total_sales()
        if total_sales is None:
            return
        plt.figure(figsize=(8, 8))
        plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%')
        plt.title('Total Sales by Product')
        plt.show()


    def plot_total_sales_3d(self):
        total_sales_per_month = self.calculate_total_sales_per_month()
        if total_sales_per_month is None:
            return
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        years = [d.year for d in total_sales_per_month.index]
        months = [d.month for d in total_sales_per_month.index]
        xpos = years
        ypos = months
        zpos = [0] * len(total_sales_per_month)  # z-position is zero
        dx = dy = 0.8
        dz = total_sales_per_month.values
        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b')
        ax.set_xlabel('Year')
        ax.set_ylabel('Month')
        ax.set_zlabel('Total Sales')
        ax.set_title('Total Sales per Month')
        plt.show()


    def plot_avg_sales_all_months_violin(self):
        avg_sales = self._average_sales_per_months()
        if avg_sales is None:
            return
        plt.figure(figsize=(10, 6))
        plt.violinplot([avg_sales], vert=False)
        plt.title('Average Sales per Month (Violin Plot)')
        plt.xlabel('Sales')
        plt.ylabel('Month')
        plt.grid(True)
        plt.show()



    def plot_cumulative_sales_bar(self):
        cumulative_sales = self.calculate_cumulative_sales()
        if cumulative_sales is None:
            return
        plt.figure(figsize=(10, 6))
        cumulative_sales.plot(kind='bar', color='skyblue')
        plt.title('Cumulative Sales per Product')
        plt.xlabel('Product')
        plt.ylabel('Cumulative Sales')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()


    def plot_divided_by_2_heatmap(self):
        if self.dataset is None:
            print("Error: No data available")
            return
        plt.figure(figsize=(10, 6))
        plt.imshow([self.dataset['BlackFridayPrice']], cmap='hot', aspect='auto')
        plt.colorbar(label='Price divided by 2')
        plt.title('Price divided by 2 Heatmap')
        plt.xlabel('Data points')
        plt.ylabel('BLACKFRIDAY')
        plt.show()


    def plot_divided_by_2_histogram(self):
        if self.dataset is None:
            print("Error: No data available")
            return
        plt.figure(figsize=(10, 6))
        plt.hist(self.dataset['BlackFridayPrice'], bins=20, color='skyblue', edgecolor='black')
        plt.title('Histogram of Price divided by 2 for BLACKFRIDAY')
        plt.xlabel('Price divided by 2')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()


    def plot_price_category_line(self):
        categorized_data = self.categorize_prices()
        price_counts = categorized_data['category'].value_counts()
        plt.figure(figsize=(10, 6))
        plt.plot(price_counts.index, price_counts.values, marker='o', linestyle='-')
        plt.title('Number of Prices in Each Category')
        plt.xlabel('Price Category')
        plt.ylabel('Count')
        plt.grid(True)
        plt.show()

    # Seaborn

    def plot_total_sales_seaborn(self):
        total_sales = self.calculate_total_sales()
        if total_sales is None:
            return
        plt.figure(figsize=(10, 6))
        sns.barplot(x=total_sales.index, y=total_sales.values, hue=total_sales.index, palette='viridis',
                    legend=False)
        plt.title('Total Sales per Product')
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()


    def plot_total_sales_per_month_seaborn_stripplot(self):
        total_sales_per_month = self.calculate_total_sales_per_month()
        if total_sales_per_month is None:
            return
        plt.figure(figsize=(10, 6))
        sns.stripplot(x=total_sales_per_month.index.strftime('%Y-%m'), y=total_sales_per_month.values)
        plt.title('Total Sales per Month')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()



    def plot_total_sales_per_month_seaborn_lineplot(self):
        total_sales_per_month = self.calculate_total_sales_per_month()
        if total_sales_per_month is None:
            return
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=total_sales_per_month.index.strftime('%Y-%m'), y=total_sales_per_month.values)
        plt.title('Total Sales per Month')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()


    def plot_mean_quantity_boxplot(self):
        mean, median, second_max = self.calculate_mean_quantity()
        data_to_plot = {'Mean': mean, 'Median': median, 'Second Max': second_max}
        plt.figure(figsize=(8, 6))
        sns.boxplot(data=[data_to_plot.values()])
        plt.title('Mean, Median, and Second Max Quantity')
        plt.ylabel('Quantity')
        plt.show()

    def plot_filtered_data(self):
        filtered_data_or = self.filter_by_sellings_or()
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.dataset, x='Price', y='Quantity', color='lightblue', label='Original Data')
        sns.scatterplot(data=filtered_data_or, x='Price', y='Quantity', color='green', label='Filtered Data')
        plt.title('Filtered Data')
        plt.xlabel('Price')
        plt.ylabel('Quantity')
        plt.legend()
        plt.show()



    def plot_price_distribution(self):
        self.categorize_prices()
        plt.figure(figsize=(8, 6))
        sns.countplot(x='category', data=self.dataset, hue='category', palette='viridis', legend=False)
        plt.title('Price Distribution by Category')
        plt.xlabel('Price Category')
        plt.ylabel('Count')
        plt.show()




    # task 7
    #3
    def generate_random_number(self, product_name):
        if self.dataset is None:
            print("Data is empty")
            return
        product_data = self.dataset[self.dataset['Product'] == product_name]
        if product_data.empty:
            return "the product not found"
        random_number = np.random.randint(product_data['Quantity'].values[0], self.dataset['Price'].max())
        arr_random = {'low number': product_data['Quantity'].values[0], 'random number': random_number,
                      'high number': self.dataset['Price'].max()}
        return arr_random

    #4
    def print_python_version():
        print("python version", sys.version)



    #5
    def process_values(*args):
        result_dict = {}
        for value in args:
            if isinstance(value, (int, float)):
                print(value)
            elif isinstance(value, str):
                result_dict[value] = value
        return result_dict




    #6
    def print_specific_rows(self):
        print("first 3 lines\n")
        print(self.dataset.head(3))
        print("last 2 lines\n")
        print(self.dataset.tail(2))
        random_row_index = np.random.randint(0, len(self.dataset) - 1)
        print("random line")
        print(self.dataset.iloc[random_row_index])
    #7
    def move_over_table(self):
        for i in self.dataset:
            if i == 'Total':
                print("Total:")
                print(self.dataset[i])
            if i == 'Price':
                print("Price:")
                print(self.dataset[i])
            if i == 'Quantity':
                print("Quantity:")
                print(self.dataset[i])




















