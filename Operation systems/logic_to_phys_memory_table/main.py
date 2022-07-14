def get_bits(num: int, start_bit: int, end_bit: int) -> int:
    return (num >> start_bit) & (2**(end_bit-start_bit+1)-1)


def extract_table_address(addr: int):
    return get_bits(addr, 12, 51) * 2**12


def is_odd(addr: int):
    return bool(addr % 2)


with open("input.txt", "r") as f:
    lines = f.readlines()
m, q, r = map(int, lines[0].split())
# print(m, q, r)
addr_map = {}
for i in range(m):
    line = lines[i+1]
    paddr, value = line.split()
    addr_map[int(paddr)] = int(value)
# print(addr_map)
req_logical_addr = []
for i in range(q):
    line = lines[m+i+1]
    req_logical_addr.append(int(line))
# print(req_logical_addr)

list_result = []
for i, logical_addr in enumerate(req_logical_addr):
    out = False
    # if i == 0:
    print("for logical ", logical_addr)
    p_table_address = r
    for tab_num in range(4):
        # eval real address
        # if i == 0:
        print("p_table_address", p_table_address)
        offset_in_logical = 12 + 9*(3-tab_num)
        """ ! Offset - translate to bytes """
        table_offset = get_bits(logical_addr, offset_in_logical, offset_in_logical+8)*2**3
        print("table_offset", table_offset)
        real_address = p_table_address + table_offset
        print("real_address", real_address)
        if real_address not in addr_map:
            # if i == 0:
            print("not in addr_map")
            list_result.append("fault")
            out = True
            break
        print("here")
        # eval table value at address
        table_value = addr_map[real_address]
        if not is_odd(table_value):
            list_result.append("fault")
            out = True
            break
        # if tab_num < 3:
        p_table_address = extract_table_address(table_value)
        # p_table_address = next_table + table_offset
        # print("next_table in ", p_table_address)
    if not out:
        # if p_table_address not in addr_map:
        #     list_result.append("fault")
        # else:
        result_value = p_table_address + get_bits(logical_addr, 0, 11)
        list_result.append(str(result_value))

result = "\n".join(list_result)

with open("output.txt", "w") as f:
    f.write(result)


# print(get_bits(31, 1, 3))
# print(extract_table_address(4097))
# print(extract_table_address(8193))
# print(extract_table_address(12289))
# print(extract_table_address(16385))
#
# print(is_odd(16385))
print(get_bits(742539174, 30, 39))