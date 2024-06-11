strs = ["dog", "racecar", "car"]

ans =" "
for i in zip(*strs):
    if len(set(i)) ==1:
        ans = ans + i[0]
    else:
        break
        ans == ""
print(ans)    