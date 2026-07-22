# 第2章 多量子比特与纠缠

> **本章导读**
>
> 第1章我们学习了单个量子比特的表示和单比特门操作。但量子计算的真正威力——那些让经典计算机望尘莫及的能力——来自**多量子比特系统**中独有的**量子纠缠（entanglement）** 现象。
>
> 本章从数学上建立多量子比特态的描述框架：张量积、计算基矢、可分态与纠缠态。然后深入最重要的两比特纠缠态——**贝尔态（Bell states）**，它是量子通信和量子密码学的基石。接着我们扩展到三体及更多体的纠缠态（GHZ态、W态），并学习**施密特分解**这个分析纠缠结构的强大工具。
>
> 如何量化"一个态有多纠缠"？2.4 节介绍几种重要的**纠缠度量**：PPT判据、负度、并发度、纠缠见证。2.5 节回到量子门层面，学习各种**两比特门**（CNOT、CZ、SWAP、iSWAP等）及其矩阵表示、电路符号和物理实现思路。最后，2.6 节展示纠缠在量子信息处理中最著名的应用：密集编码、隐形传态、SWAP网络和纠缠蒸馏。
>
> **学完本章，你将能够：**
> - 用张量积构造多量子比特态，写出 $n$ 比特计算基矢
> - 区分可分态与纠缠态
> - 写出四个贝尔态并画出生成电路
> - 理解贝尔不等式违反的物理意义
> - 描述 GHZ 态和 W 态的性质
> - 对两比特态做施密特分解并读出纠缠秩
> - 用 PPT 判据和并发度判断两比特态是否纠缠
> - 写出 CNOT、CZ、SWAP、iSWAP 的矩阵和电路符号
> - 理解密集编码和隐形传态协议
> - 理解纠缠蒸馏的基本思想
>
> **先修知识**：第1章（量子比特、单比特门）；模块一（线性代数、张量积、Dirac符号）

---

## 2.1 多比特态

### 2.1.1 张量积态

回忆模块一中我们学习的**张量积（tensor product）**。两个量子系统复合时，整个系统的 Hilbert 空间是子系统空间的张量积：

$$
\mathcal{H}_{AB} = \mathcal{H}_A \otimes \mathcal{H}_B
$$

如果 $A$ 是单量子比特（$\mathcal{H}_A \cong \mathbb{C}^2$），$B$ 也是单量子比特（$\mathcal{H}_B \cong \mathbb{C}^2$），那么复合系统的空间是 $\mathbb{C}^2 \otimes \mathbb{C}^2 \cong \mathbb{C}^4$。

> **直觉**：两个经典比特可以取 4 种组合（00, 01, 10, 11）。两个量子比特的态空间是 4 维复向量空间——它包含了这 4 种基态的任意复线性组合。

**定义 2.1（张量积态）** 如果两个量子比特分别处于态 $|\psi\rangle_A \in \mathcal{H}_A$ 和 $|\phi\rangle_B \in \mathcal{H}_B$，则复合系统的态是张量积：

$$
|\psi\rangle_{AB} = |\psi\rangle_A \otimes |\phi\rangle_B
$$

在 Dirac 符号中，通常简写为 $|\psi\rangle_A |\phi\rangle_B$ 或 $|\psi\phi\rangle_{AB}$。

**例 2.1** 设 $|\psi\rangle_A = \alpha|0\rangle_A + \beta|1\rangle_A$，$|\phi\rangle_B = \gamma|0\rangle_B + \delta|1\rangle_B$。则：

$$
\begin{aligned}
|\psi\rangle_A \otimes |\phi\rangle_B &= (\alpha|0\rangle_A + \beta|1\rangle_A) \otimes (\gamma|0\rangle_B + \delta|1\rangle_B) \\
&= \alpha\gamma|0\rangle_A|0\rangle_B + \alpha\delta|0\rangle_A|1\rangle_B + \beta\gamma|1\rangle_A|0\rangle_B + \beta\delta|1\rangle_A|1\rangle_B
\end{aligned}
$$

注意展开后有 4 个系数，与 $\mathbb{C}^4$ 维数一致。

### 2.1.2 多比特计算基矢

对于 $n$ 个量子比特，计算基矢是每个量子比特取 $|0\rangle$ 或 $|1\rangle$ 的所有可能组合：

$$
\{|b_1 b_2 \cdots b_n\rangle \;|\; b_i \in \{0,1\}\}
$$

共有 $2^n$ 个基矢。它们张成 $2^n$ 维 Hilbert 空间 $\mathcal{H} = (\mathbb{C}^2)^{\otimes n}$。

**例 2.2** 两比特系统（$n=2$）的计算基矢：

$$
|00\rangle,\quad |01\rangle,\quad |10\rangle,\quad |11\rangle
$$

在向量表示中（按字典序）：

$$
|00\rangle = \begin{pmatrix}1\\0\\0\\0\end{pmatrix},\;
|01\rangle = \begin{pmatrix}0\\1\\0\\0\end{pmatrix},\;
|10\rangle = \begin{pmatrix}0\\0\\1\\0\end{pmatrix},\;
|11\rangle = \begin{pmatrix}0\\0\\0\\1\end{pmatrix}
$$

> **记法**：有时也使用十进制标记，将 $|b_1 b_2 \cdots b_n\rangle$ 写为 $|k\rangle$，其中 $k = b_1 b_2 \cdots b_n$ 是二进制数对应的十进制值。例如 $|3\rangle$ 就是 $|11\rangle$。

**例 2.3** 三比特系统（$n=3$）的计算基矢有 $2^3 = 8$ 个：

$$
|000\rangle, |001\rangle, |010\rangle, |011\rangle, |100\rangle, |101\rangle, |110\rangle, |111\rangle
$$

**任意多量子比特态**可以表示为计算基矢的线性组合：

$$
|\Psi\rangle = \sum_{i_1=0}^{1}\sum_{i_2=0}^{1}\cdots\sum_{i_n=0}^{1} c_{i_1 i_2 \cdots i_n} |i_1 i_2 \cdots i_n\rangle
$$

归一化条件：$\sum |c_{i_1\cdots i_n}|^2 = 1$。

**例 2.4** 一个两比特叠加态：

$$
|\Psi\rangle = \frac{1}{2}\big(|00\rangle + |01\rangle + |10\rangle + |11\rangle\big)
$$

归一化验证：$|1/2|^2 \times 4 = 1$。这个态实际上是 $\left(\frac{|0\rangle+|1\rangle}{\sqrt{2}}\right) \otimes \left(\frac{|0\rangle+|1\rangle}{\sqrt{2}}\right)$，是**可分态**（见下节）。

### 2.1.3 可分态定义

有些多量子比特态可以写成单个量子比特态的乘积形式，有些则不能。这个区分是量子信息理论中最核心的概念之一。

**定义 2.2（可分态）** 一个两比特态 $|\Psi\rangle_{AB} \in \mathcal{H}_A \otimes \mathcal{H}_B$ 称为**可分态（separable state）**（或**直积态（product state）**），如果它可以写成：

$$
|\Psi\rangle_{AB} = |\alpha\rangle_A \otimes |\beta\rangle_B
$$

其中 $|\alpha\rangle_A \in \mathcal{H}_A$，$|\beta\rangle_B \in \mathcal{H}_B$。

如果 $|\Psi\rangle_{AB}$ 不能表示为任何这样的张量积形式，则称为**纠缠态（entangled state）**。

**例 2.5** 判断以下态是否可分：

(a) $|\Phi\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |01\rangle)$

$$
|\Phi\rangle = |0\rangle \otimes \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |0\rangle|+\rangle
$$

✓ **可分**（$A$ 在 $|0\rangle$，$B$ 在 $|+\rangle$）。

(b) $|\Psi\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$

假设存在 $|\alpha\rangle = a_0|0\rangle + a_1|1\rangle$，$|\beta\rangle = b_0|0\rangle + b_1|1\rangle$ 使得 $|\Psi\rangle = |\alpha\rangle \otimes |\beta\rangle$。

展开：$a_0b_0|00\rangle + a_0b_1|01\rangle + a_1b_0|10\rangle + a_1b_1|11\rangle$

与 $\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ 比较：

$$
a_0b_0 = \frac{1}{\sqrt{2}},\quad a_0b_1 = 0,\quad a_1b_0 = 0,\quad a_1b_1 = \frac{1}{\sqrt{2}}
$$

从 $a_0b_1 = 0$ 知 $a_0=0$ 或 $b_1=0$。如果 $a_0=0$，则 $a_0b_0 = 0 \neq 1/\sqrt{2}$，矛盾。如果 $b_1=0$，则 $a_1b_1 = 0 \neq 1/\sqrt{2}$，矛盾。所以不存在这样的分解。

✗ **不可分 → 纠缠态**。这就是著名的**贝尔态**之一。

**可分态的几何图像**：在布洛赫球面上，两比特可分态中的每个量子比特都有自己独立的布洛赫向量。整体态完全由两个独立的布洛赫向量决定。

> **通俗理解**：如果两个量子比特处于可分态，你知道其中一个的状态，对另一个的状态没有任何影响——它们的信息是完全独立的。处于纠缠态的两个量子比特则像一个"连体婴"：对其中一个的测量结果会即时影响另一个。

