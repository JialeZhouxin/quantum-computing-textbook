# 第1章 基础量子算法

> **本章导读**
>
> 模块三我们掌握了量子比特、量子门和量子电路模型——现在，是时候见识量子计算真正的威力了。本章将带你走进**量子算法**的世界，从最基础的概念——量子并行性、Oracle模型、相位反冲——开始，逐步构建一系列标志性算法。
>
> 你会看到：Deutsch算法如何在一次查询中解决经典需要两次的问题；Deutsch-Jozsa算法如何将这一优势扩展到n比特；Bernstein-Vazirani算法如何以单次查询学习一个隐藏字符串的每一位；Simon算法如何在指数级加速下发现周期函数的结构；最后，量子傅里叶变换（QFT）作为许多高级算法的核心引擎，将得到完整的展示。
>
> 学完本章，你将能够：
> - 理解量子并行性的来源和局限
> - 使用Oracle模型描述黑箱问题
> - 掌握相位反冲机制——量子算法中最常用的"小技巧"
> - 推导Deutsch算法和Deutsch-Jozsa算法的全部步态变化
> - 理解Bernstein-Vazirani算法如何以一次查询解决经典需要n次的问题
> - 理解Simon算法如何以多项式查询解决经典指数复杂度的周期发现问题
> - 写出QFT的定义、矩阵形式和乘积表示
> - 画出QFT的电路实现（Hadamard门+受控旋转门）
> - 了解量子加法器、乘法器和比较器的基本思想
>
> **先修知识**：模块一（线性代数、狄拉克符号、张量积）、模块三（量子比特、单比特门、多比特门、CNOT、量子电路模型、测量公设）

---

## 1.1 量子并行性

### 1.1.1 什么是量子并行性？

经典计算机在单次操作中只能处理一个输入。例如，要计算一个布尔函数 $f(x)$ 在四个可能输入 $x \in \{0,1\}^2$ 上的值，经典计算机需要四次求值（或使用并行硬件，但那样需要四倍的电路）。

量子计算机则不同。由于**叠加态**的存在，一个量子寄存器可以同时处于多个基态的叠加。当我们对叠加态施加一个量子门时，这个门作用在**所有基态分量上**——这就是**量子并行性**（quantum parallelism）的本质。

**定义 1.1（量子并行性）** 量子并行性是指：对一个处于叠加态的量子寄存器施加一个幺正算符 $U_f$，该算子同时作用于寄存器中所有基态分量，产生所有对应结果叠加的能力。

更具体地：考虑一个 $n$ 量子比特的寄存器。制备均匀叠加态：

$$
|\psi_0\rangle = H^{\otimes n} |0\rangle^{\otimes n} = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} |x\rangle
$$

现在施加幺正算符 $U_f$ 将函数 $f$ 编码到量子态上。结果是：

$$
U_f |\psi_0\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} U_f|x\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} |x, f(x)\rangle
$$

这个态包含了 $f$ 在**所有** $2^n$ 个输入上的计算结果。而实现这一切，只用了**一次** $U_f$ 的求值。

**例 1.1** 取 $n=2$。制备叠加态 $\frac{1}{2}(|00\rangle + |01\rangle + |10\rangle + |11\rangle)$。施加 $U_f$ 后：

$$
U_f \cdot \frac{1}{2}\sum_{x=00}^{11} |x\rangle|0\rangle = \frac{1}{2}(|00, f(00)\rangle + |01, f(01)\rangle + |10, f(10)\rangle + |11, f(11)\rangle)
$$

$f$ 的四个函数值同时被计算出来。

### 1.1.2 量子并行性的来源

量子并行性来源于两个核心要素：

1. **叠加态**：$n$ 个量子比特的寄存器可以处于 $2^n$ 个基态的叠加。
2. **幺正算符的线性**：量子门是线性算子。如果 $U_f$ 在基态 $|x\rangle$ 上的作用是 $U_f|x\rangle = |f(x)\rangle$（适当编码），那么由线性性：

$$
U_f\left(\sum_x \alpha_x |x\rangle\right) = \sum_x \alpha_x U_f|x\rangle = \sum_x \alpha_x |f(x)\rangle
$$

线性性保证了叠加态中的每个分量独立演化——它们互不干扰，齐头并进。

### 1.1.3 量子并行性的限制

这里有一个关键问题：**你不能直接读取这个叠加态**。

测量会破坏叠加态——你只能得到某一个 $x$ 对应的 $f(x)$，且概率为 $|\alpha_x|^2$。这看起来和经典计算没什么两样：你仍然只得到一个答案。

量子算法的艺术就在于：**设计巧妙的量子操作，使得所有并行计算的结果以某种方式"干涉"在一起，最终以高概率输出你需要的那个信息**。这正是后续每一节要展开的内容。

> **比喻**：量子并行性就像你有 $2^n$ 个计算器同时工作，但它们共享一张纸。每个计算器把自己的答案写在纸上某个位置。但你只能看这张纸一次——你看到的是所有答案叠加在一起的结果。除非你事先设计好如何让不想要的答案互相抵消，想要的答案互相增强，否则你什么也读不出来。

### 1.1.4 适合量子并行计算的问题特征

并非所有问题都能从量子并行性中获益。适合量子加速的问题通常具有以下特征：

1. **结构信息隐藏在全局性质中**：比如"函数是否恒定"（Deutsch-Jozsa）——不是问某个点的值，而是问函数的整体性质。
2. **周期或对称性**：Shor算法利用量子并行性寻找函数的周期。
3. **搜索空间巨大**：Grover算法在无结构数据库中搜索。
4. **线性结构**：Bernstein-Vazirani算法利用线性代数结构。

### 1.1.5 量子并行性与经典并行的区别

| 特性 | 经典并行 | 量子并行 |
|------|---------|---------|
| 硬件 | 多个处理器同时工作 | 单个幺正算符作用在叠加态上 |
| 资源 | 处理器数量随输入线性增长 | 量子比特数量随输入对数增长 |
| 结果读取 | 每个处理器独立输出 | 叠加态必须通过干涉提取信息 |
| 限制 | 热量、通信开销 | 相干时间、退相干、测量坍缩 |

**小结**：量子并行性本身不是终点——它为量子加速提供了**原材料**。真正的加速来源于**量子干涉**，即如何让大量的并行计算结果相互干涉，使得想要的信息脱颖而出。相位反冲和量子傅里叶变换是实现这种干涉的两个最重要的工具。

**即时练习 1.1**

1. 如果 $f$ 是定义在 $n$ 比特上的布尔函数，经典计算机计算 $f$ 在所有输入上的值需要多少次求值？量子计算机利用量子并行性需要多少次？
2. 量子并行性为什么不能直接"读取"所有结果？其根本限制是什么？
3. 思考：如果 $U_f$ 的定义是 $U_f|x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle$，这是一个幺正算符吗？验证它的酉性。

---

## 1.2 Oracle模型与相位反冲

### 1.2.1 黑箱Oracle模型

在量子算法理论中，我们经常把被查询的函数 $f$ 包装成一个**黑箱**（black box），称为 **Oracle**。所谓Oracle，就是你给它一个输入，它返回输出，但你不需要知道它内部的实现细节。

这种模型的好处：当我们讨论算法复杂度时，我们**不关心实现Oracle需要多少门**，只关心**调用了多少次Oracle**。这称为**查询复杂度**（query complexity）。

**定义 1.2（量子Oracle）** 一个量子Oracle是一个实现布尔函数 $f: \{0,1\}^n \to \{0,1\}^m$ 的幺正算符 $O_f$。最常见的两种形式是：

1. **标准形式**（可逆计算方式）：

$$
O_f |x\rangle |y\rangle = |x\rangle |y \oplus f(x)\rangle
$$

   其中 $\oplus$ 是按位异或。这种形式保证酉性。

2. **相位形式**：

$$
O_f |x\rangle = (-1)^{f(x)} |x\rangle
$$

   当 $f(x)=1$ 时翻转相位，$f(x)=0$ 时不变。

> **为什么需要 $|y\rangle$ 寄存器？** 因为 $\sum_x \alpha_x |x\rangle \to \sum_x \alpha_x |f(x)\rangle$ 一般不是幺正变换——丢失了信息（不同 $x$ 可能映射到相同 $f(x)$）。引入辅助寄存器 $|y\rangle$ 并通过异或操作保持可逆性。

### 1.2.2 标准Oracle的电路表示

