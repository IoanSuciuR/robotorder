from RPA.HTTP import HTTP
from RPA.Tables import Tables


def download_excel_file():
    """Downloads csv file from the given URL"""
    http = HTTP()
    http.download(url="https://robotsparebinindustries.com/orders.csv",target_file="Input\orders.csv", overwrite=True)
   

def get_orders():

    exTable = Tables()
    ordersTable = exTable.read_table_from_csv("Input\orders.csv")
    return ordersTable