### 2.1.4 纠缠态定义

**定义 2.3（纠缠态）** 一个纯态 $|\Psi\rangle_{AB}$ 是**纠缠的**，当且仅当它不是可分态。

对于**混合态**（密度算符描述），定义更微妙：

**定义 2.4（可分混合态）** 一个两比特密度算符 $\rho_{AB}$ 称为**可分的（separable）**，如果它可以写成凸组合：

$$
\rho_{AB} = \sum_k p_k \; \rho_A^{(k)} \otimes \rho_B^{(k)}
$$

其中 $p_k \geq 0$，$\sum_k p_k = 1$，$\rho_A^{(k)}$ 和 $\rho_B^{(k)}$ 分别是 $A$ 和 $B$ 上的密度算符。如果 $\rho_{AB}$ 不能写成这种形式，则称它为**纠缠的（entangled）**。

> **直觉**：可分混合态意味着"经典混合"——你只需要知道那个"概率 $p_k$"，就能说系统处于某个直积态 $\rho_A^{(k)} \otimes \rho_B^{(k)}$。纠缠态则存在**量子相关性**，没有经典概率模型可以解释。

**纠缠为什么重要？**

1. **非定域关联**：对 Alice 的量子比特做测量，会即时影响 Bob 的量子比特的统计性质——无论他们相隔多远。
2. **量子计算加速**：许多量子算法（如 Shor 算法、Grover 算法）都需要纠缠作为资源。
3. **量子通信基础**：纠缠是密集编码、隐形传态、量子密钥分发的核心资源。
4. **量子纠错**：纠缠是构建逻辑量子比特的必需成分。

**例 2.6** 以下态是否纠缠？

(a) $|\Psi\rangle = \frac{1}{2}(|00\rangle + |01\rangle + |10\rangle + |11\rangle)$

可分解为 $|+\rangle|+\rangle$ → **可分**。

(b) $|\Psi\rangle = \frac{1}{\sqrt{3}}(|00\rangle + |01\rangle + |10\rangle)$

尝试分解：假设 $|\alpha\rangle = a_0|0\rangle + a_1|1\rangle$，$|\beta\rangle = b_0|0\rangle + b_1|1\rangle$。

展开系数：$a_0b_0=1/\sqrt{3}$，$a_0b_1=1/\sqrt{3}$，$a_1b_0=1/\sqrt{3}$，$a_1b_1=0$。

由 $a_0b_1=1/\sqrt{3}$ 和 $a_0b_0=1/\sqrt{3}$ 得 $b_0=b_1$（如果 $a_0 \neq 0$）。那么 $a_1b_0=1/\sqrt{3}$ 和 $a_1b_1=0$ 无法同时成立（因为 $b_0 = b_1$）。如果 $a_0 = 0$，$a_0b_0 = 0$，矛盾。所以不可分。

✗ **纠缠**。

---

**小练习 2.1** 判断以下两比特态是否可分：

(a) $|\Psi_1\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$

(b) $|\Psi_2\rangle = \frac{1}{2}(|00\rangle + i|01\rangle - i|10\rangle + |11\rangle)$

**小练习 2.2** 三比特系统中，以下态是否可分（即是否可以写成三个单比特态的乘积）？

$$
|\Psi\rangle = \frac{1}{\sqrt{2}}(|000\rangle + |111\rangle)
$$

---

## 2.2 贝尔态

### 2.2.1 四个贝尔态

两比特系统中，有四个特殊的最大纠缠态，称为**贝尔态（Bell states）**：

$$
\begin{aligned}
|\Phi^+\rangle &= \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) \\
|\Phi^-\rangle &= \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle) \\
|\Psi^+\rangle &= \frac{1}{\sqrt{2}}(|01\rangle + |10\rangle) \\
|\Psi^-\rangle &= \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)
\end{aligned}
$$

**重要性质**：

1. **最大纠缠**：每个贝尔态都是最大纠缠态（在后续章节的纠缠度量意义下）。
2. **正交归一**：$\langle \Phi^+|\Phi^-\rangle = 0$，等等——四个态两两正交。
3. **构成一组正交基**：四个贝尔态张成 $\mathbb{C}^4$ 空间，称为**贝尔基（Bell basis）**。
4. **局部幺正等价**：通过单比特泡利门可以在四个贝尔态之间互相转换。

**贝尔态与泡利门的关系**：

$$
\begin{aligned}
|\Phi^-\rangle &= (I \otimes Z)|\Phi^+\rangle \\
|\Psi^+\rangle &= (I \otimes X)|\Phi^+\rangle \\
|\Psi^-\rangle &= (I \otimes XZ)|\Phi^+\rangle = (I \otimes iY)|\Phi^+\rangle
\end{aligned}
$$

**例 2.7** 验证 $|\Phi^-\rangle = (I \otimes Z)|\Phi^+\rangle$：

$$
(I \otimes Z) \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = \frac{1}{\sqrt{2}}(|0\rangle Z|0\rangle + |1\rangle Z|1\rangle) = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle) = |\Phi^-\rangle
$$

因为 $Z|0\rangle = |0\rangle$，$Z|1\rangle = -|1\rangle$。

**例 2.8** 验证四个贝尔态的正交性：

$$
\begin{aligned}
\langle \Phi^+|\Phi^-\rangle &= \frac{1}{2}(\langle 00| + \langle 11|)(|00\rangle - |11\rangle) \\
&= \frac{1}{2}(\langle 00|00\rangle - \langle 00|11\rangle + \langle 11|00\rangle - \langle 11|11\rangle) \\
&= \frac{1}{2}(1 - 0 + 0 - 1) = 0
\end{aligned}
$$

**物理意义**：$|\Psi^-\rangle$（单态，singlet）是旋转不变的——它在任何方向测量都呈现反关联。$|\Phi^+\rangle$（三重态之一）在同方向测量呈现正关联。

### 2.2.2 生成电路

如何制备贝尔态？标准电路如下：

```
|q0⟩ ──[H]──╳──
            │
|q1⟩ ───────╳──
```

其中先对第一个量子比特做 Hadamard 门，然后做 CNOT 门（控制比特为 $q_0$，目标比特为 $q_1$）。

**逐步演算**：

初始态：$|00\rangle$

步骤 1：$H$ 作用在 $q_0$

$$
|00\rangle \xrightarrow{H_1} \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes |0\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle)
$$

步骤 2：CNOT（$q_0$ 控制，$q_1$ 目标）

CNOT 的作用：当控制比特为 $|0\rangle$ 时目标不变，当控制比特为 $|1\rangle$ 时目标翻转。

$$
\frac{1}{\sqrt{2}}(|00\rangle + |10\rangle) \xrightarrow{\text{CNOT}} \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = |\Phi^+\rangle
$$

**四个贝尔态的生成**：

通过改变输入态或加入额外门，可以生成不同的贝尔态：

| 输入态 | 电路 | 输出 |
| :---: | :---: | :---: |
| \( |00\rangle \) | $H$ + CNOT | \( |\Phi^+\rangle \) |
| \( |01\rangle \) | $H$ + CNOT | \( |\Psi^+\rangle \) |
| \( |10\rangle \) | $H$ + CNOT | \( |\Phi^-\rangle \) |
| \( |11\rangle \) | $H$ + CNOT | \( |\Psi^-\rangle \) |

**验证**：输入 $|01\rangle$：

$$
|01\rangle \xrightarrow{H_1} \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes |1\rangle = \frac{1}{\sqrt{2}}(|01\rangle + |11\rangle) \xrightarrow{\text{CNOT}} \frac{1}{\sqrt{2}}(|01\rangle + |10\rangle) = |\Psi^+\rangle
$$

**另一种常见写法**：先 CNOT 再 Hadamard 也可以，但顺序不同（得到的态可能略有差异）。

> **注意**：生成贝尔态需要两比特门（CNOT）。没有两比特门，不可能从可分态产生纠缠——这正是两比特门的核心作用。

### 2.2.3 贝尔不等式违反

贝尔不等式（Bell's inequality）是量子力学中最深刻的发现之一。它提供了一个实验判据，可以区分**量子力学**和**局域隐变量理论（local hidden variable theories）**。

#### CHSH 不等式

最常用的形式是 CHSH 不等式（Clauser-Horne-Shimony-Holt）：

考虑 Alice 和 Bob 各自测量他们的量子比特。Alice 可以选择测量 $A$ 或 $A'$（取值为 $\pm 1$），Bob 可以选择测量 $B$ 或 $B'$（取值为 $\pm 1$）。定义关联量：

$$
S = \langle AB \rangle + \langle AB' \rangle + \langle A'B \rangle - \langle A'B' \rangle
$$

**局域隐变量理论**的预测是：

$$
|S| \leq 2
$$

这就是 **CHSH 不等式**。

**量子力学的预测**：对于贝尔态 $|\Phi^+\rangle$，选择测量方向：

$$
\begin{aligned}
A &= Z, \quad A' = X \\
B &= \frac{Z+X}{\sqrt{2}}, \quad B' = \frac{Z-X}{\sqrt{2}}
\end{aligned}
$$

可以计算：

$$
\langle \Phi^+| Z \otimes \frac{Z+X}{\sqrt{2}} |\Phi^+\rangle = \frac{1}{\sqrt{2}}
$$

