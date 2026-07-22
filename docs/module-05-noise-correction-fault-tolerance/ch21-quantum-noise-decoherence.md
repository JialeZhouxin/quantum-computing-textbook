# 第1章 量子噪声与退相干

> **本章导读**
>
> 模块一至四中，我们始终假设量子门是完美的、量子比特是孤立的、测量是精确的。真实量子计算机远非如此。量子比特与环境的耦合导致信息泄漏（退相干），控制脉冲的不完美引入门错误，测量器件的不确定性产生读出错误。这些噪声是量子计算走向实用的最大障碍——也是量子纠错和容错计算存在的根本理由。
>
> 本章从**开放量子系统**的数学框架出发，系统建立量子噪声的描述语言：Kraus 算符和算符和表示。然后逐一研究三种基本噪声信道——振幅阻尼、相位阻尼和退极化信道，推导它们的 Kraus 算符、作用方式和物理参数（T₁、T₂）。之后引入泡利噪声模型、噪声时间演化的模拟方法、马尔可夫近似和门错误模型，最后介绍随机基准测试这一实用噪声表征工具。
>
> 学完本章，你将能够：
> - 用 Kraus 算符表示任意量子噪声过程
> - 写出振幅阻尼、相位阻尼和退极化信道的 Kraus 算符
> - 理解 T₁ 和 T₂ 的物理含义及关系
> - 在布洛赫球上直观理解噪声的收缩效应
> - 从芯片参数构建实际噪声模型
> - 计算保真度、门错误率和读出错误混淆矩阵
> - 设计和解释随机基准测试实验
>
> **先修知识**：模块一第3章（密度矩阵与混合态）、模块三（量子门、量子电路模型、测量公设）、模块四第8章（超导芯片基础）

---

## 1.1 量子操作与映射

### 1.1.1 为什么需要新的描述工具？

回顾封闭量子系统的演化：态矢量 $|\psi\rangle$ 在幺正算符作用下变为 $|\psi'\rangle = U|\psi\rangle$，密度矩阵写为 $\rho' = U\rho U^\dagger$。

但真实量子比特**不是封闭的**。系统和环境之间存在耦合，导致：

1. **信息流向环境**：量子比特的部分信息不可逆地泄漏到环境中（退相干）
2. **非幺正演化**：系统密度矩阵的演化不再是简单的幺正变换
3. **纯态变混合态**：初始纯态可能在演化后变成混合态

我们需要一个能够描述**开放系统动力学**的数学框架。这个框架就是**量子操作**（quantum operation）或**量子映射**（quantum map）。

**定义 1.1（量子操作）** 一个量子操作 $\mathcal{E}$ 是一个将密度矩阵映射到密度矩阵的线性映射：
$$
\mathcal{E}: \rho \mapsto \rho'
$$
满足：
- **线性**：$\mathcal{E}(\alpha\rho_1 + \beta\rho_2) = \alpha\mathcal{E}(\rho_1) + \beta\mathcal{E}(\rho_2)$
- **迹非增**：$0 \le \operatorname{Tr}(\mathcal{E}(\rho)) \le 1$（保迹操作取等号）
- **完全正性**（complete positivity）：对任意辅助系统，$\mathcal{E} \otimes \mathcal{I}$ 将正定矩阵映射为正定矩阵

### 1.1.2 系统-环境模型

开放系统动力学的标准处理方法是**系统-环境模型**：把环境和系统的耦合显式写出，然后"求迹掉"环境。

设总系统（系统 $S$ + 环境 $E$）初始处于直积态 $\rho_S \otimes \rho_E$。总系统的演化是幺正的：
$$
\rho_{SE}' = U_{SE}(\rho_S \otimes \rho_E)U_{SE}^\dagger
$$

我们只关心系统 $S$ 的最终状态——对环境求部分迹：
$$
\mathcal{E}(\rho_S) = \operatorname{Tr}_E\left[U_{SE}(\rho_S \otimes \rho_E)U_{SE}^\dagger\right]
$$

这个 $\mathcal{E}$ 就是我们要找的量子操作。它描述了系统在"与环境的相互作用 + 忽略环境"之后的动力学。

### 1.1.3 Kraus 算符表示

**定理 1.1（Kraus 表示定理）** 设 $\mathcal{E}$ 是一个完全正保迹量子操作。则存在一组算符 $\{K_k\}$，满足 $\sum_k K_k^\dagger K_k = I$，使得对任意密度矩阵 $\rho$ 有：
$$
\mathcal{E}(\rho) = \sum_k K_k \rho K_k^\dagger
$$

这称为**算符和表示**（operator-sum representation）或 **Kraus 表示**，$\{K_k\}$ 称为 **Kraus 算符**。

**推导思路**：设 $\rho_E = |e_0\rangle\langle e_0|$（环境初态为纯态，混合态情况可通过谱分解归约为纯态）。设 $\{|e_k\rangle\}$ 为环境的一组基。则：
$$
\begin{aligned}
\mathcal{E}(\rho_S) &= \operatorname{Tr}_E\left[U_{SE}(\rho_S \otimes |e_0\rangle\langle e_0|)U_{SE}^\dagger\right] \\
&= \sum_k (I_S \otimes \langle e_k|) U_{SE} (\rho_S \otimes |e_0\rangle\langle e_0|) U_{SE}^\dagger (I_S \otimes |e_k\rangle) \\
&= \sum_k K_k \rho_S K_k^\dagger
\end{aligned}
$$
其中 $K_k = (I_S \otimes \langle e_k|) U_{SE} (I_S \otimes |e_0\rangle)$ 是作用在系统上的算符。

**保迹条件验证**：
$$
\operatorname{Tr}(\mathcal{E}(\rho)) = \operatorname{Tr}\left(\sum_k K_k \rho K_k^\dagger\right) = \operatorname{Tr}\left(\rho \sum_k K_k^\dagger K_k\right)
$$
要求 $\sum_k K_k^\dagger K_k = I$。

> Kraus 表示的美妙之处：它将一个复杂的"系统+环境"幺正演化，浓缩为一组仅作用在系统上的 Kraus 算符。**环境被完全编码在 Kraus 算符中**，我们不需要显式处理环境自由度。

### 1.1.4 Kraus 表示的非唯一性

