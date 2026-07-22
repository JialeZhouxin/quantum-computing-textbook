# 习题解答 · 第10章 量子电路与通用门集

---

### 基础题（第1-6题）

**4.1** 电路图（文本描述）：
```
q0: ───H───●──────────
           │
q1: ───────X───M──────
```

**4.2** 电路作用在 $|00\rangle$：
$|00\rangle \xrightarrow{H\otimes I} |+\rangle|0\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle) \xrightarrow{\text{CNOT}} \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = |\Phi^+\rangle$

**4.3** H 是 Clifford 门。

$HXH^\dagger = \frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = \begin{pmatrix}1&0\\0&-1\end{pmatrix} = Z$

$HZH^\dagger = \frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = \begin{pmatrix}0&1\\1&0\end{pmatrix} = X$

**4.4** S 是 Clifford 门。

$SXS^\dagger = \begin{pmatrix}1&0\\0&i\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1&0\\0&-i\end{pmatrix} = \begin{pmatrix}0&-i\\i&0\end{pmatrix} = Y$

$SZS^\dagger = \begin{pmatrix}1&0\\0&i\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}1&0\\0&-i\end{pmatrix} = \begin{pmatrix}1&0\\0&-1\end{pmatrix} = Z$

**4.5** $T = \begin{pmatrix}1&0\\0&e^{i\pi/4}\end{pmatrix}$

$T^2 = \begin{pmatrix}1&0\\0&e^{i\pi/2}\end{pmatrix} = S$，$T^4 = \begin{pmatrix}1&0\\0&e^{i\pi}\end{pmatrix} = Z$，$T^8 = \begin{pmatrix}1&0\\0&e^{i2\pi}\end{pmatrix} = I$

**4.6** 单比特 Clifford 群 $\mathcal{C}_1$（不计全局相位）的阶为 24。

元素：将 Pauli 矩阵映射到 $\pm$ Pauli 矩阵的置换。$\mathcal{C}_1$ 同构于四面体群（旋转对称群 $S_4$）。这 24 个元素是：Pauli 矩阵的符号改变（$\pm I, \pm X, \pm Y, \pm Z$）乘以半旋转（H、S 等）。

---

### 提高题（第7-12题）

**4.7** $\text{CNOT} = (I \otimes H) \cdot \text{CZ} \cdot (I \otimes H)$

$(I \otimes H) \cdot \text{CZ} \cdot (I \otimes H) = \begin{pmatrix}H&0\\0&H\end{pmatrix}\begin{pmatrix}I&0\\0&Z\end{pmatrix}\begin{pmatrix}H&0\\0&H\end{pmatrix}$
$= \begin{pmatrix}HIH&0\\0&HZH\end{pmatrix} = \begin{pmatrix}I&0\\0&X\end{pmatrix} = \text{CNOT}$

因为 $HIH = I$，$HZH = X$。

**4.8** $\text{SWAP} = \text{CNOT}_{1,2} \cdot \text{CNOT}_{2,1} \cdot \text{CNOT}_{1,2}$

验证在计算基上的作用：
$\text{SWAP}|00\rangle = |00\rangle$
$\text{SWAP}|01\rangle \to \text{CNOT}_{1,2}|01\rangle = |01\rangle \to \text{CNOT}_{2,1}|01\rangle = |11\rangle \to \text{CNOT}_{1,2}|11\rangle = |10\rangle$
$\text{SWAP}|10\rangle \to \text{CNOT}_{1,2}|10\rangle = |11\rangle \to \text{CNOT}_{2,1}|11\rangle = |01\rangle \to \text{CNOT}_{1,2}|01\rangle = |01\rangle$
$\text{SWAP}|11\rangle \to \text{CNOT}_{1,2}|11\rangle = |10\rangle \to \text{CNOT}_{2,1}|10\rangle = |10\rangle \to \text{CNOT}_{1,2}|10\rangle = |11\rangle$

在基 $\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$ 下的矩阵验证：
$\text{CNOT}_{1,2}\text{CNOT}_{2,1}\text{CNOT}_{1,2} = \begin{pmatrix}1&0&0&0\\0&0&0&1\\0&0&1&0\\0&1&0&0\end{pmatrix}\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}\begin{pmatrix}1&0&0&0\\0&0&0&1\\0&0&1&0\\0&1&0&0\end{pmatrix} = \begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix} = \text{SWAP}$

**4.9** 电路优化。电路由 H-H（抵消）、X 等组成。

原电路：q0: H-H-X-H = XH（因为 $HH=I$，只剩 XH）
q1: H-H-Z-H = ZH

$XH = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\-1&1\end{pmatrix}$，$ZH = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\-1&1\end{pmatrix}$ — 两者相等。

实际上每个量子比特上的两个 H 门相邻，互逆抵消。优化后只需 2 个门（q0 的 X 和 q1 的 Z）。

深度从 4 降至 1。

**4.10** 线性链 0-1-2-3-4 拓扑。

CNOT(Q0, Q3)：Q0 和 Q3 不直接耦合。最短路径 Q0-Q1-Q2-Q3，需要 3 次 SWAP（或 2 次 SWAP + 1 CNOT 方向调整）。

以下方案：
1. SWAP(0,1), SWAP(1,2), SWAP(2,3) — Q0 移到 Q3，执行 CNOT
2. 然后反向 SWAP 恢复

最少 SWAP = 3（每步移动一个位置）。实际上可以用更聪明的方法：路由时会重排初始映射。

**4.11** $H$ 在 $\{R_Z, X\}$ 中表示。