标准Oracle的电路图如下：

```
      n          ┌─────┐
|x⟩ ────────────┤     ├─────────── |x⟩
                │ O_f │
|y⟩ ────────────┤     ├─────────── |y ⊕ f(x)⟩
      m          └─────┘
```

**例 1.2** 令 $f(0)=0, f(1)=1$（恒等函数）。Oracle $O_f$ 的作用：

- $O_f |0\rangle|0\rangle = |0\rangle|0\oplus f(0)\rangle = |0\rangle|0\rangle$
- $O_f |0\rangle|1\rangle = |0\rangle|1\oplus f(0)\rangle = |0\rangle|1\rangle$
- $O_f |1\rangle|0\rangle = |1\rangle|0\oplus f(1)\rangle = |1\rangle|1\rangle$
- $O_f |1\rangle|1\rangle = |1\rangle|1\oplus f(1)\rangle = |1\rangle|0\rangle$

这正是CNOT门——因为 $f(x)=x$ 时 $O_f$ 就是 CNOT。

### 1.2.3 相位反冲机制

**相位反冲**（phase kickback）是量子算法中最常用也最优雅的小技巧。它是连接"标准Oracle"和"相位Oracle"的桥梁。

考虑标准Oracle $O_f|x\rangle|y\rangle = |x\rangle|y\oplus f(x)\rangle$。把辅助寄存器 $|y\rangle$ 设为 $|-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}$：

$$
\begin{aligned}
O_f|x\rangle|-\rangle &= O_f|x\rangle\frac{|0\rangle - |1\rangle}{\sqrt{2}} \\
&= \frac{1}{\sqrt{2}}\left(O_f|x\rangle|0\rangle - O_f|x\rangle|1\rangle\right) \\
&= \frac{1}{\sqrt{2}}\left(|x\rangle|0\oplus f(x)\rangle - |x\rangle|1\oplus f(x)\rangle\right) \\
&= \frac{1}{\sqrt{2}}\left(|x\rangle|f(x)\rangle - |x\rangle|1\oplus f(x)\rangle\right)
\end{aligned}
$$

如果 $f(x)=0$，则 $|0\oplus 0\rangle = |0\rangle$，$|1\oplus 0\rangle = |1\rangle$：

$$
O_f|x\rangle|-\rangle = \frac{1}{\sqrt{2}}\left(|x\rangle|0\rangle - |x\rangle|1\rangle\right) = |x\rangle|-\rangle
$$

如果 $f(x)=1$，则 $|0\oplus 1\rangle = |1\rangle$，$|1\oplus 1\rangle = |0\rangle$：

$$
O_f|x\rangle|-\rangle = \frac{1}{\sqrt{2}}\left(|x\rangle|1\rangle - |x\rangle|0\rangle\right) = -|x\rangle|-\rangle
$$

合并起来：

$$
O_f|x\rangle|-\rangle = (-1)^{f(x)} |x\rangle|-\rangle
$$

辅助寄存器 $|-\rangle$ **没有被改变**（它仍然是 $|-\rangle$），但它的相位被"踢回"到了数据寄存器 $|x\rangle$ 上！

**这就是相位反冲**：辅助寄存器的相位变化被转移到主寄存器上，实现了相位Oracle $O_f|x\rangle = (-1)^{f(x)}|x\rangle$。

### 1.2.4 相位反冲的电路实现

```
      n
|x⟩ ──────┬───────► (-1)^{f(x)}|x⟩
          │
|−⟩ ──────⊕───────► |−⟩（不变）
```

更完整的流程：

```
|x⟩ ──┤H├──■──┤H├── ...
       └─┘  │
|0⟩ ──┤H├──⊕──── ...
       └─┘
```

其中辅助比特先通过 Hadamard 门从 $|0\rangle$ 变为 $|-\rangle$，经过Oracle后相位反冲到主寄存器，再通过 Hadamard 门变回 $|0\rangle$（以方便后续测量或丢弃）。

### 1.2.5 相位反冲的直观理解

为什么这个技巧叫"反冲"（kickback）？想象你推开一堵墙——墙没动，但反作用力推了你。类比：

- 你把辅助比特设为 $|-\rangle$（相当于"准备反弹"）。
- Oracle试图改变辅助比特（对 $f(x)=1$ 翻转它）。
- 但 $|-\rangle$ 是 $|0\rangle$ 和 $|1\rangle$ 的等幅叠加，翻转后只是全局相位变化——辅助比特不变。
- 这个"试图改变但没成功"的能量以相位形式反弹到主寄存器上。

**关键认识**：相位反冲不是被动发现的数学巧合——它是我们**有意设计**的。我们故意把辅助寄存器放在 $|-\rangle$ 态，目的就是让Oracle的效果以相位形式编码到主寄存器上。

### 1.2.6 Oracle的查询复杂度

在算法分析中，我们关注的是**Oracle查询次数**，而不是Oracle内部的门的数量。原因：

1. Oracle代表我们不知道内部实现的"黑箱"。
2. 不同的函数 $f$ 需要不同的Oracle实现，但我们希望算法分析不依赖于具体函数。
3. 这让我们能比较"经典查询复杂度"与"量子查询复杂度"——展示量子优势。

**定义 1.3（查询复杂度）** 一个算法解决某问题的**查询复杂度**是它在最坏情况下调用Oracle的次数。

后续我们会反复看到：量子算法可以用更少的查询解决问题，这正是量子优势的体现。

**即时练习 1.2**

1. 证明 $O_f|x\rangle|y\rangle = |x\rangle|y\oplus f(x)\rangle$ 是幺正算符。
2. 如果 $f(x)=0$ 对所有 $x$ 成立，相位反冲的结果是什么？如果 $f(x)=1$ 对所有的 $x$ 成立呢？
3. 假设你想对 $f(x) \in \{0,1\}^2$（两比特输出）使用相位反冲，你会如何设置辅助寄存器？
4. 为什么标准Oracle不能是 $O_f|x\rangle = |f(x)\rangle$？请给出一个反例说明它可能不是幺正的。

---

## 1.3 Deutsch算法

### 1.3.1 问题定义

Deutsch算法是最简单的量子算法——它只处理 **1比特** 函数。但它完美展示了量子并行性和相位反冲如何协同工作，产生超越经典的能力。

**问题 1.1（Deutsch问题）** 给定一个未知的布尔函数 $f: \{0,1\} \to \{0,1\}$，判断 $f$ 是否是**常数函数**（constant）还是**平衡函数**（balanced）。

- **常数函数**：$f(0)=f(1)$，即 $f(0)=f(1)=0$ 或 $f(0)=f(1)=1$。
- **平衡函数**：$f(0)\neq f(1)$，即 $f(0)=0, f(1)=1$ 或 $f(0)=1, f(1)=0$。

**经典解法**：需要查询 $f$ 两次（先计算 $f(0)$，再计算 $f(1)$，然后比较）。如果只能查询一次，经典解法无法确定 $f$ 是否恒定。

**量子解法**：Deutsch算法只用**一次**Oracle查询就能确定答案。下面我们一步步推导。

### 1.3.2 电路概览

Deutsch算法的量子电路：

```
|0⟩ ──┤H├──■──┤H├── M ── 输出
         │
|1⟩ ──┤H├──⊕───────（丢弃）
```

其中 $\oplus$ 表示标准Oracle $O_f$，与CNOT门符号相同是因为CNOT正是 $f(x)=x$ 时的特例。

### 1.3.3 步态变化推导

我们追踪每一步的量子态。

**初始态**：

$$
|\psi_0\rangle = |0\rangle \otimes |1\rangle
$$

> 注意辅助比特初始化为 $|1\rangle$ 而不是 $|0\rangle$——这是为了后面通过Hadamard门得到 $|-\rangle$。

**第1步：Hadamard门**

对两个量子比特分别施加 $H$ 门：

$$
|\psi_1\rangle = (H|0\rangle) \otimes (H|1\rangle) = \frac{|0\rangle+|1\rangle}{\sqrt{2}} \otimes \frac{|0\rangle-|1\rangle}{\sqrt{2}}
$$

展开为：

$$
|\psi_1\rangle = \frac{1}{2}\left(|0\rangle+|1\rangle\right)\left(|0\rangle-|1\rangle\right) = \frac{1}{2}\left(|0\rangle|0\rangle - |0\rangle|1\rangle + |1\rangle|0\rangle - |1\rangle|1\rangle\right)
$$