Kraus 表示不是唯一的。如果 $\{K_k\}$ 是一组 Kraus 算符，那么 $\{K'_k\}$ 定义为：
$$
K'_k = \sum_j u_{kj} K_j
$$
其中 $[u_{kj}]$ 是一个幺正矩阵（适当补零填充），也生成完全相同的量子操作 $\mathcal{E}$。

这反映了"不同环境自由度的选择等价于同一个系统动力学"的物理事实。

**例 1.1（幺正演化的 Kraus 表示）** 如果 $\mathcal{E}(\rho) = U\rho U^\dagger$（封闭系统幺正演化），则只有一个 Kraus 算符 $K_0 = U$，满足 $U^\dagger U = I$。

**例 1.2（完全退极化的 Kraus 表示）** 将任意 $\rho$ 映射为最大混合态 $I/2$ 的操作：$\mathcal{E}(\rho) = I/2$。它有两个 Kraus 算符：
$$
K_0 = \frac{1}{\sqrt{2}} I,\quad K_1 = \frac{1}{\sqrt{2}} X
$$
验证：
$$
\mathcal{E}(\rho) = \frac{1}{2} I\rho I + \frac{1}{2} X\rho X = \frac{1}{2}\rho + \frac{1}{2}X\rho X
$$
对于单量子比特 $\rho = \frac{I + \vec{r}\cdot\vec{\sigma}}{2}$，$X\rho X = \frac{I + (r_x, -r_y, -r_z)\cdot\vec{\sigma}}{2}$，代入得 $\mathcal{E}(\rho) = I/2$，符合。

**即时练习 1.1**

1. 验证 $\mathcal{E}(\rho) = p\rho + (1-p)X\rho X$ 的保迹性，并写出它的 Kraus 算符。
2. 如果 $\rho_E$ 不是纯态而是混合态 $\sum_j q_j |e_j\rangle\langle e_j|$，推导对应的 Kraus 表示形式。
3. 证明：Kraus 算符的数量最多为 $\dim(\mathcal{H}_S) \times \dim(\mathcal{H}_E)$。

---

## 1.2 振幅阻尼信道

### 1.2.1 物理背景：能量弛豫

振幅阻尼信道（amplitude damping channel）描述**能量从量子比特流向环境**的过程——这是量子比特最主要的退相干机制之一。

在超导量子比特中：
- $|0\rangle$ 对应量子比特的基态（最低能态）
- $|1\rangle$ 对应激发态
- 通过与环境的耦合，$|1\rangle$ 态有概率自发辐射到 $|0\rangle$ 态，同时释放一个能量量子（光子、声子等）到环境中

这个过程的特征时间称为 **T₁**（能量弛豫时间，energy relaxation time）。

### 1.2.2 Kraus 算符

振幅阻尼信道的 Kraus 算符为：
$$
K_0 = \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{1-\gamma} \end{pmatrix}, \quad
K_1 = \begin{pmatrix} 0 & \sqrt{\gamma} \\ 0 & 0 \end{pmatrix}
$$

其中 $\gamma \in [0,1]$ 是阻尼参数。对于演化时间 $t$，$\gamma = 1 - e^{-t/T_1}$。

**验证保迹条件**：
$$
K_0^\dagger K_0 + K_1^\dagger K_1 = \begin{pmatrix} 1 & 0 \\ 0 & 1-\gamma \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & \gamma \end{pmatrix} = I
$$

### 1.2.3 振幅阻尼的作用

对任意单量子比特密度矩阵 $\rho = \begin{pmatrix} \rho_{00} & \rho_{01} \\ \rho_{10} & \rho_{11} \end{pmatrix}$：

$$
\mathcal{E}_{\text{AD}}(\rho) = K_0 \rho K_0^\dagger + K_1 \rho K_1^\dagger
$$

**计算每个项**：

$$
K_0 \rho K_0^\dagger = \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{1-\gamma} \end{pmatrix}
\begin{pmatrix} \rho_{00} & \rho_{01} \\ \rho_{10} & \rho_{11} \end{pmatrix}
\begin{pmatrix} 1 & 0 \\ 0 & \sqrt{1-\gamma} \end{pmatrix}
= \begin{pmatrix} \rho_{00} & \sqrt{1-\gamma}\,\rho_{01} \\ \sqrt{1-\gamma}\,\rho_{10} & (1-\gamma)\rho_{11} \end{pmatrix}
$$

$$
K_1 \rho K_1^\dagger = \begin{pmatrix} 0 & \sqrt{\gamma} \\ 0 & 0 \end{pmatrix}
\begin{pmatrix} \rho_{00} & \rho_{01} \\ \rho_{10} & \rho_{11} \end{pmatrix}
\begin{pmatrix} 0 & 0 \\ \sqrt{\gamma} & 0 \end{pmatrix}
= \begin{pmatrix} \gamma\rho_{11} & 0 \\ 0 & 0 \end{pmatrix}
$$

**合并结果**：
$$
\mathcal{E}_{\text{AD}}(\rho) = \begin{pmatrix}
\rho_{00} + \gamma\rho_{11} & \sqrt{1-\gamma}\,\rho_{01} \\
\sqrt{1-\gamma}\,\rho_{10} & (1-\gamma)\rho_{11}
\end{pmatrix}
$$

**物理意义**：
- 布居数（对角元）：$|1\rangle$ 态的布居数以概率 $\gamma$ 转移到 $|0\rangle$ 态。$\rho_{11} \to (1-\gamma)\rho_{11}$
- 相干性（非对角元）：指数衰减，衰减因子 $\sqrt{1-\gamma}$

### 1.2.4 时间演化与 T₁

将 $\gamma = 1 - e^{-t/T_1}$ 代入：

$$
\rho_{11}(t) = \rho_{11}(0)\,e^{-t/T_1}
$$
$$
\rho_{01}(t) = \rho_{01}(0)\,e^{-t/(2T_1)}
$$

T₁ 的物理含义：
- T₁ 是 $|1\rangle$ 态布居数衰减到 $1/e$ 所需的时间
- 典型值：超导量子比特 T₁ ≈ 10–300 μs；离子阱 T₁ > 10 s
- T₁ 越大，量子比特的能量弛豫越慢，保真度越高

### 1.2.5 布洛赫球图像

对于初始态 $|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle$，经过振幅阻尼后：

$$
\begin{aligned}
\langle X \rangle &= e^{-t/(2T_1)} \sin\theta \cos\phi \\
\langle Y \rangle &= e^{-t/(2T_1)} \sin\theta \sin\phi \\
\langle Z \rangle &= \cos\theta\, e^{-t/T_1} + (1 - e^{-t/T_1})
\end{aligned}
$$

布洛赫向量从球面向着 $|0\rangle$ 方向（北极）收缩——$|1\rangle$ 的激发能量耗散到环境中，最终系统停在北极 $|0\rangle$。

**图 1.1** [概念图] 振幅阻尼使布洛赫球沿 Z 轴收缩到北极——$|0\rangle$ 是唯一的不动点。

**即时练习 1.2**

1. 计算振幅阻尼信道下 $\rho = |+\rangle\langle+|$ 的输出态（$\gamma=0.3$）。
2. 证明 $\rho_{11}(t) = \rho_{11}(0)e^{-t/T_1}$。
3. 解释为什么 T₁ 时间也影响非对角元的衰减（系数 $\sqrt{1-\gamma} \approx e^{-t/(2T_1)}$）。

---

## 1.3 相位阻尼信道

### 1.3.1 物理背景：纯退相

相位阻尼信道（phase damping channel）描述**相位信息的丢失而不伴随能量交换**——这称为**纯退相**（pure dephasing）。

物理来源：
- 量子比特的能量（频率）随时间的随机涨落（由于环境噪声）
- 这种频率涨落导致量子比特的演化速度随机变化，累积为相位的随机偏移
- 结果是：叠加态中的相对相位变得不确定，非对角元衰减

特征时间称为 **T₂**（退相时间，dephasing time）。

### 1.3.2 Kraus 算符

相位阻尼的 Kraus 算符有多种等价表示。最常用的是：

**表示一（Kraus 算符）**：
$$
K_0 = \sqrt{1-\lambda}\, I, \quad K_1 = \sqrt{\lambda}\, Z
$$

其中 $\lambda \in [0,1]$ 是退相参数。对于演化时间 $t$，$\lambda = 1 - e^{-t/T_\phi}$，$T_\phi$ 是纯退相时间。

**验证**：$K_0^\dagger K_0 + K_1^\dagger K_1 = (1-\lambda)I + \lambda I = I$。

**表示二（相位翻转信道）** 另一种常见形式：
$$
K_0 = \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{1-\lambda} \end{pmatrix}, \quad
K_1 = \begin{pmatrix} 0 & 0 \\ 0 & \sqrt{\lambda} \end{pmatrix}
$$

这两种表示通过 Kraus 表示的非唯一性关联——前者更简洁，后者更直接显示对角元不变。

### 1.3.3 相位阻尼的作用

使用表示一，对 $\rho = \begin{pmatrix} \rho_{00} & \rho_{01} \\ \rho_{10} & \rho_{11} \end{pmatrix}$：

$$
\mathcal{E}_{\text{PD}}(\rho) = (1-\lambda)\rho + \lambda Z\rho Z
$$

计算 $Z\rho Z$：
$$
Z\rho Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
\begin{pmatrix} \rho_{00} & \rho_{01} \\ \rho_{10} & \rho_{11} \end{pmatrix}
\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
= \begin{pmatrix} \rho_{00} & -\rho_{01} \\ -\rho_{10} & \rho_{11} \end{pmatrix}
$$

代入得：
$$
\mathcal{E}_{\text{PD}}(\rho) = \begin{pmatrix}
\rho_{00} & (1-2\lambda)\rho_{01} \\
(1-2\lambda)\rho_{10} & \rho_{11}
\end{pmatrix}
$$

**注意**：对角元（布居数）完全不变——没有能量交换。非对角元（相干性）衰减因子为 $1-2\lambda$。

用 $\lambda = 1 - e^{-t/T_\phi}$ 表达：
$$
\rho_{01}(t) = \rho_{01}(0)\,e^{-t/T_\phi}
$$

### 1.3.4 T₂ 与 T₁ 的关系

真实量子系统的总退相时间 T₂ 来自两个贡献：
1. **能量弛豫**（T₁ 过程）：不可避免地导致相位信息丢失，贡献为 $1/(2T_1)$
2. **纯退相**（$T_\phi$ 过程）：仅相位随机化，无能量交换

总退相率：
$$
\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi}
$$

