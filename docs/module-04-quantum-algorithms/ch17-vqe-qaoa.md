# 第5章 变分量子算法：VQE与QAOA

> **本章导读**
>
> 前几章我们学习了量子门、量子电路、量子傅里叶变换和Grover搜索等基础量子算法。这些算法在理论上具有确定性的加速保证，但它们在含噪中等规模量子（NISQ）设备上的直接实现面临巨大挑战——电路深度过大、量子比特数目有限、门错误率尚不能支撑完全纠错。
>
> **变分量子算法（Variational Quantum Algorithms, VQA）** 正是为应对NISQ时代的局限而设计的算法家族。其核心思想是：**用量子电路制备参数化试验态，用经典计算机优化参数，以混合方式逼近问题的解**。本章重点介绍两个最具代表性的变分算法：
>
> - **VQE（变分量子本征值求解器）**：用于求解量子系统的基态能量，在量子化学模拟中具有重要应用
> - **QAOA（量子近似优化算法）**：用于组合优化问题的近似求解，被视为量子计算在商业优化中的潜在突破口
>
> **学完本章，你将能够：**
> - 描述变分量子-经典混合架构的工作原理
> - 理解量子化学电子结构问题如何映射为哈密顿量求解
> - 掌握Jordan-Wigner和Bravyi-Kitaev两种费米子-量子比特映射方法
> - 实现VQE算法的完整流程，包括哈密顿量测量和参数优化
> - 区分硬件高效Ansatz与UCC Ansatz的设计理念与适用场景
> - 理解泡利串的并行测量分组策略
> - 对比不同经典优化器在VQE中的表现特点
> - 理解QAOA中成本哈密顿量与混合哈密顿量的作用
> - 用QAOA求解MaxCut问题并分析近似比
> - 了解零噪声外推这一最实用的误差缓解技术
>
> **先修知识**：模块一（线性代数、本征值分解）、第10章（量子电路基础）、第11章（量子门与通用性）、第13章（量子傅里叶变换）

---

## 5.1 变分量子-经典混合架构

### 5.1.1 NISQ时代的算法设计哲学

**即时练习 5.1.1**

1. NISQ 时代的典型特征是什么？变分量子算法为何适合 NISQ 设备？
2. Rayleigh-Ritz 变分原理的内容是什么？

含噪中等规模量子（Noisy Intermediate-Scale Quantum, NISQ）时代的典型特征是：量子比特数量在几十到几百之间，门操作保真度有限，无法实现完全量子纠错。在这样的约束下，**变分量子-经典混合架构（Variational Quantum-Classical Hybrid Architecture）** 成为最可行的算法路径。

变分算法的核心思想源于变分法（Variational Method）——这是量子力学中一种强有力的近似方法。变分法指出：对于一个哈密顿量 $\hat{H}$，任意试探态 $|\psi(\boldsymbol{\theta})\rangle$ 的能量期望值一定不小于系统真实的基态能量 $E_0$：

$$
E(\boldsymbol{\theta}) = \frac{\langle\psi(\boldsymbol{\theta})|\hat{H}|\psi(\boldsymbol{\theta})\rangle}{\langle\psi(\boldsymbol{\theta})|\psi(\boldsymbol{\theta})\rangle} \ge E_0
$$

这个不等式被称为**Rayleigh-Ritz变分原理**。它告诉我们：我们可以将寻找基态能量的问题转化为一个**连续优化问题**——不断调整试探态中的参数 $\boldsymbol{\theta}$，使能量期望值 $E(\boldsymbol{\theta})$ 最小化。

> **变分法简史**：Rayleigh（1877年）和Ritz（1908年）分别独立提出了这一原理。它被广泛应用于量子化学中的Hartree-Fock方法，如今成为NISQ量子计算的核心理论基石。

### 5.1.2 混合架构的三大组件

**即时练习 5.1.2**

1. 变分量子-经典混合架构由哪三个组件构成？各自的功能是什么？
2. 为什么这种混合架构适合当前量子硬件？

变分量子-经典混合架构由三个相互配合的组件构成：

```
┌─────────────────────────────────────────────────────────────┐
│                    经典计算机（优化器）                       │
│                                                             │
│           ┌───┐          ┌──────────────┐                   │
│           │ θ │ ───────→ │  优化算法    │                   │
│           └───┘          │ (梯度下降/   │                   │
│                ←──────── │  COBYLA/     │                   │
│            E(θ)          │  SPSA等)     │                   │
│                           └──────────────┘                   │
└─────────────────────────────────────────────────────────────┘
       │                              ▲
       │ 参数 θ                       │ 能量值 E(θ)
       ▼                              │
┌─────────────────────────────────────────────────────────────┐
│                    量子处理器（电路）                         │
│                                                             │
│   |0⟩ ── H ── Rx(θ₁) ── ● ── Rx(θ₃) ── 测量 ────┐        │
│   |0⟩ ── H ── Rx(θ₂) ── ⊕ ── Rx(θ₄) ── 测量 ──┤ E(θ)   │
│                                                             │
│  每个 shot 得到一组比特串，重复 N_shot 次统计期望值          │
└─────────────────────────────────────────────────────────────┘
```

**组件1：量子电路（变分电路）**

量子电路以 $|\boldsymbol{0}\rangle$ 为初态，应用一系列参数化量子门 $U(\boldsymbol{\theta})$，制备参数化量子态 $|\psi(\boldsymbol{\theta})\rangle = U(\boldsymbol{\theta})|\boldsymbol{0}\rangle$。这个电路通常被称为**Ansatz**（试探态电路）。Ansatz的设计是变分算法中最关键的自由度——它决定了算法能探索的量子态空间的广度和深度。

**组件2：哈密顿量测量**

在量子态 $|\psi(\boldsymbol{\theta})\rangle$ 上测量目标哈密顿量 $\hat{H}$ 的期望值。由于 $\hat{H}$ 通常分解为泡利串 $P_k$ 的线性组合：

$$
\hat{H} = \sum_{k} c_k P_k, \quad P_k \in \{I, X, Y, Z\}^{\otimes n}
$$

我们需要对每个泡利串 $P_k$ 分别测量，然后加权求和得到 $E(\boldsymbol{\theta}) = \sum_k c_k \langle P_k \rangle$。每次测量需要 $N_{\text{shot}}$ 次重复采样来获取期望值的统计估计。

**组件3：经典优化器**

经典优化器根据当前参数 $\boldsymbol{\theta}$ 下的能量值 $E(\boldsymbol{\theta})$，决定下一步的参数更新方向，产生新的参数 $\boldsymbol{\theta}'$。优化器的选择极大地影响收敛速度和最终精度。

### 5.1.3 混合架构的优势与代价

**即时练习 5.1.3**

1. 变分量子-经典混合架构的主要优势是什么？
2. 这种架构付出什么代价？

**优势：**

1. **电路深度适中**：变分电路通常采用浅层电路，适合NISQ设备的噪声特性
2. **天生误差容忍**：参数化训练可以在一定程度上补偿系统噪声
3. **问题规模可扩展**：量子部分的复杂性随问题规模多项式增长
4. **通用框架**：同一套架构可应用于量子化学、优化、机器学习等多个领域

**代价：**

1. **统计采样开销**：期望值测量需要大量重复采样（shots），误差按 $O(1/\sqrt{N_{\text{shot}}})$ 衰减
2. **贫瘠高原（Barren Plateau）问题**：在大规模参数化电路中，梯度随系统尺寸指数级衰减，导致优化陷入停滞
3. **经典优化子问题**：参数空间中的能量景观常包含大量局部极小值，经典优化器难以找到全局最优
4. **测量次数与系统规模**：泡利串的数量可能随系统规模平方增长，测量代价可观

### 5.1.4 变分算法的统一形式

**即时练习 5.1.4**

1. 变分量子算法的统一形式 $\min_{\boldsymbol\theta} f(\boldsymbol\theta)$ 中，$f(\boldsymbol\theta)$ 和 $\boldsymbol\theta$ 分别如何定义？
2. VQE、QAOA 和 QNN 在统一框架下有什么区别？

所有变分量子算法可以用一个统一的框架描述。定义：

- **目标函数**：$f(\boldsymbol{\theta})$，由量子电路测量的期望值给出
- **参数化电路**：$U(\boldsymbol{\theta})$，硬件可执行的门序列
- **优化目标**：$\boldsymbol{\theta}^* = \arg\min_{\boldsymbol{\theta}} f(\boldsymbol{\theta})$

根据目标函数和电路结构的不同，衍生出不同的变分算法：

| 算法 | 哈密顿量 | 电路结构 | 应用领域 |
|------|---------|---------|---------|
| VQE | 化学/物理哈密顿量 | 化学启发/硬件高效 | 量子化学 |
| QAOA | 组合优化成本+混合器 | 问题特定 | 组合优化 |
| QNN | 标签相关哈密顿量 | 层级结构 | 量子机器学习 |
| QA | 问题哈密顿量+横场 | 绝热演化 | 优化/模拟 |

本章余下部分将深入VQE和QAOA这两个最重要、最成熟的变分算法。

---

## 5.2 量子化学电子结构问题

### 5.2.1 问题描述：找分子的基态能量

**即时练习 5.2.1**

1. VQE 要解决的核心问题是什么？
2. 分子电子哈密顿量包含哪些项？

量子化学的一个核心问题是：**给定分子构型，求解其电子基态能量**。这个问题在材料设计、药物发现、催化机理研究等领域有广泛的应用。

为什么这个问题重要？分子的物理化学性质——反应活性、光谱、导电性——都由其电子结构决定。基态能量是电子结构最基本的表征量。

从量子力学角度看，一个分子的电子系统由**定态薛定谔方程**描述：

$$
\hat{H}_{\text{mol}} |\Psi\rangle = E |\Psi\rangle
$$