**第2步：Oracle查询 $O_f$**

$O_f$ 的作用是 $O_f|x\rangle|y\rangle = |x\rangle|y\oplus f(x)\rangle$。

利用相位反冲的结论（见1.2.3节）：

$$
O_f|x\rangle|-\rangle = (-1)^{f(x)}|x\rangle|-\rangle
$$

其中 $|-\rangle = \frac{|0\rangle-|1\rangle}{\sqrt{2}}$。

因此：

$$
|\psi_2\rangle = O_f|\psi_1\rangle = \frac{1}{\sqrt{2}}\left[(-1)^{f(0)}|0\rangle + (-1)^{f(1)}|1\rangle\right] \otimes \frac{|0\rangle-|1\rangle}{\sqrt{2}}
$$

辅助寄存器部分保持不变（仍然是 $|-\rangle$），但它的相位已经反冲到了主寄存器上。

现在分两种情况：

**情况A：$f$ 是常数函数**，即 $f(0)=f(1)$。

- 如果 $f(0)=f(1)=0$，则 $(-1)^{f(0)} = (-1)^{f(1)} = 1$，所以：

$$
|\psi_2\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle + |1\rangle\right) \otimes |-\rangle
$$

- 如果 $f(0)=f(1)=1$，则 $(-1)^{f(0)} = (-1)^{f(1)} = -1$，所以：

$$
|\psi_2\rangle = \frac{1}{\sqrt{2}}\left(-|0\rangle - |1\rangle\right) \otimes |-\rangle = -\frac{1}{\sqrt{2}}\left(|0\rangle + |1\rangle\right) \otimes |-\rangle
$$

  这里全局相位 $-1$ 不影响测量结果，所以两种情况在测量上不可区分——都是 $|+\rangle = \frac{|0\rangle+|1\rangle}{\sqrt{2}}$。

**情况B：$f$ 是平衡函数**，即 $f(0)\neq f(1)$。

- 如果 $f(0)=0, f(1)=1$，则 $(-1)^{f(0)} = 1$，$(-1)^{f(1)} = -1$：

$$
|\psi_2\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle - |1\rangle\right) \otimes |-\rangle
$$

- 如果 $f(0)=1, f(1)=0$，则 $(-1)^{f(0)} = -1$，$(-1)^{f(1)} = 1$：

$$
|\psi_2\rangle = \frac{1}{\sqrt{2}}\left(-|0\rangle + |1\rangle\right) \otimes |-\rangle = -\frac{1}{\sqrt{2}}\left(|0\rangle - |1\rangle\right) \otimes |-\rangle
$$

  全局相位 $-1$ 再次不影响测量，所以情况B都是 $|-\rangle = \frac{|0\rangle-|1\rangle}{\sqrt{2}}$。

**第3步：第二个Hadamard门**

对主寄存器施加 $H$ 门：

- **常数函数**（主寄存器态为 $|+\rangle$）：

$$
H|+\rangle = H\frac{|0\rangle+|1\rangle}{\sqrt{2}} = \frac{1}{\sqrt{2}}\left(\frac{|0\rangle+|1\rangle}{\sqrt{2}} + \frac{|0\rangle-|1\rangle}{\sqrt{2}}\right) = |0\rangle
$$

- **平衡函数**（主寄存器态为 $|-\rangle$）：

$$
H|-\rangle = H\frac{|0\rangle-|1\rangle}{\sqrt{2}} = \frac{1}{\sqrt{2}}\left(\frac{|0\rangle+|1\rangle}{\sqrt{2}} - \frac{|0\rangle-|1\rangle}{\sqrt{2}}\right) = |1\rangle
$$

**第4步：测量**

在计算基下测量主寄存器：

- 如果测得 $|0\rangle$ → $f$ 是**常数函数**。
- 如果测得 $|1\rangle$ → $f$ 是**平衡函数**。

### 1.3.4 完整推导表格

下面的表格总结了每一步的状态变化：

| 步骤 | 操作 | 态（忽略辅助寄存器和全局相位） |
|------|------|-------------------------------|
| $\psi_0$ | 初始 | $\lvert 0\rangle$ |
| $\psi_1$ | $H^{\otimes 2}$ | $\frac{\lvert 0\rangle+\lvert 1\rangle}{\sqrt{2}}$ |
| $\psi_2$ | $O_f$（常数） | $\frac{\lvert 0\rangle+\lvert 1\rangle}{\sqrt{2}}$ |
| $\psi_2$ | $O_f$（平衡） | $\frac{\lvert 0\rangle-\lvert 1\rangle}{\sqrt{2}}$ |
| $\psi_3$ | $H$（常数） | $\lvert 0\rangle$ |
| $\psi_3$ | $H$（平衡） | $\lvert 1\rangle$ |
| $\psi_4$ | 测量 | 常数→0，平衡→1 |

### 1.3.5 为什么不需要第二次查询？

经典解法需要两次查询是因为它必须知道 $f(0)$ 和 $f(1)$ 各自的值。量子解法只用一次查询，因为它关心的**不是 $f(0)$ 和 $f(1)$ 的值，而是它们的异或** $f(0) \oplus f(1)$——即"是否相等"这个整体性质。

量子并行性在一次Oracle调用中同时获取了 $f(0)$ 和 $f(1)$。相位反冲将 $f(0) \oplus f(1)$ 编码到了相位中。第二个Hadamard门将这个相位信息转换为可测量的计算基信息。

### 1.3.6 重要认识

1. **Deutsch算法不是"快了一倍"**——它解决的是一类**经典必须两次查询**的问题。它展示了量子算法在查询复杂度上的优势。
2. **算法的核心不是量子并行性本身**——而是**并行性 + 干涉**。如果没有干涉（第二个Hadamard门），你无法从叠加态中提取任何有用信息。
3. **全局相位不影响测量**，但**相对相位**（比如 $|+\rangle$ 与 $|-\rangle$ 的区别）是干涉测量的关键。

**即时练习 1.3**

1. 如果辅助比特初始化为 $|0\rangle$ 而不是 $|1\rangle$，Deutsch算法还成立吗？为什么？
2. 画出 $f(0)=0, f(1)=1$ 时每一步的布洛赫球表示。
3. 证明 $H|+\rangle = |0\rangle$ 和 $H|-\rangle = |1\rangle$。
4. 如果Oracle被错误实现（例如 $O_f|x\rangle|y\rangle = |x\rangle|f(x)\rangle$ 而不是 $|x\rangle|y\oplus f(x)\rangle$），Deutsch算法还能工作吗？

---

## 1.4 Deutsch-Jozsa算法

### 1.4.1 问题定义

Deutsch-Jozsa算法是Deutsch算法的**一般化**。它将函数从1比特推广到 $n$ 比特。

**问题 1.2（Deutsch-Jozsa问题）** 给定一个未知的布尔函数 $f: \{0,1\}^n \to \{0,1\}$，承诺 $f$ 要么是**常数函数**（在所有 $2^n$ 个输入上输出相同值），要么是**平衡函数**（在恰好一半输入上输出0，另一半输出1）。判断 $f$ 是常数还是平衡。

**经典解法**：最坏情况下需要 $2^{n-1}+1$ 次查询——如果你查了 $2^{n-1}+1$ 次都得到同一个值，才能确定它是常数函数（因为平衡函数不可能在超过一半的输入上输出相同值）。

**量子解法**：Deutsch-Jozsa算法只用**一次**Oracle查询！

### 1.4.2 电路概览

Deutsch-Jozsa算法的量子电路：

```
|0⟩ ————┤H├── /^n ──■── /^n ──┤H├── M ── 输出
                      │
|1⟩ ——————┤H├────────⊕——————————（丢弃）
```

其中 $/^n$ 表示 $n$ 比特的量子总线。

### 1.4.3 步态变化推导

**初始态**：

$$
|\psi_0\rangle = |0\rangle^{\otimes n} \otimes |1\rangle
$$

**第1步：Hadamard门**

对前 $n$ 个量子比特施加 $H^{\otimes n}$，对辅助比特施加 $H$：

$$
|\psi_1\rangle = H^{\otimes n}|0\rangle^{\otimes n} \otimes H|1\rangle
$$

其中：

$$
H^{\otimes n}|0\rangle^{\otimes n} = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} |x\rangle
$$

辅助比特：$H|1\rangle = \frac{|0\rangle-|1\rangle}{\sqrt{2}} = |-\rangle$。

所以：