> **T₂ 的物理含义**
>
> - T₂ 是量子比特的相干性（非对角元）衰减到 $1/e$ 的时间
> - 由于 $2T_1 \ge T_2$ 是理论下限（当 $T_\phi \to \infty$ 时 $T_2 = 2T_1$）
> - 实际中 $T_2 < 2T_1$，因为纯退相总是存在
> - 超导量子比特典型值：T₂ ≈ 10–100 μs

**证明**：振幅阻尼使非对角元衰减因子为 $e^{-t/(2T_1)}$，相位阻尼使非对角元衰减因子为 $e^{-t/T_\phi}$，两者合并：
$$
\rho_{01}(t) = \rho_{01}(0)\,e^{-t/(2T_1)} \cdot e^{-t/T_\phi} = \rho_{01}(0)\,e^{-t/T_2}
$$
其中 $1/T_2 = 1/(2T_1) + 1/T_\phi$。

### 1.3.5 布洛赫球图像

相位阻尼的作用效果：
- $Z$ 分量不变（没有能量弛豫）
- $X$ 和 $Y$ 分量指数衰减

对于初始态布洛赫向量 $(r_x, r_y, r_z)$：
$$
(r_x, r_y, r_z) \xrightarrow{\text{相位阻尼}} (e^{-t/T_2} r_x,\; e^{-t/T_2} r_y,\; r_z)
$$

布洛赫球沿赤道方向收缩——球体变为一个"椭圆体"，Z 轴方向不变，X-Y 平面收缩。最终态是沿 Z 轴的经典混合态（但布居数保持初始值）。

**图 1.2** [概念图] 相位阻尼使布洛赫球沿赤道方向收缩到 Z 轴——Z 轴上的点是不动点。

**即时练习 1.3**

1. 相位阻尼是否改变 $\rho$ 的谱（本征值）？为什么？
2. 如果 $T_1 = 100\,\mu\text{s}$，$T_2 = 80\,\mu\text{s}$，求 $T_\phi$。
3. 证明：相位阻尼信道的 Kraus 表示的两种形式是等价的（找出它们之间的幺正变换）。

---

## 1.4 退极化信道

### 1.4.1 物理背景

退极化信道（depolarizing channel）是**最简化的噪声模型**：它以一定概率将量子比特的状态完全随机化，否则保持原样。虽然物理真实性不如振幅阻尼和相位阻尼，但它数学简洁、对称性好，广泛用于理论分析和容错阈值证明。

### 1.4.2 Kraus 算符

单量子比特退极化信道的 Kraus 算符（对称形式）：
$$
K_0 = \sqrt{1-p}\, I,\quad
K_1 = \sqrt{\frac{p}{3}}\, X,\quad
K_2 = \sqrt{\frac{p}{3}}\, Y,\quad
K_3 = \sqrt{\frac{p}{3}}\, Z
$$

其中 $p \in [0,1]$ 是退极化参数（错误概率）。

**验证保迹**：
$$
K_0^\dagger K_0 + K_1^\dagger K_1 + K_2^\dagger K_2 + K_3^\dagger K_3 = (1-p)I + \frac{p}{3}(X^2 + Y^2 + Z^2) = (1-p)I + \frac{p}{3}(3I) = I
$$

### 1.4.3 退极化的作用

$$
\mathcal{E}_{\text{dep}}(\rho) = (1-p)\rho + \frac{p}{3}(X\rho X + Y\rho Y + Z\rho Z)
$$

利用泡利矩阵性质可以简化。对于 $\rho = \frac{I + \vec{r}\cdot\vec{\sigma}}{2}$：
- $X\rho X = \frac{I + (r_x, -r_y, -r_z)\cdot\vec{\sigma}}{2}$
- $Y\rho Y = \frac{I + (-r_x, r_y, -r_z)\cdot\vec{\sigma}}{2}$
- $Z\rho Z = \frac{I + (-r_x, -r_y, r_z)\cdot\vec{\sigma}}{2}$

代入得：
$$
\mathcal{E}_{\text{dep}}(\rho) = (1-p)\rho + \frac{p}{3}\left(\frac{3I - (r_x, r_y, r_z)\cdot\vec{\sigma}}{2}\right)
= \left(1 - \frac{4p}{3}\right)\rho + \frac{4p}{3}\cdot\frac{I}{2}
$$

即：
$$
\mathcal{E}_{\text{dep}}(\rho) = \left(1 - \frac{4p}{3}\right)\rho + \frac{4p}{3}\cdot\frac{I}{2}
$$

**物理意义**：以概率 $1 - 4p/3$ 保持不变，以概率 $4p/3$ 完全退化为最大混合态 $I/2$。

### 1.4.4 布洛赫球图像

退极化信道使布洛赫向量均匀收缩：
$$
\vec{r} \to \left(1 - \frac{4p}{3}\right) \vec{r}
$$

三个方向收缩因子相同——球体均匀缩小到原点。

**定义 1.2（退极化参数与保真度）** 退极化信道的**信道保真度**（channel fidelity）定义为
$$
F = \langle\psi|\mathcal{E}(|\psi\rangle\langle\psi|)|\psi\rangle
$$
对于退极化信道，平均保真度（对所有输入纯态平均）为 $1 - p/2$。

### 1.4.5 退极化信道与量子纠错阈值

退极化信道是理论分析中最常用的噪声模型：
- **对称性**：三个泡利错误等概率，简化分析
- **容错阈值**：在退极化噪声下，表面码的容错阈值约为 $p_{\text{th}} \approx 0.01$（即每物理门错误率低于 1% 才能实现有效纠错）
- 实际硬件噪声不完全是退极化的——但通过"泡利扭曲"（Pauli twirling）技术，任意噪声信道可以转化为泡利噪声（见 1.10 节）

**即时练习 1.4**

1. 计算退极化信道作用于 $\rho = |0\rangle\langle 0|$ 的输出（$p=0.3$）。
2. 证明退极化信道的单量子比特 Kraus 算符的四种选择（$I,X,Y,Z$）是完备的——任何其他算符都可以由它们线性组合得到。
3. 退极化信道是所有噪声信道中"最对称"的——这句话具体指什么？

---

## 1.5 泡利噪声信道

### 1.5.1 定义

