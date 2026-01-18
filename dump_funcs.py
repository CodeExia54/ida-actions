import ida_funcs
import ida_segment

text = ida_segment.get_segm_by_name(".text")

out = open("func_addrs.txt", "w")

for f in ida_funcs.get_functions():
    ea = f.entry_point
    if text and text.start_ea <= ea < text.end_ea:
        out.write(hex(ea) + "\n")

out.close()

print("[+] func_addrs.txt written")
