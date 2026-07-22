# 第3章 密度矩阵与混合态

> **本章导读**
>
> 第2章我们学习了用态矢量 $|\psi\rangle$ 描述量子系统。纯态矢量可以描述一个孤立的、信息完备的量子系统。但现实世界并非如此完美——我们往往只拥有系统的**部分信息**：系统可能与环境纠缠（导致退相干），或者我们制备系统时本身就不确定它的状态。这时，态矢量就不够用了。我们需要一个更强大的工具：**密度矩阵（density matrix）**。
>
> 密度矩阵是量子力学中最优雅也最实用的发明之一。它统一了"量子概率"（叠加）和"经典概率"（混合），让我们能无缝处理孤立系统和开放系统。本章从密度矩阵的定义出发，逐步深入到纯态与混态的判据、演化规律、约化密度矩阵、量子熵以及态之间的距离度量。
>
> 学完本章，你将能够：
> - 理解为什么要引入密度矩阵
> - 写出纯态和混态的密度矩阵表示
> - 用 $\text{Tr}(\rho^2)$ 判定一个态是纯态还是混态
> - 掌握密度矩阵的演化方程
> - 用部分求迹计算约化密度矩阵
> - 计算和解释冯·诺依曼熵
> - 理解保真度和迹距离的含义
>
> **先修知识**：第1章线性代数（矩阵迹、张量积、谱分解）、第2章量子力学基本假设（态矢量、算符、测量）

---

## 3.1 密度矩阵的定义

### 3.1.1 从态矢量到密度矩阵——为什么需要它？

态矢量描述的是"信息完备"的系统——我们知道系统精确地处于某个纯态 $|\psi\rangle$。但在很多实际情况中，我们只有**部分信息**：

1. **制备不确定性**：实验装置以概率 $p_i$ 制备不同的量子态 $|\psi_i\rangle$。我们不知道单次制备具体是哪个态，只知道概率分布。
2. **纠缠系统**：当两个子系统纠缠时，每个子系统自身并不处于一个确定的纯态——它的状态只能用"约化密度矩阵"描述。
3. **退相干**：系统与环境相互作用后，量子信息泄漏到环境中，系统状态退化为混合态。

在这类情况下，我们不能再用单一的态矢量来描述系统。密度矩阵给出了一个统一的框架。

### 3.1.2 纯态的密度矩阵

如果系统处于一个已知的纯态 $|\psi\rangle$，我们定义其**密度矩阵**为：

$$
\rho = |\psi\rangle\langle\psi|
$$

**例 3.1** 对于 $|\psi\rangle = |0\rangle$，其密度矩阵为：

$$
\rho = |0\rangle\langle 0| = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}
$$

**例 3.2** 对于 $|\psi\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |+\rangle$，其密度矩阵为：

$$
\rho = |+\rangle\langle +| = \frac{1}{2}\begin{pmatrix} 1 \\ 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}
$$

**例 3.3** 对于一般单比特纯态 $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$（$|\alpha|^2 + |\beta|^2 = 1$）：

$$
\rho = \begin{pmatrix} |\alpha|^2 & \alpha\overline{\beta} \\ \overline{\alpha}\beta & |\beta|^2 \end{pmatrix}
$$

非对角元 $\alpha\overline{\beta}$ 体现了量子态的**相干性**。

> **全局相位消失了：** 还记得 $e^{i\theta}|\psi\rangle$ 和 $|\psi\rangle$ 表示同一个物理态吗？在密度矩阵中，$(e^{i\theta}|\psi\rangle)(e^{-i\theta}\langle\psi|) = |\psi\rangle\langle\psi|$，全局相位自然消失。这是密度矩阵的一个优点。

### 3.1.3 混态的必要性

假设我们有一个装置，以 50% 概率制备 $|0\rangle$，以 50% 概率制备 $|1\rangle$。我们不知道单次实验制备的是哪个态——只知道概率分布。这个系统的状态**不是**叠加态 $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$，而是一个**经典混合**。

如何区分这两种情况？

- **叠加态** $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$：有确定**相位关系**，在 $X$ 基下测量总是得到 $|+\rangle$。
- **经典混合**：以 50% 概率是 $|0\rangle$、50% 概率是 $|1\rangle$，**没有**相位关系，在 $X$ 基下测量得到 $|+\rangle$ 和 $|-\rangle$ 各 50%。

密度矩阵可以统一描述这两者。

### 3.1.4 混态的密度矩阵

**定义 3.1（密度矩阵）** 一个量子系统的**密度矩阵**定义为：

$$
\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|
$$

其中 $p_i > 0$，$\sum_i p_i = 1$，$|\psi_i\rangle$ 是（不一定正交的）归一化态矢量。

这个表达式称为**系综（ensemble）**解释：系统以概率 $p_i$ 处于态 $|\psi_i\rangle$。

**例 3.4** 等概率混合 $|0\rangle$ 和 $|1\rangle$：

$$
\rho = \frac{1}{2}|0\rangle\langle 0| + \frac{1}{2}|1\rangle\langle 1|
= \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

这是**最大混态**（maximally mixed state），也称为完全去极化态。

**例 3.5** 等概率混合 $|+\rangle$ 和 $|-\rangle$：

$$
\rho = \frac{1}{2}|+\rangle\langle +| + \frac{1}{2}|-\rangle\langle -|
= \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

和例 3.4 的结果相同！这说明**同一个密度矩阵可以由不同的系综实现**——密度矩阵包含了所有可观测信息，而系综的"具体故事"并不唯一。

> **重要思考：** 密度矩阵包含的信息比态矢量少（没有全局相位），但比经典概率分布多（包含相干信息）。它是连接量子与经典的桥梁。

### 3.1.5 密度矩阵的三条性质

一个合法的密度矩阵必须满足以下三条性质：

1. **迹为 1**：$\text{Tr}(\rho) = 1$

   **证明**：$\text{Tr}(\rho) = \sum_i p_i \text{Tr}(|\psi_i\rangle\langle\psi_i|) = \sum_i p_i \cdot 1 = 1$