泡利噪声信道（Pauli noise channel）是退极化信道的推广——允许三种泡利错误以不同概率出现：
$$
\mathcal{E}_{\text{Pauli}}(\rho) = (1-p_x-p_y-p_z)\rho + p_x X\rho X + p_y Y\rho Y + p_z Z\rho Z
$$

其中 $p_x, p_y, p_z \ge 0$ 且 $p_x+p_y+p_z \le 1$。

### 1.5.2 特殊情形

- **退极化信道**：$p_x = p_y = p_z = p/3$
- **比特翻转信道**（bit flip）：$p_x = p$，$p_y = p_z = 0$
  $$
  \mathcal{E}_{\text{BF}}(\rho) = (1-p)\rho + p X\rho X
  $$
  量子比特以概率 $p$ 发生 $|0\rangle \leftrightarrow |1\rangle$ 翻转
- **相位翻转信道**（phase flip）：$p_z = p$，$p_x = p_y = 0$
  $$
  \mathcal{E}_{\text{PF}}(\rho) = (1-p)\rho + p Z\rho Z
  $$
  这就是前面讨论的相位阻尼信道（表示一）
- **比特-相位翻转信道**：$p_y = p$，$p_x = p_z = 0$
  $$
  \mathcal{E}_{\text{BPF}}(\rho) = (1-p)\rho + p Y\rho Y
  $$

### 1.5.3 泡利信道的应用

泡利噪声模型在量子纠错理论中占据核心地位：

1. **稳定性子纠错码**：泡利错误是纠错码的"自然语言"——纠错码通常设计为纠正 $X$、$Z$ 及其组合错误
2. **错误率加权**：实际硬件中 $X$ 和 $Z$ 错误的概率可能不同（例如振幅阻尼主导时 $Z$ 错误比 $X$ 更常见）
3. **泡利扭曲**：通过随机地施加泡利门，可以将任意噪声信道转化为泡利信道，而门错误率不变——这是随机基准测试的理论基础

### 1.5.4 泡利信道的保真度

对于比特翻转信道，输入纯态 $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$：
$$
\mathcal{E}(|\psi\rangle\langle\psi|) = (1-p)|\psi\rangle\langle\psi| + p|\psi^\perp\rangle\langle\psi^\perp|
$$
其中 $|\psi^\perp\rangle = \beta^*|0\rangle - \alpha^*|1\rangle$。

保真度：
$$
F = \langle\psi|\mathcal{E}(|\psi\rangle\langle\psi|)|\psi\rangle = (1-p) \cdot 1 + p \cdot |\langle\psi|\psi^\perp\rangle|^2 = 1-p
$$

**即时练习 1.5**

1. 比特翻转信道作用于 $\rho = |+\rangle\langle+|$，输出是什么？$|+\rangle$ 对 X 错误免疫吗？
2. 能否用一个泡利信道近似振幅阻尼信道？在什么条件下近似成立？
3. 证明：泡利信道下的任何纯态的平均保真度（对所有纯态均匀平均）为 $1 - \frac{2}{3}(p_x+p_y+p_z)$。

---

## 1.6 T₁ 和 T₂ 时间演化模拟

### 1.6.1 联合演化方程

真实量子比特同时经历振幅阻尼和相位阻尼。将两个过程合并，得到非对角元和对角元的完整演化。

设初始密度矩阵 $\rho(0) = \begin{pmatrix} \rho_{00}(0) & \rho_{01}(0) \\ \rho_{10}(0) & \rho_{11}(0) \end{pmatrix}$。

**对角元（布居数）演化**——仅由 T₁ 决定：
$$
\rho_{11}(t) = \rho_{11}(0)\,e^{-t/T_1}
$$
$$
\rho_{00}(t) = 1 - \rho_{11}(t) = 1 - \rho_{11}(0)\,e^{-t/T_1}
$$

**非对角元（相干性）演化**——由 T₁ 和 T₂ 共同决定：
$$
\rho_{01}(t) = \rho_{01}(0)\,e^{-t/T_2}
$$

其中 $1/T_2 = 1/(2T_1) + 1/T_\phi$，$T_\phi$ 是纯退相时间。

### 1.6.2 联合 Kraus 算符

将振幅阻尼和相位阻尼串联，对应的联合 Kraus 算符为：

$$
K_{00} = \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{1-\gamma} \end{pmatrix} \sqrt{1-\lambda},\quad
K_{01} = \begin{pmatrix} 0 & \sqrt{\gamma} \\ 0 & 0 \end{pmatrix} \sqrt{1-\lambda}
$$
$$
K_{10} = \begin{pmatrix} 1 & 0 \\ 0 & -\sqrt{1-\gamma} \end{pmatrix} \sqrt{\lambda},\quad
K_{11} = \begin{pmatrix} 0 & \sqrt{\gamma} \\ 0 & 0 \end{pmatrix} \sqrt{\lambda}
$$

其中 $\gamma = 1 - e^{-t/T_1}$，$\lambda = 1 - e^{-t/T_\phi}$。

**验证**：对 $\rho$ 作用 $\sum_{i,j} K_{ij} \rho K_{ij}^\dagger$ 得到：
$$
\mathcal{E}(\rho) = \begin{pmatrix}
\rho_{00} + \gamma\rho_{11} & \sqrt{1-\gamma}(1-2\lambda)\rho_{01} \\
\sqrt{1-\gamma}(1-2\lambda)\rho_{10} & (1-\gamma)\rho_{11}
\end{pmatrix}
$$

代入 $\gamma$ 和 $\lambda$ 的表达式，非对角元衰减因子为 $e^{-t/(2T_1)} \cdot e^{-t/T_\phi} = e^{-t/T_2}$，符合预期。

### 1.6.3 数值模拟方法

在实际仿真中，用密度矩阵模拟噪声的步骤如下：

```
算法 1.1：带噪声的密度矩阵演化

输入：初始态 ρ₀，时间 t，T₁，T₂
输出：演化的 ρ(t)

1. 计算 γ = 1 - exp(-t/T₁)
2. 计算 λ = 1 - exp(-t/T₂ + t/(2T₁))   // 从 T₂ 反推纯退相参数
3. 构建四个 Kraus 算符 K₀₀, K₀₁, K₁₀, K₁₁
4. ρ(t) = Σᵢⱼ Kᵢⱼ ρ₀ Kᵢⱼ†
5. 返回 ρ(t)
```

**示例代码（Python 伪代码）**：
```python
import numpy as np

def amplitude_damping_kraus(gamma):
    K0 = np.array([[1, 0], [0, np.sqrt(1-gamma)]])
    K1 = np.array([[0, np.sqrt(gamma)], [0, 0]])
    return [K0, K1]

def phase_damping_kraus(lam):
    K0 = np.sqrt(1-lam) * np.eye(2)
    K1 = np.sqrt(lam) * np.array([[1, 0], [0, -1]])
    return [K0, K1]

def noise_evolution(rho, t, T1, T2):
    gamma = 1 - np.exp(-t/T1)
    lam = 1 - np.exp(-t/T2 + t/(2*T1))
    K_AD = amplitude_damping_kraus(gamma)
    K_PD = phase_damping_kraus(lam)
    rho_out = np.zeros((2,2), dtype=complex)
    for Ka in K_AD:
        for Kb in K_PD:
            K = Kb @ Ka  # 先振幅阻尼后相位阻尼
            rho_out += K @ rho @ K.conj().T
    return rho_out
```

### 1.6.4 模拟示例

**例 1.3** 设 $T_1 = 100\,\mu\text{s}$，$T_2 = 80\,\mu\text{s}$。初始态为 $|+\rangle$。求 $t = 50\,\mu\text{s}$ 时的密度矩阵。

$$
\rho(0) = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}
$$

