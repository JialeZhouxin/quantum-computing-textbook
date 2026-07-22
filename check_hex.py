"""检查 $|0 附近的原始字节"""
with open('module-01-mathematical-foundations/ch01-linear-algebra.md', 'rb') as f:
    data = f.read(5000)
idx = data.find(b'$|0')
if idx >= 0:
    start = max(0, idx-10)
    end = min(len(data), idx+40)
    print('Hex:', data[start:end].hex(' '))
    print('Repr:', repr(data[start:end]))
else:
    print('$|0 not found in first 5000 bytes')