其中 $\hat{H}_{\text{mol}}$ 是分子的**电子哈密顿量**。在玻恩-奥本海默近似下（核固定），电子哈密顿量的 explicit 形式为：

$$
\hat{H}_{\text{mol}} = -\sum_i \frac{\nabla_i^2}{2} - \sum_{i,I} \frac{Z_I}{|\boldsymbol{r}_i - \boldsymbol{R}_I|} + \sum_{i<j} \frac{1}{|\boldsymbol{r}_i - \boldsymbol{r}_j|}
$$

这里的三项分别代表：电子的动能、电子与原子核的库仑吸引势、电子之间的库仑排斥势。$\boldsymbol{r}_i$ 是第 $i$ 个电子的坐标，$\boldsymbol{R}_I$ 和 $Z_I$ 是第 $I$ 个原子核的位置和电荷数。

> **注意**：上式使用原子单位制（Hartree atomic units），其中 $\hbar = m_e = e = 1$。

### 5.2.2 从连续到离散：基组选择

**即时练习 5.2.2**

1. 什么是基组？STO-3G 和 6-31G 的区别是什么？
2. 基组大小如何影响 VQE 所需的量子比特数？

上面的哈密顿量是连续空间中的微分算符，不能直接在量子计算机上处理。我们需要将问题**离散化**。

做法是选择一组**单电子基函数（basis functions）** $\{\phi_p(\boldsymbol{r})\}$，将电子波函数用这些基函数的线性组合展开。这个过程称为**基组展开**：

$$
\psi_i(\boldsymbol{r}) = \sum_{p} C_{ip} \phi_p(\boldsymbol{r})
$$

常用的基组包括：

- **STO-3G**：最小基组，每个原子轨道用3个高斯函数拟合Slater型轨道
- **6-31G**：分裂价基，对价层轨道使用两组基函数
- **cc-pVDZ**：相关一致极化双ζ基组，精度更高

选择基组是一个权衡：基组越大，精度越高，但计算复杂度也越高。在量子化学中，这被称为**完整基组极限（Complete Basis Set Limit）**——当基组无限大时，计算结果趋近真实值。

### 5.2.3 第二量子化形式

**即时练习 5.2.3**

1. 第二量子化中如何表示多电子态？
2. 产生算符和湮灭算符满足什么反对易关系？

第一量子化（坐标空间）处理多电子系统时，波函数必须是反对称的（Pauli不相容原理），这给表示带来极大不便。**第二量子化**将问题转化为占据数表示，天然满足反对称性。

在第二量子化中，定义产生算符 $a_p^\dagger$ 和湮灭算符 $a_p$：

- $a_p^\dagger |0\rangle = |1_p\rangle$：在轨道 $p$ 上产生一个电子
- $a_p |1_p\rangle = |0_p\rangle$：在轨道 $p$ 上湮灭一个电子
- 反对称性通过**反对易关系**保证：

$$
\{a_p, a_q^\dagger\} = a_p a_q^\dagger + a_q^\dagger a_p = \delta_{pq}
$$

$$
\{a_p, a_q\} = \{a_p^\dagger, a_q^\dagger\} = 0
$$

在第二量子化下，分子哈密顿量写为：

$$
\hat{H} = \sum_{p,q} h_{pq} a_p^\dagger a_q + \frac{1}{2} \sum_{p,q,r,s} h_{pqrs} a_p^\dagger a_q^\dagger a_r a_s
$$

其中**单电子积分**和**双电子积分**为：

$$
h_{pq} = \int \phi_p^*(\boldsymbol{r}) \left( -\frac{\nabla^2}{2} - \sum_I \frac{Z_I}{|\boldsymbol{r} - \boldsymbol{R}_I|} \right) \phi_q(\boldsymbol{r}) \, d\boldsymbol{r}
$$

$$
h_{pqrs} = \int \frac{\phi_p^*(\boldsymbol{r}_1) \phi_q^*(\boldsymbol{r}_2) \phi_r(\boldsymbol{r}_2) \phi_s(\boldsymbol{r}_1)}{|\boldsymbol{r}_1 - \boldsymbol{r}_2|} \, d\boldsymbol{r}_1 d\boldsymbol{r}_2
$$

这些积分类似于量子化学的"元数据"——在经典计算机上预先计算出 $h_{pq}$ 和 $h_{pqrs}$ 后，剩下的量子计算任务就是求解该哈密顿量的基态能量。

### 5.2.4 问题规模

**即时练习 5.2.4**

1. 什么是化学精度？它的数值是多少 Hartree？
2. 为什么 VQE 的测量次数正比于 $O(N^4)$？

对于一个有 $N_e$ 个电子、$M$ 个基函数的分子体系：

- 谱（spin）轨道数量：$N_{\text{SO}} = 2M$（每个空间轨道有自旋上、下两个轨道）
- 哈密顿量中的项数：单电子项 $O(N_{\text{SO}}^2)$，双电子项 $O(N_{\text{SO}}^4)$
- 在经典计算机上，完整对角化（全组态相互作用，FCI）的计算复杂度：$O(N_{\text{SO}}!)$

举例：水分子（H₂O）使用cc-pVDZ基组时，$M=24$，$N_{\text{SO}}=48$，FCI需要处理 $C_{48}^{10} \approx 6.5 \times 10^9$ 个行列式——已经远超经典能力。但量子计算机上，只需要 $\lceil \log_2 C_{48}^{10} \rceil \approx 33$ 个量子比特即可表示这个空间。

> **量子优势的来源**：量子比特的叠加性质使得 $n$ 个量子比特可以表示 $2^n$ 维的Hilbert空间，而经典存储只能按指数增长。这是量子模拟指数加速的根本原因。

然而，33个量子比特虽少，物理实现却不容易——尤其是我们需要在这些量子比特上实现高保真度的化学精度计算。这引出了VQE的必要性。

---

## 5.3 费米子-量子比特映射

### 5.3.1 为什么需要映射？

**即时练习 5.3.1**

1. 为什么费米子算符不能直接在量子计算机上实现？
2. 映射的核心目标是什么？

第二量子化哈密顿量是用费米子算符 $a_p^\dagger, a_p$ 表示的，它们遵循反对易关系。但我们的量子计算机使用量子比特（qubits），遵循的是**泡利算符** $X, Y, Z$ 的代数。

费米子算符与泡利算符的区别在于：

| 性质 | 费米子算符 $a_p^\dagger$ | 泡利算符 $Z_p$ |
|------|------------------------|----------------|
| 代数类型 | Grassmann | Clifford |
| 反对易性 | $\{a_p^\dagger, a_q\} = \delta_{pq}$ | $\{Z_p, Z_q\} = 2\delta_{pq}Z_p$ |
| 平方 | $(a_p^\dagger)^2 = 0$ | $Z_p^2 = I$ |

我们需要一个**同态映射**：将费米子算符的对易关系忠实映射到泡利算符空间，同时保持代数结构不变。这个映射 $f$ 必须满足：

$$
\{a_p, a_q^\dagger\} = \delta_{pq} \Rightarrow \{f(a_p), f(a_q^\dagger)\} = \delta_{pq}
$$

### 5.3.2 Jordan-Wigner 映射

**即时练习 5.3.2**

1. Jordan-Wigner 映射中，$Z$ 串（Jordan-Wigner string）的作用是什么？
2. JW 映射的优缺点分别是什么？

Jordan-Wigner（JW）映射是最直观、最经典的费米子-量子比特映射方法。Eugene Wigner和Pascual Jordan于1928年提出。

**核心思想**：将每个费米子轨道 $p$ 分配给一个量子比特 $p$。费米子算符的反对易关系通过**奇偶性（parity）** 字符串实现：

$$
a_p^\dagger \rightarrow \frac{1}{2} (X_p - i Y_p) \otimes Z_{p-1} \otimes Z_{p-2} \otimes \cdots \otimes Z_0
$$

$$
a_p \rightarrow \frac{1}{2} (X_p + i Y_p) \otimes Z_{p-1} \otimes Z_{p-2} \otimes \cdots \otimes Z_0
$$

或者用更符号化的写法：

$$
a_p^\dagger = (X_p - i Y_p) \otimes \bigotimes_{j=0}^{p-1} Z_j
$$

$$
a_p = (X_p + i Y_p) \otimes \bigotimes_{j=0}^{p-1} Z_j
$$

其中的 $Z$ 字符串称为**Jordan-Wigner 串（JW string）**。它的作用是确保不同轨道算符之间的反对易关系。

**为什么需要 Z 字符串？** 考虑两个费米子算符 $a_p^\dagger$ 和 $a_q^\dagger$（$p < q$）。没有 $Z$ 字符串时，它们直接不对易；有了 $Z$ 字符串，$Z_p$ 与 $X_q$ 的反对易性提供了正确的代数结构。

**示例**：水分子（STO-3G基组，7个空间轨道，14个自旋轨道）的哈密顿量经过JW映射后，得到包含300多个泡利串的和式。每个泡利串涉及从1到14个不等的 $X, Y, Z$。

**JW映射的优缺点：**

- **优点**：概念简单，实现直观，轨道-量子比特一一对应
- **缺点**：泡利串长度线性增长 $O(N_{\text{SO}})$，导致长程相互作用在电路上需要大量CNOT门

### 5.3.3 Bravyi-Kitaev 映射

**即时练习 5.3.3**

1. Bravyi-Kitaev 映射相比 Jordan-Wigner 有什么改进？
2. BK 映射的编码方案复杂度是多少？

Bravyi-Kitaev（BK）映射是为克服JW映射长串问题而设计的。它由Sergey Bravyi和Alexei Kitaev于2002年提出。

**核心思想**：不再让一个量子比特代表一个轨道，而是让量子比特编码**轨道占据数的奇偶性信息**。具体而言，BK映射将费米子算符表示为：