$$
|\psi_1\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} |x\rangle \otimes |-\rangle
$$

**第2步：Oracle查询**

利用相位反冲（同样地，辅助比特在 $|-\rangle$ 态）：

$$
O_f |\psi_1\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} (-1)^{f(x)} |x\rangle \otimes |-\rangle
$$

辅助寄存器仍然是 $|-\rangle$，我们可以忽略它继续关注主寄存器：

$$
|\psi_2\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} (-1)^{f(x)} |x\rangle
$$

**第3步：第二个Hadamard变换**

这是关键步骤。对 $n$ 量子比特的态施加 $H^{\otimes n}$：

$$
|\psi_3\rangle = H^{\otimes n}|\psi_2\rangle = H^{\otimes n} \left( \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} (-1)^{f(x)} |x\rangle \right)
$$

我们需要一个恒等式：Hadamard门在 $n$ 比特上的作用

$$
H^{\otimes n} |x\rangle = \frac{1}{\sqrt{2^n}} \sum_{z=0}^{2^n-1} (-1)^{x \cdot z} |z\rangle
$$

其中 $x \cdot z = \sum_{i=0}^{n-1} x_i z_i \pmod 2$ 是比特向量的点积（模2）。

代入：

$$
\begin{aligned}
|\psi_3\rangle &= \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} (-1)^{f(x)} \left( H^{\otimes n} |x\rangle \right) \\
&= \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} (-1)^{f(x)} \left( \frac{1}{\sqrt{2^n}} \sum_{z=0}^{2^n-1} (-1)^{x \cdot z} |z\rangle \right) \\
&= \frac{1}{2^n} \sum_{z=0}^{2^n-1} \sum_{x=0}^{2^n-1} (-1)^{f(x) + x \cdot z} |z\rangle
\end{aligned}
$$

**第4步：测量**

我们测量前 $n$ 个量子比特。关注 $|z\rangle = |0\rangle^{\otimes n}$（即全零态）的概率幅：

$$
\alpha_{0} = \frac{1}{2^n} \sum_{x=0}^{2^n-1} (-1)^{f(x) + x \cdot 0} = \frac{1}{2^n} \sum_{x=0}^{2^n-1} (-1)^{f(x)}
$$

因为 $x \cdot 0 = 0$。

现在分两种情况：

- **如果 $f$ 是常数函数**：设 $f(x) = c$（$c=0$ 或 $1$）。则 $(-1)^{f(x)} = (-1)^c$ 对所有 $x$ 相同：

$$
\alpha_0 = \frac{1}{2^n} \sum_{x=0}^{2^n-1} (-1)^c = (-1)^c
$$

  所以 $|\alpha_0|^2 = 1$。测量得到 $|0\rangle^{\otimes n}$ 的概率为 **1**。

- **如果 $f$ 是平衡函数**：恰好在 $2^{n-1}$ 个输入上 $f(x)=0$，在另外 $2^{n-1}$ 个输入上 $f(x)=1$。所以：

$$
\alpha_0 = \frac{1}{2^n} \left( \sum_{x:f(x)=0} 1 + \sum_{x:f(x)=1} (-1) \right) = \frac{1}{2^n} (2^{n-1} - 2^{n-1}) = 0
$$

  测量得到 $|0\rangle^{\otimes n}$ 的概率为 **0**。换句话说，你**不可能**测到全零态。

### 1.4.4 算法判决规则

- 测量结果为 $|0\rangle^{\otimes n}$（全零）→ **常数函数**。
- 测量结果不是全零 → **平衡函数**。

一次查询，确定判决。这个判决是**确定性**的（概率为1），不是概率性的——前提是Oracle的实现是完美的。

### 1.4.5 为什么称"确定性"算法？

Deutsch-Jozsa算法给出正确答案的概率是100%（在无噪声的理想情况下）。对比随机化经典算法：如果随机采样 $k$ 个输入且全部相同，仍有可能误判——平衡函数也有小概率被全部采样为0或1。经典随机化算法需要 $O(\log \epsilon^{-1})$ 次查询才能达到置信度 $1-\epsilon$，而量子算法一次搞定。

### 1.4.6 完整电路示例：n=2

取 $n=2$，函数 $f$ 定义如下（平衡函数的例子）：

| $x$ | $f(x)$ |
|-----|--------|
| 00 | 0 |
| 01 | 1 |
| 10 | 1 |
| 10 | 0 |

步态追踪：

1. 初始：$|00\rangle \otimes |1\rangle$
2. 第一次 Hadamard：$\frac{1}{2}(|00\rangle+|01\rangle+|10\rangle+|11\rangle) \otimes |-\rangle$
3. Oracle：$\frac{1}{2}(|00\rangle - |01\rangle - |10\rangle + |11\rangle) \otimes |-\rangle$
   （因为 $f(00)=0 \to +$，$f(01)=1 \to -$，$f(10)=1 \to -$，$f(11)=0 \to +$，注意最后 $f(11)=0$ 所以是 $+$）
4. 第二次 Hadamard：$H^{\otimes 2}$ 作用后计算概率幅。

### 1.4.7 算法复杂度总结

| 算法 | 经典确定性 | 经典随机化 | 量子 |
|------|-----------|-----------|------|
| 查询次数 | $2^{n-1}+1$ | $O(\log\epsilon^{-1})$ | 1 |
| 错误率 | 0 | $\epsilon$ | 0（理想） |

Deutsch-Jozsa算法是指数级加速——从 $O(2^n)$ 到 $O(1)$。但它解决的问题本身比较特殊（承诺了要么常数要么平衡），所以它的主要意义是**概念证明**：量子计算机确实可以在某些问题上超越经典计算机。

**即时练习 1.4**

1. 如果 $f$ 是常数函数且 $f(x)=1$ 对所有 $x$ 成立，算法最后测量得到全零的概率是多少？
2. 证明 $H^{\otimes n} |x\rangle = \frac{1}{\sqrt{2^n}} \sum_{z} (-1)^{x \cdot z} |z\rangle$。
3. 如果Oracle承诺 $f$ 要么是常数，要么是奇数个1的函数（即 $|f^{-1}(1)|$ 奇数），Deutsch-Jozsa算法还能区分吗？
4. 在平衡函数的情况下，为什么测得 $|0\rangle^{\otimes n}$ 的概率精确为0？如果噪声使测量结果有1%的误差，算法还可靠吗？

---

## 1.5 Bernstein-Vazirani算法

### 1.5.1 问题定义

Bernstein-Vazirani（BV）算法解决的是一个**线性函数学习**问题。

**问题 1.3（Bernstein-Vazirani问题）** 给定一个未知函数 $f: \{0,1\}^n \to \{0,1\}$，承诺存在一个隐藏字符串 $s \in \{0,1\}^n$，使得：

$$
f(x) = s \cdot x \pmod 2 = \bigoplus_{i=0}^{n-1} s_i x_i
$$

其中 $\bigoplus$ 表示异或（模2加法）。目标：找出 $s$。

换句话说，$f(x)$ 是 $x$ 与隐藏向量 $s$ 的点积（模2）。

**经典解法**：对于每个比特位置 $i$，输入 $x$ 只在第 $i$ 位为1（其余为0），查询 $f(x)$ 得到 $s_i$。需要 $n$ 次查询。

**量子解法**：Bernstein-Vazirani算法只用**1次**Oracle查询即可找出全部 $n$ 个比特！

### 1.5.2 电路

BV算法的量子电路：

```
|0⟩ ————┤H├── /^n ──■── /^n ──┤H├── M ── 输出 s
                      │
|1⟩ ——————┤H├────────⊕——————————（丢弃）
```

是的——电路结构与Deutsch-Jozsa算法**完全相同**！区别仅在Oracle的内部实现（$f$ 的形式不同）和输出的解释上。

### 1.5.3 步态变化推导

**初始态**：

$$
|\psi_0\rangle = |0\rangle^{\otimes n} \otimes |1\rangle
$$

**第1步：Hadamard门**

$$
|\psi_1\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} |x\rangle \otimes |-\rangle
$$

**第2步：Oracle查询**

因为 $f(x) = s \cdot x$，相位反冲给出：

$$
|\psi_2\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} (-1)^{s \cdot x} |x\rangle \otimes |-\rangle
$$

忽略辅助寄存器：

$$
|\psi_2\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} (-1)^{s \cdot x} |x\rangle
$$

**第3步：第二个Hadamard变换**

