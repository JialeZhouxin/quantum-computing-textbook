# 习题解答 · 第14章 量子傅里叶变换与相位估计

---

### 基础题（1-6题）

**1.** 2 量子比特 QFT 矩阵。

$F_4 = \frac12\begin{pmatrix}
1&1&1&1\\
1&i&-1&-i\\
1&-1&1&-1\\
1&-i&-1&i
\end{pmatrix}$

验证幺正性：$F_4^\dagger F_4 = I$。每列模为 $(1/4)(1+1+1+1)=1$，不同列内积为 0（几何级数和）。

**2.** QPE 提取相位的原理。

相位编码态 $\frac{1}{\sqrt{2^n}}\sum_{k=0}^{2^n-1} e^{2\pi i \theta k}|k\rangle$ 正是 QFT 作用于 $|2^n\theta\rangle$（二进制表示）的结果。逆 QFT 将这种"相位编码"转换回"计算基编码"，使相位信息以二进制形式出现在测量结果中。

**3.** $U = \text{diag}(1, e^{2\pi i \cdot 0.375})$，本征态 $|1\rangle$，$\theta = 0.375 = 3/8$，二进制 $0.011$。

$n=4$ QPE 步骤：
1. 估计寄存器 H 后：$\frac{1}{\sqrt{16}}\sum_{k=0}^{15} |k\rangle|1\rangle$
2. 受控 $U$ 门后：$\frac{1}{\sqrt{16}}\sum_{k=0}^{15} e^{2\pi i \cdot 0.375 \cdot k} |k\rangle|1\rangle$
3. 逆 QFT 后：$|6\rangle|1\rangle$（因为 $2^4 \times 0.375 = 6$）
4. 测量估计寄存器：得到 6（二进制 0110）

**4.** $n=3$，$\theta = 0.3$。

$2^3 \times 0.3 = 2.4$。最近整数 $a=2$（$\tilde{\theta}=0.25$）和 $a=3$（$\tilde{\theta}=0.375$）。

概率公式：$P(a) = \frac{1}{2^{2n}}\frac{\sin^2(\pi(2^n\theta - a))}{\sin^2(\pi(2^n\theta - a)/2^n)}$

$\delta_2 = 2.4 - 2 = 0.4$，$\delta_3 = 2.4 - 3 = -0.6$。

$P(2) = \frac{1}{64} \frac{\sin^2(0.4\pi)}{\sin^2(0.4\pi/8)} \approx \frac{1}{64} \frac{0.9511^2}{0.1564^2} \approx 0.579$
$P(3) = \frac{1}{64} \frac{\sin^2(0.6\pi)}{\sin^2(0.6\pi/8)} \approx \frac{1}{64} \frac{0.9511^2}{0.2334^2} \approx 0.259$

**5.** IPEA 电路。

使用单个辅助比特的迭代电路：
```
     ┌───┐┌───────┐┌───┐┌───┐
q0: ─┤ H ├┤ U^(2^t)├┤ H ├┤ M ├──→ 经典比特 θ_t
     └───┘└───────┘└───┘└─┬─┘
q1: ───────────────────────Z──────────────────
                          │ 经典反馈
```

每轮提取相位的一个比特，从最低有效位开始。经典反馈将前轮结果用于当前轮的旋转补偿。

**6.** 受控 $R_z(\pi/4)$ 分解。

$CR_z(\pi/4) = $CZ 加单比特门。

$CR_z(\pi/4) = (I \otimes R_z(\pi/8)) \cdot \text{CNOT} \cdot (I \otimes R_z(-\pi/8)) \cdot \text{CNOT}$

而 CNOT $= (I \otimes H) \cdot \text{CZ} \cdot (I \otimes H)$，所以：

$CR_z(\pi/4) = (I \otimes R_z(\pi/8)) \cdot (I \otimes H) \cdot \text{CZ} \cdot (I \otimes H) \cdot (I \otimes R_z(-\pi/8)) \cdot (I \otimes H) \cdot \text{CZ} \cdot (I \otimes H)$

总计：CZ × 2，H × 4，$R_z$ × 2。

---

### 进阶题（7-10题）

**7.** QFT 复杂度。

H 门数：$n$（每个量子比特 1 个）
受控相位门数：$n(n-1)/2$（第 $j$ 比特需要 $n-j$ 个受控 $R_k$ 门）
SWAP 门数：$\lfloor n/2 \rfloor$（反转量子比特顺序）

总门数：$n + n(n-1)/2 + \lfloor n/2 \rfloor = O(n^2)$。

经典 FFT 需要 $O(n2^n)$ 次操作——QFT 的指数级加速。

**8.** $n=2$ 时的成功概率下界。

$\theta$ 有精确二进制表示时，测量结果确定，$P_{\text{succ}} = 1$。
$\theta$ 不精确时，最坏情况 $\theta = a/4 + 1/8$（两个最接近整数中间）：

$P_{\text{best}} = \frac{1}{16}\frac{\sin^2(\pi/2)}{\sin^2(\pi/8)} = \frac{1}{16} \cdot \frac{1}{\sin^2(\pi/8)} \approx \frac{1}{16 \times 0.1464} \approx 0.427$

下界 $4/\pi^2 \approx 0.405$。

**9.** 近似 QFT 误差。

删除 $\theta$ 小于 $2^{-m-1}$ 的受控旋转门。误差分析：被忽略的门的算子范数 $\| \Delta \| = \|\sum_{k > m} R_k - I\|$，每忽略一个 $R_k$ 引入与 $2^{-k}$ 成正比的误差。$n=10$，$m=4$ 时，最坏情况误差约 $n \cdot 2^{-(m+1)} = 10/32 \approx 0.31$ rad。

**10.** 噪声仿真（思路）。

```python
# Qiskit 噪声仿真框架
from qiskit.providers.fake_provider import FakeAthens
from qiskit_aer.noise import NoiseModel

# 创建不同噪声水平的模型
noise_model = NoiseModel.from_backend(FakeAthens())
# 缩放门错误率
for gate in ['cx']:
    noise_model.set_noise_propagation(...)
# 在不同噪声水平下运行 QPE，记录成功概率
```

---

### 挑战题（11-12题）

**11.** 贝叶斯相位估计（BPE）。

BPE 将相位估计视为贝叶斯推断问题：根据测量结果更新相位的后验概率分布。

BPE 的优势：
- 可以用更少的总门数达到相同的精度
- 对噪声更鲁棒（自然处理不确定性）
- 不需要逆 QFT

缺点：
- 需要实时经典计算（后验更新）
- 每轮结果依赖前轮（不能并行）
- 精度分析不如标准 QPE 直观

**12.** 氢分子基态能量估计。

12 个量子比特，化学精度 $1.6 \times 10^{-3}$ Hartree ≈ $1.6 \times 10^{-3} \times 2\pi \times 10^{15}$ Hz。

所需估计精度 $\epsilon = 10^{-3}$ rad，需 $n = \lceil \log_2(1/\epsilon) \rceil \approx 10$ 个估计量子比特。

总量子比特数：12 + 10 = 22。

Trotter 分解的门次数：哈密顿量项数约 $O(m^4)$（$m$ 为轨道数），每次 Trotter 步约数千个门，总深度约 $10^6$-$10^8$ 门。当前 NISQ 设备无法胜任——需要容错量子计算。