2. **半正定性**：$\rho \geq 0$（对所有 $|\phi\rangle$，$\langle\phi|\rho|\phi\rangle \geq 0$）

   这保证了所有概率幅的平方和为 1，且任何测量概率非负。

3. **自伴性**：$\rho^\dagger = \rho$

   因为每个 $|\psi_i\rangle\langle\psi_i|$ 是 Hermitian 的，实系数线性组合也 Hermitian。

反过来，任何一个满足这三条的矩阵都对应某个量子态。

**例 3.6** 判断 $\rho = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ 是否合法？

计算 $\text{Tr}(\rho) = 2 \neq 1$，迹不为 1，所以不是合法密度矩阵（归一化后 $\frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ 才合法）。

**例 3.7** 判断 $\rho = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ 是否合法？

$\text{Tr}(\rho) = 1$，$\rho^\dagger = \rho$，且特征值 $1, 0 \geq 0$。合法。

**例 3.8** 判断 $\rho = \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ 是否合法？

迹为 0，且特征值 $1/2, -1/2$ 有负值。不合法。

> **密度矩阵的谱分解**：任何密度矩阵 $\rho$ 可以谱分解为：
> $$\rho = \sum_k \lambda_k |k\rangle\langle k|$$
> 其中 $\lambda_k \geq 0$，$\sum_k \lambda_k = 1$，$\{|k\rangle\}$ 是正交归一基。这个分解非常重要，因为 $\lambda_k$ 就是测量本征态 $|k\rangle$ 的概率。

**性质总结**：

| 性质 | 数学表述 | 物理含义 |
|------|---------|---------|
| 迹为 1 | $\text{Tr}(\rho) = 1$ | 概率总和为 1 |
| 半正定 | $\rho \geq 0$ | 概率非负 |
| 自伴 | $\rho^\dagger = \rho$ | 本征值为实数 |

### 3.1.6 密度矩阵下的期望值

在态矢量描述中，算符 $A$ 的期望值为 $\langle A \rangle = \langle\psi|A|\psi\rangle$。

在密度矩阵描述中，期望值为：

$$
\langle A \rangle = \text{Tr}(\rho A)
$$

**证明**：对于 $\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$：

$$
\text{Tr}(\rho A) = \sum_i p_i \text{Tr}(|\psi_i\rangle\langle\psi_i| A) = \sum_i p_i \langle\psi_i|A|\psi_i\rangle = \langle A \rangle
$$

**例 3.9** 对于最大混态 $\rho = \frac{1}{2}I$，计算 $\langle Z \rangle$：

$$
\langle Z \rangle = \text{Tr}\left(\frac{1}{2}I \cdot Z\right) = \frac{1}{2}\text{Tr}(Z) = 0
$$

**例 3.10** 对于 $\rho = |0\rangle\langle 0|$，计算 $\langle Z \rangle$ 和 $\langle X \rangle$：

$\langle Z \rangle = \text{Tr}(|0\rangle\langle 0| Z) = \text{Tr}\left(\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\right) = 1$

$\langle X \rangle = \text{Tr}(|0\rangle\langle 0| X) = \text{Tr}\left(\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\right) = 0$

**例 3.11** 对于 $\rho = \frac{1}{2}(|0\rangle\langle 0| + |1\rangle\langle 1|)$，计算 $\langle Z \rangle$：

$\langle Z \rangle = \text{Tr}\left(\frac{1}{2}I \cdot Z\right) = 0$

这与我们对此态在 $Z$ 方向上没有极化的预期一致。

> **为什么用迹？** 迹运算给出了一个简洁的线性泛函，不需要指定具体的系综。任何两个产生相同密度矩阵的系综，对所有算符的期望值都相同——这正是物理可观测量的要求。

---

## 3.2 纯态与混态的判据

### 3.2.1 基本的判据：$\text{Tr}(\rho^2)$

如何判断一个给定的密度矩阵描述的是纯态还是混态？最直接的判据是计算**纯度（purity）**：

$$
\gamma = \text{Tr}(\rho^2)
$$

- **纯态**：$\gamma = 1$。因为 $\rho = |\psi\rangle\langle\psi|$，$\rho^2 = |\psi\rangle\langle\psi|\psi\rangle\langle\psi| = |\psi\rangle\langle\psi| = \rho$，所以 $\text{Tr}(\rho^2) = \text{Tr}(\rho) = 1$。
- **混态**：$\gamma < 1$。因为 $\rho$ 有多个非零本征值，每个小于 1，平方和小于 1。
- **最大混态**：对于 $d$ 维系统，$\gamma = 1/d$。

**例 3.12** 纯态 $\rho = |0\rangle\langle 0|$：

$$
\rho^2 = |0\rangle\langle 0|0\rangle\langle 0| = |0\rangle\langle 0| = \rho
$$
$$
\text{Tr}(\rho^2) = \text{Tr}(\rho) = 1 \quad \text{——纯态}
$$

**例 3.13** 混态 $\rho = \frac{1}{2}(|0\rangle\langle 0| + |1\rangle\langle 1|)$：

$$
\rho^2 = \frac{1}{4}(|0\rangle\langle 0| + |1\rangle\langle 1|)
$$
$$
\text{Tr}(\rho^2) = \frac{1}{4}(1 + 1) = \frac{1}{2} < 1 \quad \text{——混态}
$$

**例 3.14** 对于单比特一般态：

$$
\rho = \frac{1}{2}(I + \vec{r} \cdot \vec{\sigma}), \quad |\vec{r}| \leq 1
$$

计算 $\rho^2 = \frac{1}{4}(I + 2\vec{r}\cdot\vec{\sigma} + |\vec{r}|^2 I)$，所以：

$$
\text{Tr}(\rho^2) = \frac{1}{2}(1 + |\vec{r}|^2)
$$

- $|\vec{r}| = 1$：纯态（在布洛赫球表面）
- $|\vec{r}| < 1$：混态（在布洛赫球内部）
- $|\vec{r}| = 0$：最大混态（球心）

