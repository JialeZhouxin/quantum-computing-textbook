# 习题解答 · 第13章 基础量子算法

---

### 基础题

**1.1** 量子并行性的本质。

量子并行性源于叠加原理：对一个叠加态 $\frac{1}{\sqrt{2^n}}\sum_x |x\rangle$ 一次性应用函数 $f$，所有 $2^n$ 个输入的函数值被同时计算。但量子并行性**不能直接读取**所有结果——测量会坍缩到单个输出。经典并行用 $2^n$ 个处理器同时计算，每个结果都可读。量子并行性必须借助干涉（如 QFT、相位反冲）来提取全局信息。

**1.2** Oracle 的幺正性。

标准 Oracle $O_f|x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle$ 是幺正的，因为它是一个置换（将计算基映射到计算基），置换矩阵是正交的，自然是幺正的。

如果改为 $O_f|x\rangle = |f(x)\rangle$，当 $f$ 不是一一映射（不是双射）时，不同输入映射到同一输出，信息丢失，不是可逆操作。非双射函数对应的映射不是幺正变换。

**1.3** 相位反冲中辅助态的选择。

$|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$，$O_f|x\rangle|-\rangle = \frac{1}{\sqrt{2}}(|x\rangle|f(x)\rangle - |x\rangle|\bar{f}(x)\rangle) = (-1)^{f(x)}|x\rangle|-\rangle$。

如果改为 $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$，则 $O_f|x\rangle|+\rangle = \frac{1}{\sqrt{2}}(|x\rangle|f(x)\rangle + |x\rangle|\bar{f}(x)\rangle) = |x\rangle|+\rangle$（无论 $f(x)$ 值，结果都是 $|+\rangle$），**相位信息消失在归一化中**。$|-\rangle$ 的负号使相位能反向编码。

**1.4** 有错误的 Deutsch 算法。

如果 Oracle 实现为 $O_f|x\rangle|y\rangle = |x\rangle|f(x)\rangle$（而不是标准 $\oplus$ 形式），$O_f$ 仅在 $f(x)=0$ 时保持 $|y\rangle$ 不变，$f(x)=1$ 时将 $|y\rangle$ 替换为 $|1\rangle$——不再幺正。算法结果不可靠。

本质上，标准 Oracle 的 $\oplus$ 形式保证了可逆性和幺正性。非 $\oplus$ 形式对某些 $f$ 不可逆，无法正确实现相位反冲。

**1.5** Deutsch-Jozsa 证明。

平衡函数有 $2^{n-1}$ 个输入输出 0，$2^{n-1}$ 个输入输出 1。Hadamard 变换后，输出态为 $\sum_z \left(\frac{1}{2^n}\sum_x (-1)^{f(x)}(-1)^{x\cdot z}\right)|z\rangle$。

当 $f$ 平衡时，$\sum_x (-1)^{f(x)} = 0$（正负各半）。$z=0$ 项系数 $\propto \sum_x (-1)^{f(x)} = 0$。因此测量到 $|0\rangle^{\otimes n}$ 的概率为 0。

**1.6** Bernstein-Vazirani 的变体。

$f(x) = s \cdot x \oplus b$，一个额外的隐藏比特 $b$。

将辅助态初始化改为 $|-\rangle$，标准 BV 算法得到 $(-1)^b\sum_z \left(\frac{1}{2^n}\sum_x (-1)^{(s\oplus z)\cdot x}\right)|z\rangle = (-1)^b|s\rangle$。

测量结果 $s$ 正确，但 $b$ 的全局相位不影响测量概率——**无法通过一次查询确定 $b$**。需要执行两次（一次 $|+\rangle$，一次 $|-\rangle$）对比相位，或直接测量 $f(0)$ 来获取 $b$。

**1.7** $\frac{1}{2^n}\sum_{x\in\{0,1\}^n} (-1)^{y\cdot x} = \delta_{y,0}$。

