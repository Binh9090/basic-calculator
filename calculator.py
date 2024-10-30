def calculator():
    print("Các phép toán: +, -, *, /")
    operation = input("Bạn muốn làm phép tính nào? ")

    num1 = float(input("Số thứ nhất: "))
    num2 = float(input("Số thứ hai: "))

    if operation == '+':
        result = num1 + num2
        print("Kết quả:", result)
    elif operation == '-':
        result = num1 - num2
        print("Kết quả:", result)
    elif operation == '*':
        result = num1 * num2
        print("Kết quả:", result)
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print("Kết quả:", result)
        else:
            print("Lỗi: Không thể chia cho 0!")
    else:
        print("Phép toán không hợp lệ.")

calculator()