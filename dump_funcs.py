import ida_ua
import idaapi
import ida_segment

text = ida_segment.get_segm_by_name(".text")
out = open("func_addrs.txt", "w")

ea = text.start_ea
while ea < text.end_ea:
    insn = ida_ua.insn_t()
    if ida_ua.decode_insn(insn, ea):
        # ARM64 BL instruction
        if insn.itype == idaapi.ARM_bl:
            target = idaapi.get_operand_value(ea, 0)
            if text.start_ea <= target < text.end_ea:
                out.write(hex(target) + "\n")
        ea += insn.size
    else:
        ea += 4

out.close()
print("[+] func_addrs.txt written")
idaapi.qexit(0)
