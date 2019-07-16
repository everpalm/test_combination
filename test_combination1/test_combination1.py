# This is test version
# 7 elements stnad for 7 items of different price, choose two of them from these 7 items with 10 dollars
def append_list_10(target_x, input_y):
    if input_y <= 10:
        dummy = target_x.append(input_y)
        return True
    else:
        return False

def append_sample(target_list, append_list, b_num, z):
    y = append_list[0] + append_list[b_num]
    if append_list_10(z,y):
        dummy = target_list.append([append_list[0], append_list[b_num]])
    return target_list

if __name__ == "__main__":
    a = [3,6,8,7,9,5,2]
    z = []
    sample = []

    a_len = len(a)

#print(a_len)
#x1 = a[0:a_len]
#x2 = a[1:a_len]
#x3 = a[2:a_len]
#x4 = a[3:a_len]
#x5 = a[4:a_len]
    for a_num in range(a_len-1):
#for a_num in range(0,a_len-1,1):
        x = a[a_num:a_len]
        x_len = len(x)
        #print(x)
        for b_num in range(1, x_len, 1):
            #y = x[0] + x[b_num]
            #print(y)
            #if y <= 10:
            #    dummy = z.append(y)
            #if append_list_10(z,y):
            #    dummy = sample.append([x[0], x[b_num]])
            #else:
            #    continue
            #sample = append_sample(sample, x, b_num, z, y)
            sample = append_sample(sample, x, b_num, z)

    z_len = len(z) - 1
    #print(z_len)
    index_m = []

    for z_num in range(z_len):
        for y_num in range(z_len, z_num, -1):
            if z[y_num] < z[y_num - 1]:
                z[y_num], z[y_num - 1] = z[y_num - 1], z[y_num]
                sample[y_num], sample[y_num - 1] = sample[y_num - 1], sample[y_num]
            else:
                #dummy = index_m.insert(0,y_num)
                #print(sample[y_num])
                continue
    sample_len = len(sample)
    print(sample[sample_len - 1])
    print(sample)