$$
|\psi_3\rangle = H^{\otimes n} |\psi_2\rangle = H^{\otimes n} \left( \frac{1}{\sqrt{2^n}} \sum_{x} (-1)^{s \cdot x} |x\rangle \right)
$$

利用Hadamard变换的恒等式 $H^{\otimes n}|x\rangle = \frac{1}{\sqrt{2^n}} \sum_z (-1)^{x \cdot z}|z\rangle$：

$$
\begin{aligned}
|\psi_3\rangle &= \frac{1}{\sqrt{2^n}} \sum_{x} (-1)^{s \cdot x} \left( \frac{1}{\sqrt{2^n}} \sum_{z} (-1)^{x \cdot z}|z\rangle \right) \\
&= \frac{1}{2^n} \sum_z \sum_x (-1)^{(s \oplus z) \cdot x} |z\rangle
\end{aligned}
$$

其中 $\oplus$ 表示按位异或（因为 $(-1)^{s\cdot x}(-1)^{x \cdot z} = (-1)^{(s \oplus z) \cdot x}$）。

现在利用一个关键恒等式：

$$
\frac{1}{2^n} \sum_{x \in \{0,1\}^n} (-1)^{y \cdot x} = \begin{cases}
1, & y = 0 \\
0, & y \neq 0
\end{cases}
$$

这是因为当 $y \neq 0$ 时，恰好一半的 $x$ 使 $y \cdot x = 0$，另一半使 $y \cdot x = 1$。

令 $y = s \oplus z$，则 $\sum_x (-1)^{(s \oplus z) \cdot x} = 0$ 除非 $s \oplus z = 0$ 即 $z = s$。

因此：

$$
|\psi_3\rangle = |s\rangle
$$

**测量**得到的就是 $s$ 本身！

### 1.5.4 直观理解

BV算法的魔幻之处在于：一次Oracle查询就把 $s$ 的所有 $n$ 个比特信息"编码"到了量子态上，然后通过Hadamard变换把它们读出。

为什么会这样？因为 $f(x) = s \cdot x$ 具有**线性结构**——$f(x)$ 完全由 $s$ 决定。Hadamard变换恰好是"从相位空间到计算基空间"的桥梁：

- Oracle把 $s$ 嵌入到**相位** $(-1)^{s \cdot x}$ 上。
- 第二个 $H^{\otimes n}$ 把这个**相位模式**翻译回**计算基** $|s\rangle$。

**重要认识**：BV算法不是"把 $n$ 次查询并行化了"——它是**用一次查询提取了全部信息**，因为信息以 $(-1)^{s \cdot x}$ 这种干涉友好的方式编码。

### 1.5.5 算法复杂度总结

| 算法 | 经典 | 量子 |
|------|------|------|
| 查询次数 | $n$ | 1 |
| 加速比 | — | $n$ 倍 |

BV算法给出了量子优越性的**严格证明**：经典查询复杂度下界为 $\Omega(n)$，而量子查询复杂度为 $O(1)$。这是一个多项式加速（线性 vs 常数）。

### 1.5.6 与Deutsch-Jozsa的关系

- DJ算法和BV算法的**电路结构完全相同**。
- DJ算法区分"常数"和"平衡"这两类函数——全局性质。
- BV算法找出一个隐藏字符串——具体参数。
- 两者都利用了Hadamard变换从相位信息中提取答案。

理解了这个联系，你就理解了早期量子算法的核心设计模式：**相位编码 + 干涉提取**。

**即时练习 1.5**

1. 如果隐藏字符串 $s = 101$（$n=3$），列出所有 $2^3=8$ 个输入对应的 $f(x)$，并验证 $f(x) = s \cdot x$。
2. 证明恒等式 $\frac{1}{2^n} \sum_{x} (-1)^{y \cdot x} = \delta_{y,0}$。
3. 如果Oracle的承诺不成立（即 $f$ 不是 $s \cdot x$ 的形式），BV算法会输出什么？
4. 比较BV算法和DJ算法：为什么同样的电路解决了两个不同的问题？

---

## 1.6 Simon算法

### 1.6.1 问题定义

Simon算法是第一个展示量子计算机**指数级加速**的算法（相对于经典随机化算法）。它也是Shor算法的重要前身——Shor的周期发现思想直接受Simon算法启发。

**问题 1.4（Simon问题）** 给定一个函数 $f: \{0,1\}^n \to \{0,1\}^n$，承诺存在一个**非零**的隐藏字符串 $s \in \{0,1\}^n$（$s \neq 0^n$），使得对任意 $x, y \in \{0,1\}^n$：

$$
f(x) = f(y) \iff x \oplus y \in \{0^n, s\}
$$

换句话说，$f$ 是**2对1**的——除了 $x$ 和 $x \oplus s$ 映射到相同的输出外，没有其他碰撞。目标：找出 $s$。

**等价表述**：$f$ 具有"周期" $s$，即 $f(x) = f(x \oplus s)$ 对所有 $x$ 成立，且周期是精确的2对1（没有更小的周期）。

**经典解法**：最坏情况下需要 $\Theta(2^{n/2})$ 次查询（生日悖论——随机采样直到发现碰撞）。经典确定性算法可能需要 $2^{n-1}+1$ 次。

**量子解法**：Simon算法期望 $O(n)$ 次Oracle查询，且只需要 $O(n^2)$ 次后处理。

### 1.6.2 电路概览

Simon算法多次运行以下子电路，每次产生一个关于 $s$ 的线性方程：

```
|0⟩ ————┤H├── /^n ──■── /^n ──┤H├── M ── 得到随机 z（满足 z·s=0）
                      │
|0⟩ ————┤H├──────────⊕────────── M ── 丢弃（或用于验证）
```

注意和DJ、BV的区别：Simon算法的Oracle输出是 $n$ 比特的（$f(x)$ 也是 $n$ 比特的），因此需要两个 $n$ 量子比特的寄存器。

### 1.6.3 单次子电路推导

**初始态**：

$$
|\psi_0\rangle = |0\rangle^{\otimes n} \otimes |0\rangle^{\otimes n}
$$

**第1步：第一个寄存器上的Hadamard**

$$
|\psi_1\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} |x\rangle \otimes |0\rangle^{\otimes n}
$$

**第2步：Oracle查询**

Simon算法的Oracle实现为：

$$
O_f |x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle
$$

所以：

$$
|\psi_2\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} |x\rangle |f(x)\rangle
$$

这里我们没有把辅助寄存器设为 $|-\rangle$——这与DJ和BV不同！Simon算法不使用相位反冲（至少在这个标准表述中），而是直接利用纠缠。

**第3步：第一个寄存器上的第二个Hadamard**

$$
|\psi_3\rangle = H^{\otimes n} \otimes I^{\otimes n} |\psi_2\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} \left( H^{\otimes n}|x\rangle \right) |f(x)\rangle
$$

$$
|\psi_3\rangle = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} \left( \frac{1}{\sqrt{2^n}} \sum_{z=0}^{2^n-1} (-1)^{x \cdot z} |z\rangle \right) |f(x)\rangle
$$

$$
|\psi_3\rangle = \frac{1}{2^n} \sum_{z=0}^{2^n-1} \sum_{x=0}^{2^n-1} (-1)^{x \cdot z} |z\rangle |f(x)\rangle
$$

**第4步：测量第一个寄存器**

测量第一个寄存器得到某个 $z$ 值的概率是多少？

我们对第二个寄存器（$|f(x)\rangle$）求部分迹，得到第一个寄存器的约化密度矩阵。但更直接的方法是：对于固定的 $z$，我们关注叠加态中 $|z\rangle$ 分量的"总权重"。

因为 $f$ 是2对1的（$f(x)=f(x\oplus s)$），每个输出值恰好对应两个输入 $x$ 和 $x\oplus s$。对于固定的输出值 $y$：

$$ \sum_{x: f(x)=y} (-1)^{x \cdot z} |z\rangle |y\rangle = \left[(-1)^{x_0 \cdot z} + (-1)^{(x_0 \oplus s) \cdot z}\right] |z\rangle |y\rangle $$
其中 $x_0$ 是某个代表元。括号内的因子为：

$$
(-1)^{x_0 \cdot z}\left[1 + (-1)^{s \cdot z}\right]
$$

**关键条件**：

- 如果 $s \cdot z = 0$（模2），则 $1 + (-1)^0 = 2$，两个分量**相长干涉**。
- 如果 $s \cdot z = 1$（模2），则 $1 + (-1)^1 = 0$，两个分量**相消干涉**。

