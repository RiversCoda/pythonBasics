# 35只鸡兔94只脚，求鸡兔各多少只
# cnt = 35
# foot = 94
# for i in range(0, cnt + 1):# python中range(0, cnt + 1)表示从0到cnt，不包括cnt+1，类似于C语言的for(i=0;i<cnt+1;i++)
#     j = cnt - i
#     if i * 2 + j * 4 == foot:
#         print(f"鸡{i}只，兔{j}只")
#         break

cnt = 35
foot = 94
for i in range(0, cnt+1):
    j = cnt - i
    if i * 2 + j * 4 == foot:
        print("鸡", i, "只兔", j, "只")
        break