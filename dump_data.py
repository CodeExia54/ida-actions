# dump_data.py
import ida_segment
import ida_bytes
import idaapi

seg = ida_segment.get_segm_by_name(".data")
if not seg:
    print("[ERROR] .data segment not found")
    idaapi.qexit(1)

start = seg.start_ea
end = seg.end_ea
size = end - start

data = ida_bytes.get_bytes(start, size)

with open("data_dump.bin", "wb") as f:
    f.write(data)

print(f"[OK] .data dumped")
print(f"[INFO] .data start: {hex(start)} size: {hex(size)}")

idaapi.qexit(0)
