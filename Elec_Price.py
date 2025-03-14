def Electricity_Bill(kWh_number, type_of_customers):
    if not isinstance(kWh_number, int) or kWh_number < 0:
        return "Lỗi: Số kWh phải là số nguyên dương!"
    
    type_of_customers = type_of_customers.lower()
    Electricity_Price = 0
    
    if type_of_customers == "hộ gia đình":
        if kWh_number <= 50:
            Electricity_Price = kWh_number * 1500
        elif kWh_number <= 100:
            Electricity_Price = 50 * 1500 + (kWh_number - 50) * 2000
        elif kWh_number <= 200:
            Electricity_Price = 50 * 1500 + 50 * 2000 + (kWh_number - 100) * 2500
        else:
            Electricity_Price = 50 * 1500 + 50 * 2000 + 100 * 2500 + (kWh_number - 200) * 3000
    
    elif type_of_customers == "doanh nghiệp":
        if kWh_number <= 100:
            Electricity_Price = kWh_number * 2000
        elif kWh_number <= 200:
            Electricity_Price = 100 * 2000 + (kWh_number - 100) * 2500
        else:
            Electricity_Price = 100 * 2000 + 100 * 2500 + (kWh_number - 200) * 3500
    else:
        return "Lỗi: Loại khách hàng không hợp lệ."
    
    return f"Tổng số tiền điện cần thanh toán: {Electricity_Price} VND"

if __name__ == "__main__":
    try:
        kWh_number = int(input("Nhập số kWh tiêu thụ: "))
        type_of_customers = input("Nhập loại khách hàng (hộ gia đình/doanh nghiệp): ")
        print(Electricity_Bill(kWh_number, type_of_customers))
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")