计算：
- $\gamma = 1 - e^{-50/100} = 1 - e^{-0.5} \approx 0.3935$
- $T_\phi = (1/T_2 - 1/(2T_1))^{-1} = (1/80 - 1/200)^{-1} \approx 133.3\,\mu\text{s}$
- $\lambda = 1 - e^{-50/133.3} = 1 - e^{-0.375} \approx 0.3127$

代入公式：
$$
\rho(50\,\mu\text{s}) = \begin{pmatrix}
0.5 + 0.3935 \cdot 0.5 & \sqrt{1-0.3935}(1-2\cdot 0.3127)\cdot 0.5 \\
\sqrt{1-0.3935}(1-2\cdot 0.3127)\cdot 0.5 & (1-0.3935)\cdot 0.5
\end{pmatrix}
$$

$$
= \begin{pmatrix}
0.6967 & 0.7787 \cdot 0.3746 \cdot 0.5 \\
0.7787 \cdot 0.3746 \cdot 0.5 & 0.3033
\end{pmatrix}
\approx \begin{pmatrix}
0.6967 & 0.1459 \\
0.1459 & 0.3033
\end{pmatrix}
$$

相干性从 0.5 衰减到 0.1459，布居数向 $|0\rangle$ 偏移。

**即时练习 1.6**

1. 使用上例的参数，计算 $t = 200\,\mu\text{s}$ 时的密度矩阵。
2. 解释为什么 $T_\phi > T_2$ 总是成立。
3. 在 Python 中实现一个函数，输入 $T_1, T_2, t$，输出噪声演化的 Kraus 算符。

---

## 1.7 布洛赫球上的噪声收缩

### 1.7.1 三种噪声的布洛赫球图像总结

| 噪声类型 | X 分量 | Y 分量 | Z 分量 | 不动点 | 几何图像 |
|----------|--------|--------|--------|--------|----------|
| 振幅阻尼 | 衰减 $e^{-t/(2T_1)}$ | 衰减 $e^{-t/(2T_1)}$ | 趋向 1 | $|0\rangle$（北极） | 球体收缩到北极 |
| 相位阻尼 | 衰减 $e^{-t/T_2}$ | 衰减 $e^{-t/T_2}$ | 不变 | Z 轴所有点 | 球体收缩到 Z 轴 |
| 退极化 | 衰减 $1-4p/3$ | 衰减 $1-4p/3$ | 衰减 $1-4p/3$ | 原点（最大混合态） | 球体均匀收缩到原点 |

### 1.7.2 联合效应的几何描述

合并振幅阻尼和相位阻尼的完整噪声动力学，对布洛赫向量 $\vec{r} = (r_x, r_y, r_z)$ 的演化为：

$$
r_x(t) = r_x(0)\,e^{-t/T_2}
$$
$$
r_y(t) = r_y(0)\,e^{-t/T_2}
$$
$$
r_z(t) = 1 + (r_z(0) - 1)\,e^{-t/T_1}
$$

**三个阶段的直观理解**：
1. **早期**（$t \ll T_2 < 2T_1$）：赤道分量快速衰减，量子比特失去相干性，但布居数基本保持
2. **中期**（$T_2 < t < 2T_1$）：相干性几乎为零，只剩下布居数（经典概率混合态），Z 分量缓慢趋向北极
3. **晚期**（$t \gg 2T_1$）：所有信息都丢失，系统稳定在 $|0\rangle$（北极）

**图 1.3** [概念图] 布洛赫球上噪声的完整演化路径：从球面某点 -> 椭球面 -> Z 轴上某点 -> 北极。

### 1.7.3 保真度衰减

从初始纯态 $|\psi\rangle$ 到噪声演化后 $\rho(t)$ 的保真度：
$$
F(t) = \langle\psi|\rho(t)|\psi\rangle
$$

对于 $|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle$：
$$
F(t) = \frac{1}{2}\big[1 + (1 - \sin^2\theta\, e^{-2t/T_2} - \cos^2\theta\, e^{-2t/T_1})^{1/2}\big]
$$

当 $t \to \infty$ 时 $F(t) \to \cos^2(\theta/2)$——初始态越靠近 $|0\rangle$，最终保真度越高。

### 1.7.4 噪声与非正交态可分性

噪声对量子信息处理的核心威胁：它使原本可区分的量子态变得难以区分。

**例 1.4** 考虑两个正交态 $|0\rangle$ 和 $|1\rangle$。经过时间 $t$ 的振幅阻尼后：
$$
\rho_0(t) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix},\quad
\rho_1(t) = \begin{pmatrix} 1 - e^{-t/T_1} & 0 \\ 0 & e^{-t/T_1} \end{pmatrix}
$$

当 $t \gg T_1$ 时，$\rho_1(t) \to |0\rangle\langle 0|$——两个态变得无法区分。这就是量子信息被"擦除"的物理过程。

**即时练习 1.7**

1. 在布洛赫球上画出初始态 $|+i\rangle = (|0\rangle + i|1\rangle)/\sqrt{2}$ 受振幅阻尼和相位阻尼联合作用的轨迹（$T_1 = 50, T_2 = 40$，$t = 0, 10, 30, 100$）。
2. 为什么 Z 轴上的纯态（$|0\rangle$ 和 $|1\rangle$）不受相位阻尼影响？
3. 如果初始态是最大混合态 $I/2$，噪声能"改善"它的纯度吗？为什么？

---

## 1.8 噪声模型构建：从芯片参数

### 1.8.1 真实芯片噪声参数

构建实际噪声模型的第一步是获取硬件特征参数。以当前超导量子处理器为例：

**表 1.1：典型超导量子处理器噪声参数**

| 参数 | 符号 | 典型值范围 | 说明 |
|------|------|-----------|------|
| 能量弛豫时间 | T₁ | 10–300 μs | $|1\rangle \to |0\rangle$ 寿命 |
| 退相时间 | T₂ | 10–200 μs | 相干性寿命 |
| 单门错误率 | $\epsilon_{1Q}$ | $10^{-4}$–$10^{-3}$ | 单量子比特门错误概率 |
| CNOT 错误率 | $\epsilon_{2Q}$ | $10^{-3}$–$10^{-2}$ | 两量子比特门错误概率 |
| 读出错误率 | $\epsilon_{\text{meas}}$ | $10^{-3}$–$10^{-1}$ | 测量错误概率 |
| 门时间（单） | $t_{1Q}$ | 10–50 ns | 单门持续时间 |
| 门时间（两比特） | $t_{2Q}$ | 30–200 ns | CNOT 持续时间 |
| 测量时间 | $t_{\text{meas}}$ | 200–2000 ns | 读出持续时间 |

### 1.8.2 从 T₁、T₂ 到 Kraus 算符

给定芯片的 T₁ 和 T₂ 以及门操作时间 $t_g$，可计算门操作期间的噪声参数：

$$
\gamma_g = 1 - e^{-t_g/T_1}, \quad \lambda_g = 1 - e^{-t_g/T_\phi}
$$

其中 $T_\phi$ 由 $1/T_\phi = 1/T_2 - 1/(2T_1)$ 确定。

然后构建门操作的带噪声 Kraus 算符（先执行理想门 $U$，再施加噪声）：

$$
\mathcal{E}_{\text{noisy}}(U) = \mathcal{E}_{\text{noise}} \circ \mathcal{U}
$$

其中 $\mathcal{U}(\rho) = U\rho U^\dagger$，$\mathcal{E}_{\text{noise}}$ 是 1.6 节的联合噪声信道。

### 1.8.3 门错误率与保真度