$H = e^{i\pi/2} R_Z(\pi/2) X R_Z(\pi/2)$ 或 $H = R_Z(\pi/2) R_X(\pi/2) R_Z(\pi/2)$。

验证：$e^{i\pi/2}R_Z(\pi/2)XR_Z(\pi/2) = i\begin{pmatrix}e^{-i\pi/4}&0\\0&e^{i\pi/4}\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}e^{-i\pi/4}&0\\0&e^{i\pi/4}\end{pmatrix}$
$= i\begin{pmatrix}0&e^{-i\pi/4}\\e^{i\pi/4}&0\end{pmatrix}\begin{pmatrix}e^{-i\pi/4}&0\\0&e^{i\pi/4}\end{pmatrix} = i\begin{pmatrix}0&e^{-i\pi/2}\\-e^{i\pi/2}&0\end{pmatrix}$
$= \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = H$

**4.12** $U = R_Z(\alpha) R_X(\beta) R_Z(\gamma)$。

证明：$SU(2)$ 中任意幺正矩阵可写为 $U = \begin{pmatrix}a&b\\-b^*&a^*\end{pmatrix}$，$|a|^2+|b|^2=1$。

展开 $R_Z(\alpha)R_X(\beta)R_Z(\gamma)$：
$\begin{pmatrix}e^{-i\alpha/2}&0\\0&e^{i\alpha/2}\end{pmatrix}\begin{pmatrix}\cos(\beta/2)&-i\sin(\beta/2)\\-i\sin(\beta/2)&\cos(\beta/2)\end{pmatrix}\begin{pmatrix}e^{-i\gamma/2}&0\\0&e^{i\gamma/2}\end{pmatrix}$

$= \begin{pmatrix}e^{-i(\alpha+\gamma)/2}\cos(\beta/2) & -i e^{-i(\alpha-\gamma)/2}\sin(\beta/2) \\ -i e^{i(\alpha-\gamma)/2}\sin(\beta/2) & e^{i(\alpha+\gamma)/2}\cos(\beta/2)\end{pmatrix}$

通过适当选择 $\alpha, \beta, \gamma$ 可匹配任意 $a, b$。解方程：$\cos(\beta/2)=|a|$，$\alpha+\gamma=-2\arg(a)$，$\alpha-\gamma=-2\arg(b)+\pi$。

---

### 挑战题（第13-18题）

**4.13** $\langle H, S \rangle$ 生成 24 个 Clifford 元素。

关键是验证 $H$ 和 $S$ 的生成关系：
- $S^2 = Z$（Pauli 算符）
- $HSH = R_x(\pi/2)$（旋转）
- $SHS = R_z(\pi/2)R_y(\pi/2)$

通过组合 $H, S$ 及其幂，可生成全部 24 种 Pauli 映射（Aut$(P_1) \cong S_4$）。

**4.14** Gottesman-Knill 定理（简化证明）。

用 Heisenberg 表示：每个 $n$ 比特 Clifford 电路对应 Pauli 算符空间上的 $\mathbb{F}_2^{2n}$ 线性变换。演化一个 Pauli 算符 $P$ 通过 Clifford 门只需要更新一个长度为 $2n$ 的二进制向量（相位 $\pm 1$）。跟踪全部 $2n$ 个生成元的演化需 $O(n^2)$ 空间，$O(n^2)$ 时间/门。测量时计算概率和坍缩也是多项式时间。因此整个模拟可在 $O(n^2)$ 时间内完成。

**4.15** 初始映射问题的启发式算法。

NP 难证明：归约自图同构或最小线性排列问题。

启发式算法（如 SABRE）：使用模拟退火，以 SWAP 数或电路深度为代价函数。每次随机交换两个物理量子比特的映射，计算新代价，按 Metropolis 准则接受或拒绝。迭代至收敛。

**4.16** Solovay-Kitaev 定理弱版本：$SU(2)$ 中任意门可在 $O(\log^c(1/\epsilon))$ 个 $H, T$ 门内近似到精度 $\epsilon$。

核心思想：
1. 构建一个 $\epsilon_0$-网（$\epsilon_0$ 精度覆盖 $SU(2)$）
2. 对目标门 $U$，找到最近的网元素 $U_0$
3. 误差 $\Delta = UU_0^{-1}$ 接近单位矩阵
4. 对 $\Delta$ 递归使用群换位子 $[A,B] = ABA^{-1}B^{-1}$ 来"放大"精度
5. 每次递归将误差从 $\epsilon$ 降到 $\epsilon^{3/2}$

实际参数：$c \approx 3.97$，对数因子通常为 $\log^{3.97}(1/\epsilon)$。对于 $\epsilon = 10^{-9}$，约需 30-50 个 $H,T$ 门。

**4.17** 保真度感知的编译策略。

1. 用加权图表示耦合拓扑：边权重为对应方向 CNOT 的保真度
2. 路由时选择最高保真度方向的 CNOT：
   - 如果需 CNOT(i,j) 但 F(j,i) > F(i,j)，可以 CNOT(j,i) + 4 个 H 门反转方向
   - 权衡额外 H 门的保真度损失与 CNOT 方向的增益
3. 禁忌搜索或贪婪算法寻找最优映射和路由

**4.18** $T$ 门合成。

将任意旋转 $R_z(\theta)$ 分解为 $e^{i\phi} T^k H T^m H T^n \ldots$ 序列。

Clifford + T 通用性证明：$T$ 不是 Clifford 门，$H$ 和 $T$ 生成一个在 $SU(2)$ 中稠密的子群（由 Solovay-Kitaev 定理保证）。任何非 Clifford 门加上 Clifford 群可以生成任意幺正变换。