### 3.2.2 最大混态

**定义 3.2（最大混态）** 对于 $d$ 维量子系统，**最大混态**（maximally mixed state）定义为：

$$
\rho_* = \frac{I}{d}
$$

它对应"我们对该系统一无所知"的情况——所有基矢等概率出现。

**性质**：
- $\text{Tr}(\rho_*^2) = 1/d$，是所能达到的最小纯度
- 对于任何测量基，所有结果概率相等
- 在任何方向上的期望值都为零

**例 3.15** 单比特最大混态 $\rho = I/2$，对应布洛赫球心。$\text{Tr}(\rho^2) = 1/2$。

**例 3.16** 两个比特的最大混态 $\rho = I/4$，$\text{Tr}(\rho^2) = 1/4$。

> **为什么叫"最大"混态？** 因为在所有混态中，它的 $\text{Tr}(\rho^2)$ 最小，即"最混乱"。

### 3.2.3 布洛赫球直观

单比特密度矩阵可以在布洛赫球上直观地表示：

$$
\rho = \frac{1}{2}(I + \vec{r} \cdot \vec{\sigma}), \quad \vec{r} = (x, y, z), \quad |\vec{r}| \leq 1
$$

其中 $\vec{\sigma} = (X, Y, Z)$ 是 Pauli 矩阵向量，$\vec{r}$ 称为**布洛赫向量**。

- $|\vec{r}| = 1$：纯态（球面上）
- $|\vec{r}| < 1$：混态（球内部）
- $\vec{r} = 0$：最大混态（球心）

**纯度的几何意义**：$\text{Tr}(\rho^2) = \frac{1}{2}(1 + |\vec{r}|^2)$，所以纯度只与到球心的距离有关，与方向无关。

**例 3.17** 用布洛赫向量表示下列态：

- $|0\rangle$：$\vec{r} = (0, 0, 1)$——球北极
- $|1\rangle$：$\vec{r} = (0, 0, -1)$——球南极
- $|+\rangle$：$\vec{r} = (1, 0, 0)$——$+x$ 方向
- 最大混态：$\vec{r} = (0, 0, 0)$——球心

### 3.2.4 二维以上的纯度

对于 $d$ 维系统：

- 纯态：$\text{Tr}(\rho^2) = 1$
- 最大混态：$\text{Tr}(\rho^2) = 1/d$
- 一般混态：$1/d < \text{Tr}(\rho^2) < 1$

**例 3.18** 对于 qutrit（$d = 3$）：

- 纯态：$\text{Tr}(\rho^2) = 1$
- 最大混态 $\rho = I/3$：$\text{Tr}(\rho^2) = 1/3$
- 混态 $\rho = \text{diag}(1/2, 1/2, 0)$：$\text{Tr}(\rho^2) = 1/4 + 1/4 + 0 = 1/2$

**小练习**：对于一个 $d=4$ 的系统，一个混态的纯度范围是多少？

---

## 3.3 密度矩阵的演化

### 3.3.1 封闭系统的演化

对于封闭（孤立）量子系统，态矢量按薛定谔方程演化：

$$
i\hbar\frac{d}{dt}|\psi(t)\rangle = H|\psi(t)\rangle
$$

解为 $|\psi(t)\rangle = U(t)|\psi(0)\rangle$，其中 $U(t) = e^{-iHt/\hbar}$ 是幺正算符。

密度矩阵的演化直接由系综定义导出：

$$
\rho(t) = \sum_i p_i |\psi_i(t)\rangle\langle\psi_i(t)|
= \sum_i p_i U(t)|\psi_i(0)\rangle\langle\psi_i(0)|U^\dagger(t)
= U(t)\rho(0)U^\dagger(t)
$$

**封闭系统演化规律**：

$$
\boxed{\rho(t) = U(t)\rho(0)U^\dagger(t)}
$$

**性质**：
- 幺正演化保持纯度：$\text{Tr}(\rho(t)^2) = \text{Tr}(\rho(0)^2)$
- 纯态演化到纯态，混态演化到混态
- 演化是可逆的

**例 3.19** 初始态 $\rho(0) = |0\rangle\langle 0|$，在 $H = \frac{\pi}{2}X$（产生 $\pi$ 脉冲）下演化：

$U = e^{-iHt/\hbar}$，当 $t$ 使得 $Ut = \pi/2$ 时，$U = -iX$（忽略全局相位）：

$$
\rho(t) = X|0\rangle\langle 0|X = |1\rangle\langle 1|
$$

态从 $|0\rangle$ 翻转到 $|1\rangle$。

**例 3.20** 初始态 $\rho(0) = \frac{1}{2}(|0\rangle\langle 0| + |1\rangle\langle 1|)$（最大混态），在任意幺正演化下：

$$
\rho(t) = U \cdot \frac{I}{2} \cdot U^\dagger = \frac{I}{2}
$$

最大混态在幺正演化下不变——没有任何信息。

> **封闭系统演化定理**：密度矩阵的幺正演化保持其本征值不变（因为 $U\rho U^\dagger$ 与 $\rho$ 相似），变化的只是本征向量。

### 3.3.2 冯·诺依曼方程

对 $\rho(t) = U(t)\rho(0)U^\dagger(t)$ 求时间导数，得到密度矩阵的运动方程：

$$
\frac{d\rho}{dt} = \frac{dU}{dt}\rho(0)U^\dagger + U\rho(0)\frac{dU^\dagger}{dt}
$$

代入 $U = e^{-iHt/\hbar}$，$\frac{dU}{dt} = -\frac{i}{\hbar} H U$，得到：

$$
\boxed{i\hbar\frac{d\rho}{dt} = [H, \rho]}
$$

这就是**冯·诺依曼方程（von Neumann equation）**，也称为**刘维尔-冯·诺依曼方程**。

它与薛定谔方程**等价**，但适用范围更广——可以同时处理纯态和混态。