$$
a_p^\dagger \rightarrow \frac{1}{2} \left( X_{b(p)} \tilde{U}_p - i Y_{b(p)} \tilde{V}_p \right)
$$

$$
a_p \rightarrow \frac{1}{2} \left( X_{b(p)} \tilde{U}_p + i Y_{b(p)} \tilde{V}_p \right)
$$

其中 $b(p)$ 是某种二分树结构中 $p$ 的最高位比特位置，$\tilde{U}_p$ 和 $\tilde{V}_p$ 是作用在部分量子比特上的泡利串。

BK映射的核心是**二分树结构**。设轨道数为 $2^k$，递归地将轨道分为两半，每个节点存储其子树中占据数的奇偶性。这样，量子比特数与轨道数相同（$N_{\text{SO}}$），但每个泡利串的长度从 $O(N_{\text{SO}})$ 降低到 $O(\log N_{\text{SO}})$。

**BK映射的优缺点：**

- **优点**：泡利串长度对数增长 $O(\log N_{\text{SO}})$，短程相互作用更高效
- **缺点**：映射规则复杂，需要在二分树上进行一系列变换

### 5.3.4 映射方法对比

**即时练习 5.3.4**

1. 对比 JW 和 BK 映射的量子比特数和泡利权重。
2. 在实际的 VQE 实验中，如何选择映射方案？

| 性质 | Jordan-Wigner | Bravyi-Kitaev | 其他变体 |
|------|--------------|---------------|----------|
| 泡利串最大长度 | $O(N)$ | $O(\log N)$ | $O(1)$（三元树） |
| 单粒子哈密顿量项数 | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ |
| 双粒子哈密顿量项数 | $O(N^4)$ | $O(N^4)$ | $O(N^4)$ |
| 实现复杂性 | 低 | 中 | 高 |
| 映射后CNOT数量 | 高（长串） | 中 | 低 |

> **选择建议**：对于小分子（少于20个量子比特），JW映射足够用且易于实现。对于更大规模的模拟，BK映射或更先进的Ternary Tree映射可节省大量CNOT门。

近年来还出现了**分段对偶映射（Segmented Parity Mapping）** 和**三元树映射（Ternary Tree Mapping）** 等新方案，它们将泡利串长度压缩到 $O(1)$，适合特定硬件拓扑结构。

### 5.3.5 映射后的哈密顿量

映射完成后，分子哈密顿量从费米子形式转换为泡利形式：

$$
\hat{H}_{\text{mol}} = \sum_{\alpha} h_{\alpha} P_{\alpha}, \quad P_{\alpha} \in \{I, X, Y, Z\}^{\otimes n}
$$

其中 $h_{\alpha}$ 是从单电子和双电子积分通过映射规则计算出的系数。这个形式可以直接在量子计算机上测量。

**示例**：氢分子（H₂）在STO-3G基组下，经过JW映射后的哈密顿量为：

$$
\hat{H} = h_0 I + h_1 Z_0 + h_2 Z_1 + h_3 Z_2 + h_4 Z_3 + h_5 Z_0 Z_1 + h_6 Z_0 Z_2 + h_7 Z_0 Z_3 + h_8 Z_1 Z_2 + h_9 Z_1 Z_3 + h_{10} Z_2 Z_3 + h_{11} X_0 X_1 Y_2 Y_3 + h_{12} X_0 Y_1 Y_2 X_3 + h_{13} Y_0 X_1 X_2 Y_3 + h_{14} Y_0 Y_1 X_2 X_3
$$

这个哈密顿量只包含 $Z$ 和 $XXYY$ 类型的泡利串。在更复杂的分子中，还会出现 $X, Y, Z$ 混合的更长串。

---

## 5.4 VQE算法流程

### 5.4.1 算法总览

**即时练习 5.4.1**

1. VQE 算法的完整流程包含哪些主要步骤？
2. 量子计算机和经典计算机在 VQE 中各负责什么？

变分量子本征值求解器（Variational Quantum Eigensolver, VQE）由Peruzzo等人于2014年提出，是NISQ时代最具代表性的量子-经典混合算法。

VQE的完整流程如下：

```
输入：分子几何结构、基组选择
         │
         ▼
    ┌──────────────────┐
    │ 步骤1：计算积分    │  ←── 经典计算机
    │ h_pq, h_pqrs      │      (预先计算)
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │ 步骤2：费米子→量子│  ←── 经典计算机
    │ 比特映射(第5.3节)│      (JW/BK映射)
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │ 步骤3：选择Ansatz │  ←── 经典设计
    │ U(θ)             │      (第5.5节)
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐      ┌──────────────────┐
    │ 步骤4：制备试探态 │ ──→  │ 步骤5：测量哈密 │
    │ |ψ(θ)⟩=U(θ)|0⟩   │      │ 顿量⟨H⟩(第5.6节)│
    └──────────────────┘      └────────┬─────────┘
             │                          │
             │                          ▼
             │                 ┌──────────────────┐
             │                 │ 步骤6：经典优化  │
             │                 │ θ ← θ - η∇E(θ)  │
             │                 └────────┬─────────┘
             │                          │
             └──────────────────────────┘
                  循环直到收敛
                           │
                           ▼
    ┌──────────────────┐
    │ 输出：基态能量    │
    │ E_min ≈ E_0      │
    └──────────────────┘
```

### 5.4.2 步骤详解

**即时练习 5.4.2**

1. VQE 算法的主要步骤有哪些？简述每一步的功能。
2. 在 VQE 中，哈密顿量的期望值如何通过测量获得？

**步骤1-2：积分计算与映射**（已在5.2和5.3节介绍）

**步骤3：选择Ansatz**

Ansatz是参数化量子电路 $U(\boldsymbol{\theta})$，其输出态 $|\psi(\boldsymbol{\theta})\rangle = U(\boldsymbol{\theta})|\boldsymbol{0}\rangle$ 覆盖了Hilbert空间中可能包含基态的子空间。Ansatz的设计直接影响算法的精度和效率（见第5.5节）。

**步骤4：制备试探态**

在量子处理器上执行电路 $U(\boldsymbol{\theta})$，从 $|\boldsymbol{0}\rangle$ 制备出试探态。这一步是典型的量子态制备过程。

**步骤5：测量哈密顿量**

对试探态测量哈密顿量的期望值。由于不能直接测量 $\hat{H}$，需要将 $\hat{H}$ 分解为泡利串的和：

$$
E(\boldsymbol{\theta}) = \langle \hat{H} \rangle = \sum_{\alpha} h_{\alpha} \langle P_{\alpha} \rangle
$$

对每个泡利串 $P_{\alpha}$，需要 $N_{\text{shot}}$ 次测量来获得统计平均值。总测量次数为：

$$
N_{\text{total}} = N_{\text{shot}} \times (\text{泡利串数量})
$$

**步骤6：经典优化**

将测量的能量值 $E(\boldsymbol{\theta})$ 传递给经典优化器，更新参数 $\boldsymbol{\theta}$。优化过程持续迭代直到收敛标准满足（如能量变化小于阈值 $\epsilon$）。

### 5.4.3 能量梯度计算

在经典优化中，梯度信息 $\nabla_{\boldsymbol{\theta}} E(\boldsymbol{\theta})$ 对高效收敛至关重要。VQE中计算梯度有两种主要方法：

**方法1：有限差分法（Finite Difference）**

直接使用数值近似：

$$
\frac{\partial E}{\partial \theta_i} \approx \frac{E(\theta_i + \delta) - E(\theta_i - \delta)}{2\delta}
$$

- 优点：无需修改电路结构
- 缺点：受统计噪声影响大，需要大量采样

**方法2：参数偏移规则（Parameter Shift Rule）**

对于电路由 $e^{-i\theta G/2}$（其中 $G^2 = I$）形式的门构成，梯度可以精确计算为：

$$
\frac{\partial E}{\partial \theta_i} = \frac{E(\theta_i + \pi/2) - E(\theta_i - \pi/2)}{2}
$$

这个公式在统计意义上比有限差分更稳定，因为两个测量值的差直接给出梯度，不受离散化误差影响。

**参数偏移规则的证明**（简要）：

设 $U(\theta) = e^{-i\theta G/2}$ 且 $G^2 = I$。那么：

$$
U(\theta) = \cos(\theta/2) I - i \sin(\theta/2) G
$$

因此：

$$
E(\theta) = \langle \psi | U^\dagger(\theta) \hat{H} U(\theta) | \psi \rangle
$$

对 $\theta$ 求导，利用三角恒等式可得上述偏移公式。

### 5.4.4 VQE的收敛判据

VQE的收敛通常基于以下一种或多种条件：

1. **能量变化**：$|E(\boldsymbol{\theta}_{k+1}) - E(\boldsymbol{\theta}_k)| < \epsilon_1$
2. **梯度范数**：$\|\nabla_{\boldsymbol{\theta}} E(\boldsymbol{\theta}_k)\| < \epsilon_2$
3. **参数变化**：$\|\boldsymbol{\theta}_{k+1} - \boldsymbol{\theta}_k\| < \epsilon_3$
4. **迭代次数**：达到预设的最大迭代次数 $K_{\max}$

在量子化学应用中，通常要求能量精度达到**化学精度（chemical accuracy）**，即与精确值的误差小于 $1.6 \times 10^{-3}$ Hartree（约1 kcal/mol）。这个精度标准源于热化学实验的典型精度要求。

### 5.4.5 VQE的计算复杂度分析

VQE的计算复杂度可以从以下几个维度分析：

