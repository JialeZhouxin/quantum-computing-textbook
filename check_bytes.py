"""直接检查二进制模式"""
with open('module-01-mathematical-foundations/ch01-linear-algebra.md', 'rb') as f:
    data = f.read()

# 找所有 $|0 出现位置并打印周围字节
pat = b'$|0'
idx = 0
count = 0
while True:
    idx = data.find(pat, idx)
    if idx < 0:
        break
    count += 1
    if count <= 3:
        snippet = data[idx:idx+12]
        print(f"Hit {count} at byte {idx}: hex={snippet.hex(' ')} repr={repr(snippet)}")
    idx += 1

print(f"\nTotal $|0 occurrences: {count}")

# 尝试匹配几种模式
import re
for pattern, name in [
    (b'\\$\\|0\\r[a-z]+\\$', '$|0\\rWORD$'),
    (b'\\$\\|0\\r\\}', '$|0\\r}$'),
    (b'\\$\\|0\\r', '$|0\\r'),
]:
    matches = list(re.finditer(pattern, data))
    print(f"Pattern {name}: {len(matches)} matches")
    if matches:
        for m in matches[:3]:
            print(f"  {data[m.start():m.end()].hex(' ')} = {repr(data[m.start():m.end()])}")