类似地，所有四项贡献相同（最后一项负号来自减号）：

$$
S = \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} - \left(-\frac{1}{\sqrt{2}}\right) = 2\sqrt{2} \approx 2.828
$$

$$
2\sqrt{2} > 2 \quad \Rightarrow \quad \text{违反贝尔不等式！}
$$

这个结果是**量子力学的特有预测**，已被无数实验证实（Aspect 1982, Zeilinger 1997 等）。

**实验验证的简化示意图**：

```
Alice                    Bob
┌───┐                    ┌───┐
│ A │←── 纠缠光子 ──→    │ B │
└───┘                    └───┘
   ↑                        ↑
随机选择测量方向        随机选择测量方向
A 或 A'                  B 或 B'
```

**关键结论**：

1. 量子力学预测 $S = 2\sqrt{2}$，违反经典不等式 $|S| \leq 2$。
2. 实验证实了 $S$ 确实可以达到约 $2.828$（受实验不完美影响略低）。
3. 这意味着：任何**局域隐变量理论**（认为量子随机性背后有隐藏的确定原因）都无法解释量子力学的预测。
4. **量子非定域性（quantum nonlocality）**：纠缠态的相关性不能通过任何局域因果模型解释。

> **常见误解**：贝尔不等式违反**不**意味着超光速通信。Alice 无法控制自己的测量结果——结果总是随机的——所以她无法通过测量向 Bob 发送信息。纠缠允许"非定域关联"，但不允许"非定域信号传输"。

### 2.2.4 量子非定域性

**量子非定域性**是指：纠缠粒子之间的关联不能通过任何局域隐变量理论来解释。这与爱因斯坦的"定域实在论"（local realism）相矛盾。

**EPR 佯谬**（Einstein-Podolsky-Rosen, 1935）：

爱因斯坦、波多尔斯基和罗森提出了一个思想实验，质疑量子力学的完备性。他们的论证基于两个假设：

1. **定域性（locality）**：物理作用不能超光速传播。
2. **实在性（realism）**：物理量的值在测量之前本来就存在。

EPR 论证说：如果量子力学是完备的，那么两个分离的纠缠粒子之间就存在"鬼魅般的超距作用"（spooky action at a distance）——这显然荒谬。所以量子力学一定是不完备的。

**玻尔的反驳**：量子力学本身就是完备的——在测量之前，"实在"并不存在确定的值。纠缠粒子的关联是量子态的固有性质，不是由隐变量决定的。

**实验裁决**：贝尔不等式（1964）提供了一个实验判据。从 1970 年代到现在的所有实验（包括无漏洞实验）都支持量子力学的预测，违反了贝尔不等式。**量子非定域性是真的**。

**对于量子计算的启示**：

1. 纠缠不是"模拟经典关联"——它是一种全新的资源。
2. 量子计算之所以比经典计算强大，根本原因之一就是纠缠（以及叠加）。
3. 但纠缠本身不足以实现量子加速——还需要干涉和测量。

---

**小练习 2.3** 从输入态 $|10\rangle$ 开始，经过 H + CNOT 电路，验证输出是否为 $|\Phi^-\rangle$。

**小练习 2.4** 如果 Alice 和 Bob 分别测量贝尔态 $|\Psi^-\rangle$，Alice 在 $Z$ 基测量得到 $|0\rangle$，Bob 在 $Z$ 基测量一定会得到什么结果？如果 Alice 在 $X$ 基测量得到 $|+\rangle$，Bob 在 $X$ 基测量呢？

---

## 2.3 多体纠缠态

### 2.3.1 GHZ 态

**GHZ 态**（Greenberger-Horne-Zeilinger state）是三量子比特系统中最著名的纠缠态之一：

$$
|\text{GHZ}\rangle = \frac{1}{\sqrt{2}}(|000\rangle + |111\rangle)
$$

**性质**：

1. **最大纠缠**：GHZ 态是三体最大纠缠态之一。
2. **对称性**：任意置换量子比特，态的形式不变。
3. **测量特性**：如果在 $Z$ 基下测量所有三个量子比特，结果要么全是 $|0\rangle$，要么全是 $|1\rangle$（各 50% 概率）。
4. **相关性**：对任意两个量子比特做 $Z$ 测量，结果完全正相关。

**GHZ 态的生成电路**：

```
|q0⟩ ──[H]──╳──────────────
            │
|q1⟩ ───────╳──╳───────────
               │
|q2⟩ ──────────╳───────────
```

电路演算：

$$
|000\rangle \xrightarrow{H_1} \frac{1}{\sqrt{2}}(|000\rangle + |100\rangle)
\xrightarrow{\text{CNOT}_{12}} \frac{1}{\sqrt{2}}(|000\rangle + |110\rangle)
\xrightarrow{\text{CNOT}_{13}} \frac{1}{\sqrt{2}}(|000\rangle + |111\rangle)
$$

**n 比特 GHZ 态**：

$$
|\text{GHZ}_n\rangle = \frac{1}{\sqrt{2}}(|0\rangle^{\otimes n} + |1\rangle^{\otimes n})
$$

**GHZ 态的非定域性**：GHZ 态可以用**三体贝尔不等式**来检验非定域性，且不需要统计平均——单次测量就可以揭示与局域实在论的矛盾。

**例 2.9** GHZ 态的纠缠特性：

对 $|\text{GHZ}\rangle = \frac{1}{\sqrt{2}}(|000\rangle + |111\rangle)$ 做 $X$ 基测量：

$$
\begin{aligned}
|\text{GHZ}\rangle &= \frac{1}{\sqrt{2}}\Big[ \frac{1}{\sqrt{2}}(|+\rangle + |-\rangle) \otimes \frac{1}{\sqrt{2}}(|+\rangle + |-\rangle) \otimes \frac{1}{\sqrt{2}}(|+\rangle + |-\rangle) \\
&\qquad + \frac{1}{\sqrt{2}}(|+\rangle - |-\rangle) \otimes \frac{1}{\sqrt{2}}(|+\rangle - |-\rangle) \otimes \frac{1}{\sqrt{2}}(|+\rangle - |-\rangle) \Big]
\end{aligned}
$$

展开后可以发现：只有奇数个 $|-\rangle$ 的项存在（因为 $|111\rangle$ 展开时每个 $|1\rangle = \frac{|+\rangle - |-\rangle}{\sqrt{2}}$ 贡献一个负号）。所以 $X$ 基测量结果中，$|-\rangle$ 的个数总是奇数。

### 2.3.2 W 态

**W 态**是另一种重要的三体纠缠态：

$$
|W\rangle = \frac{1}{\sqrt{3}}(|001\rangle + |010\rangle + |100\rangle)
$$

**性质**：

1. **二分纠缠稳健性**：GHZ 态在丢失一个量子比特后变成完全可分态；W 态在丢失一个量子比特后仍然保留二分纠缠。
2. **不对称性**：W 态的纠缠结构是不对称的——每个量子比特的地位看似对称，但施密特分解后各部分的纠缠结构不同。
3. **不可通过 LOCC 互变**：GHZ 态和 W 态不能通过**局域操作和经典通信（LOCC）** 互相转换——它们属于不同的纠缠类型。

**GHZ vs W 的对比**：

| 性质 | GHZ | W |
|:---|:---|:---|
| 形式 | $\frac{1}{\sqrt{2}}(|000\rangle + \|111\rangle)$ | $\frac{1}{\sqrt{3}}(\|001\rangle + \|010\rangle + \|100\rangle)$ |
| 纠缠类型 | 三体纠缠 | 二分纠缠 |
| 丢失一体后 | 完全可分 | 保留纠缠 |
| 对称性 | 完全对称 | 对称 |
| 非定域性 | 强（GHZ 矛盾） | 弱 |

**W 态的生成电路**：

```
|q0⟩ ──[√X]──╳────────────
              │
|q1⟩ ────────╳──╳─────────
                 │
|q2⟩ ────────────╳─────────
```

其中 $\sqrt{X}$ 门是 $R_x(\pi/2)$。

**W 态的应用**：W 态在量子网络和量子通信中有重要应用，因为它对粒子损失的鲁棒性更好。

### 2.3.3 施密特分解与纠缠秩

**施密特分解（Schmidt decomposition）** 是分析两体纠缠结构的核心数学工具。

**定理 2.1（施密特分解）** 对于任意两体纯态 $|\Psi\rangle_{AB} \in \mathcal{H}_A \otimes \mathcal{H}_B$，存在正交归一基 $\{|i_A\rangle\}$（在 $\mathcal{H}_A$ 中）和 $\{|i_B\rangle\}$（在 $\mathcal{H}_B$ 中），以及非负实数 $\lambda_i \geq 0$，使得：

$$
|\Psi\rangle_{AB} = \sum_{i=1}^{r} \sqrt{\lambda_i} \, |i_A\rangle \otimes |i_B\rangle
$$

其中：

- $\sum_i \lambda_i = 1$（归一化）
- $r$ 称为**施密特秩（Schmidt rank）**（或**纠缠秩**）
- $\{\sqrt{\lambda_i}\}$ 称为**施密特系数（Schmidt coefficients）**

**施密特秩的意义**：