| 环节 | 复杂度 | 说明 |
|------|--------|------|
| 哈密顿量项数 | $O(N^4)$ | 双电子积分导致 |
| 每迭代测量次数 | $O(N_{\text{terms}} \times N_{\text{shot}})$ | 通常 $N_{\text{shot}} \sim 10^4$-$10^6$ |
| Ansatz电路深度 | $O(poly(N))$ | 取决于Ansatz设计 |
| 优化迭代次数 | $O(poly(N))$ | 取决于能量景观 |
| 总时间复杂度 | $O(N^4 \times N_{\text{shot}} \times N_{\text{iter}})$ | 远优于经典FCI的指数级 |

值得注意的是，VQE是一个**启发式算法**——没有严格的收敛保证。但在实践中，精心设计的Ansatz和优化器通常能在合理时间内达到化学精度。

---

## 5.5 参数化量子电路Ansatz

### 5.5.1 Ansatz设计的两难

Ansatz作为变分算法的核心，面临一个根本性的两难：

- **表达能力（Expressibility）**：Ansatz能够探索的Hilbert空间越大，就越有可能包含基态。但过大的空间会导致优化困难。
- **可训练性（Trainability）**：参数越少、电路越浅，优化越容易，但可能无法达到所需精度。

这被称为**表达-训练权衡（Expressibility-Trainability Trade-off）**。好的Ansatz设计需要在两者之间找到平衡。

Ansatz的设计哲学分为两大阵营：

1. **硬件高效Ansatz（Hardware-Efficient Ansatz, HEA）**：优先考虑硬件可实现性，使用本机门集合
2. **化学启发Ansatz（Chemically-Inspired Ansatz）**：优先考虑物理准确性，使用化学知识约束电路结构

### 5.5.2 硬件高效Ansatz（HEA）

硬件高效Ansatz由Kandala等人于2017年在IBM的实验中提出。其设计理念是：**使用硬件原生支持的门集合，使电路深度最小化**。

**基本结构**：

HEA通常由 $L$ 层（layers）构成，每层包含：

1. **单量子比特旋转层**：每个量子比特上应用 $R_y(\theta_i)$ 和/或 $R_z(\phi_i)$ 门
2. **纠缠层**：应用受控门（通常是CNOT或CZ）在相邻量子比特之间产生纠缠

单层HEA的结构：

```
     R_z(θ₁) ── R_y(φ₁) ── ● ────────────────────
                           │
     R_z(θ₂) ── R_y(φ₂) ── ⊕ ── ● ──────────────
                                 │
     R_z(θ₃) ── R_y(φ₃) ──────── ⊕ ── ● ────────
                                       │
     R_z(θ₄) ── R_y(φ₄) ────────────── ⊕ ── ● ──
                                             │
     R_z(θ₅) ── R_y(φ₅) ──────────────────── ⊕
```

**数学形式**：

$$
U_{\text{HEA}}(\boldsymbol{\theta}) = \prod_{l=1}^{L} \left( \bigotimes_{i=1}^{n} R_{z_i}(\theta_{i,l}^{(1)}) R_{y_i}(\theta_{i,l}^{(2)}) \right) U_{\text{ent}}
$$

其中 $U_{\text{ent}}$ 是纠缠层，通常使用线性链拓扑的CNOT梯子：

$$
U_{\text{ent}} = \prod_{i=1}^{n-1} \text{CNOT}_{i,i+1}
$$

**优点**：
- 电路深度浅，适合NISQ硬件
- 天然适应硬件拓扑（最近邻连接）
- 参数数量可调（通过调整层数 $L$）

**缺点**：
- 没有任何物理化学的先验知识，可能需要更多层才能达到化学精度
- 随系统规模增大，梯度消失问题（贫瘠高原）更严重
- 参数数量随 $n$ 和 $L$ 线性增长，但Hilbert空间指数增长，表达能力相对有限

**变体**：可通过改变纠缠模式获得不同拓扑，例如使用环形（ring）连接替代线性连接，增强纠缠能力。

### 5.5.3 UCC Ansatz（耦合簇Ansatz）

耦合簇（Coupled Cluster, CC）理论是量子化学中最成功的经典方法之一。它提供了一种高效描述电子关联的方式。UCC（Unitary Coupled Cluster）将其改造为幺正形式，使其可以在量子计算机上实现。

**经典耦合簇理论**：

经典CC的基态波函数为：

$$
|\Psi_{\text{CC}}\rangle = e^{\hat{T}} |\Psi_{\text{HF}}\rangle
$$

其中 $\hat{T}$ 是簇算符（cluster operator），$|\Psi_{\text{HF}}\rangle$ 是Hartree-Fock参考态。$\hat{T}$ 包含单激发、双激发等高阶激发：

$$
\hat{T} = \hat{T}_1 + \hat{T}_2 + \hat{T}_3 + \cdots
$$

$$
\hat{T}_1 = \sum_{i,\alpha} t_i^{\alpha} a_\alpha^\dagger a_i
$$

$$
\hat{T}_2 = \sum_{i,j,\alpha,\beta} t_{ij}^{\alpha\beta} a_\alpha^\dagger a_\beta^\dagger a_j a_i
$$

其中 $i,j$ 标记占据轨道（occupied），$\alpha,\beta$ 标记虚轨道（virtual）。

**UCC的幺正形式**：

经典CC的 $e^{\hat{T}}$ 不是幺正算符（因为 $\hat{T}$ 不是反厄米的）。UCC将其替换为幺正指数形式：

$$
|\Psi_{\text{UCC}}\rangle = e^{\hat{T} - \hat{T}^\dagger} |\Psi_{\text{HF}}\rangle
$$

定义 $\hat{\sigma} = \hat{T} - \hat{T}^\dagger$，则 $\hat{\sigma}$ 是反厄米算符，$e^{\hat{\sigma}}$ 是幺正算符。

最常用的UCCSD（UCC with Singles and Doubles）形式只保留单激发和双激发：

$$
\hat{\sigma} = \sum_{i,\alpha} \theta_i^{\alpha} (a_\alpha^\dagger a_i - a_i^\dagger a_\alpha) + \sum_{i<j,\alpha<\beta} \theta_{ij}^{\alpha\beta} (a_\alpha^\dagger a_\beta^\dagger a_j a_i - a_i^\dagger a_j^\dagger a_\beta a_\alpha)
$$

**从UCC到量子电路**：

UCC算符 $e^{\hat{\sigma}}$ 不能直接在量子计算机上实现。需要将 $\hat{\sigma}$ 分解为若干对易或非对易的子项，然后用Trotter分解近似：

$$
e^{\hat{\sigma}} \approx \prod_{k} e^{\hat{\sigma}_k}
$$

每个子指数 $e^{\hat{\sigma}_k}$ 经过费米子-量子比特映射后，可以编译为一系列单比特门和CNOT门的组合。

**UCCSD示例**（氢分子）：

对于H₂分子（2个电子，4个自旋轨道），UCCSD Ansatz包含：

- 单激发项：$e^{\theta_1 (a_2^\dagger a_0 - a_0^\dagger a_2)}$ 和 $e^{\theta_2 (a_3^\dagger a_1 - a_1^\dagger a_3)}$
- 双激发项：$e^{\theta_3 (a_2^\dagger a_3^\dagger a_1 a_0 - a_0^\dagger a_1^\dagger a_3 a_2)}$

经过JW映射后，每个指数项转化为包含多个CNOT门的泡利旋转门。总的CNOT数量约为几十到一百。

**优点**：
- 物理化学先验知识（参考态 + 激发模式）
- 使用较少参数即可达到高精度
- 对中等关联体系，UCCSD即可达到化学精度

**缺点**：
- 电路深度很大（尤其是双激发项导致大量CNOT）
- 需要Hartree-Fock预计算（经典预处理）
- 对于强关联体系（如过渡金属化合物），UCCSD仍不够

### 5.5.4 Ansatz对比与选择

| 特性 | 硬件高效（HEA） | UCCSD | 自适应（ADAPT-VQE） |
|------|---------------|-------|-------------------|
| 参数数量 | $O(nL)$ | $O(n^2 m^2)$ | 自适应增长 |
| 电路深度 | 浅 | 深 | 中等 |
| 物理先验 | 无 | 有（HF参考） | 有（梯度选择） |
| 化学精度 | 需要多层 | 通常是 | 可达 |
| 贫瘠高原 | 严重 | 中等 | 自适应缓解 |
| 实现难度 | 简单 | 中等 | 高 |
| 适用硬件 | 所有 | 低噪声设备 | 低噪声设备 |

> **选择建议**：
> - **实验中快速验证**：HEA，简单粗暴
> - **小分子高精度**：UCCSD，经典量子化学标准
> - **强关联体系**：ADAPT-VQE或其它自适应方法
> - **超导硬件的近期实验**：HEA加逐层训练

### 5.5.5 ADAPT-VQE简介

ADAPT-VQE（Adaptive Derivative-Assembled Pseudo-Trotter VQE）是由Grimsley等人于2019年提出的自适应Ansatz构建方法。其核心思想是：**不预先固定Ansatz结构，而是在优化过程中逐步添加算子**。

算法流程：

1. 从Hartree-Fock参考态开始（或HEA初始化）
2. 计算当前态对所有候选算子的梯度 $\partial E / \partial \theta_k$
3. 选择梯度最大的算子添加到Ansatz中
4. 重新优化所有参数
5. 重复直到收敛

ADAPT-VQE的优势在于：它用尽可能少的算子达到目标精度，自动适应问题的纠缠结构。但其多层迭代优化的计算开销也相应较大。

---

## 5.6 泡利串并行测量策略

### 5.6.1 测量的基本问题

**即时练习 5.6.1**

1. 为什么 VQE 中不能直接"读取"能量期望值？
2. 泡利串并行测量的核心思想是什么？

在VQE的每一次迭代中，我们需要测量哈密顿量在每个试探态上的期望值：

$$
E(\boldsymbol{\theta}) = \sum_{k=1}^{N_{\text{term}}} c_k \langle \psi(\boldsymbol{\theta}) | P_k | \psi(\boldsymbol{\theta}) \rangle
$$

