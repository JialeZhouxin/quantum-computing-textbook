# 习题解答 · 第21章 量子噪声与退相干

---

### 基础题（1-7题）

**1.** $\mathcal{E}(\rho) = \frac12\rho + \frac14 X\rho X + \frac14 Y\rho Y$。

Kraus 算符：$K_0 = \sqrt{1/2}I$，$K_1 = \sqrt{1/4}X$，$K_2 = \sqrt{1/4}Y$。

保迹：$\sum_k K_k^\dagger K_k = \frac12 I + \frac14 X^\dagger X + \frac14 Y^\dagger Y = \frac12 I + \frac14 I + \frac14 I = I$ ✓

**2.** 振幅阻尼参数 $\gamma = 0.2$。Kraus 算符：
$K_0 = \begin{pmatrix}1&0\\0&\sqrt{1-\gamma}\end{pmatrix} = \begin{pmatrix}1&0\\0&\sqrt{0.8}\end{pmatrix}$，$K_1 = \begin{pmatrix}0&\sqrt{\gamma}\\0&0\end{pmatrix} = \begin{pmatrix}0&\sqrt{0.2}\\0&0\end{pmatrix}$。

$\rho_{\text{out}} = K_0\rho K_0^\dagger + K_1\rho K_1^\dagger$
$K_0\rho K_0^\dagger = \begin{pmatrix}1&0\\0&\sqrt{0.8}\end{pmatrix}\frac12\begin{pmatrix}1&0.5\\0.5&1\end{pmatrix}\begin{pmatrix}1&0\\0&\sqrt{0.8}\end{pmatrix} = \frac12\begin{pmatrix}1&0.5\sqrt{0.8}\\0.5\sqrt{0.8}&0.8\end{pmatrix}$
$K_1\rho K_1^\dagger = \begin{pmatrix}0&\sqrt{0.2}\\0&0\end{pmatrix}\frac12\begin{pmatrix}1&0.5\\0.5&1\end{pmatrix}\begin{pmatrix}0&0\\\sqrt{0.2}&0\end{pmatrix} = \frac12\begin{pmatrix}0.2&0\\0&0\end{pmatrix}$

$\rho_{\text{out}} = \frac12\begin{pmatrix}1.2 & 0.5\sqrt{0.8}\\0.5\sqrt{0.8} & 0.8\end{pmatrix}$

保真度 $F = \langle+|\rho_{\text{out}}|+\rangle = \frac12(1,1)\rho_{\text{out}}(1,1)^T \approx 0.456$。

**3.** $1/T_2 = 1/(2T_1) + 1/T_\phi \to 1/T_\phi = 1/90 - 1/(2\times 120) = 1/90 - 1/240 = (8-3)/720 = 5/720$。$T_\phi = 144$ μs。

门时间 50 ns：$\gamma = 1 - e^{-t_g/T_1} \approx t_g/T_1 = 50/120000 \approx 4.17 \times 10^{-4}$。$\lambda = 1 - e^{-t_g/T_\phi} \approx 50/144000 \approx 3.47 \times 10^{-4}$。

**4.** 等价表示来自旋转 45° 的 Kraus 表示混合。标准退极化表示为：$E_0 = \sqrt{1-p}I$，$E_i = \sqrt{p/3}\sigma_i$。令 $\sqrt{1-3p/4} = \sqrt{1-p}$ 可解出 $p$ 与 $p$ 的关系。

**5.** 比特翻转：$K_0 = \sqrt{1-p}I$，$K_1 = \sqrt{p}X$。
$\rho_{\text{out}} = (1-p)|-\rangle\langle-| + p X|-\rangle\langle-|X = (1-p)|-\rangle\langle-| + p|+\rangle\langle+|$。
$F = \langle-|\rho_{\text{out}}|-\rangle = 1-p$。$|-\rangle$ 不免疫 $X$ 错误——$X|-\rangle = |+\rangle$，是完全翻转。

**6.** $M = \begin{pmatrix}0.97 & 0.06\\0.03 & 0.94\end{pmatrix}$。$\det M = 0.97\times0.94 - 0.06\times0.03 = 0.9118 - 0.0018 = 0.91$。
$M^{-1} = \frac{1}{0.91}\begin{pmatrix}0.94 & -0.06\\-0.03 & 0.97\end{pmatrix}$。$\vec{p}_{\text{corr}} = M^{-1}\begin{pmatrix}0.820\\0.180\end{pmatrix} = \frac{1}{0.91}(0.771 - 0.011,\; -0.025 + 0.175)^T \approx (0.835, 0.165)^T$。

**7.** RB 拟合 $P(m) = Ap^m + B$。$m\to\infty$ 时 $B=0.5$。
$m=1$：$0.949 = Ap + 0.5 \to Ap = 0.449$
$m=200$：$0.549 = Ap^{200} + 0.5 \to Ap^{200} = 0.049$
$p^{199} = 0.049/0.449 \approx 0.109$，$p \approx 0.989$。$\epsilon = (1-p)/2 \approx 0.0055$。

---

### 进阶题（8-12题）

**8.** 联合信道的总 Kraus 算符为振幅阻尼和相位阻尼 Kronecker 积：$K_{ij} = K_i^{(AD)} \otimes K_j^{(PD)}$。$\rho_{01}(t) = \rho_{01}(0) e^{-t/2T_1} e^{-t/T_\phi} = \rho_{01}(0) e^{-t/T_2}$。

**11.** 单比特门错误率与退极化参数：退极化信道的门保真度 $F = 1 - 3p/4$。门错误率 $\epsilon = 1 - F = 3p/4$。若只考虑 Pauli 噪声且假设对每种 Pauli 错误概率相同，则 $\epsilon = p/2$（对应于 $p$ 为单次 Pauli 错误平均概率）。

**12.** $F(t) = \langle+|\rho(t)|+\rangle = \frac12(1 + e^{-t/T_2})$。令 $F(t) = 0.9$：
$0.9 = \frac12(1 + e^{-t/80})$，$e^{-t/80} = 0.8$，$t = -80\ln 0.8 \approx 17.9$ μs。

---

### 挑战题（13-15题）

**14.** $p_L \approx 0.1(p/p_{\text{th}})^{(d+1)/2}$。$p=10^{-3}$，$p_{\text{th}}=0.01$，$p_L=10^{-6}$。
$10^{-6} = 0.1(0.1)^{(d+1)/2}$，$10^{-5} = 10^{-(d+1)/2}$，$d+1 = 10$，$d=9$。物理量子比特数 $n = (2d-1)^2 = 289$。

**15.** (a) 无噪声：$H|0\rangle|0\rangle = |+\rangle|0\rangle \xrightarrow{\text{CNOT}} \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = |\Phi^+\rangle$。
(b) 噪声下每个操作后引入退极化。逐比特计算得 $\rho_{\text{out}}$ 为 $|\Phi^+\rangle$ 被退极化后的混态。(c) 保真度约为 $1 - 3p/2$（$p=0.01$ 时 $F \approx 0.985$）。
