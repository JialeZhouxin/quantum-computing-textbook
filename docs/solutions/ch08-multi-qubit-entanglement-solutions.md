# 习题解答 · 第8章 多量子比特与纠缠

---

### ★ 基础题（第1-6题）

**1.** 判断两比特态是否可分。

**(a)** $|\Psi_a\rangle = \frac12(|00\rangle + |01\rangle + |10\rangle + |11\rangle)$

因式分解：$= \frac12(|0\rangle + |1\rangle) \otimes (|0\rangle + |1\rangle) = |+\rangle \otimes |+\rangle$。**可分离**。

**(b)** $|\Psi_b\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |01\rangle + |10\rangle - |11\rangle)$

$= \frac{1}{\sqrt{2}}(|0\rangle(|0\rangle - |1\rangle) + |1\rangle(|0\rangle - |1\rangle)) = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes (|0\rangle - |1\rangle) = |+\rangle \otimes |-\rangle$。**可分离**。

**(c)** $|\Psi_c\rangle = \frac{1}{\sqrt{5}}(|00\rangle + 2|11\rangle)$

系数 $1/\sqrt{5}$ 和 $2/\sqrt{5}$，不能分解为 $(\alpha|0\rangle + \beta|1\rangle)(\gamma|0\rangle + \delta|1\rangle)$ 的形式（交叉项需为零）。**纠缠**。

**(d)** $|\Psi_d\rangle = \cos\theta|00\rangle + \sin\theta|11\rangle$

当 $\theta = 0$ 时：$|00\rangle$，可分离。当 $\theta = \pi/4$ 时：$(|00\rangle + |11\rangle)/\sqrt{2}$（Bell 态），最大纠缠。当 $0 < \theta < \pi/2$ 且 $\theta \neq 0, \pi/2$：**纠缠**。

**2.** 两比特门矩阵。

**(a)** $I \otimes X = \begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}$

**(b)** $Z \otimes H = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1&0&0\\1&-1&0&0\\0&0&-1&-1\\0&0&-1&1\end{pmatrix}$

**(c)** $\text{CNOT}_{21}$（控制 q2，目标 q1）：
当 q2=0 时不变，q2=1 时翻转 q1。
$c_{21} = \begin{pmatrix}1&0&0&0\\0&0&0&1\\0&0&1&0\\0&1&0&0\end{pmatrix}$

**(d)** SWAP：
$\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix}$

**3.** H + CNOT 电路（控制比特为 q1，目标为 q2）。

**(a)** $|00\rangle \to H\otimes I|00\rangle = |+\rangle|0\rangle \to \text{CNOT}(|+\rangle|0\rangle) = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = |\Phi^+\rangle$

**(b)** $|01\rangle \to |+\rangle|1\rangle \to \frac{1}{\sqrt{2}}(|01\rangle + |10\rangle) = |\Psi^+\rangle$

**(c)** $|10\rangle \to |-\rangle|0\rangle \to \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle) = |\Phi^-\rangle$

**(d)** $|11\rangle \to |-\rangle|1\rangle \to \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle) = |\Psi^-\rangle$

**4.** 四个 Bell 态及其转换。

$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$
$|\Phi^-\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle) = Z_1|\Phi^+\rangle$
$|\Psi^+\rangle = \frac{1}{\sqrt{2}}(|01\rangle + |10\rangle) = X_2|\Phi^+\rangle$
$|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle) = Z_1X_2|\Phi^+\rangle = iY_2|\Phi^+\rangle$

任意两个 Bell 态之间可以通过单比特 Pauli 门相互转换。

**5.** 施密特秩和系数。

**(a)** $|\Phi^+\rangle$：施密特分解 $= \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$。秩 = 2，系数 $\{1/\sqrt{2}, 1/\sqrt{2}\}$。

**(b)** $|\Psi\rangle = \frac{1}{\sqrt{2}}(|0\rangle_A|+\rangle_B + |1\rangle_A|-\rangle_B)$
展开：$= \frac{1}{\sqrt{2}}\left(|0\rangle\frac{|0\rangle+|1\rangle}{\sqrt{2}} + |1\rangle\frac{|0\rangle-|1\rangle}{\sqrt{2}}\right) = \frac{1}{2}(|00\rangle + |01\rangle + |10\rangle - |11\rangle)$

施密特分解：$\cos(\pi/8)|0\rangle_A|\bar{0}\rangle_B + \sin(\pi/8)|1\rangle_A|\bar{1}\rangle_B$。

更简单：$\rho_A = \text{Tr}_B(|\Psi\rangle\langle\Psi|) = \frac12 I$，本征值 $\{1/2, 1/2\}$。施密特系数 $\{\sqrt{1/2}, \sqrt{1/2}\}$。秩 = 2。

**(c)** $|\Psi\rangle = \frac35|00\rangle + \frac45|11\rangle$：已是施密特分解形式。系数 $\{3/5, 4/5\}$。秩 = 2。

**6.** $|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$。

并发度：$\mathcal{C} = 2|0 \times 1/\sqrt{2} - 1/\sqrt{2} \times 0| = 2 \times 1/2 = 1$。最大纠缠。

纠缠熵：$\rho_A = I/2$，$S(\rho_A) = \log_2 2 = 1$ bit。最大纠缠。

---

### ★★ 计算题（第7-14题）

**7.** 四贝尔态两两正交。

$|\Phi^+\rangle$ 与 $|\Phi^-\rangle$：$\langle\Phi^+|\Phi^-\rangle = \frac12(\langle 00| + \langle 11|)(|00\rangle - |11\rangle) = \frac12(1 - 1) = 0$

$|\Phi^+\rangle$ 与 $|\Psi^+\rangle$：$\langle\Phi^+|\Psi^+\rangle = \frac12(\langle 00| + \langle 11|)(|01\rangle + |10\rangle) = \frac12(0 + 0) = 0$