因此，在测量时，只有那些满足 $s \cdot z = 0$ 的 $z$ 值会被观察到。满足 $s \cdot z = 1$ 的 $z$ 概率为零。

### 1.6.4 多次运行与经典后处理

一次运行Simon子电路得到一个随机的 $z$，满足：

$$
s \cdot z = 0 \pmod 2
$$

这是一个关于 $s$ 的**线性方程**。$s$ 有 $n$ 个未知比特（$s_0, s_1, \ldots, s_{n-1}$），所以我们需要大约 $n$ 个独立的线性方程才能唯一确定 $s$。

每次运行子电路：

1. 制备叠加态。
2. 调用一次Oracle。
3. 施加 $H^{\otimes n}$。
4. 测量第一个寄存器，得到 $z_i$。
5. 记录方程 $s \cdot z_i = 0$。

收集到 $O(n)$ 个线性无关的方程后，用高斯消元法解线性方程组，得到 $s$。

**需要多少次运行？** 期望的独立方程个数为 $n$ 左右，所以总的Oracle查询次数为 $O(n)$。每次查询产生一个 $z$ 的概率分布均匀分布在 $2^{n-1}$ 个满足 $s \cdot z = 0$ 的 $z$ 上。

### 1.6.5 算法总流程

```
1. 重复以下操作直到收集到 n-1 个独立的线性方程:
   a) 制备 |0⟩^{⊗n}|0⟩^{⊗n}
   b) 施加 H^{⊗n} 在第一个寄存器
   c) 施加 Oracle O_f
   d) 施加 H^{⊗n} 在第一个寄存器
   e) 测量第一个寄存器，得到 z
   f) 记录方程 z·s = 0
2. 解线性方程组得到 s
3. 验证: 随机选择 x 验证 f(x) = f(x⊕s)
```

**验证步骤**：如果解出的 $s=0^n$（无意义）或验证失败，则重新运行。

### 1.6.6 复杂度分离——指数级加速

| 算法 | 经典（确定性） | 经典（随机化） | 量子 |
|------|--------------|--------------|------|
| Oracle查询次数 | $2^{n-1}+1$ | $\Theta(2^{n/2})$ | $O(n)$ |
| 总复杂度 | $O(2^n)$ | $O(2^{n/2})$ | $O(n^2)$ |

这是**指数级加速**——Simon算法证明了存在一个Oracle问题，量子计算机可以用多项式资源解决，而经典计算机需要指数资源。

**重要认识**：Simon算法展示的不是"更快的计算"，而是**全新的计算范式**——利用量子叠加和干涉，以经典无法实现的方式提取函数的全局结构信息。

### 1.6.7 Simon算法与Shor算法的联系

Simon算法是Shor算法（因式分解）的直接思想先驱：

| Simon | Shor |
|-------|------|
| 寻找 $f$ 的周期 $s$（模2加法） | 寻找 $f(x)=a^x \bmod N$ 的周期 $r$ |
| 函数是2对1的 | 函数是 $r$ 对1的 |
| 用 $H^{\otimes n}$ 提取周期 | 用QFT提取周期 |
| $O(n)$ 次查询 | $O(\text{poly}(n))$ 次查询 |
| 周期隐藏在模2加法中 | 周期隐藏在模 $N$ 乘法中 |

Shor算法的核心也是周期发现——只是从"模2加法"推广到了"模 $N$ 乘法"。而模 $N$ 下的周期发现需要用**量子傅里叶变换**代替Hadamard变换。

**即时练习 1.6**

1. 对于 $n=2$，$s=11$，写出 $f$ 的一个具体定义（满足 $f(x)=f(x\oplus 11)$ 且2对1）。
2. 证明如果 $s \cdot z = 1$，则 $(-1)^{x\cdot z} + (-1)^{(x\oplus s)\cdot z} = 0$。
3. 收集 $n-1$ 个独立方程为什么还不足以唯一确定 $s$？还需要什么信息？（提示：$s=0^n$ 总是满足所有方程）
4. 为什么Simon算法不能直接用于破解密码学？它的承诺条件（2对1）在现实中很难天然满足。

---

## 1.7 量子傅里叶变换（QFT）

### 1.7.1 从经典傅里叶变换到量子傅里叶变换

**经典离散傅里叶变换（DFT）** 将长度为 $N$ 的复向量 $(x_0, x_1, \ldots, x_{N-1})$ 变换为 $(y_0, y_1, \ldots, y_{N-1})$：

$$
y_k = \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x_j \omega_N^{jk}, \quad \omega_N = e^{2\pi i / N}
$$

经典DFT的时间复杂度为 $O(N \log N)$（FFT）。但经典计算中，$N$ 个数据需要 $N$ 个存储单元。

**量子傅里叶变换（QFT）** 是DFT在量子计算中的对应。它作用在量子态上——一个 $n$ 量子比特的态向量有 $N=2^n$ 个分量。QFT只需要 $O(n^2)$ 个门（约 $n(n+1)/2$ 个门），而经典FFT需要 $O(N \log N) = O(2^n n)$ 次操作——这是**指数级加速**！

但注意：QFT的输出是编码在量子态的概率幅中的，你不能直接"读出"所有 $N$ 个分量——测量只能得到 $n$ 比特的信息。所以QFT的加速体现在**作为子程序嵌入到其他算法**中（如相位估计、Shor算法），而不是独立的数据处理工具。

**定义 1.4（量子傅里叶变换）** QFT 是定义在 $N=2^n$ 维Hilbert空间上的幺正算符 $F_N$：

$$
F_N |j\rangle = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} e^{2\pi i j k / N} |k\rangle
$$

作用于任意叠加态：

$$
F_N \left( \sum_{j=0}^{N-1} x_j |j\rangle \right) = \sum_{k=0}^{N-1} y_k |k\rangle, \quad y_k = \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x_j e^{2\pi i j k / N}
$$

### 1.7.2 矩阵形式

QFT的矩阵元为：

$$
[F_N]_{jk} = \frac{1}{\sqrt{N}} e^{2\pi i j k / N}
$$

其中 $j,k = 0, 1, \ldots, N-1$。

**例 1.3（$n=1$, $N=2$）**：

$$
F_2 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & e^{\pi i} \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = H
$$

是的——单比特的QFT就是Hadamard门！这说明QFT是Hadamard门在更大维度上的推广。

**例 1.4（$n=2$, $N=4$）**：

$$
F_4 = \frac{1}{2} \begin{pmatrix}
1 & 1 & 1 & 1 \\
1 & \omega_4 & \omega_4^2 & \omega_4^3 \\
1 & \omega_4^2 & \omega_4^4 & \omega_4^6 \\
1 & \omega_4^3 & \omega_4^6 & \omega_4^9
\end{pmatrix}
= \frac{1}{2} \begin{pmatrix}
1 & 1 & 1 & 1 \\
1 & i & -1 & -i \\
1 & -1 & 1 & -1 \\
1 & -i & -1 & i
\end{pmatrix}
$$

其中 $\omega_4 = e^{2\pi i / 4} = i$。

### 1.7.3 乘积表示（二进制分数表示）

QFT有一个极为重要的**乘积表示**（product representation），它是电路实现的基础。

将整数 $j$ 表示为 $n$ 比特二进制数 $j = j_1 j_2 \ldots j_n$，其中 $j_1$ 是最高位（MSB）：

$$
j = j_1 2^{n-1} + j_2 2^{n-2} + \cdots + j_n 2^0
$$

那么QFT可以写成：

$$
F_N |j\rangle = \frac{1}{\sqrt{N}} \bigotimes_{l=1}^{n} \left( |0\rangle + e^{2\pi i j / 2^l} |1\rangle \right)
$$

或者更明确地：

$$
F_N |j\rangle = \frac{1}{\sqrt{2^n}} \left( |0\rangle + e^{2\pi i 0.j_n} |1\rangle \right) \left( |0\rangle + e^{2\pi i 0.j_{n-1}j_n} |1\rangle \right) \cdots \left( |0\rangle + e^{2\pi i 0.j_1 j_2 \ldots j_n} |1\rangle \right)
$$

其中 $0.j_1 j_2 \ldots j_k = \frac{j_1}{2} + \frac{j_2}{4} + \cdots + \frac{j_k}{2^k}$ 表示二进制分数。

**推导**：