- **$r = 1$**：态是可分的（直积态）
- **$r \geq 2$**：态是纠缠的
- **$r$ 越大**：纠缠越强（在给定维数下）

**寻找施密特分解的方法**：

1. 写出 $|\Psi\rangle_{AB}$ 在计算基下的系数矩阵 $C$（$d_A \times d_B$ 矩阵）
2. 对 $C$ 做奇异值分解（SVD）：$C = U \Sigma V^\dagger$
3. 奇异值 $\sigma_i$ 就是 $\sqrt{\lambda_i}$
4. $U$ 的列给出 $\{|i_A\rangle\}$，$V$ 的列给出 $\{|i_B\rangle\}$

**例 2.10** 对 $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ 做施密特分解。

系数矩阵（$2 \times 2$）：

$$
C = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

SVD：$C = I \cdot \frac{1}{\sqrt{2}}I \cdot I$，所以 $\lambda_1 = \lambda_2 = 1/2$。

施密特秩 $r = 2$ → **纠缠态**。施密特系数 $\sqrt{\lambda_1} = \sqrt{\lambda_2} = 1/\sqrt{2}$，说明是最大纠缠。

**例 2.11** 对 $|\Psi\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |01\rangle)$ 做施密特分解。

系数矩阵：

$$
C = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}
$$

SVD：只有 1 个非零奇异值 $\sigma_1 = 1/\sqrt{2} \times \sqrt{2} = 1$，所以 $\lambda_1 = 1$。

施密特秩 $r = 1$ → **可分态**。

**例 2.12** 对贝尔态 $|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$ 做施密特分解。

系数矩阵：

$$
C = \frac{1}{\sqrt{2}} \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
$$

SVD：奇异值 $\sigma_1 = \sigma_2 = 1/\sqrt{2}$，$\lambda_1 = \lambda_2 = 1/2$。

施密特秩 $r = 2$ → **纠缠态**。$|1_A\rangle = |0\rangle$，$|2_A\rangle = |1\rangle$；$|1_B\rangle = -|1\rangle$，$|2_B\rangle = |0\rangle$（符号可吸收到相位）。

**例 2.13** GHZ 态的施密特分解（按 A | BC 划分）：

$$
|\text{GHZ}\rangle = \frac{1}{\sqrt{2}}(|000\rangle + |111\rangle) = \frac{1}{\sqrt{2}}|0\rangle_A \otimes |00\rangle_{BC} + \frac{1}{\sqrt{2}}|1\rangle_A \otimes |11\rangle_{BC}
$$

$\{|0\rangle_A, |1\rangle_A\}$ 和 $\{|00\rangle_{BC}, |11\rangle_{BC}\}$ 都是正交基。施密特秩 $r = 2$ → 在 A|BC 划分下纠缠。

**纠缠熵**：施密特系数 $\lambda_i$ 可以定义为**纠缠熵（entanglement entropy）**：

$$
S(|\Psi\rangle_{AB}) = -\sum_{i=1}^{r} \lambda_i \log_2 \lambda_i
$$

- 可分态：$S = 0$（只有一个 $\lambda_1 = 1$）
- 最大纠缠态：$S = \log_2(\min(d_A, d_B))$（所有 $\lambda_i$ 相等）
- 两比特最大纠缠：$S = \log_2 2 = 1$（纠缠为 1 ebit）

**例 2.14** 计算 $|\Phi^+\rangle$ 的纠缠熵：

$$
S = -\frac{1}{2}\log_2\frac{1}{2} - \frac{1}{2}\log_2\frac{1}{2} = 1 \text{ ebit}
$$

**例 2.15** W 态的纠缠熵（按 A | BC 划分）：

$$
|W\rangle = \frac{1}{\sqrt{3}}(|001\rangle + |010\rangle + |100\rangle)
$$

写成 A | BC 形式：

$$
|W\rangle = \frac{1}{\sqrt{3}}|0\rangle_A \otimes (|01\rangle + |10\rangle)_{BC} + \frac{1}{\sqrt{3}}|1\rangle_A \otimes |00\rangle_{BC}
$$

施密特系数：$\lambda_1 = 2/3$，$\lambda_2 = 1/3$。

纠缠熵：

$$
S = -\frac{2}{3}\log_2\frac{2}{3} - \frac{1}{3}\log_2\frac{1}{3} \approx 0.918 \text{ ebit}
$$

小于 1 ebit → 不是最大纠缠。

---

**小练习 2.5** 对 $|\Psi\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$ 做施密特分解，并求纠缠熵。

**小练习 2.6** 考虑态 $|\Psi\rangle = \frac{1}{\sqrt{3}}|00\rangle + \frac{\sqrt{2}}{\sqrt{3}}|11\rangle$。计算其施密特系数和纠缠熵。这个态是否最大纠缠？

---

## 2.4 纠缠度量

### 2.4.1 PPT 判据与部分转置

给定一个两比特密度算符 $\rho_{AB}$，如何判断它是否纠缠？**PPT 判据**（Peres-Horodecki 判据）是最简单有效的必要条件。

**定义 2.5（部分转置）** 对两体密度算符 $\rho_{AB}$，对子系统 $B$ 做部分转置（partial transpose）$\rho_{AB}^{T_B}$，定义为：

$$
\langle i_A, j_B | \rho_{AB}^{T_B} | k_A, l_B \rangle = \langle i_A, l_B | \rho_{AB} | k_A, j_B \rangle
$$

即在计算基下，交换 $B$ 的指标。

**定理 2.2（PPT 判据）** 如果 $\rho_{AB}$ 是可分的，则 $\rho_{AB}^{T_B}$（部分转置后的矩阵）的所有本征值都非负（即 $\rho_{AB}^{T_B} \succeq 0$）。反过来，如果 $\rho_{AB}^{T_B}$ 有负本征值，则 $\rho_{AB}$ 一定是纠缠的。

对于 $2 \times 2$ 和 $2 \times 3$ 系统，PPT 判据既是**必要条件也是充分条件**。对于更高维系统，存在 PPT 纠缠态（bound entanglement）。

**例 2.16** 对 $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ 的密度算符做部分转置。

密度算符：

$$
\rho = |\Phi^+\rangle\langle\Phi^+| = \frac{1}{2}(|00\rangle\langle00| + |00\rangle\langle11| + |11\rangle\langle00| + |11\rangle\langle11|)
$$

矩阵形式（基序：00, 01, 10, 11）：

$$
\rho = \frac{1}{2} \begin{pmatrix}
1 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
1 & 0 & 0 & 1
\end{pmatrix}
$$

对 $B$ 做部分转置（交换 $B$ 的指标，即交换 01 和 10 对应的行/列）：

$$
\rho^{T_B} = \frac{1}{2} \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

计算本征值：$\{1/2, 1/2, 1/2, -1/2\}$。

有负本征值 $-1/2$ → **纠缠**。

**例 2.17** 对可分态 $\rho = |00\rangle\langle00|$：

$$
\rho = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

部分转置后不变（因为除了 $|00\rangle\langle00|$ 外全为 0），本征值：$\{1, 0, 0, 0\}$ → 无负本征值 → 可分。

### 2.4.2 负度

**负度（negativity）** 是一个可计算的纠缠度量，它量化了部分转置的负本征值的程度。

**定义 2.6（负度）** 对于两体密度算符 $\rho_{AB}$，负度定义为：

$$
\mathcal{N}(\rho) = \frac{\|\rho^{T_B}\|_1 - 1}{2}
$$

其中 $\|\cdot\|_1$ 是迹范数（所有奇异值之和）。等价地：

$$
\mathcal{N}(\rho) = \max\left(0, -\sum_{\lambda_i < 0} \lambda_i\right) = \sum_{\lambda_i < 0} |\lambda_i|
$$

其中 $\{\lambda_i\}$ 是 $\rho^{T_B}$ 的本征值。

**性质**：

- $\mathcal{N} = 0$：态是 PPT 的（可分或 bound entangled）
- $\mathcal{N} > 0$：态是纠缠的
- 对于两比特纯态最大纠缠：$\mathcal{N} = 1/2$

**例 2.18** 计算 $|\Phi^+\rangle$ 的负度：

$$
\rho^{T_B} \text{ 本征值：} \{1/2, 1/2, 1/2, -1/2\}
$$

$$
\mathcal{N} = |{-1/2}| = 1/2
$$

**例 2.19** 计算混合态 $\rho = p|\Phi^+\rangle\langle\Phi^+| + (1-p)|00\rangle\langle00|$ 的负度。

对于 $p=0.3$：

$$
\rho = 0.3 \cdot \frac{1}{2}\begin{pmatrix}
1 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
1 & 0 & 0 & 1
\end{pmatrix} + 0.7 \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}
= \begin{pmatrix}
0.85 & 0 & 0 & 0.15 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0.15 & 0 & 0 & 0.15
\end{pmatrix}
$$

部分转置后本征值：随着 $p$ 从 0 到 1，负本征值从 0 变到 $-0.5$。存在阈值 $p > 1/3$ 时出现负本征值。

### 2.4.3 并发度（两比特）

**并发度（concurrence）** 是两比特系统最常用的纠缠度量之一，由 Wootters 在 1998 年提出。

**定义 2.7（并发度）** 对于两比特态 $\rho$，并发度定义为：