**性质**：
- 保持迹：$\frac{d}{dt}\text{Tr}(\rho) = 0$
- 保持 Hermiticity：$\rho(t)^\dagger = \rho(t)$
- 保持纯度：$\frac{d}{dt}\text{Tr}(\rho^2) = 0$
- 解为 $\rho(t) = e^{-iHt/\hbar}\rho(0)e^{iHt/\hbar}$

> **冯·诺依曼方程的重要性**：它告诉我们，封闭系统的信息是守恒的。退相干和不可逆性只出现在我们对部分系统取迹时——这就是下一节的内容。

### 3.3.3 与薛定谔方程对比

| 属性 | 薛定谔方程 | 冯·诺依曼方程 |
|------|-----------|--------------|
| 适用范围 | 纯态 | 纯态和混态 |
| 数学形式 | 一阶线性微分方程 | 一阶线性微分方程 |
| 是否可逆 | 是 | 是 |
| 保持纯度 | 自动满足（$|\psi\rangle$ 保持模为 1） | $\frac{d}{dt}\text{Tr}(\rho^2) = 0$ |
| 算符形式 | $i\hbar\frac{d}{dt}|\psi\rangle = H|\psi\rangle$ | $i\hbar\frac{d\rho}{dt} = [H, \rho]$ |

**例 3.21** 使用冯·诺依曼方程验证：对于 $H = \omega Z$，初始态 $\rho(0) = |+\rangle\langle +|$，求 $\rho(t)$。

$[H, \rho(0)] = \omega[Z, \frac{1}{2}(I+X)] = \frac{\omega}{2}[Z, X] = \frac{\omega}{2} \cdot 2iY = i\omega Y$

$\frac{d\rho}{dt} = -\frac{i}{\hbar}[H, \rho] = \frac{\omega}{\hbar} Y$

解为 $\rho(t) = \frac{1}{2}(I + \cos(2\omega t) X + \sin(2\omega t) Y)$——在 Bloch 球 $xy$ 平面旋转。

### 3.3.4 开放系统的演化——简介

真实量子系统几乎总是**开放系统**，与环境有相互作用。此时系统不再满足冯·诺依曼方程。开放系统演化的标准处理是**系统-环境模型**：

总系统（系统 $S$ + 环境 $E$）是封闭的，满足冯·诺依曼方程。系统的状态通过对环境求部分迹得到：

$$
\rho_S(t) = \text{Tr}_E[U_{SE}(t)(\rho_S(0) \otimes \rho_E(0))U_{SE}^\dagger(t)]
$$

这种演化通常不再保纯度——系统从纯态演化为混态，这就是**退相干**。

> **适用范围**：对开放系统动力学更深入的讨论（Kraus 算符、Lindblad 方程、量子噪声信道）见模块五第21章。

---

## 3.4 约化密度矩阵

### 3.4.1 问题场景

考虑一个由两个子系统 $A$ 和 $B$ 组成的复合系统。如果我们只关心子系统 $A$——也就是说，我们只能对 $A$ 进行测量——应该如何描述 $A$ 的状态？

即使整个复合系统处于纯态 $|\Psi\rangle_{AB}$，子系统 $A$ 一般也不处于纯态。我们需要一个工具来"扔掉" $B$ 的信息，保留 $A$ 的全部可观测信息——这就是**约化密度矩阵（reduced density matrix）**。

### 3.4.2 部分求迹

**定义 3.3（部分求迹）** 对于复合系统 $AB$ 上的密度矩阵 $\rho_{AB}$，子系统 $A$ 的**约化密度矩阵**定义为：

$$
\rho_A = \text{Tr}_B(\rho_{AB})
$$

其中 $\text{Tr}_B$ 表示对子系统 $B$ 求部分迹。

**部分求迹的规则**：如果 $\rho_{AB} = \rho_A \otimes \rho_B$（可分离的直积态），则：

$$
\text{Tr}_B(\rho_A \otimes \rho_B) = \rho_A \cdot \text{Tr}(\rho_B) = \rho_A
$$

更一般地，部分迹定义为线性扩展：

$$
\text{Tr}_B\left(\sum_{i,j,k,l} c_{ijkl} |i\rangle\langle j|_A \otimes |k\rangle\langle l|_B\right) = \sum_{i,j,k} c_{ijkk} |i\rangle\langle j|_A
$$

**例 3.22** 若 $\rho_{AB} = |0\rangle\langle 0|_A \otimes |0\rangle\langle 0|_B$，则：

$\rho_A = \text{Tr}_B(|0\rangle\langle 0|_A \otimes |0\rangle\langle 0|_B) = |0\rangle\langle 0|_A \cdot \text{Tr}(|0\rangle\langle 0|_B) = |0\rangle\langle 0|_A$

**例 3.23** 对于更一般的 $\rho_{AB} = \sum_{ijkl} a_{ijkl} |i\rangle\langle j|_A \otimes |k\rangle\langle l|_B$：

$\rho_A = \sum_{ij} \left(\sum_k a_{ijkk}\right) |i\rangle\langle j|_A$

$A$ 的矩阵元是 $\rho_{AB}$ 中 $B$ 的"对角块"的迹。

### 3.4.3 例子：贝尔态的约化密度矩阵

考虑 Bell 态 $|\Phi^+\rangle_{AB} = \frac{1}{\sqrt{2}}(|00\rangle_{AB} + |11\rangle_{AB})$。

整个系统的密度矩阵：

$$
\rho_{AB} = |\Phi^+\rangle\langle\Phi^+|_{AB} = \frac{1}{2}\begin{pmatrix}
1 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
1 & 0 & 0 & 1
\end{pmatrix}
$$

对 $B$ 求部分迹，得到 $A$ 的约化密度矩阵：

$$
\rho_A = \text{Tr}_B(\rho_{AB}) = \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

同理，$\rho_B = \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$。

**关键洞察**：虽然整个系统处于纯态（$\text{Tr}(\rho_{AB}^2) = 1$），但每个子系统都处于最大混态（$\text{Tr}(\rho_A^2) = 1/2$）。这正是纠缠的特征——子系统的信息隐藏在关联中。

