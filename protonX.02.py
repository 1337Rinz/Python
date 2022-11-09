#Tìm trong mảng [xs] xem có bao nhiêu chuỗi là chuỗi con của y



def exercise2(xs, y):
    
    # Lập trình tại đây
    result = 0
    # y = y.split()

    for i in xs:
      if i in y:
        result += 1

    return result
    
    
    
# TEST CODE
SECOND = '2'
try:
    q = SECOND
    inp = [
      (['hổ', 'bò', 'gà', 'tủ lạnh'], 'hổ mang bò lên núi'), 
      (['hổ', 'bò', 'gà', 'tủ lạnh'], 'Hổ mang bò lên núi'), 
    ]
    out = [
    2,
    1,
    ]
    
    res_list = [False for _ in range(len(inp))]
    for i, inpi in enumerate(inp):
        res_list[i] = exercise2(*inpi) == out[i]
    
    ans = 'Câu {}:\n'.format(q)
    for i, item in enumerate(res_list):
        if not res_list[i]:
            ans += "\nTest case {} được tính đúng?: {}.\n\t Giá trị đầu vào: {}".format(i + 1, res_list[i], inp[i])
        else:
            ans += "\nTest case {} được tính đúng?: {}.".format(i + 1, res_list[i])
    print(ans)
except Exception as e:
    print("Lỗi thực thi: ", e)
