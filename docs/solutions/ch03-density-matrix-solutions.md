# 习题解答 · 第3章 密度矩阵与混合态

---

### 基础知识题

**1.** 判断以下矩阵是否为合法的单比特密度矩阵：

**(a)** $\begin{pmatrix} 1/2 & 0 \\ 0 & 1/2 \end{pmatrix}$

**解：** $\text{Tr} = 1/2 + 1/2 = 1$，$\rho^\dagger = \rho$，半正定（本征值 $1/2, 1/2 \geq 0$）→ **合法**。这是最大混态。

**(b)** $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$

**解：** $\text{Tr} = 1$，$\rho^\dagger = \rho$，本征值 $1, 0 \geq 0$ → **合法**。这是纯态 $|0\rangle\langle 0|$。

**(c)** $\begin{pmatrix} 1/3 & 1/2 \\ 1/2 & 2/3 \end{pmatrix}$

**解：** $\text{Tr} = 1$，$\rho^\dagger = \rho$。行列式 $= (1/3)(2/3) - (1/2)^2 = 2/9 - 1/4 = 8/36 - 9/36 = -1/36 < 0$，本征值一正一负 → **不合法**（不半正定）。

**(d)** $\begin{pmatrix} 1/2 & 1/2 \\ 1/2 & 1/2 \end{pmatrix}$

**解：** $\text{Tr} = 1$，$\rho^\dagger = \rho$。本征值 $1, 0 \geq 0$ → **合法**。这是纯态 $|+\rangle\langle +|$。

**2.** 对于 $\rho = \frac{3}{4}|0\rangle\langle 0| + \frac{1}{4}|1\rangle\langle 1|$，计算 $\text{Tr}(\rho^2)$，判断它是纯态还是混态。

**解：**
$$
\rho = \begin{pmatrix} 3/4 & 0 \\ 0 & 1/4 \end{pmatrix},\quad
\rho^2 = \begin{pmatrix} 9/16 & 0 \\ 0 & 1/16 \end{pmatrix}
$$
$$
\text{Tr}(\rho^2) = \frac{9}{16} + \frac{1}{16} = \frac{10}{16} = \frac{5}{8} < 1
$$
$\text{Tr}(\rho^2) < 1$ → **混态**。

**3.** 证明：对于任何密度矩阵 $\rho$，$0 \leq \text{Tr}(\rho^2) \leq 1$，且等号在纯态时取 1。

**解：** 设 $\rho$ 的本征值为 $\{\lambda_i\}$，满足 $\lambda_i \geq 0$，$\sum_i \lambda_i = 1$。

$\text{Tr}(\rho^2) = \sum_i \lambda_i^2$。由于 $0 \leq \lambda_i \leq 1$，有 $\lambda_i^2 \leq \lambda_i$，因此：
$$
\sum_i \lambda_i^2 \leq \sum_i \lambda_i = 1
$$
等号成立当且仅当一个本征值 $= 1$，其余 $= 0$ → 纯态。

下界 $\sum_i \lambda_i^2 \geq 0$ 显然成立，等号当 $\rho = 0$，但迹为 1 排除此情况。实际下界为 $\text{Tr}(\rho^2) \geq 1/d$，$d$ 为维度（由 Cauchy-Schwarz 或 Jensen 不等式）。

**4.** 计算 $\rho = \frac{1}{2}(|0\rangle\langle 0| + |1\rangle\langle 1|)$ 在 $X$ 基下的测量概率分布。

**解：** $\rho = I/2$。$X$ 基 $\{|+\rangle, |-\rangle\}$。测量概率：
$$
P(+) = \langle+|\rho|+\rangle = \frac{1}{2}\langle+|+\rangle = \frac{1}{2},\quad
P(-) = \frac{1}{2}
$$
最大混态在任何基下测量都是均匀分布。

**5.** 写出 $|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$ 的密度矩阵。

**解：**
$$
\rho = |-\rangle\langle -| = \frac{1}{2}(|0\rangle - |1\rangle)(\langle 0| - \langle 1|)
= \frac{1}{2}(|0\rangle\langle 0| - |0\rangle\langle 1| - |1\rangle\langle 0| + |1\rangle\langle 1|)
$$
$$
= \frac{1}{2}\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}
$$

---

### 演化与约化密度矩阵

**1.** 初始态 $\rho(0) = |+\rangle\langle +|$，在 $H = \omega Z$ 下演化。求 $\rho(t)$ 和 $\text{Tr}(\rho(t)^2)$。