**例 3.24** 对于可分离态 $|\Psi\rangle_{AB} = |+\rangle_A \otimes |+\rangle_B$：

$$
\rho_A = |+\rangle\langle +|_A
$$

子系统 $A$ 处于纯态——没有纠缠。

**例 3.25** 对于混态 $\rho_{AB} = \frac{1}{2}(|00\rangle\langle 00| + |11\rangle\langle 11|)$（经典关联，无纠缠）：

$$
\rho_A = \frac{1}{2}(|0\rangle\langle 0| + |1\rangle\langle 1|) = \frac{I}{2}
$$

虽然 $\rho_A$ 和 Bell 态的情况相同，但全局态的纠缠性质完全不同。

### 3.4.4 纠缠与子系统的混合性

**施密特分解**：任意两体纯态 $|\Psi\rangle_{AB}$ 可以写为：

$$
|\Psi\rangle_{AB} = \sum_i \lambda_i |i\rangle_A |i\rangle_B
$$

其中 $\lambda_i \geq 0$，$\sum_i \lambda_i^2 = 1$，$\{|i\rangle_A\}$ 和 $\{|i\rangle_B\}$ 分别是 $A$ 和 $B$ 的正交基。

此时约化密度矩阵为：

$$
\rho_A = \sum_i \lambda_i^2 |i\rangle\langle i|_A, \quad \rho_B = \sum_i \lambda_i^2 |i\rangle\langle i|_B
$$

- 若 $\lambda_1 = 1$ 且其他 $\lambda_i = 0$：可分离态，$\rho_A$ 和 $\rho_B$ 都是纯态。
- 若有多个非零 $\lambda_i$：纠缠态，$\rho_A$ 和 $\rho_B$ 都是混态。

**定理**：对于两体纯态，$\rho_A$ 和 $\rho_B$ 有相同的非零本征值（$\lambda_i^2$）。因此 $\text{Tr}(\rho_A^2) = \text{Tr}(\rho_B^2)$。

### 3.4.5 经典关联与量子关联

密度矩阵可以区分经典关联和量子关联（纠缠）：

- **可分离态**：$\rho_{AB} = \sum_i p_i \rho_A^{(i)} \otimes \rho_B^{(i)}$（经典关联或无关）
- **纠缠态**：不能写成上述形式的态

**关键区别**：在 Bell 态 $|\Phi^+\rangle\langle\Phi^+|$ 中，子系统 $A$ 和 $B$ 的测量结果存在量子关联——在 $X$ 基测量时，两者正相关；在 $Z$ 基测量时，两者也正相关。这种"超越基选择的关联"在经典关联中不可能存在。

> **关键点**：两个混态子系统可以既来自一个纠缠纯态（如 Bell 态），也来自一个经典混合态。仅看 $\rho_A$ 和 $\rho_B$ **无法区分**这两种情况——你需要知道它们的联合状态。这体现了关联信息的不可约性。

### 3.4.6 部分求迹的物理意义

部分求迹对应这样一个物理过程：我们只能访问子系统 $A$，对 $B$ 进行的所有可能测量结果被"平均掉"。

$\rho_A$ 包含了所有只对 $A$ 进行的测量的统计预测——不多也不少。对于任何只作用在 $A$ 上的算符 $O_A$：

$$
\langle O_A \rangle = \text{Tr}_{AB}(\rho_{AB} (O_A \otimes I_B)) = \text{Tr}_A(\rho_A O_A)
$$

---

## 3.5 量子熵

### 3.5.1 冯·诺依曼熵的定义

经典信息论中，Shannon 熵 $H(X) = -\sum_i p_i \log p_i$ 度量一个随机变量的不确定性。

量子信息论中，**冯·诺依曼熵（von Neumann entropy）** 是密度矩阵 $\rho$ 的不确定性度量：

$$
S(\rho) = -\text{Tr}(\rho \log \rho)
$$

如果 $\rho$ 有本征值 $\{\lambda_i\}$（$0 \leq \lambda_i \leq 1$，$\sum \lambda_i = 1$），则：

$$
S(\rho) = -\sum_i \lambda_i \log \lambda_i
$$

**约定**：$0 \log 0 = 0$，对数底取 2 时熵的单位为比特（qubit）。

**例 3.26** 纯态 $\rho = |0\rangle\langle 0|$：

本征值 $\{1, 0\}$，$S(\rho) = -1\log 1 - 0\log 0 = 0$

纯态的熵为零——我们拥有全部信息。

**例 3.27** 单比特最大混态 $\rho = I/2$：

本征值 $\{1/2, 1/2\}$，$S(\rho) = -\frac{1}{2}\log\frac{1}{2} - \frac{1}{2}\log\frac{1}{2} = 1$（$\log$ 底为 2）

**例 3.28** $d$ 维最大混态 $\rho = I/d$：$S(\rho) = \log d$

> **注意**：冯·诺依曼熵与 Shannon 熵的关键区别——Shannon 熵来自经典概率分布，冯·诺依曼熵来自密度矩阵的**本征值谱**，而密度矩阵中的非对角元（相干性）会影响本征值。

### 3.5.2 冯·诺依曼熵的性质

1. **非负性**：$S(\rho) \geq 0$，等号成立当且仅当 $\rho$ 是纯态。
2. **上界**：对于 $d$ 维系统，$S(\rho) \leq \log d$，等号成立当且仅当 $\rho = I/d$。
3. **幺正不变性**：$S(U\rho U^\dagger) = S(\rho)$。
4. **凹性**：$S(\sum_i p_i \rho_i) \geq \sum_i p_i S(\rho_i)$。
5. **次可加性**：$S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)$。
6. **强次可加性**：$S(\rho_{ABC}) + S(\rho_B) \leq S(\rho_{AB}) + S(\rho_{BC})$。

**例 3.29** 对于 Bell 态 $|\Phi^+\rangle\langle\Phi^+|$：