其中 $P_k$ 是泡利串（如 $Z_0 Z_1 X_2 Y_3$）。

一个天真的方案是：对每个泡利串 $P_k$ 分别执行一次量子电路并测量 $N_{\text{shot}}$ 次。这将导致总测量次数为 $N_{\text{term}} \times N_{\text{shot}}$。对于大分子，$N_{\text{term}} \sim O(N^4)$，这个代价是难以接受的。

**并行测量的核心思想**：如果两个泡利算符对易，它们可以在同一个电路中同时测量。这样可以将 $N_{\text{term}}$ 个项分组为 $N_{\text{group}}$ 个可同时测量的组。

### 5.6.2 对易性与可同时测量

**即时练习 5.6.2**

1. 两个泡利串 $P_i$ 和 $P_j$ 对易的条件是什么？
2. 举例说明哪些泡利串可以同时测量，哪些不能。

两个泡利串 $P_i$ 和 $P_j$**对易**当且仅当它们在每个量子比特位上的泡利算符要么相同，要么至少一个是 $I$：

$$
[P_i, P_j] = 0 \iff \forall q: P_i^{(q)} = P_j^{(q)} \text{ 或 } P_i^{(q)} = I \text{ 或 } P_j^{(q)} = I
$$

当两个泡利串满足这个条件时，它们共享一组本征态，可以在同一个基下测量。

**示例**：

- $Z_0 Z_1$ 与 $Z_0 I$ 对易 → 可同时测量（都测量在 $Z$ 基）
- $Z_0 Z_1$ 与 $X_0 X_1$ 不对易 → 需要分别测量
- $Z_0 I$ 与 $I Z_1$ 对易 → 可同时测量

### 5.6.3 测量分组策略

**即时练习 5.6.3**

1. 测量分组问题如何转化为图着色问题？
2. 贪心着色算法的基本步骤是什么？

将 $N_{\text{term}}$ 个泡利串划分为尽可能少的可同时测量组，构成一个**图着色问题**：

- 将每个泡利串视为图的一个顶点
- 如果两个泡利串不对易，则在它们之间连一条边
- 用最少的颜色给顶点着色，使得相邻顶点颜色不同
- 同色的一组泡利串可以同时测量

**贪心着色算法**：

```
输入：泡利串集合 {P_1, P_2, ..., P_M}
输出：组划分 {G_1, G_2, ..., G_K}

1. 排序泡利串（按长度或系数大小）
2. 初始化 K = 0
3. 对每个泡利串 P_i：
   a. 遍历已有组 G_1...G_K
   b. 如果 P_i 与组内所有成员对易，加入该组
   c. 如果找不到，创建新组 G_{K+1}，将 P_i 加入
4. 返回划分
```

优化版策略还包括：

- **最小团覆盖**：精确求解NP难，但小规模可用整数规划
- **系数阈值分组**：将系数小于阈值的项合并处理
- **度数排序**：优先处理连接最多的节点

### 5.6.4 基变换电路

**即时练习 5.6.4**

1. 测量 $X_q$ 前需要施加什么基变换门？
2. 测量 $Y_q$ 前需要施加什么基变换门？

当泡利串包含 $X$ 和 $Y$ 算符时，我们需要在测量前施加基变换门，将 $X$ 和 $Y$ 转化为标准 $Z$ 基测量。

变换规则：

- 测量 $X_q$ 前：施加 $H_q$（Hadamard门），将 $X$ 变为 $Z$
- 测量 $Y_q$ 前：施加 $S_q^\dagger$ 后接 $H_q$，将 $Y$ 变为 $Z$

具体来说，对于测量基变换：

$$
H X H^\dagger = Z, \quad H S Y S^\dagger H^\dagger = Z
$$

因此，如果一个组包含泡利串 $Z_0 X_1 Y_2$，则需要在该组测量前施加 $H_1$ 和 $S_2^\dagger H_2$。

### 5.6.5 测量采样与方差

**即时练习 5.6.5**

1. 能量方差 $\text{Var}[E]$ 的表达式是什么？
2. 有哪些方差缩减策略？

对于每个组的测量，重复 $N_{\text{shot}}$ 次，得到每个泡利串的期望值 $\langle P_k \rangle$ 及其方差：

$$
\text{Var}[\langle P_k \rangle] = \frac{1 - \langle P_k \rangle^2}{N_{\text{shot}}}
$$

哈密顿量总能量的方差为各组测量方差的加权和：

$$
\text{Var}[E] = \sum_{k} c_k^2 \frac{1 - \langle P_k \rangle^2}{N_{\text{shot}}^{(k)}}
$$

要达到目标精度 $\epsilon$ 所需的总测量次数正比于：

$$
N_{\text{total}} \propto \frac{\left( \sum_k |c_k| \right)^2}{\epsilon^2}
$$

**方差缩减策略**：

1. **局部测量（Commuting Groups）**：利用对易性减少组数
2. **系数感知采样（Coefficient-Aware Sampling）**：对系数大的泡利串分配更多shots
3. **迭代方差缩减**：前几轮用少量shots预估计，后续优化分配

---

## 5.7 经典优化器选择

### 5.7.1 VQE优化问题的特点

**即时练习 5.7.1**

1. VQE 优化问题有哪些独特特点？
2. 为什么不能直接套用深度学习中的大批量 Adam 优化器？

VQE中的优化问题具有不同于标准监督学习的独特特点：

1. **噪声梯度**：梯度通过量子测量获得，包含统计误差，不是精确的
2. **非凸能量景观**：参数空间中的能量函数包含大量局部极小和鞍点
3. **测量成本高昂**：每次函数求值都需要运行量子电路
4. **无显式梯度公式**：梯度需要额外电路（参数偏移）或数值近似
5. **函数值可达但不可解析**：可以直接测量 $E(\boldsymbol{\theta})$，但没有闭式表达式

这些特点决定了不能简单套用深度学习中的大批量Adam等优化器。

### 5.7.2 梯度类优化器

**即时练习 5.7.2**

1. SPSA 优化器如何估计梯度？每次迭代需要多少次函数求值？
2. SPSA 和 Adam 在 VQE 中的优缺点分别是什么？

**（1）SPSA（Simultaneous Perturbation Stochastic Approximation）**

SPSA是VQE中最常用的梯度类优化器之一。它在每次迭代中只测量两次函数值即可估计梯度：

$$
g_i^{(k)} = \frac{E(\boldsymbol{\theta}^{(k)} + \epsilon\boldsymbol{\Delta}^{(k)}) - E(\boldsymbol{\theta}^{(k)} - \epsilon\boldsymbol{\Delta}^{(k)})}{2\epsilon \Delta_i^{(k)}}
$$

其中 $\boldsymbol{\Delta}^{(k)}$ 是服从Rademacher分布的随机扰动向量（每个分量 $\pm 1$ 等概率）。

参数更新：

$$
\boldsymbol{\theta}^{(k+1)} = \boldsymbol{\theta}^{(k)} - \eta_k g^{(k)}
$$

**优点**：
- 每次迭代只需2次函数求值（不随参数数量增加）
- 天然抗噪声
- 无梯度消失问题

**缺点**：
- 收敛慢（亚线性）
- 对步长序列 $\eta_k$ 敏感

**SPSA参数建议**：

$$
\eta_k = \frac{a}{(A + k + 1)^\alpha}, \quad \epsilon_k = \frac{c}{(k + 1)^\gamma}
$$

典型值：$\alpha = 0.602, \gamma = 0.101, a$ 和 $c$ 需要调参。

**（2）Adam（自适应矩估计）**

标准Adam可以应用于VQE，但需要对梯度做额外处理——因为VQE的梯度是噪声的：

$$
m_k = \beta_1 m_{k-1} + (1 - \beta_1) g_k
$$

$$
v_k = \beta_2 v_{k-1} + (1 - \beta_2) g_k^2
$$

$$
\hat{m}_k = \frac{m_k}{1 - \beta_1^k}, \quad \hat{v}_k = \frac{v_k}{1 - \beta_2^k}
$$

$$
\theta^{(k+1)} = \theta^{(k)} - \eta \frac{\hat{m}_k}{\sqrt{\hat{v}_k} + \delta}
$$

**优点**：
- 自适应步长，易于使用
- 对超参数不太敏感

**缺点**：
- 需要完整梯度向量（参数数量次求值）
- 在大参数场景中测量成本高

### 5.7.3 无梯度优化器

**即时练习 5.7.3**

1. COBYLA 和 Nelder-Mead 优化器各有什么特点？
2. 什么情况下应该选择无梯度优化器？

**（1）COBYLA（Constrained Optimization BY Linear Approximations）**

COBYLA是一种无梯度优化方法，通过线性插值逼近目标函数，在约束区域内寻找最优点。

**优点**：
- 完全无梯度，不需要参数偏移电路
- 适用于强噪声环境

**缺点**：
- 参数数量多时收敛极慢
- 不支持大规模参数空间

**（2）Nelder-Mead（单纯形法）**

Nelder-Mead使用 $n+1$ 个顶点构成的单纯形，通过反射、扩张、收缩操作探索参数空间。

**优点**：
- 简单稳定，不需要梯度
- 对于小参数数量的问题效果好

**缺点**：
- 参数数量 $> 10$ 时效率急剧下降
- 可能收敛到非驻点

### 5.7.4 优化器对比

**即时练习 5.7.4**

1. 参数 ≤ 20 时推荐使用什么优化器？为什么？
2. 大规模 VQE 中常用的优化器是什么？

