import openpyxl

def get_login_data():
    workbook = openpyxl.load_workbook('C://Users//User//PycharmProjects//Selenium//part_c//sauce-framework//test_data//loginData.xlsx')
    sheet = workbook['Saucedemodata']

    data = []
    for row in sheet.iter_rows(min_row=2,values_only=True):
        data.append(row)

    return data
