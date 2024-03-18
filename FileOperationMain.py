import pandas as pd
from FileOperation import FileOperation
class FileOperationMain:
    file_op = FileOperation()
    file_op.read_csv("YafeNof.csv")
    data = {
        'Product': ['A', 'B', 'A', 'B', 'C', 'A', 'B', 'C'],
        'Quantity': [10, 20, 30, 40, 50, 60, 70, 80],
        'Price': [100, 150, 200, 250, 300, 350, 400, 450],
        'Date': ['2024-01-01', '2024-01-15', '2024-02-05', '2024-02-20', '2024-03-10', '2024-03-15', '2024-04-05',
                 '2024-04-20']
    }
    file_op.save_to_csv(pd.DataFrame(data), "output.csv")






