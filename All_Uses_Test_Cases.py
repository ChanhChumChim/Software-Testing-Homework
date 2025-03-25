import pytest
from Elec_Price import Electricity_Bill

def test_invalid_kWh():
    assert Electricity_Bill(-5, "hộ gia đình") == "Lỗi: Số kWh phải là số nguyên dương!"

def test_household_50():
    assert Electricity_Bill(50, "hộ gia đình") == "Tổng số tiền điện cần thanh toán: 75000 VND"

def test_household_75():
    assert Electricity_Bill(75, "hộ gia đình") == "Tổng số tiền điện cần thanh toán: 125000 VND"

def test_household_150():
    assert Electricity_Bill(150, "hộ gia đình") == "Tổng số tiền điện cần thanh toán: 275000 VND"

def test_household_250():
    assert Electricity_Bill(250, "hộ gia đình") == "Tổng số tiền điện cần thanh toán: 525000 VND"

def test_business_100():
    assert Electricity_Bill(100, "doanh nghiệp") == "Tổng số tiền điện cần thanh toán: 200000 VND"

def test_business_150():
    assert Electricity_Bill(150, "doanh nghiệp") == "Tổng số tiền điện cần thanh toán: 325000 VND"

def test_business_250():
    assert Electricity_Bill(250, "doanh nghiệp") == "Tổng số tiền điện cần thanh toán: 575000 VND"

def test_invalid_customer():
    assert Electricity_Bill(50, "khách sạn") == "Lỗi: Loại khách hàng không hợp lệ."

if __name__ == "__main__":
    pytest.main()