$$
\mathcal{C}(\rho) = \max(0, \sqrt{\lambda_1} - \sqrt{\lambda_2} - \sqrt{\lambda_3} - \sqrt{\lambda_4})
$$

其中 $\{\lambda_i\}$ 是矩阵 $R = \rho(\sigma_y \otimes \sigma_y)\rho^*(\sigma_y \otimes \sigma_y)$ 的本征值，按降序排列。$\rho^*$ 是 $\rho$ 在计算基下的复共轭。

**对于纯态**：$|\Psi\rangle = a|00\rangle + b|01\rangle + c|10\rangle + d|11\rangle$，有更简单的公式：

$$
\mathcal{C}(|\Psi\rangle) = 2|ad - bc|
$$

**性质**：

- $\mathcal{C} = 0$：可分态
- $\mathcal{C} = 1$：最大纠缠态（贝尔态）
- $0 < \mathcal{C} < 1$：部分纠缠态

**例 2.20** 计算 $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ 的并发度。

$$
a = \frac{1}{\sqrt{2}},\; b = 0,\; c = 0,\; d = \frac{1}{\sqrt{2}}
$$

$$
\mathcal{C} = 2\left|\frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} - 0 \cdot 0\right| = 2 \cdot \frac{1}{2} = 1
$$

**最大纠缠**。

**例 2.21** 计算 $|\Psi\rangle = \frac{1}{\sqrt{3}}|00\rangle + \frac{\sqrt{2}}{\sqrt{3}}|11\rangle$ 的并发度。

$$
a = \frac{1}{\sqrt{3}},\; b = 0,\; c = 0,\; d = \frac{\sqrt{2}}{\sqrt{3}}
$$

$$
\mathcal{C} = 2\left|\frac{1}{\sqrt{3}} \cdot \frac{\sqrt{2}}{\sqrt{3}} - 0\right| = \frac{2\sqrt{2}}{3} \approx 0.943
$$

小于 1 → 不是最大纠缠。

**例 2.22** 计算 $|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$ 的并发度。

$$
a = 0,\; b = \frac{1}{\sqrt{2}},\; c = -\frac{1}{\sqrt{2}},\; d = 0
$$

$$
\mathcal{C} = 2\left|0 \cdot 0 - \frac{1}{\sqrt{2}} \cdot \left(-\frac{1}{\sqrt{2}}\right)\right| = 2 \cdot \frac{1}{2} = 1
$$

**最大纠缠**。

**并发度 vs 负度**：

| 性质 | 并发度 $\mathcal{C}$ | 负度 $\mathcal{N}$ |
|:---|:---:|:---:|
| 两比特最大纠缠值 | 1 | 1/2 |
| 计算难度 | 需要 SVD | 需要部分转置 |
| 混合态适用 | 是（Wootters 公式） | 是 |
| 单调性 | 是（纠缠单调） | 是 |

### 2.4.4 纠缠见证

**纠缠见证（entanglement witness）** 是一个可观测量 $W$，满足：

1. 对所有可分态 $\rho_{\text{sep}}$：$\operatorname{Tr}(W \rho_{\text{sep}}) \geq 0$
2. 存在至少一个纠缠态 $\rho_{\text{ent}}$：$\operatorname{Tr}(W \rho_{\text{ent}}) < 0$

**几何解释**：

```
      所有态
    ┌──────────────┐
    │  可分态区域   │
    │  ┌───────┐   │
    │  │Tr(Wρ)≥0│   │
    │  └───────┘   │
    │  ·纠缠态·    │
    │  ·Tr(Wρ)<0·  │
    └──────────────┘
```

纠缠见证 $W$ 对应一个超平面，将一些纠缠态与所有可分态分开。

**例 2.23** 对于贝尔态 $|\Phi^+\rangle$，一个简单的纠缠见证是：

$$
W = \frac{1}{2}I - |\Phi^+\rangle\langle\Phi^+|
$$

验证：

- 对于 $|\Phi^+\rangle$：$\operatorname{Tr}(W |\Phi^+\rangle\langle\Phi^+|) = 1/2 - 1 = -1/2 < 0$
- 对于可分态 $|00\rangle$：$\operatorname{Tr}(W |00\rangle\langle00|) = 1/2 - |\langle00|\Phi^+\rangle|^2 = 1/2 - 1/2 = 0$
- 对于可分态 $|01\rangle$：$\operatorname{Tr}(W |01\rangle\langle01|) = 1/2 - 0 = 1/2 > 0$

**实验意义**：纠缠见证**不需要完整的量子态层析**——只需要测量几个期望值。这使得它在实验中非常实用。

**例 2.24** 一个实验上容易实现的纠缠见证（基于泡利测量）：

$$
W = \frac{1}{2}(I + Z_A Z_B + X_A X_B)
$$

对于 $|\Phi^+\rangle$：

$$
\langle \Phi^+| Z_A Z_B |\Phi^+\rangle = 1,\quad \langle \Phi^+| X_A X_B |\Phi^+\rangle = 1
$$

$$
\operatorname{Tr}(W |\Phi^+\rangle\langle\Phi^+|) = \frac{1}{2}(1 + 1 + 1) = \frac{3}{2} > 0
$$

等等——这不小于 0，所以这个见证不适用于 $|\Phi^+\rangle$。实际上需要调整系数。

**正确的 CHSH 类纠缠见证**：

$$
W = \frac{1}{2}I - \frac{1}{2\sqrt{2}}(X_A X_B + X_A Z_B + Z_A X_B - Z_A Z_B)
$$

对 $|\Phi^+\rangle$：期望值 $= 1/2 - (2\sqrt{2})/(2\sqrt{2}) = 1/2 - 1 = -1/2 < 0$。

**纠缠见证的优缺点**：

- ✅ 不需要完整层析，实验开销小
- ✅ 可以检测特定类的纠缠态
- ❌ 没有一个普适的见证能检测所有纠缠态
- ❌ 见证的设计依赖于目标纠缠态的先验知识

---

**小练习 2.7** 对 $\rho = |\Psi^-\rangle\langle\Psi^-|$ 做部分转置，计算负度。

**小练习 2.8** 计算 $|\Psi\rangle = 0.8|00\rangle + 0.6|11\rangle$ 的并发度。它是否为最大纠缠？

---

## 2.5 两比特门

### 2.5.1 CNOT 门

**CNOT 门**（controlled-NOT）是最重要的两比特门之一。它有一个控制比特（control qubit）和一个目标比特（target qubit）。

**定义 2.8（CNOT 门）**

$$
\text{CNOT} = |0\rangle\langle0| \otimes I + |1\rangle\langle1| \otimes X
$$

**矩阵形式**（控制比特为第一个量子比特，基序：00, 01, 10, 11）：

$$
\text{CNOT} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{pmatrix}
$$

**真值表**：

| 输入 | 输出 |
|:---:|:---:|
| $|00\rangle$ | $|00\rangle$ |
| $|01\rangle$ | $|01\rangle$ |
| $|10\rangle$ | $|11\rangle$ |
| $|11\rangle$ | $|10\rangle$ |

即：控制比特为 $|0\rangle$ 时目标不变，控制比特为 $|1\rangle$ 时目标翻转。

**电路符号**：

```
控制 ──●──
       │
目标 ──⊕──
```

其中实心圆 ● 在控制线上，⊕ 在目标线上。

**性质**：

1. **幺正**：$\text{CNOT}^\dagger = \text{CNOT}$，$\text{CNOT}^2 = I$
2. **产生纠缠**：$H + \text{CNOT}$ 从 $|00\rangle$ 产生贝尔态
3. **通用性**：CNOT + 所有单比特门构成通用量子门集

**例 2.25** CNOT 在不同基下的表示。

在 $X$ 基（$|+\rangle, |-\rangle$）下，CNOT 的"控制"和"目标"角色互换——这称为 **Kraus-Cirac 定理**：

$$
\text{CNOT} = \frac{1}{2}(I \otimes I + Z \otimes I + I \otimes X - Z \otimes X)
$$

### 2.5.2 CZ 门

**CZ 门**（controlled-Z）是另一个基本的两比特门。

**定义 2.9（CZ 门）**

$$
\text{CZ} = |0\rangle\langle0| \otimes I + |1\rangle\langle1| \otimes Z
$$

**矩阵形式**：

$$
\text{CZ} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & -1
\end{pmatrix}
$$

**真值表**：

| 输入 | 输出 |
|:---:|:---:|
| $|00\rangle$ | $|00\rangle$ |
| $|01\rangle$ | $|01\rangle$ |
| $|10\rangle$ | $|10\rangle$ |
| $|11\rangle$ | $-|11\rangle$ |

只有 $|11\rangle$ 获得相位 $-1$。

**电路符号**：

```
控制 ──●──
       │
目标 ──●──
```

两个 ● 表示受控 $Z$ 门（因为是泡利 $Z$，它不区分控制和目标——CZ 是对称的）。

**CZ 与 CNOT 的转换**：

$$
\text{CNOT} = (I \otimes H) \, \text{CZ} \, (I \otimes H)
$$

**验证**：

$$
(I \otimes H) \, \text{CZ} \, (I \otimes H) = |0\rangle\langle0| \otimes HIH + |1\rangle\langle1| \otimes HZH = |0\rangle\langle0| \otimes I + |1\rangle\langle1| \otimes X = \text{CNOT}
$$