$$
\begin{aligned}
F_N |j\rangle &= \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} e^{2\pi i j k / N} |k\rangle \\
&= \frac{1}{\sqrt{N}} \sum_{k_1=0}^{1} \cdots \sum_{k_n=0}^{1} e^{2\pi i j (\sum_{l=1}^n k_l 2^{-l})} |k_1 \ldots k_n\rangle \\
&= \frac{1}{\sqrt{N}} \bigotimes_{l=1}^{n} \left( \sum_{k_l=0}^{1} e^{2\pi i j k_l 2^{-l}} |k_l\rangle \right) \\
&= \frac{1}{\sqrt{N}} \bigotimes_{l=1}^{n} \left( |0\rangle + e^{2\pi i j / 2^l} |1\rangle \right)
\end{aligned}
$$

### 1.7.4 QFT的量子电路

基于乘积表示，QFT的电路实现如下：

**步骤**：对于每个量子比特 $l$（从 $l=1$ 最高位到 $l=n$ 最低位，或反向），施加：

1. 一个Hadamard门。
2. 一系列受控 $R_k$ 旋转门（以低位比特为控制位）。

受控旋转门定义为：

$$
R_k = \begin{pmatrix} 1 & 0 \\ 0 & e^{2\pi i / 2^k} \end{pmatrix}
$$

其中 $k = 2, 3, \ldots, n-l+1$。

**QFT电路图**（$n=3$）：

```
|j₁⟩ ──┤H├──•──────•─────── | 输出比特1
            │      │
|j₂⟩ ──────⊕──┤H├─•─────── | 输出比特2
                  │
|j₃⟩ ────────────⊕──┤H├─── | 输出比特3

其中 •—⊕ 表示受控 R_k 门
```

更精确的按位表示（从最低位开始构建）：

```
     n=3 的 QFT 电路（标准排序）
     
|j₁⟩ ──┤H├──R₂──R₃─────────────────── |k₁⟩（最高位）
            ↓    ↓
|j₂⟩ ──⊕──────┤H├──R₂──────────────── |k₂⟩
            ↓         ↓
|j₃⟩ ──⊕──────⊕───────┤H├─────────── |k₃⟩（最低位）
```

其中：

- $H$ 是Hadamard门。
- $R_k = \begin{pmatrix} 1 & 0 \\ 0 & e^{2\pi i / 2^k} \end{pmatrix}$，控制位来自更低位的量子比特。
- 输出比特的顺序通常是反转的，需要SWAP门调整。

### 1.7.5 受控旋转门与电路深度

**受控 $R_k$ 门的展开**：

$$
CR_k = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & e^{2\pi i / 2^k}
\end{pmatrix}
$$

对于大 $k$（即小角度旋转），$R_k$ 门接近单位矩阵。在实际实现中，当 $k > O(\log n)$ 时，这些旋转可以近似忽略（因为 $e^{2\pi i / 2^k} \approx 1$ 对 $k$ 很大时成立）。这引出了**近似QFT**的概念——一种更高效的变体。

### 1.7.6 逆QFT

逆QFT（$F_N^\dagger$）是QFT的逆变换。因为QFT是幺正的，$F_N^\dagger = F_N^{-1}$：

$$
F_N^\dagger |k\rangle = \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} e^{-2\pi i j k / N} |j\rangle
$$

逆QFT的电路与QFT方向相反：从最低位开始，先做受控旋转，再做Hadamard。

逆QFT在量子相位估计（QPE）中至关重要——它把相位信息从频率域转换回计算基。

### 1.7.7 QFT的量子门复杂度

QFT电路需要：

- $n$ 个Hadamard门。
- $\frac{n(n-1)}{2}$ 个受控旋转门（$CR_k$，$k=2,\ldots,n$）。
- 约 $n/2$ 个SWAP门（用于反转输出比特顺序）。

总门数：$O(n^2)$。对比经典FFT的 $O(N \log N) = O(2^n n)$：

| $n$ | $N=2^n$ | QFT门数 $O(n^2)$ | FFT操作数 $O(N \log N)$ |
|-----|---------|--------------------|--------------------------|
| 10 | 1024 | ~100 | ~10240 |
| 20 | 1,048,576 | ~400 | ~20,971,520 |
| 30 | ~10亿 | ~900 | ~30亿 |

QFT需要指数级更少的门操作——这是它作为量子算法子程序强大的原因。但再次强调：你不能直接读取QFT的"输出向量"——它的 $2^n$ 个概率幅只能通过测量间接获取。

### 1.7.8 QFT的应用

1. **量子相位估计（QPE）**：见第14章，QFT是QPE的核心组件。
2. **Shor因式分解算法**：Shor算法使用QFT来发现模指数函数的周期。
3. **量子计数**：结合Grover迭代和QPE来估计标记态的数量。
4. **哈密顿量模拟**：量子化学模拟经常使用QFT在位置和动量基之间切换。
5. **量子机器学习**：一些量子ML算法使用QFT提取特征。

### 1.7.9 从Hadamard到QFT

我们已经看到 $F_2 = H$。$F_4$ 与两个量子比特上的 $H^{\otimes 2}$ 有何不同？

- $H^{\otimes 2}$ 将 $|j_1 j_2\rangle$ 变为 $\frac{1}{2} \sum_{k_1,k_2} (-1)^{j_1 k_1 + j_2 k_2} |k_1 k_2\rangle$。
- $F_4$ 将 $|j\rangle$ 变为 $\frac{1}{2} \sum_k e^{2\pi i j k / 4} |k\rangle$。

区别在于**相位**：$H^{\otimes 2}$ 的相位只能是 $\pm 1$，而QFT的相位可以是 $e^{2\pi i / 4} = i$ 等复数根。这正是QFT比Hadamard变换更强大的原因——它提供了更丰富的相位编码能力。

**即时练习 1.7**

1. 写出 $n=3$ 的QFT矩阵（$8\times 8$ 矩阵的前两行）。
2. 验证对于 $n=1$，QFT矩阵就是Hadamard矩阵。
3. 证明QFT是幺正算符（即 $F_N^\dagger F_N = I$）。
4. 解释为什么QFT不能直接用于"加速傅里叶变换数据处理"——它的输出和经典FFT的输出有什么不同？

---

## 1.8 量子算术

### 1.8.1 为什么需要量子算术？

许多量子算法（Shor算法、Grover算法、量子化学模拟、量子优化）都需要在量子计算机上执行基本的算术运算——加法、减法、乘法、比较。这些运算是构建更复杂量子子程序的基础。

量子算术设计面临两个核心挑战：

1. **可逆性**：所有量子门必须酉（可逆）。经典算术门（如不可逆的AND）需要改造为可逆形式。
2. **辅助比特**：如果不保存中间结果，算术运算会丢失信息——必须引入辅助比特（ancilla）来保持可逆性。

### 1.8.2 量子加法器

**最简单加法器：CNOT加法**

对于两个单量子比特 $|a\rangle$ 和 $|b\rangle$：

$$
\text{CNOT} |a\rangle|b\rangle = |a\rangle|a \oplus b\rangle
$$

如果 $b$ 初始为 $|0\rangle$，则 CNOT 复制 $a$：$\text{CNOT}|a\rangle|0\rangle = |a\rangle|a\rangle$。但这不是"加法"——它是复制（不可克隆定理的"漏洞"？不——这只复制计算基态，不能复制叠加态）。

**全加器（Full Adder）**

一个量子全加器计算 $a + b + c_{\text{in}}$，输出和 $s$ 与进位 $c_{\text{out}}$。

使用**Toffoli门**（CCNOT）和CNOT门可以实现量子全加器：

```
|a⟩ ──────⊕──────────────────── |a⟩
          │
|b⟩ ──────⊕──────⊕──────────── |s⟩ = a⊕b⊕c_in
               │
|c_in⟩ ──•──────⊕──────────── |c_in⟩
         │
|0⟩ ─────⊕─────────────────── |c_out⟩

其中:
• 表示控制位
⊕ 表示目标位
第一个 Toffoli (•,•,⊕) 计算进位
后续 CNOT 计算和
```

更具体地，**QuMA 加法器**（Cuccaro等人，2004）是当前最常用的量子加法器之一，其门复杂度为 $O(n)$，仅需要 $n$ 个辅助比特（其中很多可以重用）。

**加法器的复杂度**

对于 $n$ 比特加法：