| 优化器 | 每迭代测量次数 | 支持噪声 | 收敛速度 | 参数量扩展 | 常用场景 |
|-------|--------------|---------|---------|-----------|---------|
| SPSA | 2 | 优秀 | 中 | 优秀 | 大规模VQE |
| Adam | $2n$（参数偏移） | 良好 | 快 | 差 | 中等规模 |
| COBYLA | 1 | 好 | 慢 | 差 | 小参数，强噪声 |
| Nelder-Mead | $n+1$ | 好 | 慢 | 差 | 小参数 |
| NGD | $2n$ | 良好 | 快 | 差 | 精确梯度可用 |
| BFGS | $2n$ | 差 | 快 | 中 | 低噪声环境 |

> **经验法则**：
> - 参数 $\le 20$：COBYLA或Nelder-Mead，简单直接
> - 参数 $20 \sim 100$：SPSA，兼顾效率和鲁棒性
> - 参数 $> 100$：SPSA + 逐层训练策略
> - 可用量子自然梯度（Quantum Natural Gradient, QNG）时：优先使用，收敛最快

### 5.7.5 量子自然梯度（QNG）

**即时练习 5.7.5**

1. 量子自然梯度相比标准梯度下降有什么优势？
2. QNG 的主要缺点是什么？

量子自然梯度是经典自然梯度在量子场景中的推广。它考虑参数空间的**几何结构**，使用Fubini-Study度规（量子Fisher信息矩阵）来修正梯度方向：

$$
g(\boldsymbol{\theta})_{\text{QNG}} = F^{-1}(\boldsymbol{\theta}) \cdot \nabla E(\boldsymbol{\theta})
$$

其中 $F(\boldsymbol{\theta})$ 是量子Fisher信息矩阵：

$$
F_{ij}(\boldsymbol{\theta}) = 4 \operatorname{Re} \left[ \langle \partial_i \psi(\boldsymbol{\theta}) | \partial_j \psi(\boldsymbol{\theta}) \rangle - \langle \partial_i \psi(\boldsymbol{\theta}) | \psi(\boldsymbol{\theta}) \rangle \langle \psi(\boldsymbol{\theta}) | \partial_j \psi(\boldsymbol{\theta}) \rangle \right]
$$

**优点**：
- 收敛速度显著快于梯度下降（尤其是接近极小值时）
- 自动适应参数空间的曲率
- 减少对学习率调参的依赖

**缺点**：
- 每次迭代需要 $O(n^2)$ 次测量（$n$ 为参数数量）
- Fisher信息矩阵求逆计算成本高
- 对于大参数体系不实用

> 量子自然梯度代表了VQE优化中的"几何智慧"——尊重参数空间的内在度规，避免在平坦方向上浪费梯度更新。但随着参数规模增大，其测量成本也迅速增长。

---

## 5.8 QAOA算法原理

### 5.8.1 从VQE到QAOA

**即时练习 5.8.1**

1. QAOA 与 VQE 的本质区别是什么？
2. QAOA 主要用于解决什么类型的问题？

VQE主要用于连续优化问题（求解哈密顿量基态）。但许多实际应用涉及**组合优化**——在离散集合中寻找最优解。经典例子包括：最大割（MaxCut）、旅行商问题（TSP）、图着色等。

**量子近似优化算法（Quantum Approximate Optimization Algorithm, QAOA）** 由Edward Farhi、Jeffrey Goldstone和Sam Gutmann于2014年提出，专门用于求解组合优化问题。QAOA可以看作VQE在组合优化领域的特化版本——它使用特定的问题驱动Ansatz。

QAOA与VQE的本质区别：

- **VQE**：针对任意哈密顿量的基态近似
- **QAOA**：针对组合优化问题，使用问题特定的分层电路
- **VQE的Ansatz**：灵活设计（HEA/UCC等）
- **QAOA的Ansatz**：由问题哈密顿量和混合哈密顿量交替驱动

### 5.8.2 将组合优化问题编码为哈密顿量

**即时练习 5.8.2**

1. QAOA 中成本哈密顿量 $\hat{H}_C$ 如何构造？
2. 对于 MaxCut 问题，成本哈密顿量的具体形式是什么？

QAOA的第一步：将组合优化问题的**成本函数** $C(z)$ 编码为**成本哈密顿量** $\hat{H}_C$。

成本函数 $C(z)$ 定义在 $n$ 个比特的二进制字符串 $z = z_1 z_2 \cdots z_n$ 上。我们需要找到一个哈密顿量 $\hat{H}_C$，使得每个计算基态 $|z\rangle$ 的本征值等于成本函数值：

$$
\hat{H}_C |z\rangle = C(z) |z\rangle
$$

这样，寻找最优（最小或最大）成本等价于寻找 $\hat{H}_C$ 的基态或激发态。

**构造方法**：将成本函数中的每个子项转化为泡利算符。

例如，对于MaxCut问题（详细见5.9节），成本函数为：

$$
C(z) = \sum_{\langle i,j \rangle} \frac{1 - z_i z_j}{2}
$$

对应的成本哈密顿量为：

$$
\hat{H}_C = \sum_{\langle i,j \rangle} \frac{1}{2} (I - Z_i Z_j)
$$

其中 $Z_i$ 是作用在第 $i$ 个量子比特上的泡利 $Z$ 算符，$z_i \in \{+1, -1\}$ 是 $Z_i$ 的本征值。

### 5.8.3 QAOA电路结构

**即时练习 5.8.3**

1. $p$ 层 QAOA 电路 $|\psi_p(\boldsymbol\gamma, \boldsymbol\beta)\rangle$ 的表达式是什么？
2. 初态 $|+\rangle^{\otimes n}$ 如何制备？

QAOA的电路结构由 $p$ 层（称为QAOA深度）构成，每层包含两个核心部分：

1. **成本哈密顿量演化层**：对 $\hat{H}_C$ 演化时间 $\gamma_i$
2. **混合哈密顿量演化层**：对 $\hat{H}_B$ 演化时间 $\beta_i$

第 $i$ 层的幺正算符为：

$$
U_C(\gamma_i) = e^{-i \gamma_i \hat{H}_C}, \quad U_B(\beta_i) = e^{-i \beta_i \hat{H}_B}
$$

整个 $p$ 层QAOA电路为：

$$
|\psi_p(\boldsymbol{\gamma}, \boldsymbol{\beta})\rangle = U_B(\beta_p) U_C(\gamma_p) \cdots U_B(\beta_1) U_C(\gamma_1) |+\rangle^{\otimes n}
$$

其中初态 $|+\rangle^{\otimes n}$ 是所有计算基态等权叠加态：

$$
|+\rangle^{\otimes n} = \frac{1}{\sqrt{2^n}} \sum_{z \in \{0,1\}^n} |z\rangle
$$

**混合哈密顿量**的标准选择为：

$$
\hat{H}_B = \sum_{i=1}^{n} X_i
$$

这是横场（transverse field）哈密顿量，它在计算基上的作用是在各比特间引入量子隧穿（tunneling）——允许系统在不同计算基态之间跃迁。

$U_B(\beta)$ 在单量子比特层面可分解为：

$$
U_B(\beta) = e^{-i \beta \sum_i X_i} = \bigotimes_{i=1}^{n} e^{-i \beta X_i} = \bigotimes_{i=1}^{n} R_{x_i}(2\beta)
$$

### 5.8.4 QAOA的几何直觉

**即时练习 5.8.4**

1. QAOA 与量子绝热算法有什么关系？
2. 为什么说 QAOA 是"有限时间版本的绝热计算"？

QAOA的运作机制可以从量子绝热定理（Quantum Adiabatic Theorem）获得直觉。

**绝热定理**说：如果一个量子系统从某个哈密顿量的基态出发，并且哈密顿量变化得足够慢，系统将始终保持在瞬时基态。

QAOA可以看作**绝热演化的离散Troterized近似**：

$$
\hat{H}(t) = (1 - t/T) \hat{H}_B + (t/T) \hat{H}_C
$$

从 $\hat{H}_B$ 的基态（$|+\rangle^{\otimes n}$）开始，缓慢演化到 $\hat{H}_C$ 的基态（最优解）。QAOA用有限层 $p$ 离散逼近这条绝热路径。

当 $p \to \infty$ 时，QAOA的期望值收敛到全局最优：

$$
\lim_{p \to \infty} \langle \psi_p(\boldsymbol{\gamma}^*, \boldsymbol{\beta}^*) | \hat{H}_C | \psi_p(\boldsymbol{\gamma}^*, \boldsymbol{\beta}^*) \rangle = E_{\min}
$$

但对于有限 $p$，QAOA只能提供**近似解**——其近似质量由 $p$ 和问题结构共同决定。

### 5.8.5 QAOA的变分优化

**即时练习 5.8.5**

1. QAOA 需要优化多少个参数参数？它们各自的取值范围是多少？
2. QAOA 参数优化的独特性质有哪些？

与VQE类似，QAOA使用经典优化器优化 $2p$ 个参数：

$$
\boldsymbol{\gamma} = (\gamma_1, \gamma_2, \ldots, \gamma_p), \quad \boldsymbol{\beta} = (\beta_1, \beta_2, \ldots, \beta_p)
$$

目标函数为：

$$
F_p(\boldsymbol{\gamma}, \boldsymbol{\beta}) = \langle \psi_p(\boldsymbol{\gamma}, \boldsymbol{\beta}) | \hat{H}_C | \psi_p(\boldsymbol{\gamma}, \boldsymbol{\beta}) \rangle
$$

约束条件：

$$
\gamma_i \in [0, 2\pi), \quad \beta_i \in [0, \pi)
$$

QAOA的参数优化有其独特性质：

1. **参数空间周期性**：$\gamma_i$ 和 $\beta_i$ 具有周期性边界，可以利用约化
2. **优化地形的对称性**：问题对称性反映在参数空间中
3. **参数传递（Parameter Transfer）**：小问题的优化参数可以作为大问题参数初始化的参考