$S(\rho_{AB}) = 0$（整体是纯态）

$S(\rho_A) = S(\rho_B) = 1$（每个子系统是最大混态）

这里 $S(\rho_{AB}) < S(\rho_A) + S(\rho_B)$，次可加性严格成立。

### 3.5.3 线性熵

计算冯·诺依曼熵需要对数，有时不便。**线性熵（linear entropy）** 是其简单近似：

$$
S_L(\rho) = 1 - \text{Tr}(\rho^2)
$$

- 纯态：$S_L = 0$
- 最大混态（$d$ 维）：$S_L = 1 - 1/d$

线性熵与 $\text{Tr}(\rho^2)$ 一一对应，计算更方便。

**例 3.30** 比较冯·诺依曼熵和线性熵：

| 态 | $\text{Tr}(\rho^2)$ | $S(\rho)$（底 2） | $S_L(\rho)$ |
|------|---------|------|------|
| 纯态 | 1 | 0 | 0 |
| $I/2$ | 1/2 | 1 | 1/2 |
| $I/3$ | 1/3 | $\log 3 \approx 1.585$ | 2/3 |
| $I/d$ | $1/d$ | $\log d$ | $1 - 1/d$ |

### 3.5.4 熵与纠缠——纠缠熵

对于一个两体纯态 $|\Psi\rangle_{AB}$，**纠缠熵（entanglement entropy）** 定义为子系统约化密度矩阵的冯·诺依曼熵：

$$
E(|\Psi\rangle_{AB}) = S(\rho_A) = S(\rho_B)
$$

纠缠熵度量了子系统之间的纠缠程度：

- 可分离态（无纠缠）：$E = 0$
- 最大纠缠态：$E = \log(\min(d_A, d_B))$

**例 3.31** Bell 态的纠缠熵：$S(\rho_A) = 1$（$\log 2$，底为 2）——这是两比特系统的最大纠缠。

**例 3.32** $W$ 态 $|W\rangle = \frac{1}{\sqrt{3}}(|001\rangle + |010\rangle + |100\rangle)$：

对其中一个比特求部分迹，约化密度矩阵为 $\frac{2}{3}|0\rangle\langle 0| + \frac{1}{3}|1\rangle\langle 1|$（假设比特可区分），纠缠熵约为 $-\frac{2}{3}\log\frac{2}{3} - \frac{1}{3}\log\frac{1}{3}  \approx 0.918$。

**例 3.33** GHZ 态 $|GHZ\rangle = \frac{1}{\sqrt{2}}(|000\rangle + |111\rangle)$：

任意一个比特的约化密度矩阵为 $I/2$，纠缠熵为 1。对于三比特 GHZ 态，每对子系统的纠缠都是最大的。

> **重要关系**：对于纯态，纠缠熵完全由约化密度矩阵的谱决定。施密特系数 $\{\lambda_i\}$ 给出了 $\rho_A$ 的本征值 $\{\lambda_i^2\}$，纠缠熵为 $S(\rho_A) = -\sum_i \lambda_i^2 \log \lambda_i^2$。

### 3.5.5 熵与纯度的对比

| 度量 | 公式 | 纯态取值 | 最大混态取值 |
|------|------|---------|------------|
| 纯度 | $\text{Tr}(\rho^2)$ | 1 | $1/d$ |
| 冯·诺依曼熵 | $-\text{Tr}(\rho\log\rho)$ | 0 | $\log d$ |
| 线性熵 | $1 - \text{Tr}(\rho^2)$ | 0 | $1 - 1/d$ |

它们本质上是等价的信息——都反映态是"有序"还是"混乱"。纯度越大（接近 1），熵越小（接近 0）。对不同的应用可以选择更方便的度量。

---

## 3.6 量子态的距离度量

如何判断两个量子态是否相近？在量子信息中，有两个重要的距离度量。

### 3.6.1 保真度

**定义 3.4（保真度）** 两个密度矩阵 $\rho$ 和 $\sigma$ 之间的**保真度（fidelity）** 定义为：

$$
F(\rho, \sigma) = \text{Tr}\left(\sqrt{\sqrt{\rho}\,\sigma\sqrt{\rho}}\right)
$$

保真度的取值范围为 $0 \leq F(\rho, \sigma) \leq 1$。

- $F(\rho, \sigma) = 1$：$\rho = \sigma$（相同态）
- $F(\rho, \sigma) = 0$：$\rho$ 和 $\sigma$ 正交（完全可区分）

**特殊情况**：当一个态是纯态 $\rho = |\psi\rangle\langle\psi|$ 时：

$$
F(|\psi\rangle\langle\psi|, \sigma) = \sqrt{\langle\psi|\sigma|\psi\rangle}
$$

当两个态都是纯态 $\rho = |\psi\rangle\langle\psi|$，$\sigma = |\phi\rangle\langle\phi|$ 时：

$$
F(|\psi\rangle\langle\psi|, |\phi\rangle\langle\phi|) = |\langle\psi|\phi\rangle|
$$

**例 3.34** 计算 $F(|0\rangle\langle 0|, |1\rangle\langle 1|)$：

$F = |\langle 0|1\rangle| = 0$——两个态正交，完全可区分。

**例 3.35** 计算 $F(|0\rangle\langle 0|, |+\rangle\langle +|)$：

$F = |\langle 0|+\rangle| = \frac{1}{\sqrt{2}} \approx 0.707$

**例 3.36** 计算 $F(|0\rangle\langle 0|, I/2)$：

$F = \sqrt{\langle 0|(I/2)|0\rangle} = \sqrt{1/2} \approx 0.707$

> **直观理解**：保真度是"两个态有多像"的量子推广。对于纯态，它简化为内积的模。

### 3.6.2 Uhlmann 定理

**定理 3.1（Uhlmann 定理）** 对于两个密度矩阵 $\rho$ 和 $\sigma$：

