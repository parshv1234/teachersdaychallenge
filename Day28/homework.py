T = int(input())
for _ in range(T):
    n = int(input())
    sub = input()
    m = int(input())
    app = list(map(str,input()))
    v_d = list(map(str,input()))    
    # print(v_d)
    # dict_map = dict(zip(v_d, app))
    # print(dict_map)
    new = sub
    for i,key in enumerate (v_d):
        value = app[i]
        # value = dict_map[key]
        # print(f"{key}: {value}")
        if key == "D":
            new = new + value
     
        else:
            new = value + new
   
    print(new)