### 5.8.6 QAOA的近似比

**即时练习 5.8.6**

1. QAOA 的性能通常用什么指标衡量？$p=1$ 层 QAOA 对 MaxCut 的保证近似比是多少？
2. 当 $p \to \infty$ 时近似比会怎样？

QAOA的性能通常用**近似比** $r$ 衡量：

$$
r = \frac{F_p(\boldsymbol{\gamma}^*, \boldsymbol{\beta}^*)}{C_{\max}}
$$

对于最大割问题，$p=1$ 时的QAOA保证近似比 $r \ge 0.6924$。这意味着无论图多大，单层QAOA至少能捕获最优解约69%的质量。

当 $p \to \infty$ 时，$r \to 1$（达到最优）。但实际中，$p$ 受限于噪声和量子比特数。

---

## 5.9 MaxCut问题的QAOA求解

### 5.9.1 MaxCut问题定义

**即时练习 5.9.1**

1. MaxCut 问题的目标是什么？它是什么复杂度的？
2. 对于三角形图，MaxCut 的最优解割值是多少？

最大割（Maximum Cut, MaxCut）是组合优化领域的经典NP-hard问题，也是QAOA最常用的基准测试问题。

**问题定义**：

给定一个无向图 $G = (V, E)$，其中 $V = \{1, 2, \ldots, n\}$ 是顶点集，$E$ 是边集。每条边 $(i,j)$ 有权重 $w_{ij} \ge 0$。MaxCut的目标是将顶点划分为两个集合 $S$ 和 $\bar{S}$，使得跨越两个集合的边的总权重最大：

$$
\max_{S \subseteq V} \sum_{(i,j) \in E} w_{ij} \cdot \mathbf{1}[i \in S \neq j \in S]
$$

**示例**：三角形图（3个顶点，3条边）

```
     1
    / \
   /   \
  2─────3
```

最优解：将顶点1分到集合A，顶点2和3分到集合B，割边为(1,2)和(1,3)，割值=2。另一个最优解是(2在A, 1和3在B)，也得到2。

### 5.9.2 MaxCut的哈密顿量编码

**即时练习 5.9.2**

1. MaxCut 的成本哈密顿量如何编码？写出其表达式。
2. $Z_i Z_j$ 项在这个编码中起什么作用？

用二进制变量 $z_i \in \{+1, -1\}$ 表示顶点 $i$ 所属的集合（$+1$ = 集合A, $-1$ = 集合B）。

边 $(i,j)$ 的贡献为：

$$
\frac{w_{ij}}{2} (1 - z_i z_j)
$$

当 $z_i \neq z_j$（跨越割）时贡献为 $w_{ij}$，否则为 $0$。

MaxCut的成本哈密顿量为：

$$
\hat{H}_C = \sum_{(i,j) \in E} \frac{w_{ij}}{2} (I - Z_i Z_j) = \frac{1}{2} \sum_{(i,j) \in E} w_{ij} I - \frac{1}{2} \sum_{(i,j) \in E} w_{ij} Z_i Z_j
$$

由于第一项是常数，优化只依赖于第二项：

$$
\hat{H}_C = \text{const} - \frac{1}{2} \sum_{(i,j) \in E} w_{ij} Z_i Z_j
$$

最大化 $C(z)$ 等价于最小化 $\hat{H}_C$ 的能量。在实际的QAOA实现中，我们直接使用：

$$
\hat{H}_C = \sum_{(i,j) \in E} Z_i Z_j
$$

配合适当的符号和偏移处理。

### 5.9.3 p=1层QAOA的详细分析

**即时练习 5.9.3**

1. $p=1$ 层 QAOA 需要优化几个参数？最优参数如何寻找？
2. 对于 3 度正则图，$p=1$ QAOA 的保证近似比是多少？

对于 $p=1$ 层QAOA，电路只有两个参数 $\gamma$ 和 $\beta$：

$$
|\psi_1(\gamma, \beta)\rangle = e^{-i\beta \hat{H}_B} e^{-i\gamma \hat{H}_C} |+\rangle^{\otimes n}
$$

**期望值计算**：

对于MaxCut，$p=1$ 层QAOA的期望值可以解析求解。以正则图（每个顶点度数相同）为例，期望值可以表示为：

$$
F_1(\gamma, \beta) = \frac{1}{2} \sum_{(i,j) \in E} w_{ij} \left[ 1 - \langle \psi_1(\gamma, \beta) | Z_i Z_j | \psi_1(\gamma, \beta) \rangle \right]
$$

对于每条边 $(i,j)$，$\langle Z_i Z_j \rangle$ 的计算只涉及与 $i$ 和 $j$ 相邻的顶点。对于 $d$ 度正则图，结果为：

$$
\langle Z_i Z_j \rangle = \sin(2\beta) \sin(2\gamma) \cos^{d-2}(2\gamma)
$$

这个解析表达式使得 $p=1$ 的优化极其高效——只需两参数优化。

**最优参数**：

对于3度正则图，最优参数约为：

$$
\gamma^* \approx 0.615, \quad \beta^* \approx 0.393
$$

对应的近似比 $r \approx 0.6924$。

### 5.9.4 QAOA电路实现

**即时练习 5.9.4**

1. 成本层 $e^{-i\gamma Z_i Z_j}$ 如何用 CNOT 和 $R_z$ 门实现？
2. 混合层 $e^{-i\beta X_i}$ 如何实现？

QAOA电路在量子硬件上的实现涉及两个子电路：

**成本层 $e^{-i\gamma \hat{H}_C}$**：

对于MaxCut，$\hat{H}_C$ 是 $Z_i Z_j$ 的和。由于 $[Z_i Z_j, Z_k Z_l] = 0$（所有项对易），成本层可以精确分解（无需Trotter）：

$$
e^{-i\gamma \hat{H}_C} = \prod_{(i,j) \in E} e^{-i\gamma Z_i Z_j}
$$

每个 $e^{-i\gamma Z_i Z_j}$ 可以用两个CNOT和一个 $R_z(2\gamma)$ 实现：

```
q_i: ── ● ──────────── ● ──
         │              │
q_j: ── ⊕ ── R_z(2γ) ─ ⊕ ──
```

**混合层 $e^{-i\beta \hat{H}_B}$**：

混合哈密顿量 $\hat{H}_B = \sum_i X_i$ 的所有项也对易，因此同样精确分解：

$$
e^{-i\beta \hat{H}_B} = \bigotimes_{i=1}^{n} e^{-i\beta X_i} = \bigotimes_{i=1}^{n} R_{x_i}(2\beta)
$$

**完整电路示意**（$p=1$，3量子比特MaxCut）：

```
|0⟩ ── H ── e^{-iγ Z₀Z₁} ── e^{-iγ Z₀Z₂} ── R_x(2β) ── 测量
|0⟩ ── H ── e^{-iγ Z₀Z₁} ── e^{-iγ Z₁Z₂} ── R_x(2β) ── 测量
|0⟩ ── H ── e^{-iγ Z₀Z₂} ── e^{-iγ Z₁Z₂} ── R_x(2β) ── 测量
```

### 5.9.5 多层级QAOA与近似比提升

**即时练习 5.9.5**

1. 增加 $p$ 对近似比有什么影响？
2. 增加 $p$ 在硬件上面临什么挑战？

增加 $p$ 可以提升近似比。下面是 $p$ 对近似比影响的典型规律：

| $p$ | 近似比 $r$（3正则图） | 说明 |
|-----|---------------------|------|
| 1 | 0.6924 | 理论保证的下界 |
| 2 | 约0.76 | 经验结果 |
| 3 | 约0.79 | 经验结果 |
| 5 | 约0.84 | 经验结果 |
| 10 | 约0.91 | 经验结果 |
| $\infty$ | 1.0 | 精确解 |

理论上，对于任意图，QAOA在 $p \to \infty$ 时保证收敛到全局最优。但在实际硬件中，$p$ 的增加意味着：

- 电路深度线性增长
- 门错误累积
- 参数数量 $2p$ 增加，优化更困难

**实例**：对 20 量子比特的MaxCut问题，$p=3$ 通常需要约 $60$ 个参数优化，电路深度约 $6$ 层CNOT，在NISQ设备上是可行的。

### 5.9.6 QAOA vs 经典算法

**即时练习 5.9.6**

1. Goemans-Williamson 算法的近似比是多少？
2. QAOA 相比经典 MaxCut 算法的主要优势是什么？

| 算法 | 近似比保证 | 时间复杂度 | 适用规模 |
|------|-----------|-----------|---------|
| Goemans-Williamson（SDP） | 0.878 | $O(n^3)$ | 中等 |
| 随机贪心 | 0.5 | $O(n+m)$ | 非常大 |
| QAOA $p=1$ | 0.692 | 浅电路 | 受限于硬件 |
| QAOA $p \to \infty$ | 1.0 | 深电路 | 受限于硬件 |
| 精确求解（分支定界） | 1.0 | $O(2^n)$ | 小（$\le 50$） |

Goemans-Williamson算法是经典MaxCut近似算法的黄金标准，其近似比0.878至今未被超越。QAOA的主要优势不在于提供更好的近似比，而在于：

1. 它是**通用框架**，可推广到其他组合优化问题（如MaxSAT、TSP）
2. 随着量子硬件的进步，$p$ 可以不断提高
3. 对某些特定图族，QAOA可以超越经典算法的近似比

---

## 5.10 变分算法的零噪声外推

### 5.10.1 NISQ噪声的影响

**即时练习 5.10.1**

1. 噪声对变分量子算法的影响体现在哪两方面？
2. 零噪声外推（ZNE）的核心思想是什么？

变分量子算法在真实量子硬件上运行时，噪声会严重影响其性能。噪声的影响体现在两方面：

