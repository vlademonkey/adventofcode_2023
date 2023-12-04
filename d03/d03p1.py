
sum = 0
matrix = []
with open("input.txt") as fin:
    for line in fin:
        matrix.append([c for c in line.strip()])

curr_num = ""
curr_adjacent = False

for row_idx,row_val in enumerate(matrix):
    for col_idx,col_val in enumerate(row_val):
        if not col_val.isnumeric():
            if curr_adjacent:
                sum += int(curr_num)
            curr_num = ""
            curr_adjacent = False
        else:
            # print(f"int:{col_val} at {row_idx},{col_idx}")
            curr_num += col_val
            # check surrounding for symbol
            for chk_row_idx in range(max(row_idx-1,0), min(row_idx+1,len(matrix))+1):
                if chk_row_idx > len(matrix)-1:
                    continue
                for chk_col_idx in range(max(col_idx-1,0), min(col_idx+1,len(row_val))+1):
                    if chk_col_idx > len(row_val)-1:
                        continue
                    if not matrix[chk_row_idx][chk_col_idx].isnumeric() and matrix[chk_row_idx][chk_col_idx] != ".":
                        curr_adjacent = True

print(sum)