因为 $HZH = X$。

反之：

$$
\text{CZ} = (I \otimes H) \, \text{CNOT} \, (I \otimes H)
$$

### 2.5.3 SWAP 门

**SWAP 门**交换两个量子比特的状态。

**定义 2.10（SWAP 门）**

$$
\text{SWAP} = |00\rangle\langle00| + |01\rangle\langle10| + |10\rangle\langle01| + |11\rangle\langle11|
$$

**矩阵形式**：

$$
\text{SWAP} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

**作用效果**：

$$
\text{SWAP} |\psi\rangle |\phi\rangle = |\phi\rangle |\psi\rangle
$$

**电路符号**：

```
──╳──
  │
──╳──
```

**用 CNOT 实现 SWAP**：

```
──╳──   =   ──●───────●──
  │           │       │
──╳──       ──⊕──●───⊕──
                 │
              （或者更简洁地：CNOT₁₂, CNOT₂₁, CNOT₁₂）
```

即：

$$
\text{SWAP} = \text{CNOT}_{12} \; \text{CNOT}_{21} \; \text{CNOT}_{12}
$$

**验证**：

$$
\begin{aligned}
|01\rangle &\xrightarrow{\text{CNOT}_{12}} |01\rangle \xrightarrow{\text{CNOT}_{21}} |11\rangle \xrightarrow{\text{CNOT}_{12}} |10\rangle \\
|10\rangle &\xrightarrow{\text{CNOT}_{12}} |11\rangle \xrightarrow{\text{CNOT}_{21}} |01\rangle \xrightarrow{\text{CNOT}_{12}} |01\rangle
\end{aligned}
$$

成功交换。

### 2.5.4 iSWAP 门

**iSWAP 门**是超导量子比特平台中常见的**本征门**（native gate）。

**定义 2.11（iSWAP 门）**

$$
\text{iSWAP} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & i & 0 \\
0 & i & 0 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

**作用效果**：

| 输入 | 输出 |
|:---:|:---:|
| $|00\rangle$ | $|00\rangle$ |
| $|01\rangle$ | $i|10\rangle$ |
| $|10\rangle$ | $i|01\rangle$ |
| $|11\rangle$ | $|11\rangle$ |

**iSWAP 的平方**：

$$
\text{iSWAP}^2 = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & i & 0 \\
0 & i & 0 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}^2 = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix} = I
$$

所以 $\text{iSWAP}^\dagger = \text{iSWAP} = \text{iSWAP}^{-1}$（也是自逆的）。

**$\sqrt{\text{iSWAP}}$ 门**：也是超导平台中常见的本征门。

$$
\sqrt{\text{iSWAP}} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & \frac{1}{\sqrt{2}} & \frac{i}{\sqrt{2}} & 0 \\
0 & \frac{i}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

它与 CNOT 可以通过单比特门互相转换。

**iSWAP 的应用**：iSWAP 在超导量子比特中通常比 CNOT 更容易实现，因为它是通过相邻量子比特的**可调耦合器**直接实现的。

### 2.5.5 受控旋转门

受控旋转门（controlled rotation）是 CNOT 和 CZ 的推广。

**定义 2.12（受控 $U$ 门）**

$$
\text{CU} = |0\rangle\langle0| \otimes I + |1\rangle\langle1| \otimes U
$$

其中 $U$ 是任意单比特幺正门。

**矩阵形式**（基序：00, 01, 10, 11）：

$$
\text{CU} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & u_{00} & u_{01} \\
0 & 0 & u_{10} & u_{11}
\end{pmatrix}
$$

**重要特例**：

1. **受控 $R_x(\theta)$**（CRx）：

$$
\text{CR}_x(\theta) = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & \cos\frac{\theta}{2} & -i\sin\frac{\theta}{2} \\
0 & 0 & -i\sin\frac{\theta}{2} & \cos\frac{\theta}{2}
\end{pmatrix}
$$

2. **受控 $R_y(\theta)$**（CRy）：

$$
\text{CR}_y(\theta) = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\
0 & 0 & \sin\frac{\theta}{2} & \cos\frac{\theta}{2}
\end{pmatrix}
$$

3. **受控 $R_z(\theta)$**（CRz）：

$$
\text{CR}_z(\theta) = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & e^{-i\theta/2} & 0 \\
0 & 0 & 0 & e^{i\theta/2}
\end{pmatrix}
$$

**电路符号**：

```
控制 ──●──
       │
目标 ──[U]──
```

其中 $[U]$ 可以是 $R_x(\theta)$、$R_y(\theta)$ 等。

**受控门的分解**：任意受控门 $\text{CU}$ 可以用 CNOT 和单比特门实现：

$$
\text{CU} = (I \otimes A) \; \text{CNOT} \; (I \otimes B)
$$

其中 $A$ 和 $B$ 满足 $AB = U$，$A\sigma_x B = U\sigma_x$ 等（具体的分解依赖于 $U$）。

### 2.5.6 任意两比特门分解

任意两比特门 $U \in SU(4)$ 可以分解为更简单的门序列。最重要的分解定理是：

**定理 2.3（Kraus-Cirac 分解）** 任意两比特门 $U \in SU(4)$ 可以分解为：

$$
U = (A_1 \otimes A_2) \; e^{i(\alpha X \otimes X + \beta Y \otimes Y + \gamma Z \otimes Z)} \; (B_1 \otimes B_2)
$$

其中 $A_1, A_2, B_1, B_2$ 是单比特门，$\alpha, \beta, \gamma$ 是实数。

**等价形式**：任意两比特门最多需要 3 个 CNOT 门加上单比特门即可实现。

**CNOT 计数**：

| 门类型 | 最少 CNOT 数 |
|:---|:---:|
| 可分门（直积） | 0 |
| SWAP | 3 |
| 一般两比特门 | 3 |
| 特殊两比特门（如 CNOT 本身） | 1 |

**例 2.26** 任意两比特门的通用分解（使用 3 个 CNOT）：

```
──[A1]────●──────────●────[B1]──
           │          │
──[A2]────⊕──[R]──●──⊕────[B2]──
                   │
                （其中 [R] 是 Z 旋转）
```

实际分解非常复杂，编译器通常会做优化。现代量子编译器（如 Qiskit、Cirq 的 transpiler）可以自动将任意两比特幺正矩阵编译为特定平台的本征门序列。

### 2.5.7 两比特门物理实现思路

不同物理平台实现两比特门的机制各异。这里只给出高层次的物理图像。

#### 超导量子比特

**CNOT（或 CZ）的典型实现**：

1. **固定耦合方案**：两个量子比特通过电容或谐振器固定耦合，通过调谐量子比特频率到共振来实现门。
2. **可调耦合方案**：通过一个可调耦合器（transmon 或 CR 耦合器），只在需要时打开耦合。
3. **Cross-Resonance（CR）方案**：在控制比特上施加驱动频率等于目标比特频率的微波，产生 ZZ 类相互作用，等效于 CNOT。

**iSWAP 的实现**：两个量子比特共振耦合一段时间 $t = \pi/(2g)$，实现 $\sqrt{\text{iSWAP}}$。

#### 离子阱

**CNOT 的典型实现**（Mølmer-Sørensen 方案）：

1. 用激光照射两个离子，同时驱动它们的**侧带跃迁**（sideband transition）。
2. 通过集体振动模式（phonon）作为"总线"传递纠缠。
3. 可以实现高保真度（$>99.9\%$）的两比特门。

**特点**：离子阱的任意两比特门（通过 MS 门）本质上实现的是 XX 类相互作用。

#### 硅量子点

**SWAP 门**：通过调控两个量子点之间的交换耦合 $J(t)$，实现 SWAP 或 $\sqrt{\text{SWAP}}$。

**CNOT**：通过 $\sqrt{\text{SWAP}}$ 序列 + 单比特门构造。

#### 中性原子

**CZ 门**：通过**里德伯阻塞（Rydberg blockade）** 机制实现。

1. 用激光将原子激发到里德伯态（高激发态，$n \gg 1$）。
2. 里德伯原子间的强偶极-偶极相互作用导致"阻塞"效应：两个原子不能同时处于里德伯态。
3. 利用这种阻塞实现 CZ 门。

---

**小练习 2.9** 用矩阵乘法验证 $\text{SWAP} = \text{CNOT}_{12} \; \text{CNOT}_{21} \; \text{CNOT}_{12}$。

**小练习 2.10** 证明 $CZ = (I \otimes H) \; \text{CNOT} \; (I \otimes H)$。

---

## 2.6 纠缠应用

### 2.6.1 密集编码

**密集编码（superdense coding）** 是一个令人惊奇的量子通信协议：它允许 Alice 通过发送**一个**量子比特给 Bob，传递**两个**经典比特的信息。

**前提条件**：Alice 和 Bob 预先共享一个贝尔态 $|\Phi^+\rangle$。

**协议步骤**：