| 加法器类型 | Toffoli门数 | CNOT门数 | 辅助比特数 |
|-----------|------------|---------|-----------|
| 简单进位传播 | $O(n)$ | $O(n)$ | $O(n)$ |
| QuMA（进位前瞻） | $O(n)$ | $O(n)$ | $O(1)$ |
| 加法器树 | $O(\log n)$ 深度 | $O(n)$ | $O(n)$ |

### 1.8.3 量子乘法器

量子乘法器基于加法器的重复：$a \times b = \sum_{i} b_i (a \ll i)$，其中 $b_i$ 是 $b$ 的第 $i$ 位。

基本思路：

1. 对于 $b$ 的每一位 $b_i$，如果 $b_i = 1$，则把 $a$ 左移 $i$ 位后加到累加器中。
2. 使用受控加法器（当 $b_i=1$ 时执行加法，否则跳过）。
3. 每次加法由Toffoli门控制。

**量子乘法器的复杂度**：

- 门数：$O(n^2)$（因为 $n$ 次加法，每次 $O(n)$）。
- 辅助比特：$O(n)$。
- 深度：$O(n^2)$（可优化到 $O(n \log n)$ 使用加法器树）。

**例 1.5** 计算 $3 \times 3 = 9$（$n=2$）：

- $a=11_2=3$, $b=11_2=3$
- $b_0=1$：加 $a$（左移0位）= $11 \to$ 累加器 = $0011$
- $b_1=1$：加 $a$（左移1位）= $110 \to$ 累加器 = $0011 + 0110 = 1001_2 = 9$

### 1.8.4 量子比较器

量子比较器判断两个 $n$ 比特数 $a$ 和 $b$ 的大小关系。最常见的方案基于**减法**：计算 $a-b$，检查结果的符号位（最高位）。

**比较器电路**：

```
|a⟩ ──┤ 比较器 ├──── |a⟩（不变）
|b⟩ ──┤        ├──── |b⟩（不变）
|0⟩ ──┤        ├──── |c⟩（c=1 if a<b, else 0）
```

量子比较器使用借位减法（borrow-save subtraction），与加法器结构对称。

### 1.8.5 量子算术的可逆性约束

量子算术必须可逆意味着：

- 不能丢弃中间进位。
- 每个算术步骤必须使用辅助比特保存"垃圾信息"。
- 使用后需要**清理**（uncompute）辅助比特——通过逆向执行部分电路将辅助比特恢复为 $|0\rangle$。

**例 1.6（清理模式）**：

```
     ┌───┐     ┌───┐
|a⟩ ─┤   ├──■──┤   ├── |a⟩
     │ + │  │  │ + │
|b⟩ ─┤   ├──⊕──┤   ├── |b⟩
     └───┘     └───┘
|0⟩ ────────────      ── |0⟩（清理后）
```

先计算 $a+b$ 到辅助比特，复制结果，然后逆运算恢复辅助比特。这种"计算-复制-逆计算"模式是量子算术中的标准技巧。

### 1.8.6 量子算术的现状

目前（2020年代中期），量子加法器已经可以在50+量子比特的处理器上运行，但乘法器的实现仍需数百个门，在NISQ（含噪中等规模量子）设备上错误累积严重。未来的容错量子计算机（需要量子纠错）才能大规模运行量子算术。

**即时练习 1.8**

1. 用CNOT和Toffoli门实现一个1比特的全加器（输入 $a,b,c_{\text{in}}$，输出 $s, c_{\text{out}}$）。
2. 为什么量子算术必须是可逆的？不可逆的算术操作违反了量子力学的哪个公设？
3. 解释"计算-复制-逆计算"模式如何清理辅助比特。
4. 如果 $n=4$，设计一个计算 $a \times b$ 的量子乘法器草图（不需要门级细节）。

---

## 1.9 本章习题

### 基础题

**1.1** 量子并行性的本质是什么？它与经典并行计算的根本区别是什么？

**1.2** 解释为什么标准Oracle $O_f|x\rangle|y\rangle = |x\rangle|y\oplus f(x)\rangle$ 是幺正算符。如果改为 $O_f|x\rangle = |f(x)\rangle$ 为什么可能不是幺正的？

**1.3** 相位反冲中，为什么辅助寄存器必须初始化为 $|-\rangle$ 态？如果改为 $|+\rangle$ 态，推导会有什么变化？

**1.4** Deutsch算法中，如果Oracle的实现有错误——$O_f|x\rangle|y\rangle = |x\rangle|f(x)\rangle$（而不是 $|x\rangle|y\oplus f(x)\rangle$），算法还能正确区分常数和平衡函数吗？为什么？

**1.5** Deutsch-Jozsa算法中，证明如果 $f$ 是平衡函数，测量得到 $|0\rangle^{\otimes n}$ 的概率为0。

**1.6** Bernstein-Vazirani算法中，如果Oracle承诺的函数是 $f(x) = s \cdot x \oplus b$（其中 $b$ 是未知比特），一次Oracle查询还能找出 $s$ 吗？如果能，怎么改？如果不能，为什么？

**1.7** 证明恒等式 $\frac{1}{2^n}\sum_{x\in\{0,1\}^n} (-1)^{y\cdot x} = \delta_{y,0}$。

### 进阶题

**1.8** Simon算法中，证明每次运行子电路得到的 $z$ 满足 $s\cdot z = 0$ 的概率为1（即必然满足）。什么条件下观察不到有效的 $z$？

**1.9** 对于Simon算法的 $n=3$ 情况，隐藏字符串 $s=101$。列出一次运行后可能测到的所有 $z$ 值及其概率。

**1.10** 写出 $n=3$ 时QFT的乘积表示。验证乘积表示与定义 $\frac{1}{\sqrt{8}}\sum_{k=0}^{7} e^{2\pi i j k / 8}|k\rangle$ 等价。

**1.11** 画出 $n=4$ 的QFT电路图，标注所有 $R_k$ 门。

**1.12** 证明QFT是幺正算符（即 $F_N^\dagger F_N = I_N$）。

**1.13** 为什么Simon算法被称为"第一个展示指数级量子加速的算法"？它和Deutsch-Jozsa算法有什么本质不同？

### 拓展题

**1.14** **思考题**：考虑一个修改版的Deutsch-Jozsa问题——$f: \{0,1\}^n \to \{0,1\}$，承诺 $f$ 要么是常数，要么在恰好 $3/4$ 的输入上输出1（在 $1/4$ 上输出0）。设计一个量子算法区分这两种情况，分析你的算法需要的Oracle查询次数。

**1.15** **编程题**（使用Qiskit或Cirq）：实现Deutsch-Jozsa算法，在模拟器上测试常数函数 $f(x)=1$ 和平衡函数 $f(x)=x_0$（即只取输入第一位）。验证输出结果。

---

> **本章核心公式速查**
>
> | 概念 | 公式 |
> |------|------|
> | 量子并行性 | $U_f \frac{1}{\sqrt{2^n}}\sum_x |x\rangle = \frac{1}{\sqrt{2^n}}\sum_x |f(x)\rangle$ |
> | 相位反冲 | $O_f|x\rangle|-\rangle = (-1)^{f(x)}|x\rangle|-\rangle$ |
> | Hadamard变换 | $H^{\otimes n}|x\rangle = \frac{1}{\sqrt{2^n}}\sum_z (-1)^{x\cdot z}|z\rangle$ |
> | QFT定义 | $F_N|j\rangle = \frac{1}{\sqrt{N}}\sum_k e^{2\pi i j k / N}|k\rangle$ |
> | QFT乘积表示 | $F_N|j\rangle = \frac{1}{\sqrt{N}}\bigotimes_{l=1}^n (|0\rangle + e^{2\pi i j/2^l}|1\rangle)$ |
| 正交恒等式 | $\frac{1}{2^n}\sum_x (-1)^{y\cdot x} = \delta_{y,0}$ |

---

### 知识点索引

> 按拼音/字母顺序排列。

- **Bernstein-Vazirani算法**：1.5节
- **Deutsch算法**：1.3节
- **Deutsch-Jozsa算法**：1.4节
- **Hadamard变换**：1.1.2节
- **Oracle模型**：1.2节
- **QFT（量子傅里叶变换）**：1.7节
- **Simon算法**：1.6节
- **相位反冲**：1.2.2节
- **幺正算符**：1.2节
- **量子并行性**：1.1节
- **量子乘法器**：1.8.3节
- **量子加法器**：1.8.2节
- **量子比较器**：1.8.4节
- **量子算术**：1.8节