**解：** $U(t) = e^{-i\omega t Z/2} = \cos(\omega t/2)I - i\sin(\omega t/2)Z$。

$$
\rho(t) = U(t)\rho(0)U^\dagger(t) = U(t)|+\rangle\langle +|U^\dagger(t)
$$

由 ch02-5 结果，$|\psi(t)\rangle = \frac{1}{\sqrt{2}}(e^{-i\omega t/2}|0\rangle + e^{i\omega t/2}|1\rangle)$，对应密度矩阵：
$$
\rho(t) = \frac{1}{2}\begin{pmatrix} 1 & e^{i\omega t} \\ e^{-i\omega t} & 1 \end{pmatrix}
$$

$\text{Tr}(\rho(t)^2) = 1$（纯态在幺正演化下保持纯态）。

几何意义：布洛赫向量绕 $z$ 轴旋转，长度不变。

**2.** 对于 Bell 态 $|\Phi^-\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle)$，计算 $\rho_A$ 和 $\rho_B$，并求 $\text{Tr}(\rho_A^2)$。

**解：**
$$
\rho_{AB} = |\Phi^-\rangle\langle\Phi^-| = \frac{1}{2}(|00\rangle\langle 00| - |00\rangle\langle 11| - |11\rangle\langle 00| + |11\rangle\langle 11|)
$$

对 $B$ 求部分迹：$\rho_A = \text{Tr}_B(\rho_{AB})$。

$$
\rho_A = \frac{1}{2}(|0\rangle\langle 0|\cdot 1 + 0 + 0 + |1\rangle\langle 1|\cdot 1) = \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

同理 $\rho_B = I/2$。$\text{Tr}(\rho_A^2) = 1/2$。

整个系统处于纯态（$\text{Tr}(\rho_{AB}^2) = 1$），但每个子系统是最大混态——纠缠的特征。

**3.** 三个比特的 GHZ 态 $|GHZ\rangle = \frac{1}{\sqrt{2}}(|000\rangle + |111\rangle)$。求第一个比特的约化密度矩阵和纯度。

**解：** 全密度矩阵 $\rho_{ABC} = \frac{1}{2}(|000\rangle\langle 000| + |000\rangle\langle 111| + |111\rangle\langle 000| + |111\rangle\langle 111|)$。

对 BC 求部分迹：
$$
\rho_A = \text{Tr}_{BC}(\rho_{ABC}) = \frac{1}{2}(|0\rangle\langle 0| + |1\rangle\langle 1|) = \frac{I}{2}
$$

纯度 $\text{Tr}(\rho_A^2) = 1/2$。每个单比特子系统都是最大混态。

**4.** 对于 $\rho_{AB} = \frac{1}{2}(|00\rangle\langle 00| + |11\rangle\langle 11|)$（经典关联），计算 $\rho_A$ 并与 Bell 态的结果比较。

**解：**
$$
\rho_A = \text{Tr}_B(\rho_{AB}) = \frac{1}{2}(|0\rangle\langle 0| + |1\rangle\langle 1|) = \frac{I}{2}
$$

$\rho_A$ **和 Bell 态的情况完全相同**（$I/2$）。但两系统的关联性质不同：
- Bell 态 $\to$ 量子关联（纠缠），可用 Bell 不等式检测
- 经典混合 $\to$ 经典关联，遵守 Bell 不等式

结论：仅凭 $\rho_A$ 无法区分纠缠态和经典关联态。

**5.** 验证：对于两体纯态 $|\Psi\rangle_{AB}$，总有不变量 $S(\rho_A) = S(\rho_B)$。

**解：** $|\Psi\rangle_{AB}$ 的施密特分解：
$$
|\Psi\rangle_{AB} = \sum_i \lambda_i |i\rangle_A|i\rangle_B
$$

约化密度矩阵：
$$
\rho_A = \sum_i \lambda_i^2 |i\rangle\langle i|_A,\quad \rho_B = \sum_i \lambda_i^2 |i\rangle\langle i|_B
$$

两个约化矩阵有完全相同的非零本征值 $\{\lambda_i^2\}$。冯·诺依曼熵只依赖于本征值谱：
$$
S(\rho_A) = -\sum_i \lambda_i^2\log\lambda_i^2 = S(\rho_B)
$$

---

### 熵与距离

**1.** 计算 $\rho = \frac{2}{3}|0\rangle\langle 0| + \frac{1}{3}|1\rangle\langle 1|$ 的冯·诺依曼熵和线性熵。

**解：**
$$
\rho = \begin{pmatrix} 2/3 & 0 \\ 0 & 1/3 \end{pmatrix}
$$