```
步骤 0: 共享纠缠
    Alice ───── ┌───┐ ──── Bob
                │ H │   （初始 Bell 对制备）
                └───┘
    Alice: 持有第一个量子比特
    Bob: 持有第二个量子比特

步骤 1: Alice 编码（选择四种操作之一）
    ┌──────┬──────────┐
    │ 信息  │ Alice 操作 │
    ├──────┼──────────┤
    │  00  │  I（不做）│
    │  01  │  X       │
    │  10  │  Z       │
    │  11  │  XZ (=iY)│
    └──────┴──────────┘

步骤 2: Alice 发送她的量子比特给 Bob

步骤 3: Bob 做贝尔测量
    ──●──[H]── 测量
      │
    ──⊕──────── 测量
```

**编码详述**：

Alice 想要发送两比特信息 $b_1 b_2$：

- **00**: 不做操作 → $|\Phi^+\rangle$
- **01**: 应用 $X$ → $(I \otimes X)|\Phi^+\rangle = |\Psi^+\rangle$
- **10**: 应用 $Z$ → $(I \otimes Z)|\Phi^+\rangle = |\Phi^-\rangle$
- **11**: 应用 $XZ$ → $(I \otimes XZ)|\Phi^+\rangle = |\Psi^-\rangle$

Bob 在收到 Alice 的量子比特后，对两个量子比特做**贝尔基测量**（即逆贝尔态制备电路 + 计算基测量）：

$$
\text{Bell测量} = \text{CNOT} \cdot (H \otimes I)
$$

将贝尔基映射回计算基：

| 贝尔态 | CNOT(H⊗I) 后的态 | 测量结果 |
| :---: | :---: | :---: |
| \( |\Phi^+\rangle \) | \( |00\rangle \) | 00 |
| \( |\Psi^+\rangle \) | \( |01\rangle \) | 01 |
| \( |\Phi^-\rangle \) | \( |10\rangle \) | 10 |
| \( |\Psi^-\rangle \) | \( |11\rangle \) | 11 |

**信息论意义**：经典通信中，发送 1 个量子比特最多传递 1 比特经典信息（如 Holevo 界）。密集编码通过预共享纠缠实现了 1 → 2 的信息传输——但代价是预共享的纠缠资源。

### 2.6.2 隐形传态

**量子隐形传态（quantum teleportation）** 允许 Alice 将一个未知量子态 $|\psi\rangle$ 传送给 Bob，而**不需要传输任何物理载体**——只需要传输两个经典比特和预共享纠缠。

**前提条件**：

- Alice 和 Bob 共享贝尔态 $|\Phi^+\rangle$
- Alice 有一个未知态 $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$

**协议步骤**：

```
初始状态：(α|0⟩ + β|1⟩)ₐ ⊗ ½(|00⟩+|11⟩)ₐᴮ

Alice 的两个量子比特：a（未知态）和 A（贝尔对的一半）
Bob 的一个量子比特：B（贝尔对的另一半）

步骤 1: Alice 对 a 和 A 做贝尔测量
步骤 2: Alice 通过经典信道发送 2 比特测量结果给 Bob
步骤 3: Bob 根据收到的结果对 B 应用纠错门
```

**详细演算**：

初始三比特态：

$$
|\Psi_0\rangle = (\alpha|0\rangle_a + \beta|1\rangle_a) \otimes \frac{1}{\sqrt{2}}(|00\rangle_{AB} + |11\rangle_{AB})
$$

展开（注意下标：$a$ 是未知态，$A$ 是 Alice 的纠缠对一半，$B$ 是 Bob 的纠缠对一半）：

$$
\begin{aligned}
|\Psi_0\rangle &= \frac{1}{\sqrt{2}} \big[ \alpha|0\rangle_a|00\rangle_{AB} + \alpha|0\rangle_a|11\rangle_{AB} \\
&\qquad\qquad + \beta|1\rangle_a|00\rangle_{AB} + \beta|1\rangle_a|11\rangle_{AB} \big]
\end{aligned}
$$

也可以将前两个量子比特（$a$ 和 $A$）按贝尔基展开：

$$
\begin{aligned}
|0\rangle_a|0\rangle_A &= \frac{1}{\sqrt{2}}(|\Phi^+\rangle_{aA} + |\Phi^-\rangle_{aA}) \\
|0\rangle_a|1\rangle_A &= \frac{1}{\sqrt{2}}(|\Psi^+\rangle_{aA} + |\Psi^-\rangle_{aA}) \\
|1\rangle_a|0\rangle_A &= \frac{1}{\sqrt{2}}(|\Psi^+\rangle_{aA} - |\Psi^-\rangle_{aA}) \\
|1\rangle_a|1\rangle_A &= \frac{1}{\sqrt{2}}(|\Phi^+\rangle_{aA} - |\Phi^-\rangle_{aA})
\end{aligned}
$$

重新整理 $|\Psi_0\rangle$：

$$
\begin{aligned}
|\Psi_0\rangle &= \frac{1}{2} \Big[ |\Phi^+\rangle_{aA} \otimes (\alpha|0\rangle_B + \beta|1\rangle_B) \\
&\qquad\qquad + |\Phi^-\rangle_{aA} \otimes (\alpha|0\rangle_B - \beta|1\rangle_B) \\
&\qquad\qquad + |\Psi^+\rangle_{aA} \otimes (\alpha|1\rangle_B + \beta|0\rangle_B) \\
&\qquad\qquad + |\Psi^-\rangle_{aA} \otimes (\alpha|1\rangle_B - \beta|0\rangle_B) \Big]
\end{aligned}
$$

Alice 对 $(a,A)$ 做贝尔测量，四种结果等概率（各 1/4）：

| 测量结果 | 传输信息 | Bob 的态 | Bob 的门 |
|:---:|:---:|:---|:---:|
| $|\Phi^+\rangle$ | 00 | $\alpha|0\rangle + \beta|1\rangle$ | $I$ |
| $|\Phi^-\rangle$ | 10 | $\alpha|0\rangle - \beta|1\rangle$ | $Z$ |
| $|\Psi^+\rangle$ | 01 | $\alpha|1\rangle + \beta|0\rangle$ | $X$ |
| $|\Psi^-\rangle$ | 11 | $\alpha|1\rangle - \beta|0\rangle$ | $ZX$ |

Bob 根据收到的两比特信息应用对应的门，恢复出 $\alpha|0\rangle + \beta|1\rangle$。

**电路图**：

```
Alice                   Bob
|ψ⟩ ──●──[H]── M ──┐
     │         │    │ 经典信道
|Φ⁺⟩A─⊕──────── M ──┼──────────
                   │    │
|Φ⁺⟩B─────────────┴────⊕──[Z^c₂]──[X^c₁]── |ψ⟩
```

其中 $c_1, c_2$ 是 Alice 的经典测量结果。

**重要认识**：

1. **没有超光速通信**：Bob 必须等待 Alice 的经典信息（光速上限）。
2. **没有克隆**：隐形传态**破坏了原始态**（Alice 的态在测量后坍缩），不违反不可克隆定理。
3. **不是传送物质**：传送的是**量子态**（信息），不是粒子本身。
4. **保真度**：理想情况下 $F = 1$。实验上，随着距离增加保真度下降，但可以通过量子中继器改善。

### 2.6.3 SWAP 门网络

SWAP 门在量子电路中用于**重新排列量子比特**。在大多数量子计算机中，两个量子比特之间的相互作用只限于**相邻**量子比特（最近邻耦合）。因此，要作用在非相邻量子比特上就需要 SWAP 网络。

**线性最近邻（LNN）架构**：

```
q0 ──○──○────────────────
     │  │
q1 ──⊕──⊕──○──○──────────
           │  │
q2 ────────⊕──⊕──○──○────
                 │  │
q3 ──────────────⊕──⊕────
```

**例 2.27** 在 LNN 架构中实现 $q_0$ 到 $q_3$ 的 CNOT：

需要将 $q_0$ 和 $q_3$ 通过 SWAP 移到相邻位置。

```
q0 ──╳─────────────╳──●──
     │              │  │
q1 ──╳──╳────────╳──╳──│──
        │        │      │
q2 ─────╳──╳──╳──╳─────│──
           │            │
q3 ────────╳────────────⊕──
```

这个网络使用 3 个 SWAP（9 个 CNOT），加上中间的一个 CNOT。

**SWAP 网络的优化**：

1. **线路路由（routing）**：通过编译优化，找到最优的 SWAP 插入方案。
2. **桥接 CNOT（bridged CNOT）**：对于远距离 CNOT，可以用 4 个 CNOT 代替 3 个 SWAP + CNOT。
3. **交换网络（swap network）**：在量子傅里叶变换中，SWAP 网络用于反转量子比特顺序。

### 2.6.4 纠缠蒸馏概念

现实中的纠缠态**不完美**——因为噪声、退相干和门误差，制备的纠缠态总是混合的、部分纠缠的。

**纠缠蒸馏（entanglement distillation）**（也称为**纠缠纯化，entanglement purification**）是将多个不完美的纠缠对通过 LOCC 操作"提纯"为少几个高保真度纠缠对的过程。

**基本原理**：

```
Alice                     Bob
┌───┐                     ┌───┐
│ρ₁ │──── 低保真纠缠 ────→│   │
│ρ₂ │──── 低保真纠缠 ────→│   │
│   │                     │   │
│ 联合测量                 │ 联合测量
│ 经典通信                 │ 经典通信
│   │                     │   │
│ρ' │──── 高保真纠缠 ────→│   │
└───┘                     └───┘
```