**定义 1.3（门错误率）** 一个量子门 $\mathcal{U}$ 的**门错误率**（gate error rate）定义为 1 减去该门在噪声信道下的平均保真度（平均 over 所有输入纯态）：
$$
\epsilon = 1 - \int d\psi \langle\psi| \mathcal{E}_{\text{noisy}}(|\psi\rangle\langle\psi|) |\psi\rangle
$$

对于单量子比特门，如果噪声是退极化信道（参数 $p$），门错误率 $\epsilon = p/2$。

### 1.8.4 构建完整噪声模型

从芯片参数构建噪声模型的标准化流程：

```
算法 1.2：构建芯片噪声模型

输入：T₁, T₂, t_{1Q}, t_{2Q}, ε_{meas}
输出：完整噪声模型

[单比特噪声]
1. 计算 γ₁ = 1 - exp(-t_{1Q}/T₁)
2. 计算 λ₁ = 1 - exp(-t_{1Q}/T_φ)
3. 构建单比特 Kraus 集 {K₀₀, K₀₁, K₁₀, K₁₁}

[两比特噪声]
4. 计算 γ₂ = 1 - exp(-t_{2Q}/T₁)
5. 计算 λ₂ = 1 - exp(-t_{2Q}/T_φ)
6. 构建两比特 Kraus 集 = 张量积单比特 Kraus 集

[读出噪声]
7. 构建混淆矩阵 M (见 1.11 节)

[可选：门错误校准]
8. 如果测量了实际门错误率 ε_{meas,1Q} 和 ε_{meas,2Q},
   调整退极化参数 p 使模型门错误率匹配测量值
```

### 1.8.5 案例：构建 IBM Quantum 系统的噪声模型

以 IBM Quantum 系统（例如 ibm_sherbrooke）的典型参数为例：
- T₁ ≈ 150 μs，T₂ ≈ 120 μs
- 单门时间 $t_{1Q} = 35.6$ ns
- CNOT 时间 $t_{2Q} = 320$ ns

计算单门噪声参数：
- $\gamma_{1Q} = 1 - e^{-35.6\times10^{-3}/150} \approx 2.37\times10^{-4}$
- $T_\phi = (1/120 - 1/300)^{-1} \approx 200\,\mu\text{s}$
- $\lambda_{1Q} = 1 - e^{-35.6\times10^{-3}/200} \approx 1.78\times10^{-4}$

可见门操作期间噪声很小（$\gamma, \lambda \sim 10^{-4}$ 量级），这正是当前量子处理器能运行数千次门操作的基础。

**即时练习 1.8**

1. 给定 $T_1 = 50\,\mu\text{s}$，$T_2 = 40\,\mu\text{s}$，计算 $t_g = 50\,\text{ns}$ 时的 $\gamma$ 和 $\lambda$。
2. 解释为什么两比特门通常比单比特门有更高的错误率。
3. 如果实际测量的单比特门错误率为 $5\times10^{-4}$，而 T₁/T₂ 模型预测的门错误率为 $2\times10^{-4}$，额外的错误可能来自哪些因素？

---

## 1.9 马尔可夫近似

### 1.9.1 什么是马尔可夫近似？

本章至今讨论的噪声模型都假设了一个关键性质：**马尔可夫性**（Markovianity）——噪声过程没有记忆。即，系统在时刻 $t$ 的演化只依赖于当前状态，而不依赖于历史路径。

数学上，马尔可夫量子动力学由 **Lindblad 主方程**（Lindblad master equation）描述：
$$
\frac{d\rho}{dt} = -i[H, \rho] + \sum_k \left(L_k \rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\}\right)
$$

其中 $L_k$ 是 **Lindblad 算符**（或跳跃算符）。Kraus 算符对应于主方程在有限时间间隔上的积分。

### 1.9.2 马尔可夫近似成立的条件

马尔可夫近似成立需要：

1. **环境关联时间很短**：环境的记忆时间 $\tau_E$ 远小于系统演化的特征时间尺度 $\tau_S$：$\tau_E \ll \tau_S$
2. **弱耦合**：系统-环境耦合强度 $g$ 足够弱，使得环境受系统的影响可以忽略
3. **玻恩近似**：系统-环境态始终近似为直积态 $\rho_S(t) \otimes \rho_E$（环境不被系统"污染"）

当这些条件满足时，系统动力学是**马尔可夫**的——Kraus 算符只依赖于当前时间窗，可以写成 $t$ 的函数而不需要积分历史。

### 1.9.3 何时马尔可夫近似不成立？

非马尔可夫（non-Markovian）效应出现在：

1. **环境关联时间长**：例如核自旋环境对量子点的反馈（记忆效应显著）
2. **强耦合**：系统-环境纠缠不可忽略，环境状态被系统显著修改
3. **结构化的环境谱**：环境有离散的共振模式（如腔量子电动力学中的 Purcell 效应）

非马尔可夫动力学需要更复杂的描述（如张量网络、层级运动方程），不在本章范围。

### 1.9.4 为什么马尔可夫近似足够？

在大多数当前量子计算平台中：
- 环境（如超导线路中的热库、声子浴）的关联时间 $\sim$ ps–ns 量级
- 量子门操作时间 $\sim$ 10–300 ns
- 量子比特相干时间 $\sim$ 10–300 μs

因此 $\tau_E \ll \tau_S$ 成立，马尔可夫近似是好的。本章的所有噪声模型都建立在这个近似基础上。

**即时练习 1.9**

1. 用 Lindblad 主方程写出振幅阻尼信道的生成元（提示：$L = \sqrt{\gamma}\,\sigma_-$，其中 $\sigma_- = |0\rangle\langle 1|$）。
2. 为什么长时间存储（$t$ 接近 T₁/T₂ 量级）时，马尔可夫近似可能不再准确？
3. 搜索"非马尔可夫量子噪声"——它和"1/f 噪声"之间有什么关系？

---

## 1.10 门错误

### 1.10.1 从噪声信道到门错误

上一节我们构建了量子比特在空闲时间（idle）的噪声模型。但实际量子计算中，**门操作期间**也会引入噪声。门错误（gate error）包括：
- **操作期间的退相干**：门操作期间 T₁ 和 T₂ 仍在作用
- **控制脉冲不完美**：脉冲幅度、相位、频率的误差
- **串扰**（crosstalk）：对其他量子比特的意外影响
- **泄漏**（leakage）：从计算子空间到非计算能级的跃迁

### 1.10.2 泡利错误模型

门错误的最常用模型是**泡利错误模型**：在理想门之后，跟随一个泡利噪声信道。

对于单量子比特门 $U$：
$$
\mathcal{E}_{\text{noisy}}(U) = \mathcal{E}_{\text{Pauli}} \circ \mathcal{U}
$$

其中 $\mathcal{E}_{\text{Pauli}}(\rho) = (1-p_x-p_y-p_z)\rho + p_x X\rho X + p_y Y\rho Y + p_z Z\rho Z$。

**关键假设**：
- 错误与门本身无关（门无关错误模型）
- 错误是马尔可夫的
- 错误可以完全用泡利算符展开

### 1.10.3 门错误率与误差预算

单量子比特门的错误率通常定义为：
$$
\epsilon_{1Q} = 1 - \int d\psi \, \langle\psi| U^\dagger \mathcal{E}_{\text{noisy}}(|\psi\rangle\langle\psi|)U |\psi\rangle
$$

对于退极化噪声模型（门无关），$\epsilon_{1Q} = p/2$。

**误差预算**（error budget）示例：

**表 1.2：典型 CNOT 门的误差预算分解**