$$
F(\rho, \sigma) = \max_{|\psi_\rho\rangle, |\psi_\sigma\rangle} |\langle\psi_\rho|\psi_\sigma\rangle|
$$

其中 $|\psi_\rho\rangle$ 和 $|\psi_\sigma\rangle$ 分别是 $\rho$ 和 $\sigma$ 的**纯化（purification）**——即满足 $\text{Tr}_B(|\psi_\rho\rangle\langle\psi_\rho|) = \rho$ 的纯态，最大值在所有可能的纯化上取。

**Uhlmann 定理的重要性**：
1. 将混态的保真度归结为纯态内积的最大可能值——几何意义清晰。
2. 保真度是"两个态最相似时它们的纯化间内积"。
3. 用于证明保真度的许多重要性质（如强凹性、单调性）。

**例 3.37** 对于 $\rho = I/2$（单比特），其最简单的纯化是 Bell 态 $|\Phi^+\rangle_{AB}$。$|\Phi^+\rangle$ 对 $B$ 求迹给出 $I/2$。

> **Uhlmann 定理的关键推论**：保真度在量子操作下不增——$F(\mathcal{E}(\rho), \mathcal{E}(\sigma)) \geq F(\rho, \sigma)$。这使保真度成为量子信息处理中衡量"信息损失"的重要工具。

### 3.6.3 迹距离

**定义 3.5（迹距离）** 两个密度矩阵 $\rho$ 和 $\sigma$ 之间的**迹距离（trace distance）** 定义为：

$$
D(\rho, \sigma) = \frac{1}{2}\text{Tr}|\rho - \sigma|
$$

其中 $|A| = \sqrt{A^\dagger A}$。迹距离度量了两个态在**最优测量**下的可区分程度。

取值范围：$0 \leq D(\rho, \sigma) \leq 1$。
- $D(\rho, \sigma) = 0$：$\rho = \sigma$
- $D(\rho, \sigma) = 1$：$\rho$ 和 $\sigma$ 完全可区分

**物理意义**：对于任意 POVM 测量 $\{E_m\}$，两个态产生的统计分布之间的总变差距离最大为 $D(\rho, \sigma)$：

$$
\max_{\{E_m\}} \frac{1}{2}\sum_m |\text{Tr}(\rho E_m) - \text{Tr}(\sigma E_m)| = D(\rho, \sigma)
$$

**例 3.38** 两个纯态 $\rho = |0\rangle\langle 0|$，$\sigma = |1\rangle\langle 1|$：

$$
|\rho - \sigma| = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} - \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

$$
D(\rho, \sigma) = \frac{1}{2}\text{Tr}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = 1
$$

完全可区分。

**例 3.39** $\rho = |0\rangle\langle 0|$ 和 $\sigma = |+\rangle\langle +|$：

$$
\rho - \sigma = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} - \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1 & -1 \\ -1 & -1 \end{pmatrix}
$$

本征值为 $\pm 1/\sqrt{2}$，所以 $|\rho - \sigma|$ 的本征值为 $\pm 1/\sqrt{2}$取绝对值的和：

$D(\rho, \sigma) = \frac{1}{2} \cdot \frac{2}{\sqrt{2}} = \frac{1}{\sqrt{2}} \approx 0.707$

**例 3.40** $\rho = |0\rangle\langle 0|$ 和 $\sigma = I/2$：

$$
\rho - \sigma = \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

$|\rho - \sigma| = \frac{1}{2}I$，$D(\rho, \sigma) = \frac{1}{2}$

> **直观理解**：迹距离是"两个态能在多大程度上区分"的度量。如果你可以做任意测量，$D = 0.5$ 意味着你可以以 75% 的正确率区分两个态（比随机猜稍好）。

### 3.6.4 保真度与迹距离的关系

保真度和迹距离是量子态距离的两种不同度量。它们之间存在以下关系：

$$
1 - F(\rho, \sigma) \leq D(\rho, \sigma) \leq \sqrt{1 - F(\rho, \sigma)^2}
$$

对于纯态，上界取等号：$D(|\psi\rangle, |\phi\rangle) = \sqrt{1 - |\langle\psi|\phi\rangle|^2} = \sqrt{1 - F^2}$。

**例 3.41** $\rho = |0\rangle\langle 0|$，$\sigma = |+\rangle\langle +|$：

$F = 1/\sqrt{2}$，$\sqrt{1 - F^2} = \sqrt{1 - 1/2} = 1/\sqrt{2} \approx 0.707$

$D = 1/\sqrt{2} \approx 0.707$

上界取等号（两个纯态）。

**例 3.42** $\rho = |0\rangle\langle 0|$，$\sigma = I/2$：

$F = 1/\sqrt{2} \approx 0.707$，$\sqrt{1 - F^2} = 0.707$

$D = 0.5$

这里 $D < \sqrt{1 - F^2}$，严格不等式。

### 3.6.5 保真度与迹距离的物理意义

| 度量 | 含义 | 范围 | 纯态-纯态 | 纯态-最大混态 |
|------|------|------|-----------|-------------|
| 保真度 $F$ | 两个态有多"像" | $[0, 1]$ | $|\langle\psi|\phi\rangle|$ | $1/\sqrt{2}$ |
| 迹距离 $D$ | 最优区分概率 | $[0, 1]$ | $\sqrt{1 - |\langle\psi|\phi\rangle|^2}$ | $1/2$ |

**例 3.43（具体实验场景）** 考虑一个量子存储器。开始时存储 $|0\rangle$（$\rho = |0\rangle\langle 0|$）。经过一段时间后，由于退相干，它变成 $\sigma = (1-p)|0\rangle\langle 0| + p|1\rangle\langle 1|$。求保真度和迹距离作为 $p$ 的函数：

$F = \sqrt{\langle 0|\sigma|0\rangle} = \sqrt{1-p}$

$D = \frac{1}{2}\text{Tr}|(1-p)|0\rangle\langle 0| + p|1\rangle\langle 1| - |0\rangle\langle 0|| = \frac{1}{2}\text{Tr}|-p|0\rangle\langle 0| + p|1\rangle\langle 1|| = p$