1. **能量估计偏差**：测量得到的能量值偏离真实期望值，导致优化器做出错误的参数更新
2. **保真度损失**：制备的量子态偏离目标态，缩小了有效搜索空间

**零噪声外推（Zero-Noise Extrapolation, ZNE）** 是一种经典的**误差缓解**（Error Mitigation）技术，它在不依赖量子纠错的情况下，通过经典后处理来估计无噪声情况下的期望值。

### 5.10.2 ZNE的基本原理

**即时练习 5.10.2**

1. ZNE 的实现步骤是什么？噪声放大因子如何选择？
2. 外推如何从不同噪声水平的数据中恢复无噪声估计？

ZNE的核心思想是：

1. 在**不同噪声水平**下测量目标期望值
2. 拟合测量值关于噪声强度的函数
3. **外推**到噪声强度为零的情况

**实现步骤**：

```
步骤1：选择噪声放大因子 λ ∈ {1, 2, 3, ..., M}
步骤2：对每个 λ，在噪声水平放大的条件下
       执行 VQE/QAOA 电路并测量 ⟨H⟩_λ
步骤3：拟合 ⟨H⟩(λ) = a₀ + a₁λ + a₂λ² + ...
步骤4：外推 λ=0 处的值作为无噪声估计
```

### 5.10.3 噪声放大方法

**即时练习 5.10.3**

1. 噪声放大有哪几种方法？各有什么优缺点？
2. 门折叠如何实现噪声放大？

**方法1：脉冲拉伸（Pulse Stretching）**

在脉冲级控制层面，将门操作时间延长 $\lambda$ 倍，噪声（如退相干）相应放大。这种方法需要硬件层面的脉冲访问权限。

**方法2：门折叠（Gate Folding）**

对电路中的每个门 $U$，插入其逆门和正门对 $U U^\dagger U$，使有效噪声放大。这个方法不需要硬件特殊访问：

$$
U \to U U^\dagger U
$$

总电路层数从 $L$ 变为 $(2\lambda - 1)L$。

**方法3：回路折叠（Circuit Folding）**

对整个电路应用相同的折叠操作，适用于无法单独访问每个门的情况。

### 5.10.4 外推方法

**即时练习 5.10.4**

1. ZNE 中常用的外推方法有哪些？
2. 线性外推和多项式外推分别适用什么场景？

**线性外推**：

$$
\langle H \rangle_{\text{ZNE}} = 2\langle H \rangle_{\lambda=1} - \langle H \rangle_{\lambda=2}
$$

**指数外推**（适合噪声对期望值呈指数衰减的情况）：

$$
\langle H \rangle_{\text{ZNE}} = \frac{\langle H \rangle_{\lambda=2}^2}{\langle H \rangle_{\lambda=4}}
$$

**多项式外推**（通用）：

$$
\langle H \rangle_{\lambda} = a_0 + a_1 \lambda + a_2 \lambda^2 + \cdots + a_k \lambda^k
$$

其中 $a_0$ 即为零噪声估计值。

### 5.10.5 ZNE在VQE中的应用

**即时练习 5.10.5**

1. ZNE 在 VQE 中的应用需要注意什么？
2. ZNE 的局限性是什么？它不能缓解哪类噪声？

在VQE中应用ZNE时，需要注意：

1. **每个参数更新步骤都做ZNE**：这会显著增加测量次数
2. **替代方案：终点ZNE**：只在优化收敛后对最终态做ZNE校正
3. **自适应ZNE**：根据噪声水平动态选择外推阶数

实验表明，ZNE可以将VQE的化学精度从约 $10^{-2}$ Hartree提升到 $10^{-3}$ Hartree水平，是目前的实用误差缓解方案中最有效的方法之一。

> **ZNE的局限**：ZNE假设噪声是**单调且可预测的**。当噪声模型不满足这一假设时（例如，相干噪声或非高斯噪声），外推结果可能不准确。

---

## 5.11 本章习题

### 基础题（1-5题）

**1.** 简述变分量子-经典混合架构的三个核心组件及其功能。

**2.** 利用Rayleigh-Ritz变分原理，证明：对于任意试探态 $|\psi\rangle$，有 $\langle \psi | \hat{H} | \psi \rangle \ge E_0$，其中 $E_0$ 是 $\hat{H}$ 的最小本征值。

**3.** Jordan-Wigner映射中，为什么需要引入 $Z$ 串（Jordan-Wigner string）？请用反对易关系说明。

**4.** 对于氢分子（H₂）在STO-3G基组下的哈密顿量，经过Jordan-Wigner映射后，总共需要多少个量子比特？

**5.** 什么是"化学精度"？它的数值定义是什么（以Hartree为单位）？

### 进阶题（6-10题）

**6.** 在VQE中，测量哈密顿量期望值时，为什么要将哈密顿量分解为泡利串的和？请解释 $Z$ 基测量如何得到 $X$ 和 $Y$ 算符的期望值。

**7.** 参数偏移规则（Parameter Shift Rule）给出：对于 $U(\theta) = e^{-i\theta G/2}$ 且 $G^2 = I$，有：

$$
\frac{\partial E}{\partial \theta} = \frac{E(\theta + \pi/2) - E(\theta - \pi/2)}{2}
$$

请推导这个公式。

**8.** 比较硬件高效Ansatz（HEA）和UCCSD Ansatz的优缺点。在NISQ设备上，你更推荐哪个？为什么？

**9.** SPSA优化器在每次迭代中只需要2次函数求值。请分析：为什么SPSA适合VQE而不是传统的梯度下降？

**10.** 描述泡利串测量分组的图着色算法。对于一个由 $Z_0 Z_1, Z_1 Z_2, X_0 X_1, Y_0 Y_1$ 构成的泡利串集合，如何进行分组？

### 应用题（11-15题）

**11.** 考虑一个三角形图（3个顶点，每条边权重为1）。请：
（a）写出MaxCut问题的成本函数；
（b）写出对应的成本哈密顿量 $\hat{H}_C$；
（c）画出 $p=1$ 层QAOA的量子电路。

**12.** 对于4-正则图上的MaxCut问题，$p=1$ 层QAOA的 $\langle Z_i Z_j \rangle$ 解析表达式为 $\sin(2\beta) \sin(2\gamma) \cos^2(2\gamma)$。请：
（a）在区域 $[0, \pi] \times [0, \pi/2]$ 内搜索最优的参数 $\gamma^*, \beta^*$；
（b）计算对应的近似比 $r$。

**13.** 在VQE中，对于一个有 $N_{\text{term}} = 50$ 个泡利串的哈密顿量，每个泡利串需要 $N_{\text{shot}} = 10^4$ 次测量。如果通过分组将对易的泡利串合并到 $K = 8$ 组中同时测量，试计算总测量次数的节省比例。

**14.** 零噪声外推（ZNE）中，假设噪声强度 $\lambda$ 下测量的能量值为 $\langle H \rangle_\lambda = E_0 + \epsilon \lambda + \delta \lambda^2$。已知 $\lambda = 1, 2, 3$ 时的测量值分别为 $-1.02, -1.08, -1.18$（单位：Hartree）。请用二次多项式外推估计零噪声能量 $E_0$。

**15.** 比较VQE和QAOA的异同。从算法结构、参数空间、应用领域三个角度分析。在什么情况下你会选择VQE？什么情况下选择QAOA？

---

> **本章参考文献**
>
> 1. Peruzzo, A., et al. "A variational eigenvalue solver on a photonic quantum processor." *Nature Communications* 5, 4213 (2014).
> 2. Kandala, A., et al. "Hardware-efficient variational quantum eigensolver for small molecules and quantum magnets." *Nature* 549, 242-246 (2017).
> 3. Farhi, E., Goldstone, J., & Gutmann, S. "A quantum approximate optimization algorithm." arXiv:1411.4028 (2014).
> 4. Grimsley, H. R., et al. "An adaptive variational algorithm for exact molecular simulations on a quantum computer." *Nature Communications* 10, 3007 (2019).
> 5. Jordan, P., & Wigner, E. "Über das Paulische Äquivalenzverbot." *Zeitschrift für Physik* 47, 631-651 (1928).
> 6. Bravyi, S., & Kitaev, A. "Fermionic quantum computation." *Annals of Physics* 298, 210-226 (2002).
> 7. Temme, K., Bravyi, S., & Gambetta, J. M. "Error mitigation for short-depth quantum circuits." *Physical Review Letters* 119, 180509 (2017).
> 8. McArdle, S., et al. "Quantum computational chemistry." *Reviews of Modern Physics* 92, 015003 (2020).
> 9. Cerezo, M., et al. "Variational quantum algorithms." *Nature Reviews Physics* 3, 625-644 (2021).
> 10. Hadfield, S., et al. "From the quantum approximate optimization algorithm to a quantum alternating operator ansatz." *Algorithms* 12, 34 (2019).

---

### 知识点索引

> 按拼音/字母顺序排列。

- **ADAPT-VQE**：5.5.5节
- **Ansatz（电路模板）**：5.5节
- **Bravyi-Kitaev 映射**：5.3.3节
- **HEA（硬件高效 Ansatz）**：5.5.2节
- **Jordan-Wigner 映射**：5.3.2节
- **MaxCut 问题**：5.9节
- **NISQ**：5.1.1节
- **QAOA（量子近似优化算法）**：5.8节
- **Rayleigh-Ritz 变分原理**：5.1.1节
- **SPSA 优化器**：5.7.2节
- **UCCSD Ansatz**：5.5.3节
- **VQE（变分量子本征值求解器）**：5.2节
- **变分量子-经典混合架构**：5.1节
- **参数偏移规则**：5.7节
- **泡利串并行测量**：5.6节
- **零噪声外推（ZNE）**：5.10节
- **化学精度**：5.2.4节
- **哈密顿量测量**：5.6节
- **费米子-量子比特映射**：5.3节