所有组合均得零——四个 Bell 态构成 $\mathbb{C}^2 \otimes \mathbb{C}^2$ 的正交归一基。

**8.** $\rho = |\Phi^+\rangle\langle\Phi^+|$ 的部分转置。

$\rho = \frac12\begin{pmatrix}1&0&0&1\\0&0&0&0\\0&0&0&0\\1&0&0&1\end{pmatrix}$

对系统 B 做部分转置：$\rho^{T_B} = \frac12\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix}$

本征值：$\{1/2, 0, 0, -1/2\}$。有一个负本征值 $-1/2$。负度 $\mathcal{N} = |\sum \text{负本征值}| = 1/2$。

**9.** 并发度公式推导。

$\rho = |\Psi\rangle\langle\Psi|$，$|\Psi\rangle = \alpha|00\rangle + \beta|01\rangle + \gamma|10\rangle + \delta|11\rangle$。

$\tilde{\rho} = (\sigma_y \otimes \sigma_y)\rho^*(\sigma_y \otimes \sigma_y)$

$\sigma_y \otimes \sigma_y = \begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&1&0&0\\-1&0&0&0\end{pmatrix}$

$\rho^*$ 的矩阵元 $\rho_{ij}^* = \overline{\rho_{ij}}$。

计算 $R = \rho\tilde{\rho}$ 本征值的平方根 $\lambda_i$。并发度 $\mathcal{C} = \max\{0, \lambda_1 - \lambda_2 - \lambda_3 - \lambda_4\}$。

对于两比特纯态，简化为 $\mathcal{C} = 2|\alpha\delta - \beta\gamma|$。

**10.** $\text{CNOT} = (I \otimes H) \cdot \text{CZ} \cdot (I \otimes H)$。

验证：$(I \otimes H) \cdot \text{CZ} \cdot (I \otimes H) = \begin{pmatrix}H&0\\0&H\end{pmatrix}\begin{pmatrix}I&0\\0&Z\end{pmatrix}\begin{pmatrix}H&0\\0&H\end{pmatrix}$

$= \begin{pmatrix}H^2&0\\0&HZH\end{pmatrix} = \begin{pmatrix}I&0\\0&X\end{pmatrix} = \text{CNOT}$

因为 $H^2 = I$，$HZH = X$。

**11.** 受控 $R_y(\theta)$ 的实现。

分解：$\text{C-}R_y(\theta) = (I \otimes R_y(\theta/2)) \cdot \text{CNOT} \cdot (I \otimes R_y(-\theta/2)) \cdot \text{CNOT}$

电路：
```
q1: ──■────────────■──
     │             │
q2: ──Ry(θ/2)──X──Ry(-θ/2)──X──
```

**12.** GHZ 态在 $\sigma_x^{\otimes n}$ 基下的测量。

$|GHZ_n\rangle = \frac{1}{\sqrt{2}}(|0\rangle^{\otimes n} + |1\rangle^{\otimes n})$。在 $X$ 基下测量每个比特。

$|0\rangle = \frac{1}{\sqrt{2}}(|+\rangle + |-\rangle)$，$|1\rangle = \frac{1}{\sqrt{2}}(|+\rangle - |-\rangle)$。

$|GHZ_n\rangle = \frac{1}{\sqrt{2^{n+1}}}\left(|+\rangle^{\otimes n} + |-\rangle^{\otimes n} + \sum_{\text{混合项}}\right)$

偶数个 $|-\rangle$ 的项有正干涉增强，奇数个 $|-\rangle$ 的项相消。测量结果总包含偶数个 $|-\rangle$。

**13.** 量子隐形传态（标准协议推导）。

初始：$|\psi\rangle_1 \otimes |\Phi^+\rangle_{23}$。Alice 对两个比特做 Bell 测量，将测量结果（2 bit 经典信息）发给 Bob。Bob 根据结果对 q3 施加对应单比特门：
- 00 → $I$，01 → $X$，10 → $Z$，11 → $ZX = iY$

最终 q3 变为 $|\psi\rangle$。

**14.** 超密编码。

Bob 有 Bell 态的一半。Alice（有另一半）要对她的比特施加 Pauli 门，选择：$I, X, Z, XZ$ 之一。然后发送她的 1 个量子比特给 Bob。Bob 做 Bell 测量即可区分 4 种情况，获取 2 bit 信息。

---

### ★★★ 扩展题（第15-18题）

**15.** 纠缠蒸馏与纯化（BBPSSW 协议）。通过两个拷贝的 CNOT 操作和测量，将保真度从 $F < 1$ 提高到 $F' > F$。每次成功的蒸馏消耗两个拷贝。重复可逼近最大纠缠。

**16.** Mermin 不等式：对 GHZ 态测量 $M = \sigma_x\sigma_x\sigma_x$。经典局域实在论预言 $|\langle M\rangle| \leq 1$，量子力学预言 $\langle M\rangle = \pm 1$（对特定测量设置 $\pm 1$）。实验每次都与量子力学一致。

**17.** 纠缠交换：将两个独立的 Bell 对 $\text{AB}$ 和 $\text{CD}$ 纠缠，对 BC 做 Bell 测量后，AD 变为纠缠态。纠缠不需要直接相互作用——通过测量中间节点建立。

**18.** $W$ 态 $|W\rangle = \frac{1}{\sqrt{3}}(|001\rangle + |010\rangle + |100\rangle)$。单比特保真度：任意丢失一个比特后，剩余两比特仍是纠缠的（但非最大纠缠）。GHZ 态丢失一个比特后剩余两比特不纠缠。$W$ 态对粒子丢失更鲁棒。