当 $p = 0.5$ 时，$F = 1/\sqrt{2} \approx 0.707$，$D = 0.5$。

> **保真度是量子态距离度量，用于比较两个态和量子态区分。**

---

## 3.7 本章习题

### 基础知识题

1. 判断以下矩阵是否为合法的单比特密度矩阵：

   (a) $\begin{pmatrix} 1/2 & 0 \\ 0 & 1/2 \end{pmatrix}$

   (b) $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$

   (c) $\begin{pmatrix} 1/3 & 1/2 \\ 1/2 & 2/3 \end{pmatrix}$

   (d) $\begin{pmatrix} 1/2 & 1/2 \\ 1/2 & 1/2 \end{pmatrix}$

2. 对于 $\rho = \frac{3}{4}|0\rangle\langle 0| + \frac{1}{4}|1\rangle\langle 1|$，计算 $\text{Tr}(\rho^2)$，判断它是纯态还是混态。

3. 证明：对于任何密度矩阵 $\rho$，$0 \leq \text{Tr}(\rho^2) \leq 1$，且等号只在纯态时取 1。

4. 计算 $\rho = \frac{1}{2}(|0\rangle\langle 0| + |1\rangle\langle 1|)$ 在 $X$ 基下的测量概率分布。

5. 写出 $|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$ 的密度矩阵。

### 演化与约化密度矩阵

1. 初始态 $\rho(0) = |+\rangle\langle +|$，在 $H = \omega Z$ 下演化。求 $\rho(t)$ 和 $\text{Tr}(\rho(t)^2)$。

2. 对于 Bell 态 $|\Phi^-\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle)$，计算 $\rho_A$ 和 $\rho_B$，并求 $\text{Tr}(\rho_A^2)$。

3. 三个比特的 GHZ 态 $|GHZ\rangle = \frac{1}{\sqrt{2}}(|000\rangle + |111\rangle)$。求第一个比特的约化密度矩阵和纯度。

4. 对于 $\rho_{AB} = \frac{1}{2}(|00\rangle\langle 00| + |11\rangle\langle 11|)$（经典关联），计算 $\rho_A$ 并与 Bell 态的结果比较。

5. 验证：对于两体纯态 $|\Psi\rangle_{AB}$，总有不变量 $S(\rho_A) = S(\rho_B)$。

### 熵与距离

1. 计算 $\rho = \frac{2}{3}|0\rangle\langle 0| + \frac{1}{3}|1\rangle\langle 1|$ 的冯·诺依曼熵和线性熵。

2. 两个 qutrit 的 Bell 态 $|\Psi\rangle = \frac{1}{\sqrt{3}}(|00\rangle + |11\rangle + |22\rangle)$ 求纠缠熵。

3. 计算 $F(|0\rangle\langle 0|, |-\rangle\langle -|)$ 和 $D(|0\rangle\langle 0|, |-\rangle\langle -|)$，验证纯态关系 $D = \sqrt{1-F^2}$。

4. 对于 $\rho = \frac{1}{2}|0\rangle\langle 0| + \frac{1}{2}|1\rangle\langle 1|$ 和 $\sigma = |0\rangle\langle 0|$，计算 $F(\rho, \sigma)$ 和 $D(\rho, \sigma)$。

5. 证明：对于任意 $\rho$ 和 $\sigma$，$0 \leq F(\rho, \sigma) \leq 1$。

---

### 知识点索引

| 中文 | 英文 | 章节 |
|------|------|------|
| 保真度 | Fidelity | 3.6.1 |
| 布洛赫球 | Bloch sphere | 3.2.3 |
| 纯态 | Pure state | 3.1.2 |
| 纯化 | Purification | 3.6.2 |
| 迹距离 | Trace distance | 3.6.3 |
| 纠缠熵 | Entanglement entropy | 3.5.4 |
| 冯·诺依曼熵 | von Neumann entropy | 3.5.1 |
| 混态 | Mixed state | 3.1.4 |
| Lindblad 方程 | Lindblad equation | 3.3.2 |
| 密度矩阵 | Density matrix | 3.1 |
| 约化密度矩阵 | Reduced density matrix | 3.4 |
| 部分求迹 | Partial trace | 3.4.2 |
| 保真度与迹距离关系 | Fidelity-trace distance relation | 3.6.4 |
| 最大混态 | Maximally mixed state | 3.2.2 |
| $\text{Tr}(\rho^2)$ 判据 | Purity criterion | 3.2.1 |

---

> **本章小结**
>
> 1. **密度矩阵** $\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$ 统一了量子概率（叠加）和经典概率（混合），可以描述信息不完备的量子系统。
> 2. **纯态 vs 混态**：纯态的 $\text{Tr}(\rho^2) = 1$，混态的 $\text{Tr}(\rho^2) < 1$。布洛赫球面上纯态在表面，混态在内部。
> 3. **幺正演化** $\rho \to U\rho U^\dagger$ 保持纯度；冯·诺依曼方程 $i\hbar\dot{\rho} = [H, \rho]$ 是密度矩阵的运动方程。
> 4. **约化密度矩阵** $\rho_A = \text{Tr}_B(\rho_{AB})$ 通过对部分系统求迹得到，是描述子系统状态的正确工具。
> 5. **纠缠与熵**：对于两体纯态，纠缠熵 $S(\rho_A) = S(\rho_B)$ 是纠缠的度量。Bell 态的纠缠熵为 $\log 2 = 1$（底 2）。
> 6. **保真度** $F(\rho, \sigma)$ 和**迹距离** $D(\rho, \sigma)$ 是量子态距离的两重要度量，满足 $1-F \leq D \leq \sqrt{1-F^2}$。
>
> 密度矩阵是连接"量子"和"经典"的桥梁。它的概念贯穿量子计算与量子信息的每一个角落——从量子噪声到量子纠错，从量子信道到量子密码学。掌握了密度矩阵，你就拥有了理解量子世界的第二语言。
