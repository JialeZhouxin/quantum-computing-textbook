# 习题解答 · 第16章 Grover算法与振幅放大

---

### 基础题（1-6题）

**1.** Grover 算法的三个主要步骤：

1. **初始化**：制备均匀叠加态 $|s\rangle = H^{\otimes n}|0\rangle^{\otimes n}$
2. **Grover 迭代**（重复 $k_{\text{opt}}$ 次）：(a) Oracle $O$ 翻转标记项的相位；(b) 扩散算符 $D$ 对均匀叠加态做反射
3. **测量**：得到标记项的高概率结果

Oracle 在标记子空间上引入相位差，扩散算符放大这个差异——两者的组合等价于在二维子空间中旋转 $2\theta$ 角。

**2.** $N=8$（$n=3$）。

**(a)** $\theta = \arcsin(1/\sqrt{8}) = \arcsin(1/2\sqrt{2}) \approx \arcsin(0.3536) \approx 0.3614$ rad。
$k_{\text{opt}} = \lfloor \pi/(4\theta) \rfloor \approx \lfloor 2.172 \rfloor = 2$。

**(b)** 一次迭代后：$\sin(3\theta) \approx \sin(1.0842) \approx 0.883$，标记项振幅 $\approx 0.883$。

**(c)** $k=2$ 时：$\sin(5\theta) \approx \sin(1.807) \approx 0.972$。
$P_{\text{succ}} \approx 0.972^2 \approx 0.945$。

**3.** Oracle 电路（$N=8$，标记 $|101\rangle$）：

$|101\rangle$ 对应二进制值 5。Oracle 需要翻转 $|101\rangle$ 的相位。

电路：对量子比特 $q_0, q_1, q_2$，应用 $X$ 门在 $q_0$ 和 $q_2$（使 $|101\rangle \to |111\rangle$），然后应用三重控制的 $Z$ 门（$CCZ$），再应用 $X$ 门恢复。

```
q0: ──X──●──X──
         │
q1: ─────●─────
         │
q2: ──X──●──X──
```

$CCZ$ 可用两个 $H$ 门和一个 $CCX$（Toffoli）实现。

**4.** 几何图像：

二维子空间由 $|t\rangle$（目标态）和 $|t^\perp\rangle$（非目标态的正交分量）张成。$|s\rangle$ 与 $|t^\perp\rangle$ 夹角 $\theta$。

- Oracle $O$：关于 $|t^\perp\rangle$ 的反射
- 扩散算符 $D$：关于 $|s\rangle$ 的反射
- $G = D \cdot O$：两次反射的复合 = 绕 $|s\rangle \times |t^\perp\rangle$ 轴旋转 $2\theta$

每次迭代将 $|s\rangle$ 向 $|t\rangle$ 方向转动 $2\theta$。$k_{\text{opt}}$ 次后最接近 $|t\rangle$。

**5.** $n=2$ 扩散算符。

$|s\rangle = \frac12(|00\rangle + |01\rangle + |10\rangle + |11\rangle)$。
$D = 2|s\rangle\langle s| - I$。

$D = \frac12\begin{pmatrix}-1&1&1&1\\1&-1&1&1\\1&1&-1&1\\1&1&1&-1\end{pmatrix}$

验证 $D = H^{\otimes 2}(2|00\rangle\langle 00| - I)H^{\otimes 2}$：
$2|00\rangle\langle 00| - I = \text{diag}(1, -1, -1, -1)$。
$H^{\otimes 2} \cdot \text{diag}(1, -1, -1, -1) \cdot H^{\otimes 2}$ 计算可得上矩阵 ✓。

**6.** $N=64$，$M=4$。

**(a)** $\theta_M = \arcsin(\sqrt{4/64}) = \arcsin(1/4) \approx 0.2527$ rad。
$k_{\text{opt}} = \lfloor \pi/(4 \times 0.2527) \rfloor = \lfloor 3.108 \rfloor = 3$。