冯·诺依曼熵（$\log$ 底取 2）：
$$
S(\rho) = -\frac{2}{3}\log\frac{2}{3} - \frac{1}{3}\log\frac{1}{3}
= -\frac{2}{3}(\log 2 - \log 3) - \frac{1}{3}(-\log 3)
= -\frac{2}{3} + \frac{2}{3}\log 3 + \frac{1}{3}\log 3
= -\frac{2}{3} + \log 3
\approx -0.667 + 1.585 = 0.918\ \text{bit}
$$

线性熵：
$$
S_L(\rho) = 1 - \text{Tr}(\rho^2) = 1 - \left(\frac{4}{9} + \frac{1}{9}\right) = 1 - \frac{5}{9} = \frac{4}{9} \approx 0.444
$$

**2.** 两个 qutrit 的 Bell 态 $|\Psi\rangle = \frac{1}{\sqrt{3}}(|00\rangle + |11\rangle + |22\rangle)$ 求纠缠熵。

**解：** 施密特系数为 $\lambda_i = 1/\sqrt{3}$（$i = 0, 1, 2$）。
$$
\rho_A = \frac{1}{3}(|0\rangle\langle 0| + |1\rangle\langle 1| + |2\rangle\langle 2|) = \frac{I}{3}
$$
$$
S(\rho_A) = -\sum_{i=0}^2 \frac{1}{3}\log\frac{1}{3} = \log_2 3 \approx 1.585\ \text{qutrit}
$$

这是 $d=3$ 系统的最大纠缠——纠缠熵达到了最大值 $\log d$。

**3.** 计算 $F(|0\rangle\langle 0|, |-\rangle\langle -|)$ 和 $D(|0\rangle\langle 0|, |-\rangle\langle -|)$，验证纯态关系 $D = \sqrt{1 - F^2}$。

**解：** 两个都是纯态，$F = |\langle 0|-\rangle| = |1/\sqrt{2}| = 1/\sqrt{2} \approx 0.707$。
$$
D = \sqrt{1 - F^2} = \sqrt{1 - 1/2} = 1/\sqrt{2} \approx 0.707
$$

直接计算验证：
$$
\rho - \sigma = |0\rangle\langle 0| - |-\rangle\langle -| = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$
$|\rho - \sigma|$ 的本征值为 $1/\sqrt{2}$，$D = \frac{1}{2} \cdot \frac{2}{\sqrt{2}} = 1/\sqrt{2}$。验证通过。

**4.** 对于 $\rho = \frac{1}{2}|0\rangle\langle 0| + \frac{1}{2}|1\rangle\langle 1|$ 和 $\sigma = |0\rangle\langle 0|$，计算 $F(\rho, \sigma)$ 和 $D(\rho, \sigma)$。

**解：** $\rho = I/2$，$\sigma = |0\rangle\langle 0|$。$\sigma$ 是纯态，所以：
$$
F(\rho, \sigma) = \sqrt{\langle 0|\rho|0\rangle} = \sqrt{1/2} = 1/\sqrt{2} \approx 0.707
$$

迹距离：
$$
\rho - \sigma = \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}
$$
$|\rho - \sigma| = \frac{1}{2}I$，$D = \frac{1}{2}\text{Tr}|\rho - \sigma| = \frac{1}{2} \cdot 1 = 0.5$。

验证关系：$F = 1/\sqrt{2}$，$D = 0.5 = \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} = \sqrt{1 - F^2} \cdot \frac{\sqrt{2}}{2}$。此处 $D < \sqrt{1 - F^2}$——上界不等式 $D \leq \sqrt{1 - F^2}$ 取严格不等式（因 $\rho$ 非纯）。

**5.** 证明：对于任意 $\rho$ 和 $\sigma$，$0 \leq F(\rho, \sigma) \leq 1$。

**解：** 由 Uhlmann 定理，$F(\rho, \sigma) = \max_{|\psi_\rho\rangle, |\psi_\sigma\rangle} |\langle\psi_\rho|\psi_\sigma\rangle|$。

$|\langle\psi_\rho|\psi_\sigma\rangle|$ 的取值范围为 $[0, 1]$（内积模的最大值 1 由 Cauchy-Schwarz 保证，最小值 0 对应正交态），最大值在所有可能的纯化上取，因此 $0 \leq F(\rho, \sigma) \leq 1$。

$F = 1$ 当且仅当 $\rho = \sigma$；$F = 0$ 当且仅当 $\rho$ 和 $\sigma$ 的支持集正交。