若 $y=0$，$(-1)^{0\cdot x} = 1$ 对所有 $x$，和为 $2^n/2^n = 1$。
若 $y\neq 0$，设 $y_k = 1$，将和按 $x_k$ 拆分：$\frac{1}{2^n}\sum_{x_k=0,1} (-1)^{x_k}\sum_{x'\in\{0,1\}^{n-1}} (-1)^{y'\cdot x'} = \frac{1}{2}(1-1)\cdot(\text{})=0$。

**1.8** Simon 算法。

每次运行得到 $z$ 满足 $s\cdot z = 0$（模 2 内积为 0）。证明：$z$ 满足 $\prod_{x} |r_x - r_{x\oplus s}| = (-1)^{z\cdot s}$ 恒等式。

当 $z=0$ 时不提供信息（$0\cdot s = 0$平凡成立）。当测到 $z=0$ 时该轮无效。$O(n)$ 次有效运行后从线性方程组解出 $s$。

**1.9** $n=3$，$s=101$。

可能测到的 $z$ 值：所有与 $s$ 正交的 3 位二进制串。$z\cdot s = z_1 \cdot 1 + z_2 \cdot 0 + z_3 \cdot 1 = z_1 + z_3 = 0 \pmod{2}$，即 $z_1 = z_3$。

有效 $z$：$\{000, 010, 101, 111\}$。每个概率相等（假设均匀分布）。

**1.10** $n=3$ 时 QFT 的乘积表示。

$F_8|j\rangle = \frac{1}{\sqrt{2^3}}\bigotimes_{l=1}^3 (|0\rangle + e^{2\pi i j/2^l}|1\rangle)$

展开：$= \frac{1}{\sqrt{8}}(|0\rangle + e^{2\pi i j/8}|1\rangle) \otimes (|0\rangle + e^{2\pi i j/4}|1\rangle) \otimes (|0\rangle + e^{2\pi i j/2}|1\rangle)$

与定义式 $\frac{1}{\sqrt{8}}\sum_{k=0}^{7} e^{2\pi i j k/8}|k\rangle$ 等价——将 $k$ 按二进制展开 $k = k_1 k_2 k_3$ 即可逐位验证。

**1.11** $n=4$ QFT 电路图（文本）：

```
q0: ──H──R2──R3──R4──●───────────────────────
                     │
q1: ──────●───H──R2──R3──●───────────────────
          │              │
q2: ──────────●─────H──R2──R3──●─────────────
               │              │
q3: ────────────────●─────H──R2──●───────────
                                 │
                         SWAP───○─○──────────
```

其中 $R_k = \begin{pmatrix}1&0\\0&e^{2\pi i/2^k}\end{pmatrix}$。

**1.12** QFT 幺正性。

$(F_N)_{jk} = \frac{1}{\sqrt{N}} e^{2\pi i j k / N}$

$(F_N^\dagger F_N)_{jl} = \sum_k \frac{1}{\sqrt{N}} e^{-2\pi i j k / N} \cdot \frac{1}{\sqrt{N}} e^{2\pi i k l / N} = \frac{1}{N}\sum_k e^{2\pi i k (l-j)/N} = \delta_{jl}$

最后一步利用了 $\sum_{k=0}^{N-1} e^{2\pi i k m/N} = N\delta_{m,0}$。$F_N^\dagger F_N = I$，故 QFT 幺正。

**1.13** Simon 算法 vs Deutsch-Jozsa。

Simon 算法是第一个展示**指数级量子加速**的算法：经典解决 Simon 问题需要 $\Omega(2^{n/2})$ 次查询，量子只需 $O(n)$ 次。Deutsch-Jozsa 只展示指数级"查询复杂度"加速，但经典确定性算法的最坏情况也是 $2^{n-1}+1$ 次查询——加速巨大但问题本身不实用。Simon 的问题有实际意义的结构（隐藏子群问题），直接启发了 Shor 算法。

---

### 拓展题

**1.14** 修改版 Deutsch-Jozsa。

$f$ 要么常数（全 0 或全 1），要么在精确 $3/4$ 输入上输出 1。采样 $k$ 个随机输入，统计 1 的个数。如果全是常数，观察到 1 的比例为 0 或 1。如果是 $3/4$ 函数，观察到比例为 $3/4$。

量子方法：使用振幅估计（QE）精确估计 $\sum_x (-1)^{f(x)}/2^n$。常数函数给出 $\pm 1$，$3/4$ 平衡函数给出 $-1/2$。一次 Oracle 查询即可区分。

**1.15** 编程题（思路）

```python
# Qiskit 实现 Deutsch-Jozsa 算法框架
from qiskit import QuantumCircuit

def deutsch_jozsa(oracle, n):
    qc = QuantumCircuit(n+1, n)
    qc.x(n)  # 辅助为 |1>
    qc.h(range(n+1))  # 所有比特 H
    qc.append(oracle, range(n+1))
    qc.h(range(n))
    qc.measure(range(n), range(n))
    return qc

# 常数函数 f(x)=1: Oracle = X 门作用在辅助
# 平衡函数 f(x)=x0: Oracle = CNOT 从 q0 到辅助
# 模拟：所有结果 = 0 为常数，否则平衡
```