**(b)** 单目标 $M=1$：$\theta = \arcsin(1/8) \approx 0.1253$，$k_{\text{opt}} = \lfloor \pi/(4 \times 0.1253) \rfloor = \lfloor 6.27 \rfloor = 6$。
多目标 $M=4$ 只需一半的迭代次数，因为更多标记使初始态更接近目标方向。

---

### 进阶题（7-10题）

**7.** 最优性证明（概要）。

混合态参数方法（BBBV 下界）：任何量子搜索算法经过 $T$ 次 Oracle 查询后，输出态与无 Oracle 情况下的最大区分度不超过 $O(T/\sqrt{N})$。要达到恒定成功概率，需 $T = \Omega(\sqrt{N})$。

**8.** $N=10^4$，$k_{\text{opt}} = \lfloor \pi\sqrt{N}/4 \rfloor = \lfloor 78.54 \rfloor = 78$。

成功概率 $P_{\text{succ}}(k) = \sin^2((2k+1)\theta)$，$\theta = \arcsin(1/100) \approx 0.01$。
$k=78$ 时：$(2\times78+1)\times0.01 = 1.57 \approx \pi/2$，$P_{\text{succ}} \approx 1$。
概率首次低于 0.5 的迭代次数：$(2k+1)\theta < \pi/4$ 或 $(2k+1)\theta > 3\pi/4$，约 $k < 38$ 或 $k > 117$。

**9.** 振幅放大。

$p=0.02$，不放大时重复次数：$(1-p)^m < 0.01$，$m > \ln(0.01)/\ln(0.98) \approx 228$ 次。
振幅放大：$\theta = \arcsin(\sqrt{p}) \approx \arcsin(0.1414) \approx 0.1419$。
$k_{\text{opt}} = \lfloor \pi/(4\theta) \rfloor \approx \lfloor 5.54 \rfloor = 5$ 次迭代。
加速比：$228/5 \approx 45$ 倍。

**10.** 噪声仿真（思路）。

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error

# 创建去极化噪声模型
noise_model = NoiseModel()
for eps in [0.001, 0.005, 0.01, 0.02]:
    error = depolarizing_error(eps, 1)
    noise_model.add_all_qubit_quantum_error(error, ['h', 'x', 'cz'])
    
    # 对每个 k 运行 Grover，测量成功概率
    # 观察：k_opt 随噪声增大而减小，最大成功概率下降
```

---

### 挑战题（11-12题）

**11.** 量子计数。

用量子相位估计（QPE）估计 Grover 算符的本征相位 $\pm 2\theta_M$，其中 $\sin^2\theta_M = M/N$。

$M$ 的相对误差 10%，需要 $n$ 个 QPE 估计量子比特使 $\Delta\theta_M \approx 0.1\theta_M$。$\theta_M \approx \sqrt{M/N}$。

对于 $N=10^6$，若 $M$ 约 $10^3$，$\theta \approx \sqrt{10^{-3}} \approx 0.0316$。10% 精度需误差 $\Delta\theta \approx 0.00316$，需 $n \approx \log_2(2\pi/0.00316) \approx 11$ 个 QPE 量子比特。Oracle 查询数约 $O(2^n) = O(\sqrt{N})$。

**12.** 固定点 Grover 搜索。

**(a)** 核心思想：使用变角 Grover 迭代（每次迭代的旋转角度不同），使旋转在接近目标时"减速"，避免过度旋转。

**(b)** 证明：固定点算法的成功概率单调递增趋近 1，消除了标准 Grover 的周期性行为。代价是常数因子（约 2-3 倍）的额外查询。

**(c)** $p = M/N \in [0.01, 0.1]$（范围跨度 10 倍）。标准 Grover 需要根据 $p$ 精确选择 $k$，过估计会导致过度旋转。固定点搜索的迭代次数 ≈ $(1/\sqrt{0.01}) \times \text{常数} \approx 10\sqrt{N} \times \text{常数}$，约 $30\sqrt{N}$ 量级——比知道精确 $M$ 的标准 Grover 多约 3 倍。
