"""
                   HƯỚNG DẪN CÁCH COMMENT TRONG PYTHON
================================================================================
Comment là cách để giải thích code, ghi chú hoặc vô hiệu hóa code tạm thời.
Python hỗ trợ nhiều cách comment khác nhau để phù hợp với từng mục đích sử dụng.
================================================================================
"""

#------------------------------------------------------------------------------
# 1. COMMENT MỘT DÒNG (SINGLE-LINE COMMENTS) 
#------------------------------------------------------------------------------
# Sử dụng dấu # để comment một dòng

# Đây là một comment một dòng
name = "Alice"    # Khai báo biến name

# Cách tính điểm trung bình
average = (math + physics + chemistry) / 3


#------------------------------------------------------------------------------
# 2. COMMENT NHIỀU DÒNG (MULTI-LINE COMMENTS)
#------------------------------------------------------------------------------

# Cách 1: Sử dụng # cho mỗi dòng
# Đây là comment dòng 1
# Đây là comment dòng 2
# Đây là comment dòng 3

# Cách 2: Sử dụng chuỗi nhiều dòng với dấu nháy kép/đơn 3 lần
"""
Đây là comment nhiều dòng
Sử dụng dấu nháy kép ba lần
Thường dùng để viết docstring
"""

'''
Đây là chuỗi nháy đơn
'''

#------------------------------------------------------------------------------
# 3. DOCSTRING (DOCUMENTATION STRINGS)
#------------------------------------------------------------------------------
# Docstring là comment đặc biệt mô tả chức năng của function, class, module

def calculate_average(math, physics, chemistry):
   """
   Tính điểm trung bình của 3 môn học
   
   Parameters:
       math (float): Điểm môn Toán
       physics (float): Điểm môn Lý
       chemistry (float): Điểm môn Hóa
   
   Returns:
       float: Điểm trung bình của 3 môn
   """
   return (math + physics + chemistry) / 3


#------------------------------------------------------------------------------
# 4. QUY TẮC VIẾT COMMENT TỐT
#------------------------------------------------------------------------------

# BAD: Comment không cần thiết
x = x + 1    # Tăng x lên 1

# GOOD: Comment giải thích lý do/logic
retry_count = retry_count + 1    # Tăng số lần thử lại sau khi kết nối thất bại

# BAD: Comment lặp lại code
# Kiểm tra age có lớn hơn 18 không
if age > 18:
   pass

# GOOD: Comment giải thích ý nghĩa nghiệp vụ
# Kiểm tra người dùng đã đủ tuổi đăng ký tài khoản
if age > 18:
   pass


#------------------------------------------------------------------------------
# 5. SỬ DỤNG COMMENT ĐỂ DEBUG TẠM THỜI
#------------------------------------------------------------------------------

def process_data():
   # print("Debug: Bắt đầu xử lý")    # Comment tạm thời dòng debug
   result = complex_calculation()
   # print("Debug: Kết quả=", result)  # Comment tạm thời dòng debug
   return result


#------------------------------------------------------------------------------
# 6. VÍ DỤ THỰC TẾ TRONG TESTING
#------------------------------------------------------------------------------

def test_login():
   """
   Test case kiểm tra chức năng đăng nhập
   
   Các bước thực hiện:
   1. Nhập username và password hợp lệ
   2. Click nút đăng nhập
   3. Kiểm tra redirect về trang chủ
   """
   # Setup test data
   username = "testuser"
   password = "Test@123"
   
   # Thực hiện login
   login_result = login(username, password)
   
   # Kiểm tra kết quả
   assert login_result.success == True    # Đảm bảo đăng nhập thành công
   assert login_result.redirect_url == "/home"    # Kiểm tra redirect đúng trang