| 错误来源 | 贡献 | 说明 |
|----------|------|------|
| T₁/T₂ 退相干 | $3\times10^{-4}$ | 门时间 300 ns，T₁ = 100 μs |
| 脉冲幅度误差 | $5\times10^{-4}$ | 校准精度 0.1% |
| 脉冲相位误差 | $2\times10^{-4}$ | 相位校准残留 |
| 串扰 | $1\times10^{-4}$ | 相邻量子比特影响 |
| 泄漏 | $2\times10^{-4}$ | 到 |2⟩ 能级的跃迁 |
| **总计** | $\mathbf{1.3\times10^{-3}}$ | |

### 1.10.4 两比特门错误

两比特门的错误模型通常写为两个单比特泡利错误的张量积：
$$
\mathcal{E}_{\text{2Q}}(\rho) = \sum_{i,j} p_{ij} (P_i \otimes P_j) \rho (P_i^\dagger \otimes P_j^\dagger)
$$

其中 $P_i, P_j \in \{I, X, Y, Z\}$，$\sum_{i,j} p_{ij} = 1$。共有 16 项（包括 $I\otimes I$）。

在实际建模中，常用简化假设：
- **对称噪声**：$p_{ij} = p_{ji}$
- **主导错误**：只保留 $p_{IX}, p_{IZ}, p_{XI}, p_{ZI}$ 等最大的几项
- **纠缠错误**：$p_{XX}, p_{ZZ}$ 等

**即时练习 1.10**

1. 设单比特门的退极化参数 $p = 2\times10^{-3}$，求门错误率。
2. 如果 CNOT 门错误率主要来自 T₁/T₂ 退相干，估算 $T_1 = T_2 = 80\,\mu\text{s}$，门时间 $t_{2Q} = 400\,\text{ns}$ 时的 CNOT 错误率下限。
3. 解释为什么门无关错误模型对长门时间的操作（如 Toffoli 门）可能不够准确。

---

## 1.11 读出错误

### 1.11.1 读出错误的来源

测量（读出）不是完美的。在超导量子比特中，读出错误的来源包括：
- **态依赖的读出保真度**：$|0\rangle$ 和 $|1\rangle$ 的读出正确率可能不同
- **T₁ 弛豫**：在测量过程中 $|1\rangle$ 可能衰减为 $|0\rangle$，导致"误读为 0"
- **谐振器重叠**：两个态的谐振器响应分布有重叠区域
- **放大器噪声**：约瑟夫森参量放大器（JPA）的量子噪声

### 1.11.2 混淆矩阵

读出错误用**混淆矩阵**（confusion matrix / assignment fidelity matrix）完整描述：

$$
M = \begin{pmatrix}
P(0|0) & P(0|1) \\
P(1|0) & P(1|1)
\end{pmatrix}
$$

其中 $P(j|i)$ 是准备在 $|i\rangle$ 但读成 $j$ 的概率。满足 $P(0|i) + P(1|i) = 1$。

更紧凑的表达用读出错误率：
- $e_0 = P(1|0)$：将 $|0\rangle$ 误读为 $|1\rangle$ 的概率
- $e_1 = P(0|1)$：将 $|1\rangle$ 误读为 $|0\rangle$ 的概率

混淆矩阵：
$$
M = \begin{pmatrix}
1 - e_0 & e_1 \\
e_0 & 1 - e_1
\end{pmatrix}
$$

**读出保真度**定义为：
$$
F_{\text{readout}} = \frac{1}{2}\big[(1-e_0) + (1-e_1)\big] = 1 - \frac{e_0 + e_1}{2}
$$

### 1.11.3 读出错误对概率估计的影响

实验上，我们测量到的"原始"概率分布 $\vec{p}_{\text{raw}} = (p_0^{\text{raw}}, p_1^{\text{raw}})^T$ 与真实概率分布 $\vec{p}_{\text{true}} = (p_0^{\text{true}}, p_1^{\text{true}})^T$ 的关系为：

$$
\vec{p}_{\text{raw}} = M \cdot \vec{p}_{\text{true}}
$$

因此可以通过矩阵求逆恢复真实概率分布：
$$
\vec{p}_{\text{true}} = M^{-1} \cdot \vec{p}_{\text{raw}}
$$

这称为**读出误差缓解**（readout error mitigation）。

### 1.11.4 读出错误缓解

**算法 1.3：读出误差缓解**

```
1. 校准阶段：
   制备 |0⟩，测量 N 次，得到 e₀ = N(测得 1) / N
   制备 |1⟩，测量 N 次，得到 e₁ = N(测得 0) / N
   构建混淆矩阵 M

2. 缓解阶段：
   对原始测量结果计算 p_raw
   求解 p_true = M^{-1} · p_raw
   对 p_true 做约束（非负、归一化）
```

**重要限制**：
- 混淆矩阵本身也有统计误差（需要大量校准样本）
- 混淆矩阵在长时间内可能漂移（需要定期校准）
- 对于多量子比特，混淆矩阵呈指数增长（$2^n \times 2^n$），需要张量积近似或专门方法

**即时练习 1.11**

1. 如果 $e_0 = 0.02$，$e_1 = 0.05$，求读出保真度和混淆矩阵。
2. 测得 $\vec{p}_{\text{raw}} = (0.85, 0.15)^T$，使用上题的混淆矩阵，求 $\vec{p}_{\text{true}}$。
3. 为什么 $e_1$ 通常大于 $e_0$？（提示：考虑测量过程中的 T₁ 弛豫）

---

## 1.12 随机基准测试

### 1.12.1 为什么需要随机基准测试？

门错误率 $\epsilon$ 的测量本身存在悖论：要测量一个门的错误率，需要先运行这个门；但如果门错误率太高，测量结果本身不可靠。

随机基准测试（Randomized Benchmarking, RB）通过以下方式解决这个难题：
1. 运行**随机的门序列**（而不是单个门）
2. 利用序列长度增加时保真度的**指数衰减**拟合出平均门错误率
3. 对态制备和测量（SPAM）错误不敏感

### 1.12.2 基本 RB 协议

**单量子比特 RB 协议**：

```
算法 1.4：单量子比特随机基准测试

输入：门集 G（通常是 Clifford 门），序列长度集合 {m₁, m₂, ..., m_K}
输出：平均门错误率 ε

对每个序列长度 m：

  1. 随机生成 m 个 Clifford 门 {C₁, C₂, ..., C_m}
     从均匀分布随机选取

  2. 计算逆门：C_{m+1} = (C_m ··· C₂·C₁)⁻¹
     确保总序列等效于恒等操作

  3. 制备初始态 |0⟩，依次施加 C₁, C₂, ..., C_m, C_{m+1}

  4. 在计算基测量，统计得到 |0⟩ 的概率 P_m

  5. 重复步骤 1-4 多次（不同随机序列），取平均

对 {m, P_m} 做指数拟合：
  P_m = A·(1 - 2ε)^m + B

平均门错误率 ε 从拟合指数中提取
```

**为什么是指数衰减？** 因为每次门操作引入的错误是独立的（马尔可夫假设），经过 $m$ 个门后，总保真度与 $(1 - 2\epsilon)^m$ 成正比——这是独立随机错误累积的典型行为。

### 1.12.3 RB 结果解释

**图 1.4** [概念图] 随机基准测试典型数据：横轴为 Clifford 门数量 $m$，纵轴为 $|0\rangle$ 观测概率 $P_m$，数据点呈指数衰减。

拟合参数：
- $\epsilon$：平均门错误率（每个 Clifford 门）
- $A$：SPAM 相关常数（反映态制备和测量保真度）
- $B$：偏移常数（当 $m \to \infty$ 时的渐近值，通常为 $1/2$）

**典型结果**：
- 超导量子比特：单量子比特 Clifford 门错误率 $\sim 2\times10^{-4}$
- 对应退极化参数 $p \sim 4\times10^{-4}$

### 1.12.4 RB 的变体