**BBPSSW 协议**（Bennett-Brassard-Popescu-Schumacher-Smolin-Wootters, 1996）：

这是最早的纠缠蒸馏协议之一，适用于 Werner 态。

**步骤**：

1. Alice 和 Bob 有两对纠缠对 $(\rho_1, \rho_2)$
2. 每对各自做 CNOT（Alice 控制自己的 A1 和 A2，Bob 控制自己的 B1 和 B2）
3. 测量两对中的一对（在 $Z$ 基）
4. 如果测量结果匹配（都得到 $|0\rangle$ 或都得到 $|1\rangle$），保留另一对；否则丢弃

**保真度提升**：

| 初始保真度 | 蒸馏后保真度（一轮） |
|:---:|:---:|
| 0.75 | 0.900 |
| 0.80 | 0.941 |
| 0.85 | 0.973 |
| 0.90 | 0.994 |

**纠缠蒸馏的重要性**：

1. **量子中继器**：长距离量子通信需要定期蒸馏来克服损耗和噪声。
2. **容错量子计算**：蒸馏可以生产高保真度的纠缠资源。
3. **量子网络**：多个节点间的纠缠分发后需要蒸馏。

> **类比**：就像黄金提纯——你投入多块低纯度金矿石，经过化学处理，得到一块高纯度的金锭。但这个过程不是免费的——你损失了数量，换取了质量。

---

**小练习 2.11** 在密集编码中，如果 Alice 和 Bob 预共享的是 $|\Psi^-\rangle$ 而不是 $|\Phi^+\rangle$，Alice 的编码操作需要如何调整？

**小练习 2.12** 在隐形传态中，如果 Alice 只发送了 1 比特（而不是 2 比特）结果给 Bob，Bob 能否恢复出完整的 $|\psi\rangle$？为什么？

---

### 知识点索引

| 术语 | 英文 | 节 |
|------|------|----|
| CHSH不等式 | CHSH inequality | 2.2.3 |
| W态 | W state | 2.3.2 |
| 贝尔不等式 | Bell's inequality | 2.2.3 |
| 贝尔基 | Bell basis | 2.2.1 |
| 贝尔测量 | Bell measurement | 2.6.1 |
| 贝尔态 | Bell states | 2.2.1 |
| 并发度 | concurrence | 2.4.3 |
| 部分转置 | partial transpose | 2.4.1 |
| 测量 | measurement | 2.6 |
| 纠缠度量 | entanglement measure | 2.4 |
| 纠缠态 | entangled state | 2.1.4 |
| 纠缠蒸馏 | entanglement distillation | 2.6.4 |
| 纠缠熵 | entanglement entropy | 2.4.4 |
| 负度 | negativity | 2.4.2 |
| 密集编码 | dense coding | 2.6.1 |
| 施密特分解 | Schmidt decomposition | 2.3.3 |
| 施密特秩 | Schmidt rank | 2.3.3 |
| 双量子点 | double quantum dot | 2.5 |
| 计算基矢 | computational basis | 2.1.2 |
| 量子非定域性 | quantum nonlocality | 2.2.4 |
| 量子纠缠 | quantum entanglement | 2.1.4 |
| 分态 | separable state | 2.1.3 |
| 隐形传态 | quantum teleportation | 2.6.2 |
| 张量积 | tensor product | 2.1.1 |
| 直积态 | product state | 2.1.3 |
| 纠缠见证 | entanglement witness | 2.4.4 |
| CNOT门 | CNOT gate | 2.5.1 |
| CZ门 | CZ gate | 2.5.2 |
| GHZ态 | GHZ state | 2.3.1 |
| iSWAP门 | iSWAP gate | 2.5.4 |
| LOCC | Local Operations and Classical Communication | 2.6 |
| PPT判据 | PPT criterion | 2.4.1 |
| SWAP门 | SWAP gate | 2.5.3 |

## 2.7 本章习题

### ★ 基础题（第 1-6 题）

**1.** 判断以下两比特态是否可分。若可分，给出张量积分解。

(a) $|\Psi_a\rangle = \frac{1}{2}(|00\rangle + |01\rangle + |10\rangle + |11\rangle)$

(b) $|\Psi_b\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |01\rangle + |10\rangle - |11\rangle)$

(c) $|\Psi_c\rangle = \frac{1}{\sqrt{5}}(|00\rangle + 2|11\rangle)$

(d) $|\Psi_d\rangle = \cos\theta|00\rangle + \sin\theta|11\rangle$

**2.** 写出以下两比特门在计算基 $\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$ 下的矩阵形式：

(a) $I \otimes X$

(b) $Z \otimes H$

(c) $\text{CNOT}_{21}$（控制比特为 q2，目标为 q1）

(d) $\text{SWAP}$

**3.** 从以下输入态出发，经过 H + CNOT 电路，分别输出哪个态？

(a) $|00\rangle$ → ?

(b) $|01\rangle$ → ?

(c) $|10\rangle$ → ?

(d) $|11\rangle$ → ?

**4.** 列出四个贝尔态，并写出它们之间的转换关系（用单比特泡利门表示）。

**5.** 计算以下态的施密特秩和施密特系数：

(a) $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$

(b) $|\Psi\rangle = \frac{1}{\sqrt{2}}(|0\rangle_A|+\rangle_B + |1\rangle_A|-\rangle_B)$

(c) $|\Psi\rangle = \frac{3}{5}|00\rangle + \frac{4}{5}|11\rangle$

**6.** 计算 $|\Psi^-\rangle$ 的并发度和纠缠熵。

### ★★ 计算题（第 7-14 题）

**7.** 证明四贝尔态两两正交。提示：归一化因子为 $1/\sqrt{2}$，计算每个内积。

**8.** 对 $\rho = |\Phi^+\rangle\langle\Phi^+|$ 做部分转置，列出本征值，计算负度。

**9.** 对两比特纯态 $|\Psi\rangle = \alpha|00\rangle + \beta|01\rangle + \gamma|10\rangle + \delta|11\rangle$，推导并发度公式 $\mathcal{C} = 2|ad - bc|$ 的步骤。

提示：先写出 $\tilde{\rho} = (\sigma_y \otimes \sigma_y) \rho^* (\sigma_y \otimes \sigma_y)$，再求本征值。

**10.** 用矩阵乘法验证 $\text{CNOT} = (I \otimes H) \, \text{CZ} \, (I \otimes H)$。

**11.** 用 CNOT 和单比特门实现受控 $R_y(\theta)$ 门，画出电路并写出分解公式。

**12.** 推导密集编码中从 $|\Phi^+\rangle$ 到四个编码态的完整变换。如果共享的初始贝尔态是 $|\Psi^-\rangle$，Alice 的操作应该是什么？

**13.** 在隐形传态协议中，写出 Alice 的四个测量结果对应的 Bob 态，并证明 Bob 应用对应的纠错门后总能得到 $\alpha|0\rangle + \beta|1\rangle$。

**14.** 设 Alice 和 Bob 共享一个部分纠缠态 $|\Psi\rangle = \sqrt{0.8}|00\rangle + \sqrt{0.2}|11\rangle$。Alice 有一个未知态 $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ 要传送。是否可以用标准的隐形传态协议？如果可以，Bob 的纠错门是否相同？讨论保真度。

### ★★★ 证明题（第 15-18 题）

**15.** 证明：两比特纯态 $|\Psi\rangle$ 可分的充要条件是施密特秩 $r = 1$。

提示：从施密特分解的定义出发。

**16.** 证明任意两比特门最多需要 3 个 CNOT 门就能实现（Kraus-Cirac 定理的陈述）。简略说明构造思路即可。

**17.** **GHZ 矛盾**：证明对于 GHZ 态 $\frac{1}{\sqrt{2}}(|000\rangle + |111\rangle)$，局域实在论预测 $X_1 X_2 X_3$ 的测量结果必须满足某种关系，而量子力学预测违反该关系。

提示：$X_i$ 的测量结果为 $\pm 1$。考虑 $X_1 X_2 X_3$ 和单个 $X_i$ 测量的关联。

**18.** 证明：对于 Bell 态 $|\Phi^+\rangle$，CHSH 不等式中的 $S$ 最大值为 $2\sqrt{2}$（Tsirelson 上界）。

提示：定义算符 $C = A \otimes B + A \otimes B' + A' \otimes B - A' \otimes B'$，求 $C^\dagger C$ 的上界。

---

> **拓展阅读建议**：
>
> 1. **纠缠与贝尔不等式**：J. S. Bell, *Speakable and Unspeakable in Quantum Mechanics* (1987)
> 2. **纠缠度量综述**：R. Horodecki et al., "Quantum entanglement", *Rev. Mod. Phys.* **81**, 865 (2009)
> 3. **纠缠蒸馏**：Bennett et al., "Purification of Noisy Entanglement", *Phys. Rev. Lett.* **76**, 722 (1996)
> 4. **量子隐形传态**：Bennett et al., "Teleporting an Unknown Quantum State via Dual Classical and Einstein-Podolsky-Rosen Channels", *Phys. Rev. Lett.* **70**, 1895 (1993)
> 5. **两比特门分解**：Vatan & Williams, "Realization of a general three-qubit quantum gate", *Phys. Rev. A* **69**, 032315 (2004)
