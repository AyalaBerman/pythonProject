from SalesData import SalesData
from FileOperation import FileOperation
import pandas as pd


if __name__ == '__main__':
    file_op = FileOperation()
    data = file_op.read_csv("YafeNof.csv")
    df = pd.DataFrame(data)
    sales_data = SalesData(df)
    # 2

    # sales_data.eliminate_duplicates()
    # sales_data.calculate_total_sales()
    # sales_data._calculate_total_sales_per_month()
    # sales_data._identify_best_selling_product()
    # sales_data._identify_month_with_highest_sales()
    # sales_data.analyze_sales_data()
    # sales_data.add_additional_values()
    #
    # #3
    #
    # sales_data.calculate_cumulative_sales()
    # sales_data.bar_chart_category_sum()
    # sales_data.calculate_mean_quantity()
    # sales_data.divide_by_2()
    # sales_data.categorize_prices()