- **两比特 RB**：测量两比特 Clifford 门的平均错误率
- **直接随机基准测试（Direct RB）**：不限于 Clifford 门，可评估任意门集
- **循环基准测试（Cycle Benchmarking）**：评估特定量子操作的错误
- **镜像电路基准测试（Mirror Circuit Benchmarking）**：用镜像电路结构快速评估

**即时练习 1.12**

1. 解释为什么 RB 对 SPAM 错误不敏感。（提示：指数衰减的截距 $A$ 吸收 SPAM 错误，但斜率 $\epsilon$ 不受影响。）
2. 如果 RB 拟合得到 $P_m = 0.95 \times (0.998)^m + 0.5$，求平均每 Clifford 门的错误率。
3. 思考：如果马尔可夫近似不成立（即错误有记忆），RB 的指数衰减假设还成立吗？

---

## 1.13 本章习题

### 基础题（1–7题）

**1.** 写出以下量子操作的 Kraus 算符：
$$
\mathcal{E}(\rho) = \frac{1}{2}\rho + \frac{1}{4}X\rho X + \frac{1}{4}Y\rho Y
$$
验证保迹条件。

**2.** 振幅阻尼信道的 $\gamma = 0.2$，输入 $\rho = \frac{1}{2}\begin{pmatrix} 1 & 0.5 \\ 0.5 & 1 \end{pmatrix}$。计算输出密度矩阵和保真度 $F = \langle+|\rho_{\text{out}}|+\rangle$。

**3.** 某量子比特的 $T_1 = 120\,\mu\text{s}$，$T_2 = 90\,\mu\text{s}$。求纯退相时间 $T_\phi$。如果门时间为 $50\,\text{ns}$，计算 $\gamma$ 和 $\lambda$。

**4.** 证明退极化信道的 Kraus 算符也可以写为：
$$
K_0 = \sqrt{1-\frac{3p}{4}} I,\quad K_i = \frac{\sqrt{p}}{2} \sigma_i \;(i=1,2,3)
$$
并说明这两个表示之间的关系。

**5.** 比特翻转信道（概率 $p$）作用于 $\rho = |-\rangle\langle-|$，计算输出态和保真度。$|-\rangle$ 对 $X$ 错误免疫吗？

**6.** 混淆矩阵 $M = \begin{pmatrix} 0.97 & 0.06 \\ 0.03 & 0.94 \end{pmatrix}$。测量得到 1000 次中 820 次 $|0\rangle$、180 次 $|1\rangle$。估计真实概率分布。

**7.** 随机基准测试数据：$m=1$ 时 $P=0.949$，$m=10$ 时 $P=0.885$，$m=50$ 时 $P=0.682$，$m=200$ 时 $P=0.549$。估计平均门错误率 $\epsilon$。

### 进阶题（8–12题）

**8.** 推导振幅阻尼 + 相位阻尼联合信道的 Kraus 算符，并验证得到的 $\rho_{01}(t)$ 衰减因子为 $e^{-t/T_2}$。

**9.** 考虑一个两量子比特的退极化信道：每个量子比特独立经历退极化（参数 $p$）。写出这个联合信道的 Kraus 算符（共 16 项），并求 $|00\rangle$ 保真度。

**10.** 证明：对任意量子操作 $\mathcal{E}$，输入 $\rho$ 和输出 $\mathcal{E}(\rho)$ 之间的迹距离满足：
$$
D(\rho, \mathcal{E}(\rho)) \le \frac{1}{2}\sum_k \operatorname{Tr}\left(|[K_k, \rho]|\right)
$$
其中 $[A,B] = AB - BA$ 是对易子。

**11.** 推导单比特门退极化错误模型下，门错误率 $\epsilon$ 与退极化参数 $p$ 的关系：$\epsilon = p/2$。

**12.** 假设一个量子比特在空闲时受振幅阻尼和相位阻尼作用（$T_1 = 100\,\mu\text{s}$，$T_2 = 80\,\mu\text{s}$）。初始制备在 $|+\rangle$。问：经过多长时间，保真度 $F = \langle+|\rho(t)|+\rangle$ 降至 0.9？

### 挑战题（13–15题）

**13.** **Kraus 表示的非唯一性**。设 $\{K_k\}$ 和 $\{K'_k\}$ 是两组 Kraus 算符，它们生成相同的量子操作 $\mathcal{E}$。证明存在一个幺正矩阵 $U$（适当补零成为方阵）使得 $K'_k = \sum_j u_{kj} K_j$。

**14.** **退极化信道的容错阈值估算**。假设表面码（surface code）的容错阈值 $p_{\text{th}} \approx 0.01$（退极化参数）。如果每个物理门的错误率 $\epsilon = 10^{-3}$，问需要多少物理量子比特才能编码一个逻辑量子比特使得逻辑错误率降到 $10^{-6}$？（提示：逻辑错误率与物理错误率的关系为 $p_L \approx C (p/p_{\text{th}})^{(d+1)/2}$，其中 $d$ 是码距，$C \approx 0.1$ 为常数。）

**15.** **噪声下的纠缠制备**。两个量子比特初始为 $|00\rangle$，施加 CNOT 门（控制比特为 q₀，目标比特为 q₁）前先对 q₀ 施加 Hadamard 门。每个量子比特在操作期间经历独立的退极化噪声（参数 $p=0.01$）。计算：
   (a) 在没有噪声的情况下，输出态是什么？
   (b) 在噪声下，输出密度矩阵是什么（写出完整的 $4\times4$ 矩阵）？
   (c) 计算输出态与 Bell 态 $|\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$ 之间的保真度。

---

### 知识点索引

振幅阻尼信道, 保迹条件, 比特翻转信道, 比特-相位翻转信道, 布洛赫球, 纯退相, 读出保真度, 读出错误, 读出误差缓解, 错误传播, 马尔可夫近似, 非马尔可夫过程, 混淆矩阵, 开放量子系统, Kraus 算符, 门错误, 门错误率, 能量弛豫, 泡利噪声信道, 平均门错误率, 谱分解, 腔量子电动力学, 量子操作, 量子映射, 量子极限, 随机基准测试, T₁, T₂, Tₚ, 算符和表示, 退极化信道, 退相干, 系统-环境模型, 相位翻转信道, 相位阻尼信道, 信道保真度, 幺正演化, 1/f 噪声, 振幅阻尼, 误差预算

> **本章小结**
>
> 量子噪声是量子计算从理论走向实践的核心挑战。本章建立了量子噪声的系统描述框架：
>
> - **Kraus 算符**是描述任意量子操作的通用语言，将开放系统动力学浓缩为一组作用在系统上的算符
> - **三类基本噪声信道**——振幅阻尼（T₁）、相位阻尼（T₂）、退极化——分别对应能量弛豫、纯退相和各向同性错误
> - **T₁ 和 T₂** 是量子比特最基本的相干性指标，两者关系 $1/T_2 = 1/(2T_1) + 1/T_\phi$ 揭示了能量弛豫和纯退相的共同贡献
> - **布洛赫球**提供了噪声过程的直观几何图像：振幅阻尼使球体收缩到北极，相位阻尼使球体收缩到 Z 轴，退极化使球体均匀收缩到原点
> - **从芯片参数构建噪声模型**的过程——T₁/T₂ → 门噪声参数 → Kraus 算符——是连接硬件和仿真算法的桥梁
> - **马尔可夫近似**保证了 Kraus 算符形式的时间无关性，是全部噪声信道理论的前提
> - **门错误、读出错误和随机基准测试**是噪声的表征和测量工具，让我们能够定量评估量子处理器的性能
>
> 下一章我们将学习如何对抗这些噪声——量子纠错码的基本原理。
