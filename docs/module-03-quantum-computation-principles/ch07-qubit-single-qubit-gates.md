# 第1章 量子比特与单比特门

> **本章导读**
>
> 模块一我们建立了量子力学的数学框架——复向量空间、Dirac 符号、矩阵算符、张量积、布洛赫球面。现在，是时候用这些工具来刻画量子计算的核心对象了：**量子比特（qubit）** 和**量子门（quantum gate）**。
>
> 本章从量子比特的严格数学定义出发，逐步建立单比特量子门的完整图像。你会看到：经典比特只有 0 和 1 两种状态，而量子比特可以处于 $\alpha|0\rangle + \beta|1\rangle$ 这样的叠加态。单比特门就是作用在量子比特上的 $2 \times 2$ 幺正矩阵——它们在布洛赫球面上对应各种旋转。
>
> 本章尤其重视**旋转图像**：每个量子门在布洛赫球面上做了什么？泡利门是绕轴旋转 180°，Hadamard 门是旋转 90° 再反射，参数化旋转门 $R_x(\theta), R_y(\theta), R_z(\theta)$ 则是绕任意角度旋转。你将学会用欧拉分解把任意单比特门拆解为三次旋转。
>
> 从 1.5 节开始，我们走出纯数学，进入物理实现层面：什么是虚拟 $Z$ 门？什么是相位帧跟踪？拉比频率和脉冲面积如何决定门操作？高斯脉冲和 DRAG 脉冲为什么能抑制泄漏？这些概念是连接"数学门"与"真实量子硬件"的桥梁。
>
> **学完本章，你将能够：**
> - 用狄拉克符号和矩阵表示描述任意单量子比特态
> - 在布洛赫球面上可视化量子态和量子门操作
> - 写出泡利 X/Y/Z、Hadamard、S、T 门的矩阵形式并解释其几何意义
> - 用 $R_x(\theta), R_y(\theta), R_z(\theta)$ 表示任意旋转
> - 用欧拉分解（Z-Y 分解）将任意单比特门拆解为标准门序列
> - 理解虚拟 $Z$ 门和相位帧跟踪的原理
> - 解释拉比频率、脉冲面积、门保真度的基本概念
> - 了解高斯脉冲和 DRAG 脉冲的设计动机
>
> **先修知识**：模块一（线性代数、量子力学基本假设、布洛赫球面）

---

## 1.1 量子比特定义

### 1.1.1 从经典比特到量子比特

经典计算机的基本信息单元是**比特（bit）**——它只能取两个值之一：0 或 1。你无法让一个比特"同时是 0 和 1"。

量子计算机的基本信息单元是**量子比特（qubit）**。一个量子比特也是一个二能级系统，但它与经典比特有本质区别：量子比特可以处于 $|0\rangle$ 和 $|1\rangle$ 的**叠加态（superposition state）**。

**定义 1.1（量子比特）** 一个**量子比特**是定义在二维复 Hilbert 空间 $\mathcal{H} \cong \mathbb{C}^2$ 中的单位向量：

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \quad \alpha, \beta \in \mathbb{C}, \quad |\alpha|^2 + |\beta|^2 = 1
$$

其中 $\{|0\rangle, |1\rangle\}$ 是 $\mathbb{C}^2$ 的一组标准正交基，称为**计算基（computational basis）**：

$$
|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

两个复数 $\alpha$ 和 $\beta$ 称为**概率幅（probability amplitudes）**。

### 1.1.2 物理二能级标签 vs 量子计算代数标签

同一套 $\mathbb{C}^2$，物理课与量子计算课常用**两套叫法**，矩阵可以相同，语义不要混：

| 物理（能量 / 原子、电路） | 量子计算（信息 / 电路模型） | 典型矩阵（本征基） |
|---|---|---|
| 基态 $\|g\rangle$、较低能量 | 计算基 $\|0\rangle$ | $\begin{pmatrix}1\\0\end{pmatrix}$ |
| 激发态 $\|e\rangle$、较高能量 | 计算基 $\|1\rangle$ | $\begin{pmatrix}0\\1\end{pmatrix}$ |
| 自由哈密顿常取对角 $H_0=\tfrac12\hbar\omega_q Z$ 或 $\hbar\omega_q\|e\rangle\langle e\|$ | “计算基下 $Z$ 本征态” | $Z=\mathrm{diag}(1,-1)$ 等约定 |

**要点：**

1. **计算基是信息标签**，默认把编码用的两个能级叫 $|0\rangle,|1\rangle$；多数超导/原子实现里 $|0\rangle\leftrightarrow$ 基态、$|1\rangle\leftrightarrow$ 第一激发态，但**编码约定可翻转**（有时故意把激发当 $|0\rangle$），读文献先看作者的映射。  
2. **物理矩阵**常在能量本征基（$H_0$ 对角）里写；**算法矩阵**在计算基里写门。二者重合时最省事；若中间还有旋转波坐标系、相互作用绘景，会出现“同一物理态、不同表象矩阵”——这是表象变换，不是两套量子力学。  
3. 更高能级 $|f\rangle,|h\rangle,\ldots$ 在计算中叫**泄漏能级**；理想单比特门假定动力学留在 $\{|0\rangle,|1\rangle\}$ 子空间，脉冲工程（DRAG 等）就是在压泄漏。

后文凡写 $|0\rangle,|1\rangle$，在无额外声明时即采用「基态 $\leftrightarrow|0\rangle$、第一激发 $\leftrightarrow|1\rangle$」的主流硬件约定。

**例 1.1** 以下哪些是合法的量子比特？

(a) $|\psi\rangle = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle$ ✓（$|\alpha|^2 + |\beta|^2 = 1/2 + 1/2 = 1$）

(b) $|\psi\rangle = \frac{1}{2}|0\rangle + \frac{\sqrt{3}}{2}|1\rangle$ ✓（$1/4 + 3/4 = 1$）

(c) $|\psi\rangle = \frac{1}{3}|0\rangle + \frac{2}{3}|1\rangle$ ✗（$1/9 + 4/9 = 5/9 \neq 1$——未归一化）

(d) $|\psi\rangle = \frac{1}{\sqrt{2}}|0\rangle - \frac{i}{\sqrt{2}}|1\rangle$ ✓（$1/2 + 1/2 = 1$）

### 1.1.3 概率解释

当我们测量一个量子比特时——比如在计算基 $\{|0\rangle, |1\rangle\}$ 下测量——测量结果是一个**经典比特**（0 或 1），而不是量子叠加态。Born 规则告诉我们：

$$
\begin{aligned}
P(0) &= |\langle 0|\psi\rangle|^2 = |\alpha|^2 \\
P(1) &= |\langle 1|\psi\rangle|^2 = |\beta|^2
\end{aligned}
$$

且 $P(0) + P(1) = |\alpha|^2 + |\beta|^2 = 1$。

**关键认识**：

1. **测量前**：量子比特处于叠加态 $\alpha|0\rangle + \beta|1\rangle$，没有确定的经典值
2. **测量瞬间**：以概率 $|\alpha|^2$ "坍缩"到 $|0\rangle$，以概率 $|\beta|^2$ 坍缩到 $|1\rangle$
3. **测量后**：叠加态被破坏，量子比特变为经典结果

> **类比**：想象一枚旋转中的硬币。在它停下来之前，它既不是正面也不是反面——它是"正面和反面的叠加"。只有当它落下停稳，你才能说它到底是正面还是反面。量子比特的测量就像在硬币还在旋转时拍了一张快照——这一拍就"冻结"了它的状态。

**例 1.2** 制备 1000 个相同的量子比特 $|\psi\rangle = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle$ 并逐一测量。预期结果：约 500 次测得 $|0\rangle$，约 500 次测得 $|1\rangle$。

### 1.1.4 叠加态原理

叠加态原理是量子力学最反直觉的核心：

> **叠加原理**：如果 $|\psi_1\rangle$ 和 $|\psi_2\rangle$ 是系统的可能状态，则它们的任意线性组合（叠加）$c_1|\psi_1\rangle + c_2|\psi_2\rangle$ 也是系统的可能状态。

对量子比特而言：

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
$$

这个"同时处于两个状态"的能力让一个量子比特包含的信息量远超一个经典比特。但注意：**你不能直接"读取" $\alpha$ 和 $\beta$ 的值**——测量只能得到一个经典比特。$\alpha$ 和 $\beta$ 的信息以概率幅的形式"隐藏"在量子态中，只有通过量子门操作才能操控它们。

**关键区分：叠加 vs. 概率混合**

$|\psi\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ 和"以 50% 概率处于 $|0\rangle$、50% 概率处于 $|1\rangle$ 的经典混合"是**不同的物理状态**。

- 叠加态：$\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$——有确定的相位关系（相干性）
- 混合态：50% $|0\rangle$、50% $|1\rangle$——没有相位关系（非相干）

这两种状态在后续的量子门操作下表现不同，因此可以通过实验区分。

### 1.1.5 布洛赫球面表示

任何一个单量子比特态都可以用布洛赫球面（Bloch sphere）来可视化。量子比特的归一化条件 $|\alpha|^2 + |\beta|^2 = 1$ 和全局相位不可观测性共同决定了：任意量子比特态可以唯一地（除全局相位外）表示为：

$$
|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\varphi}\sin\frac{\theta}{2}|1\rangle
$$

其中 $\theta \in [0, \pi]$，$\varphi \in [0, 2\pi)$。

**布洛赫球面坐标**：

```
                    z (|0⟩)
                    ↑
                    |
                    |  · P (θ, φ)
                   /|
                  / |θ
                 /  |
                /   |
      ---------+----+-------→ x
               |    |
               |    |
               |    |
               ↓    |
            -z (|1⟩)   φ (在 xy 平面)
```

**几个重要状态在布洛赫球面上的位置**：

| 状态 | $\theta$ | $\varphi$ | 球面坐标 | 几何位置 |
|:---|:---:|:---:|:---|:---|
| $\lvert 0\rangle$ | 0 | — | $(0,0,1)$ | 北极 |
| $\lvert 1\rangle$ | $\pi$ | — | $(0,0,-1)$ | 南极 |
| $\lvert +\rangle = \frac{1}{\sqrt{2}}(\lvert 0\rangle + \lvert 1\rangle)$ | $\pi/2$ | 0 | $(1,0,0)$ | $x$ 轴正向 |
| $\lvert -\rangle = \frac{1}{\sqrt{2}}(\lvert 0\rangle - \lvert 1\rangle)$ | $\pi/2$ | $\pi$ | $(-1,0,0)$ | $x$ 轴负向 |
| $\lvert +_y\rangle = \frac{1}{\sqrt{2}}(\lvert 0\rangle + i\lvert 1\rangle)$ | $\pi/2$ | $\pi/2$ | $(0,1,0)$ | $y$ 轴正向 |
| $\lvert -_y\rangle = \frac{1}{\sqrt{2}}(\lvert 0\rangle - i\lvert 1\rangle)$ | $\pi/2$ | $3\pi/2$ | $(0,-1,0)$ | $y$ 轴负向 |

**从振幅到球面坐标的转换**：

给定 $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$（已归一化），先消去全局相位使 $\alpha$ 为非负实数：

$$
\theta = 2\arccos(|\alpha|), \quad \varphi = \arg(\beta) - \arg(\alpha)
$$

**例 1.3** 将 $|\psi\rangle = \frac{1}{\sqrt{3}}|0\rangle + \sqrt{\frac{2}{3}}|1\rangle$ 用布洛赫球面坐标表示。

解：$\alpha = \frac{1}{\sqrt{3}}$（已是正实数），$\beta = \sqrt{\frac{2}{3}}$（正实数）。

$$
\theta = 2\arccos\left(\frac{1}{\sqrt{3}}\right) \approx 2 \times 0.955 = 1.910 \text{ rad} \approx 109.5^\circ
$$

$$
\varphi = \arg(\beta) - \arg(\alpha) = 0 - 0 = 0
$$

所以 $|\psi\rangle$ 对应布洛赫球面上 $\theta \approx 109.5^\circ$、$\varphi = 0$ 的点——位于 $xz$ 平面的下半球。

**布洛赫球面的重要性质**：

1. **球面每一点**对应一个不同的量子态（相差全局相位的态对应同一点）
2. **南极和北极**分别对应计算基 $|0\rangle$ 和 $|1\rangle$
3. **赤道上的点**对应等概率叠加态（$|\alpha| = |\beta| = 1/\sqrt{2}$）
4. **正交态**在球面上互为对径点（例如 $|0\rangle$ 和 $|1\rangle$、$|+\rangle$ 和 $|-\rangle$）

> **为什么用 $\theta/2$ 而不是 $\theta$？**
>
> 使用 $\theta/2$ 是为了保证：当 $\theta$ 从 0 变到 $\pi$ 时，北极 $|0\rangle$ 平滑地过渡到南极 $|1\rangle$。更重要的是，后续的旋转门在布洛赫球面上正好对应 $\theta$ 角度的旋转——这种参数化让旋转图像变得直观。

---

**小练习 1.1** 判断以下状态是否合法量子比特态。若合法，写出布洛赫球面坐标。

(a) $\frac{1}{\sqrt{2}}|0\rangle - \frac{1}{\sqrt{2}}|1\rangle$

(b) $\frac{1}{2}|0\rangle + \frac{\sqrt{3}}{2}|1\rangle$

(c) $\frac{1}{2}|0\rangle - \frac{i}{2}|1\rangle$ （提示：检查归一化条件）

**小练习 1.2** 布洛赫球面上 $\theta = \pi/3$、$\varphi = \pi/4$ 对应的量子态是什么？写出它的狄拉克符号形式和列向量形式。

---

## 1.2 单比特门旋转图像

### 1.2.1 什么是量子门？

在经典计算中，**逻辑门**（如 NOT、AND、OR）将输入比特映射为输出比特。在量子计算中，**量子门（quantum gate）** 是作用在量子比特上的**幺正算符**（幺正算符）。

**定义 1.2（单比特量子门）** 一个 $2 \times 2$ 复矩阵 $U$ 称为单比特量子门，如果它是**幺正的**（unitary）：

$$
U^\dagger U = U U^\dagger = I
$$

其中 $U^\dagger = (U^T)^*$ 是 $U$ 的共轭转置。

幺正性保证了量子门：

1. **保范数**：$\|U|\psi\rangle\| = \||\psi\rangle\| = 1$——输出仍然是合法的量子态
2. **可逆**：$U^{-1} = U^\dagger$——量子门没有信息损失
3. **保内积**：$\langle U\phi|U\psi\rangle = \langle\phi|\psi\rangle$——保持态之间的夹角

**几何图像**：在布洛赫球面上，单比特量子门对应一个**旋转**（可能加上反射）。因为布洛赫球面上的态向量在幺正变换下保持长度不变，唯一的可能就是做旋转操作。

### 1.2.2 泡利 X 门（量子 NOT 门）

泡利 X 门是最简单的量子门，它对应经典 NOT 门的量子版本。

**矩阵表示**：

$$
X = \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
$$

**作用效果**：

$$
X|0\rangle = |1\rangle, \quad X|1\rangle = |0\rangle
$$

对一般叠加态：

$$
X(\alpha|0\rangle + \beta|1\rangle) = \alpha|1\rangle + \beta|0\rangle
$$

**验证幺正性**：

$$
X^\dagger X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}^\dagger \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
$$

注意 $X$ 是厄米的（$X^\dagger = X$）且幺正的（$X^2 = I$）。

**布洛赫球面几何**：$X$ 门绕 $x$ 轴旋转 180°（$\pi$）：

- $|0\rangle$（北极）$\xrightarrow{X}$ $|1\rangle$（南极）
- $|1\rangle$（南极）$\xrightarrow{X}$ $|0\rangle$（北极）
- $|+\rangle$（$x$ 轴正向）$\xrightarrow{X}$ $|+\rangle$（不变！）
- $|-\rangle$（$x$ 轴负向）$\xrightarrow{X}$ $|-\rangle$（不变！）

**电路符号**：

```
──[X]──
```

### 1.2.3 泡利 Y 门

**矩阵表示**：

$$
Y = \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
$$

**作用效果**：

$$
Y|0\rangle = i|1\rangle, \quad Y|1\rangle = -i|0\rangle
$$

对一般叠加态：

$$
Y(\alpha|0\rangle + \beta|1\rangle) = i\alpha|1\rangle - i\beta|0\rangle
$$

**布洛赫球面几何**：$Y$ 门绕 $y$ 轴旋转 180°（$\pi$）。

注意 $Y$ 也是厄米的且幺正的（$Y^2 = I$）。

**电路符号**：

```
──[Y]──
```

### 1.2.4 泡利 Z 门

**矩阵表示**：

$$
Z = \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

**作用效果**：

$$
Z|0\rangle = |0\rangle, \quad Z|1\rangle = -|1\rangle
$$

对一般叠加态：

$$
Z(\alpha|0\rangle + \beta|1\rangle) = \alpha|0\rangle - \beta|1\rangle
$$

Z 门给 $|1\rangle$ 分量加上一个 $-1$ 相位（即 $\pi$ 相位），而 $|0\rangle$ 分量不变。

**布洛赫球面几何**：$Z$ 门绕 $z$ 轴旋转 180°（$\pi$）。

**电路符号**：

```
──[Z]──
```

**泡利门小结**：

| 门 | 矩阵 | 几何旋转 | 本征值 | 本征态 |
|:---|:---|:---:|:---:|:---|
| $X$ | $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | 绕 $x$ 轴转 $\pi$ | $\pm 1$ | $\vert \pm\rangle$ |
| $Y$ | $\begin{pmatrix}0&-i\\i&0\end{pmatrix}$ | 绕 $y$ 轴转 $\pi$ | $\pm 1$ | $\vert \pm_y\rangle$ |
| $Z$ | $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ | 绕 $z$ 轴转 $\pi$ | $\pm 1$ | $\lvert 0\rangle,\lvert 1\rangle$ |

### 1.2.5 Hadamard 门

Hadamard 门是量子计算中最重要的门之一。它把计算基态变成等概率叠加态。

**矩阵表示**：

$$
H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

**作用效果**：

$$
\begin{aligned}
H|0\rangle &= \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |+\rangle \\
H|1\rangle &= \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) = |-\rangle
\end{aligned}
$$

**验证幺正性**：

$$
H^\dagger H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}^\dagger \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = I
$$

注意 $H$ 是厄米的（$H^\dagger = H$）且 $H^2 = I$。

**布洛赫球面几何**：Hadamard 门的作用可以看作**绕 $(x+z)/\sqrt{2}$ 轴旋转 $\pi$ 角**——更直观的解释是：
- $|0\rangle$（北极）$\xrightarrow{H}$ $|+\rangle$（$x$ 轴正向）
- $|1\rangle$（南极）$\xrightarrow{H}$ $|-\rangle$（$x$ 轴负向）
- $|+\rangle$（$x$ 轴正向）$\xrightarrow{H}$ $|0\rangle$（北极）
- $|-\rangle$（$x$ 轴负向）$\xrightarrow{H}$ $|1\rangle$（南极）

换言之，$H$ 在 $z$ 轴和 $x$ 轴之间"交换"基向量。

**电路符号**：

```
──[H]──
```

**例 1.4** 计算 $H X H$。

解：

$$
H X H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

先算 $XH$：

$$
XH = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}
$$

再乘 $H$：

$$
H X H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1+1 & -1+1 \\ 1-1 & -1-1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = Z
$$

所以 $H X H = Z$。类似可以验证 $H Z H = X$。这个关系说明 $H$ 在 $X$ 和 $Z$ 之间建立了**共轭变换**。

**重要恒等式**：

$$
H X H = Z, \quad H Z H = X, \quad H Y H = -Y
$$

### 1.2.6 S 门（相位门）

S 门（也称相位门）给 $|1\rangle$ 分量加上 $i$ 相位（即 $\pi/2$ 相位）。

**矩阵表示**：

$$
S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}
$$

**作用效果**：

$$
S|0\rangle = |0\rangle, \quad S|1\rangle = i|1\rangle
$$

$$
S(\alpha|0\rangle + \beta|1\rangle) = \alpha|0\rangle + i\beta|1\rangle
$$

**布洛赫球面几何**：$S$ 门绕 $z$ 轴旋转 $\pi/2$（90°）。

**验证幺正性**：

$$
S^\dagger S = \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
$$

$S$ 的逆是 $S^\dagger = \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix}$，且 $S^2 = Z$（验证：$S^2 = \begin{pmatrix} 1 & 0 \\ 0 & i^2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = Z$）。

**电路符号**：

```
──[S]──
```

### 1.2.7 T 门

T 门（也称 $\pi/8$ 门）给 $|1\rangle$ 分量加上 $e^{i\pi/4}$ 相位（即 $\pi/4$ 相位）。

**矩阵表示**：

$$
T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}
$$

**作用效果**：

$$
T|0\rangle = |0\rangle, \quad T|1\rangle = e^{i\pi/4}|1\rangle
$$

**布洛赫球面几何**：$T$ 门绕 $z$ 轴旋转 $\pi/4$（45°）。

**验证幺正性**：

$$
T^\dagger T = \begin{pmatrix} 1 & 0 \\ 0 & e^{-i\pi/4} \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
$$

注意 $T^2 = S$，$T^4 = Z$，$T^8 = I$。

**为什么叫 $\pi/8$ 门？** 历史上这个门被定义为 $T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$。但如果忽略全局相位，可以写成 $e^{i\pi/8}\begin{pmatrix} e^{-i\pi/8} & 0 \\ 0 & e^{i\pi/8} \end{pmatrix}$，其中对角线元素是 $e^{\pm i\pi/8}$——因此得名 $\pi/8$ 门。

**电路符号**：

```
──[T]──
```

### 1.2.8 门总结表

| 门名称 | 矩阵 | 布洛赫球面旋转 | 重要性质 |
|:---|:---|:---:|:---|
| $X$ | $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | 绕 $x$ 轴转 $\pi$ | $X^2 = I$ |
| $Y$ | $\begin{pmatrix}0&-i\\i&0\end{pmatrix}$ | 绕 $y$ 轴转 $\pi$ | $Y^2 = I$ |
| $Z$ | $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ | 绕 $z$ 轴转 $\pi$ | $Z^2 = I$ |
| $H$ | $\frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ | 绕 $(x+z)/\sqrt{2}$ 轴转 $\pi$ | $H^2 = I$, $HXH = Z$ |
| $S$ | $\begin{pmatrix}1&0\\0&i\end{pmatrix}$ | 绕 $z$ 轴转 $\pi/2$ | $S^2 = Z$ |
| $T$ | $\begin{pmatrix}1&0\\0&e^{i\pi/4}\end{pmatrix}$ | 绕 $z$ 轴转 $\pi/4$ | $T^2 = S$, $T^8 = I$ |

---

**小练习 1.3** 计算 $H|+\rangle$ 和 $H|-\rangle$ 的结果，并与 $H$ 门的几何解释对照。

**小练习 1.4** 验证 $S^\dagger = S^3$，并写出 $S^\dagger$ 的矩阵形式。

**小练习 1.5** 证明：$X H X = H$。（提示：利用 $HXH = Z$ 和 $X$ 的性质）

---

## 1.3 参数化旋转门

前节的泡利门、$H$、$S$、$T$ 都是**离散门**——它们只能实现特定的旋转角度。但真实的量子物理允许我们实现连续角度的旋转。本节引入**参数化旋转门**。

### 1.3.1 从矩阵指数到旋转

矩阵指数、幺正性与用谱分解计算 $e^{-i\theta H}$ 的代数工具见模块一第 1 章 §1.10；本节在**已有布洛赫球**的前提下，把它们读成单比特旋转门。回忆：如果 $A$ 是厄米矩阵，则 $e^{-i\theta A}$ 是幺正矩阵。对于泡利矩阵，我们有：

$$
e^{-i\theta X} = I\cos\theta - iX\sin\theta = \begin{pmatrix} \cos\theta & -i\sin\theta \\ -i\sin\theta & \cos\theta \end{pmatrix}
$$

但量子计算中更常用的定义是引入因子 $1/2$：

$$
R_x(\theta) = e^{-i\theta X/2} = \cos\frac{\theta}{2}\, I - i\sin\frac{\theta}{2}\, X
$$

$$
R_y(\theta) = e^{-i\theta Y/2} = \cos\frac{\theta}{2}\, I - i\sin\frac{\theta}{2}\, Y
$$

$$
R_z(\theta) = e^{-i\theta Z/2} = \cos\frac{\theta}{2}\, I - i\sin\frac{\theta}{2}\, Z
$$

**为什么要有 $1/2$ 因子？** 因为这样参数 $\theta$ 正好对应布洛赫球面上的旋转角度。$R_z(\theta)$ 绕 $z$ 轴旋转 $\theta$ 角——当 $\theta = \pi$ 时，$R_z(\pi) = -iZ$（相差全局相位 $-i$，与 $Z$ 门等价）。这个几何一致性使得 $R$ 门非常直观。

### 1.3.2 Rx(θ) 门

**矩阵形式**：

$$
R_x(\theta) = \cos\frac{\theta}{2} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - i\sin\frac{\theta}{2} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} \cos\frac{\theta}{2} & -i\sin\frac{\theta}{2} \\ -i\sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}
$$

**特殊角度**：

| $\theta$ | $R_x(\theta)$ | 等价于 |
|:---:|:---|:---:|
| $0$ | $I$ | 什么都不做 |
| $\pi$ | $\begin{pmatrix}0&-i\\-i&0\end{pmatrix} = -iX$ | $X$ 门（忽略全局相位） |
| $\pi/2$ | $\frac{1}{\sqrt{2}}\begin{pmatrix}1&-i\\-i&1\end{pmatrix}$ | $\sqrt{X}$ 门 |
| $2\pi$ | $-I$ | 全局相位 $-1$ |

**作用效果**：$R_x(\theta)$ 在布洛赫球面上绕 $x$ 轴旋转 $\theta$ 角。

**电路符号**：

```
──[Rx(θ)]──
```

### 1.3.3 Ry(θ) 门

**矩阵形式**：

$$
R_y(\theta) = \cos\frac{\theta}{2} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - i\sin\frac{\theta}{2} \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}
$$

**特殊角度**：

| $\theta$ | $R_y(\theta)$ | 等价于 |
|:---:|:---|:---:|
| $0$ | $I$ | 什么都不做 |
| $\pi$ | $\begin{pmatrix}0&-1\\1&0\end{pmatrix} = -iY$ | $Y$ 门（忽略全局相位） |
| $\pi/2$ | $\frac{1}{\sqrt{2}}\begin{pmatrix}1&-1\\1&1\end{pmatrix}$ | $\sqrt{Y}$ 门 |
| $2\pi$ | $-I$ | 全局相位 $-1$ |

**作用效果**：$R_y(\theta)$ 在布洛赫球面上绕 $y$ 轴旋转 $\theta$ 角。

注意到 $R_y(\theta)$ 的矩阵元全是实数——这是一个重要性质。$R_y$ 门保持态向量的系数为实数（如果初始态系数是实数）。

**电路符号**：

```
──[Ry(θ)]──
```

### 1.3.4 Rz(θ) 门

**矩阵形式**：

$$
R_z(\theta) = \cos\frac{\theta}{2} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - i\sin\frac{\theta}{2} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}
$$

**特殊角度**：

| $\theta$ | $R_z(\theta)$ | 等价于 |
|:---:|:---|:---:|
| $0$ | $I$ | 什么都不做 |
| $\pi$ | $\begin{pmatrix}-i&0\\0&i\end{pmatrix} = -iZ$ | $Z$ 门（忽略全局相位） |
| $\pi/2$ | $\begin{pmatrix}e^{-i\pi/4}&0\\0&e^{i\pi/4}\end{pmatrix}$ | $S$ 门（相差全局相位） |
| $\pi/4$ | $\begin{pmatrix}e^{-i\pi/8}&0\\0&e^{i\pi/8}\end{pmatrix}$ | $T$ 门（相差全局相位） |
| $2\pi$ | $\begin{pmatrix}-1&0\\0&-1\end{pmatrix} = -I$ | 全局相位 $-1$ |

**作用效果**：$R_z(\theta)$ 在布洛赫球面上绕 $z$ 轴旋转 $\theta$ 角。

特别地，$R_z(\theta)$ 是对角矩阵——它只在 $|0\rangle$ 和 $|1\rangle$ 上施加不同的相位：

$$
R_z(\theta)(\alpha|0\rangle + \beta|1\rangle) = e^{-i\theta/2}\alpha|0\rangle + e^{i\theta/2}\beta|1\rangle
$$

注意 $R_z(\theta)$ 给 $|0\rangle$ 和 $|1\rangle$ 的相位变化是相反的。如果忽略全局相位，可以写成：

$$
R_z(\theta) \triangleq \begin{pmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{pmatrix} \quad (\text{相差全局相位 } e^{i\theta/2})
$$

这个简化形式在很多量子计算教材中使用。

**电路符号**：

```
──[Rz(θ)]──
```

### 1.3.5 例：Rz(θ) 对 |+ 的作用

计算 $R_z(\theta)|+\rangle$：

$$
|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)
$$

$$
R_z(\theta)|+\rangle = \frac{1}{\sqrt{2}}(e^{-i\theta/2}|0\rangle + e^{i\theta/2}|1\rangle)
$$

忽略全局相位 $e^{-i\theta/2}$：

$$
R_z(\theta)|+\rangle \triangleq \frac{1}{\sqrt{2}}(|0\rangle + e^{i\theta}|1\rangle)
$$

这正是布洛赫球面上绕 $z$ 轴旋转 $\theta$ 角——$|+\rangle$（$x$ 轴正向）旋转到赤道上另一个点。

### 1.3.6 任意单比特门的欧拉分解

一个重要的定理告诉我们：**任意单比特幺正门都可以分解为三次旋转**。

> **定理 1.1（Z-Y 欧拉分解）** 任意 $2 \times 2$ 幺正矩阵 $U$ 可以表示为：
>
> $$
> U = e^{i\alpha} R_z(\beta) R_y(\gamma) R_z(\delta)
> $$
>
> 其中 $\alpha, \beta, \gamma, \delta$ 是实数，$e^{i\alpha}$ 是全局相位。

另一种常用的分解方式（Z-X-Z 分解）：

$$
U = e^{i\alpha} R_z(\phi) R_x(\theta) R_z(\psi)
$$

**证明思路**：任意 $2 \times 2$ 幺正矩阵可以写成：

$$
U = \begin{pmatrix} a & b \\ -b^* & a^* \end{pmatrix} \quad \text{若 } \det U = 1
$$

（更一般地，$\det U = e^{i\alpha}$，我们可以先提取全局相位。）

将 $U$ 参数化：

$$
U = \begin{pmatrix} e^{i(\alpha - \beta/2 - \delta/2)}\cos\frac{\gamma}{2} & -e^{i(\alpha - \beta/2 + \delta/2)}\sin\frac{\gamma}{2} \\ e^{i(\alpha + \beta/2 - \delta/2)}\sin\frac{\gamma}{2} & e^{i(\alpha + \beta/2 + \delta/2)}\cos\frac{\gamma}{2} \end{pmatrix}
$$

而 $e^{i\alpha} R_z(\beta) R_y(\gamma) R_z(\delta)$ 展开正好是这个形式。因此**任何单比特门都可以用三个旋转参数唯一表示**（除全局相位外）。

**例 1.5** 求 Hadamard 门的 Z-Y 分解。

解：$H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$。设 $H = e^{i\alpha} R_z(\beta) R_y(\gamma) R_z(\delta)$。

通过比较矩阵元（或者查表）可得一种常见分解：

$$
H = e^{i\pi/2} R_z(\pi/2) R_y(\pi/2) R_z(\pi/2)
$$

验证：

$$
\begin{aligned}
R_z(\pi/2) R_y(\pi/2) R_z(\pi/2) &=
\begin{pmatrix} e^{-i\pi/4} & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}
\begin{pmatrix} \cos\pi/4 & -\sin\pi/4 \\ \sin\pi/4 & \cos\pi/4 \end{pmatrix}
\begin{pmatrix} e^{-i\pi/4} & 0 \\ 0 & e^{i\pi/4} \end{pmatrix} \\
&= \begin{pmatrix} e^{-i\pi/4} & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}
\begin{pmatrix} \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{pmatrix}
\begin{pmatrix} e^{-i\pi/4} & 0 \\ 0 & e^{i\pi/4} \end{pmatrix} \\
&= \frac{1}{\sqrt{2}} \begin{pmatrix} e^{-i\pi/2} & e^{-i\pi/2} \\ e^{i\pi/2} & -e^{i\pi/2} \end{pmatrix} \\
&= \frac{1}{\sqrt{2}} \begin{pmatrix} -i & -i \\ i & -i \end{pmatrix} = -i H
\end{aligned}
$$

所以 $H = i \cdot (-i H) = e^{i\pi/2} R_z(\pi/2) R_y(\pi/2) R_z(\pi/2)$。✓

**欧拉分解的实用版本**（Z-X-Z 分解）：

$$
U = e^{i\alpha} R_z(\phi) R_x(\theta) R_z(\psi)
$$

其中 $\phi, \theta, \psi$ 是三个实参数（全局相位可略）。

### 1.3.7 硬件友好分解族：XYX / YXY 与驱动动机

欧拉分解不唯一。把“中间一转”选在哪根轴上，由**硬件能原生打出什么旋转**决定。

| 形式 | 写法（略全局相位） | 中间轴 | 硬件动机（超导微波典型） |
|---|---|---|---|
| Z–Y–Z | $R_z(\beta)R_y(\gamma)R_z(\delta)$ | $Y$ | 教材默认；两翼 $R_z$ 可虚拟 |
| Z–X–Z | $R_z(\phi)R_x(\theta)R_z(\psi)$ | $X$ | 中间用共振 $X$ 包络脉冲 |
| **X–Y–X** | $R_x(\alpha)R_y(\beta)R_x(\gamma)$ | $Y$ | 仅用**共振可驱动的横场** $X/Y$；无显式 $R_z$ 脉冲 |
| **Y–X–Y** | $R_y(\alpha)R_x(\beta)R_y(\gamma)$ | $X$ | 同上，轴角色对调 |

**物理事实（接 1.5 节）：**

- **共振驱动**的微波（旋转波近似下）在布洛赫球上生成 **$xy$ 平面内**的旋转：载波**初相**选 $0$ 或 $\pi/2$ 即选 $R_x$ 或 $R_y$（更一般的初相 $\phi$ 给出 $R_{\hat n}$，$\hat n$ 在赤道上）。  
- **$R_z$ 不能靠同一套横场共振脉冲“顺便”做完**：纵向旋转要么来自**失谐**（帧与比特频率差积累相位，要占时间、吃噪声），要么用 **虚拟 $Z$**——不发 $Z$ 包络，而靠**调制后续 $X/Y$ 驱动的初相**改变旋转轴（§1.5.1 论证：初相是物理控制量）。  
- 因此编译器常把任意单比特门收成 **$R_z$–$R_x$–$R_z$**（两翼虚拟 $Z$ + 一次物理 $X$ 包络），或在必须用横场拼装时使用 **XYX / YXY**。

**XYX 与 ZYZ 的关系（互化，不另起炉灶）：**  
利用恒等式 $R_y(\theta)=R_z(-\pi/2)R_x(\theta)R_z(\pi/2)$ 等（见 §1.4），任一 ZYZ 形式可改写成只含 $R_x,R_y$ 的 XYX/YXY；反之亦然。存在性与 ZYZ 相同：都是 $SU(2)$ 的欧拉角参数化，只是轴约定不同。

**例（形式）** 忽略全局相位时，常见编译目标为

$$
U \simeq R_z(\phi)\,R_x(\theta)\,R_z(\lambda)
\quad\text{或}\quad
U \simeq R_x(\alpha)\,R_y(\beta)\,R_x(\gamma).
$$

具体角度由矩阵元反解（与定理 1.2 同类手续，只换轴）。

> **思考 1.A** $R_i(\theta)=e^{-i\theta \sigma_i/2}$（$i\in\{x,y,z\}$）的矩阵形式如何由指数级数或本征分解得到？任意 $U\in SU(2)$ 的 ZYZ（或 XYX）角度满足怎样的矩阵方程？先尝试自推，再对照定理 1.2 的步骤。

### 1.3.8 Z-Y 分解定理

前一小节讨论的是存在性。现在给出一个更精确的定理和计算三个角度的方法。

> **定理 1.2（Z-Y 分解定理）** 任意 $2 \times 2$ 幺正矩阵 $U$ 都可以写成：
>
> $$
> U = e^{i\alpha} R_z(\beta) R_y(\gamma) R_z(\delta)
> $$
>
> 其中 $\alpha, \beta, \gamma, \delta \in \mathbb{R}$。

**如何计算 $\alpha, \beta, \gamma, \delta$？**

设 $U = \begin{pmatrix} u_{00} & u_{01} \\ u_{10} & u_{11} \end{pmatrix}$ 且 $\det U = e^{i\alpha}$。

步骤：

1. 提取相位 $\alpha$：$\alpha$ 由 $\det U = e^{i\alpha}$ 给出（注意 $\det U$ 的模为 1）
2. 计算 $\gamma$：$\cos\frac{\gamma}{2} = |u_{00}|$，$\sin\frac{\gamma}{2} = |u_{10}|$（注意 $\gamma \in [0, \pi]$）
3. 计算 $\beta$ 和 $\delta$：
   - 如果 $\sin(\gamma/2) \neq 0$：

$$
     \beta = \arg(u_{10}) - \arg(u_{00}), \quad \delta = \arg(u_{01}) - \arg(u_{10})
$$

- 如果 $\sin(\gamma/2) = 0$（即 $U$ 是对角矩阵）：取 $\gamma = 0$，$\beta + \delta = \arg(u_{11}) - \arg(u_{00})$

**例 1.6** 求 $X$ 门的 Z-Y 分解。

$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$，$\det X = -1 = e^{i\pi}$，所以 $\alpha = \pi$。

$\cos\frac{\gamma}{2} = |0| = 0 \Rightarrow \gamma/2 = \pi/2 \Rightarrow \gamma = \pi$。

$\beta = \arg(1) - \arg(0) = 0$（这里 $\arg(0)$ 未定义，但 $\gamma = \pi$ 时公式退化——我们需要单独处理）。

实际上当 $\gamma = \pi$ 时，$R_y(\pi) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$，所以：

$$
X = e^{i\pi} R_z(\beta) R_y(\pi) R_z(\delta) = - \begin{pmatrix} e^{-i(\beta+\delta)/2} \cdot 0 & -e^{-i(\beta-\delta)/2} \\ e^{i(\beta-\delta)/2} \cdot 0 & e^{i(\beta+\delta)/2} \cdot 0 \end{pmatrix}
$$

令 $e^{-i(\beta-\delta)/2} = 1$ 且 $-1 \cdot e^{i(\beta-\delta)/2} = 1$，可得 $\beta - \delta = 0$，$\beta + \delta = \pi$。取 $\beta = \pi/2$，$\delta = \pi/2$。

所以 $X = e^{i\pi} R_z(\pi/2) R_y(\pi) R_z(\pi/2) = e^{i\pi} \cdot (-iX) \cdot (-i) = X$。✓

（欧拉分解不是唯一的——不同的参数选择可以得到不同的分解。）

### 1.3.9 任意单比特门的通用性

Z-Y 分解定理有一个重要的推论：

> **推论 1.1** 任意单比特量子门可以用 $R_z$ 和 $R_y$（或 $R_x$ 和 $R_z$）的有限序列精确实现。

这意味着**单比特门的集合 $\{R_z(\theta), R_y(\phi)\}$ 是通用的**——任何单比特门都可以由它们组合而成。这在物理实现中非常实用：如果硬件只能原生实现 $R_z$ 和 $R_y$ 旋转（许多超导量子计算平台正是如此），我们仍然可以实现任意单比特门。

---

**小练习 1.6** 计算 $R_x(\pi/2)|0\rangle$ 的结果，并解释在布洛赫球面上的几何含义。

**小练习 1.7** 求 $S$ 门的 Z-Y 分解（用 $\alpha, \beta, \gamma, \delta$ 表示）。

**小练习 1.8** 验证 $R_z(\theta) R_y(\phi) R_z(\psi)$ 的矩阵形式，并证明它可以表示任意单比特幺正门（忽略全局相位）。

**小练习 1.9** 由 $R_i(\theta)=e^{-i\theta\sigma_i/2}$ 出发，用本征分解或幂级数写出 $R_x(\theta)$ 的矩阵；并说明如何把它嵌入 ZXZ 或 XYX 分解。

---

## 1.4 门组合与代数恒等式

### 1.4.1 门组合的基本规则

量子门的组合就是矩阵乘法。按**时间顺序**：先应用的门在右边，后应用的在左边。
$$U_{\text{总}} = U_k \cdots U_2 U_1$$
**例 1.7** 先 $H$ 后 $T$ 再 $H$：

$$
H T H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix} \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

先算 $T H$：

$$
T H = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix} \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ e^{i\pi/4} & -e^{i\pi/4} \end{pmatrix}
$$

再乘 $H$：

$$
H T H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ e^{i\pi/4} & -e^{i\pi/4} \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1+e^{i\pi/4} & 1-e^{i\pi/4} \\ 1-e^{i\pi/4} & 1+e^{i\pi/4} \end{pmatrix}
$$

### 1.4.2 相位门家族

把 $R_z(\theta)$ 门的几种特例放在一起看：

| 门 | $\theta$ | 矩阵 | 名称 |
|:---|:---:|:---|:---:|
| $I$ | 0 | $\begin{pmatrix}1&0\\0&1\end{pmatrix}$ | 恒等门 |
| $T$ | $\pi/4$ | $\begin{pmatrix}1&0\\0&e^{i\pi/4}\end{pmatrix}$ | $\pi/8$ 门 |
| $S$ | $\pi/2$ | $\begin{pmatrix}1&0\\0&i\end{pmatrix}$ | 相位门 |
| $Z$ | $\pi$ | $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ | 泡利 Z 门 |

**关系**：

$$
T^2 = S, \quad S^2 = Z, \quad Z^2 = I
$$

$$
T^4 = Z, \quad T^8 = I
$$

$$S = T^2, \quad Z = T^4$$
### 1.4.3 常用恒等式

以下恒等式在量子电路化简中非常有用：

**恒等式 1**：$H X H = Z$，$H Z H = X$（前面已证）

**恒等式 2**：$X Z X = -Z$，$Z X Z = -X$

**证明**：

$$
X Z X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} = -Z
$$

**恒等式 3**：$X R_z(\theta) X = R_z(-\theta)$

**证明**：

$$
X R_z(\theta) X = X \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix} X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
$$

$$
= \begin{pmatrix} 0 & e^{i\theta/2} \\ e^{-i\theta/2} & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} e^{i\theta/2} & 0 \\ 0 & e^{-i\theta/2} \end{pmatrix} = R_z(-\theta)
$$

**恒等式 4**：$Y R_z(\theta) Y = R_z(-\theta)$（同样成立，因为 $Y$ 交换 $|0\rangle$ 和 $|1\rangle$ 并引入相位）

**恒等式 5**：$H R_z(\theta) H = R_x(\theta)$

**证明**：

$$
H R_z(\theta) H = H \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix} H
$$

利用 $H X H = Z$ 的关系，这个恒等式本质上是 $H$ 在 $z$ 和 $x$ 轴之间的共轭变换。

**恒等式 6**：$R_x(\theta) = H R_z(\theta) H$

**直接验证**：

$$
H R_z(\theta) H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix} \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

$$
= \frac{1}{2} \begin{pmatrix} e^{-i\theta/2}+e^{i\theta/2} & e^{-i\theta/2}-e^{i\theta/2} \\ e^{-i\theta/2}-e^{i\theta/2} & e^{-i\theta/2}+e^{i\theta/2} \end{pmatrix} = \begin{pmatrix} \cos(\theta/2) & -i\sin(\theta/2) \\ -i\sin(\theta/2) & \cos(\theta/2) \end{pmatrix} = R_x(\theta)
$$

**恒等式 7**：$R_y(\theta) = S H R_z(\theta) H S^\dagger$（通过组合 $H$ 和 $S$ 实现轴变换）

### 1.4.4 用恒等式化简电路

**例 1.8** 化简电路：$H T H$。

前面我们计算了 $H T H$ 的矩阵。但利用恒等式可以更巧妙：

$T = R_z(\pi/4)$，而 $H R_z(\theta) H = R_x(\theta)$，所以：

$$
H T H = H R_z(\pi/4) H = R_x(\pi/4)
$$

这个化简把三个门压缩为一个 $R_x(\pi/4)$ 门——在需要优化电路深度时非常有用。

**例 1.9** 化简 $X S X$。

利用恒等式 3：$X R_z(\theta) X = R_z(-\theta)$，且 $S = e^{i\pi/4} R_z(\pi/2)$（忽略全局相位）：

$$
X S X \triangleq X R_z(\pi/2) X = R_z(-\pi/2) \triangleq S^\dagger
$$

所以 $X S X = S^\dagger$（注意忽略全局相位）。

### 1.4.5 门组合的几何图像

从布洛赫球面看，门组合就是**旋转的合成**。三个欧拉角分解的本质就是：

$$
U = R_z(\beta) R_y(\gamma) R_z(\delta)
$$

这意味着任意单比特门都可以理解为：

1. 先绕 $z$ 轴旋转 $\delta$ 角
2. 再绕 $y$ 轴旋转 $\gamma$ 角
3. 最后绕 $z$ 轴旋转 $\beta$ 角

这种"$z$-$y$-$z$"分解在物理实现中特别有用，因为许多硬件平台（如超导量子比特）可以很方便地实现 $z$ 轴旋转（通过虚拟 $z$ 门，见 1.5 节）和 $y$ 轴旋转（通过微波脉冲）。

---

**小练习 1.9** 化简 $X H X$，并验证结果。

**小练习 1.10** 证明：$S^\dagger = S^3$，并用 $S^\dagger$ 表示 $X S X$ 的结果。

**小练习 1.11** 将 $T$ 门表示为 $R_z(\theta)$ 的形式，然后利用恒等式求 $H T H$。

---

## 1.5 物理实现概念

前面的内容全部是纯数学。但真实的量子计算机不是用矩阵乘法的——它们是物理设备，产生电磁脉冲来操控量子态。本节介绍连接"数学门"和"物理门"的关键概念。

### 1.5.1 虚拟 Z 门——相位是物理的，省掉的是 Z 脉冲

在数学上，$R_z(\theta)$ 是对角的：

$$
R_z(\theta) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}.
$$

硬件上实现纵向旋转有两条路：

1. **物理 $Z$**：失谐驱动、磁通偏置、$Z$ 线路上的波形等，让相对相位在真实时间里积累——占门时间，引入噪声与校准负担。  
2. **虚拟 $Z$**：不发专门的 $Z$ 包络，而把等价效果推到**后续横场驱动的载波初相**上。

“虚拟”指的是**不必单独打一发 $Z$ 脉冲**，**不是**说 $Z$ 旋转没有物理对应、全靠软件主观改数。

#### 物理内核：改的是 $X/Y$ 轴在赤道上的指向

旋转波近似下，近共振驱动的有效哈密顿量在相互作用绘景里形如（$\hbar=1$）

$$
H_{\mathrm{drive}}
= \frac{\Omega(t)}{2}\big(\cos\phi\,X + \sin\phi\,Y\big)
= \frac{\Omega(t)}{2}\,R_z(\phi)\,X\,R_z(-\phi),
$$

其中 $\Omega(t)$ 是包络，$\phi$ 是**驱动微波的初相**（相对本振 / 数字上变频的载波相位）。  
因此：

- $\phi=0$ → 绕实验室 $x$ 轴转（$R_x$）；  
- $\phi=\pi/2$ → 绕 $y$ 轴转（$R_y$）；  
- 一般 $\phi$ → 绕赤道上转过 $\phi$ 的轴 $\hat n(\phi)$ 旋转。

共轭恒等式

$$
R_z(\theta)\,R_x(\alpha)\,R_z(-\theta)
= R_{\hat n}(\alpha)
$$

表明：**先做 $R_z(\theta)$ 再做 $R_x$，等价于做一次绕新轴的横场旋转**。  
虚拟 $Z$ 正是利用这一点：需要 $R_z(\theta)$ 时，不在比特上施加纵向波形，而是把**后续所有 $XY$ 脉冲的初相**统一加上 $\theta$（相位帧 $\phi_f\leftarrow\phi_f+\theta$）。  
AWG / 上变频器输出的场是真实的

$$
\varepsilon(t)\propto \Omega(t)\cos(\omega t+\phi_f+\phi_{\mathrm{pulse}}),
$$

**$\phi_f$ 进入物理电磁场**——这是客观的控制自由度，不是“软件里改个标签就算转了”。软件相位帧只是**记录并下发**应当使用的 $\phi_f$；没有这套相位被真正调制进微波，虚拟 $Z$ 不成立。

#### 纠正两种误解

| 误解 | 更正 |
|---|---|
| “虚拟 $Z$=零物理操作，纯软件定义” | 省掉的是**纵向 $Z$ 脉冲**；代价是后续 **$XY$ 驱动初相**必须按帧更新，而初相是物理量 |
| “相位帧只是数学坐标系，与实验无关” | 帧是实验室微波相位参考；改帧 = 改驱动场在 $xy$ 平面的极化方向 |

#### 操作步骤（与编译一致）

1. 维护帧变量 $\phi_f$（初值常 0）。  
2. 遇到电路中的 $R_z(\theta)$：$\phi_f\leftarrow\phi_f+\theta$，**不发射** $Z$ 包络。  
3. 遇到物理 $R_x(\alpha)$ / $R_y$：把脉冲载波初相设为 $\phi_f$（或 $\phi_f+\pi/2$），再发 $\Omega(t)$ 包络。  
4. 测量前若读出对相位敏感，需按约定补偿 $\phi_f$（或在软件里旋转判别轴）。

**优势（在初相控制可靠的前提下）：**

- **零 $Z$ 门时间**、不引入 $Z$ 通道噪声；  
- 角度连续，分辨率受相位位数与本振稳定度限制；  
- 与 ZXZ / 虚拟 $Z$ + 单 $X$ 包络的编译天然合拍。

**例 1.10** 帧初值 $\phi_f=0$：

1. 物理 $R_x(\pi/2)$（$\phi=0$ 的共振脉冲）；  
2. 虚拟 $R_z(\pi/4)$：$\phi_f=\pi/4$（无 $Z$ 包络，但记下物理初相偏移）；  
3. 再发包络形状同 $R_x(\pi/2)$ 的脉冲，**载波初相 $=\pi/4$** → 实验室里这是绕转过 $\pi/4$ 的赤道轴旋转，等效于帧语言中的“$R_z$ 之后的 $R_x$”。

净效果（略全局相位）等价于序列中含 $R_z(\pi/4)$ 的编译结果，例如 $R_x(\pi/2)R_z(\pi/4)R_x(\pi/2)$ 一类目标的实现路径之一。

> **一句话**：虚拟 $Z$ 的物理实在 = **调制 $XY$ 驱动初相以旋转横场轴**；“虚拟”=不占用 $Z$ 脉冲资源，不是否定相位的客观性。更深的旋转波与线路实现见 ch12 / ch27。

### 1.5.2 相位帧跟踪技术

**相位帧跟踪（phase frame tracking）** 是虚拟 $Z$ 门的推广。

**基本流程**：

1. 在量子程序中，每遇到一个 $R_z(\theta)$ 门，并不生成物理脉冲
2. 而是更新一个**帧跟踪变量** $\phi_f$：

$$
   \phi_f \leftarrow \phi_f + \theta
$$

3. 所有后续物理脉冲（如 $R_x(\phi)$）的相位参数偏移 $\phi_f$：

$$
   R_x(\phi) \rightarrow R_x(\phi + \phi_f)
$$

4. 遇到测量指令时，需在测量结果中补偿 $\phi_f$ 的影响

**数学解释**：

设当前量子态为 $|\psi\rangle$，相位帧为 $\phi_f$。在"帧空间"中，我们操作的态是：

$$
|\tilde\psi\rangle = R_z(-\phi_f)|\psi\rangle
$$

即我们"取消"了累计的 $z$ 旋转，使得帧空间中的 $|0\rangle$ 和 $|1\rangle$ 没有相对相位差。

施加一个物理 $R_x(\theta)$ 脉冲（在实验室坐标系中沿 $x$ 轴），相当于在帧空间中施加：

$$
\tilde U = R_z(-\phi_f) R_x(\theta) R_z(\phi_f) = R_{\hat n}(\theta)
$$

其中 $\hat n$ 不是 $x$ 轴，而是在 $xy$ 平面中旋转了 $\phi_f$ 角度的轴——这正是我们想要的：在帧空间中，$R_z(\phi_f)$ 已经被虚拟地完成，而物理脉冲相当于一个绕 $xy$ 平面中某个轴的旋转。

**优势总结**：

- 任何数量的 $R_z$ 门都不消耗时间
- $R_z$ 门的精度只受浮点数精度限制（软件层面）
- 量子电路中的"计数"次数只包含非虚拟门

> **重要说明**：虚拟 $Z$ 门只能在**有参考系**的连续门序列中使用。如果在 $R_z$ 门之后做测量，相位信息不能在测量中恢复——此时 $R_z$ 必须是物理的（除非测量也做相位补偿）。

### 1.5.3 门时间与脉冲长度

物理实现量子门时，每个门需要一定的**门时间（gate time）** $t_g$。

对于绕 $x$ 轴的旋转 $R_x(\theta)$，门时间由**拉比频率（Rabi frequency）** $\Omega$ 决定：

$$
t_g = \frac{\theta}{\Omega}
$$

其中 $\Omega$ 是驱动场的强度（以角频率单位度量）。

**例 1.11** 如果拉比频率 $\Omega = 2\pi \times 20$ MHz，要实现一个 $\pi$ 脉冲（$R_x(\pi)$）：

$$
t_g = \frac{\pi}{2\pi \times 20 \times 10^6} = \frac{1}{40 \times 10^6} = 25 \text{ ns}
$$

**典型时间尺度**（超导量子比特）：

| 操作 | 时间 |
|:---|:---:|
| 单比特门 | 20-100 ns |
| 两比特门 | 50-500 ns |
| 测量 | 100-1000 ns |
| $T_1$（弛豫时间） | 10-100 $\mu$s |
| $T_2$（退相干时间） | 10-100 $\mu$s |

**为什么门时间重要？**

- 门时间越短，在退相干发生前可以执行的运算越多
- 门时间受限于驱动功率（功率越大 $\Omega$ 越大，门越快）
- 但驱动功率受限于非谐性和泄漏层级的限制

### 1.5.4 门保真度定义

量子门不是完美的——硬件噪声、控制误差、退相干都会使门偏离理想幺正操作。**门保真度（gate fidelity）** 量化了一个真实门与理想门的接近程度。

**定义 1.3（门保真度）** 设 $U$ 是理想幺正门，$\mathcal{E}$ 是真实的噪声量子过程（用 Choi 矩阵或过程矩阵表示）。门保真度的常见定义是：

$$
F(U, \mathcal{E}) = \langle \psi| U^\dagger \mathcal{E}(|\psi\rangle\langle\psi|) U |\psi\rangle
$$

其中平均是对所有输入态 $|\psi\rangle$ 进行的。更精确地说，**平均门保真度（average gate fidelity）** 为：

$$
F_{\text{avg}}(U, \mathcal{E}) = \int d\psi \langle\psi| U^\dagger \mathcal{E}(|\psi\rangle\langle\psi|) U |\psi\rangle
$$

其中积分是对所有量子态按 Haar 均匀分布求平均。

**门保真度的直观理解**：

- $F = 1$：完美门（没有误差）
- $F = 0.99$：每 100 次操作中有 1 次出错
- $F = 0.999$：每 1000 次操作中有 1 次出错

**当前技术水平**（截至 2024 年）：

| 平台 | 单比特门保真度 | 两比特门保真度 |
|:---|:---:|:---:|
| 超导 | $> 99.9\%$ | $> 99.5\%$ |
| 离子阱 | $> 99.99\%$ | $> 99.9\%$ |
| 硅量子点 | $> 99.9\%$ | $> 99\%$ |
| 中性原子 | $> 99.9\%$ | $> 99\%$ |

**保真度损失的主要来源**：

1. **退相干**：$T_1$ 和 $T_2$ 过程导致量子信息丢失
2. **控制误差**：脉冲幅度、相位、频率的校准误差
3. **泄漏**：量子比特漏到非计算能级
4. **串扰**：相邻量子比特的耦合干扰
5. **测量误差**：状态读出的错误分类

### 1.5.5 拉比频率与脉冲面积

**拉比振荡（Rabi oscillation）** 是驱动二能级系统时观察到的最基本现象。

考虑一个二能级系统，哈密顿量为：

$$
H = -\frac{\hbar\omega_0}{2} \sigma_z + \hbar\Omega \cos(\omega_d t) \sigma_x
$$

第一项是量子比特的本征能量（$\omega_0$ 是量子比特频率），第二项是微波驱动（$\omega_d$ 是驱动频率）。

在旋转波近似（RWA）和共振驱动（$\omega_d = \omega_0$）下，哈密顿量在旋转坐标系中简化为：

$$
H_{\text{rot}} = \frac{\hbar\Omega}{2} \sigma_x
$$

这个哈密顿量的演化算符是：

$$
U(t) = e^{-i H_{\text{rot}} t/\hbar} = e^{-i (\Omega t/2) \sigma_x} = R_x(\Omega t)
$$

**脉冲面积（pulse area）** 定义为：

$$
A = \int_0^{t_g} \Omega(t) dt
$$

对于恒定驱动（$\Omega$ 不变），$A = \Omega t_g$。

- $\pi$ 脉冲：$A = \pi$，实现 $X$ 门（翻转）
- $\pi/2$ 脉冲：$A = \pi/2$，实现 $\sqrt{X}$ 门或 Hadamard 类操作
- $2\pi$ 脉冲：$A = 2\pi$，回到初始态（但附加全局相位 $-1$）

**例 1.12** 拉比振荡实验。

准备 $|0\rangle$ 态，施加不同长度的驱动脉冲（固定 $\Omega$），然后测量 $P(|1\rangle)$。结果：

$$
P(|1\rangle) = \sin^2\left(\frac{\Omega t}{2}\right)
$$

这是一个正弦振荡——拉比振荡。通过拟合这个正弦曲线，可以精确确定 $\Omega$。

```
P(|1⟩)
1.0 |    ·       ·       ·
    |   / \     / \     / \
0.5 |  /   \   /   \   /   \
    | /     \ /     \ /     \
0.0 |·       ·       ·       ·
    +------------------------→ 时间 t
         π/Ω   2π/Ω   3π/Ω
```

### 1.5.6 脉冲波形

前面我们假设驱动脉冲是矩形的——$\Omega$ 在 $[0, t_g]$ 内恒定。但实际硬件中，矩形脉冲有严重问题：

1. **频谱旁瓣**：矩形脉冲在频域有宽旁瓣（$\text{sinc}$ 函数），会激发非目标能级
2. **泄漏**：如果量子比特有更高能级（如超导量子比特的 $|2\rangle$ 态），矩形脉冲会导致泄漏

因此实际中使用**成形脉冲（shaped pulse）**。

#### 高斯脉冲

最常见的脉冲包络是**高斯函数**：

$$
\Omega(t) = \Omega_0 \exp\left(-\frac{(t - t_0)^2}{2\sigma^2}\right)
$$

其中 $\sigma$ 决定脉冲宽度，$t_0$ 是脉冲中心，$\Omega_0$ 是峰值幅度。

高斯脉冲的频域也是高斯——频谱紧凑，旁瓣低。但高斯脉冲的尾部在有限时间截断会产生小旁瓣。

**优势**：频谱集中，对非目标能级的泄漏小。
**劣势**：在相同峰值功率下，高斯 $\pi$ 脉冲比矩形脉冲慢。

#### DRAG 脉冲

高斯脉冲仍然会导致部分泄漏到 $|2\rangle$ 能级——因为 $|0\rangle \leftrightarrow |1\rangle$ 和 $|1\rangle \leftrightarrow |2\rangle$ 的跃迁频率差（非谐性）有限，驱动脉冲的频谱尾部仍然可以激发 $|1\rangle \leftrightarrow |2\rangle$ 跃迁。

**DRAG（Derivative Removal by Adiabatic Gate）脉冲** 在高斯脉冲的基础上添加一个**同相正交分量**（即 $y$ 分量）来抵消泄漏：

$$
\Omega_x(t) = \Omega_{\text{Gaussian}}(t)
$$

$$
\Omega_y(t) = -\frac{\dot{\Omega}_x(t)}{\Delta}
$$

其中 $\Delta$ 是非谐性（$|1\rangle$ 到 $|2\rangle$ 的跃迁频率与 $|0\rangle$ 到 $|1\rangle$ 的跃迁频率之差）。

**直观解释**：DRAG 利用的是"导数校正"的思想——$y$ 分量的时间导数正好抵消驱动 $x$ 脉冲时产生的非绝热泄漏路径。

**DRAG 的优势**：

- 将泄漏误差降低 1-2 个数量级
- 允许更快的门（因为可以容忍更接近旁瓣的驱动功率）
- 是目前超导量子比特平台的**标准脉冲方案**

### 1.5.7 量子比特的物理哈密顿量概况

以超导量子比特（Transmon）为例，单比特控制的物理哈密顿量（在旋转坐标系下）是：

$$
H = \frac{\hbar}{2} \begin{pmatrix} 0 & \Omega_x(t) - i\Omega_y(t) \\ \Omega_x(t) + i\Omega_y(t) & 0 \end{pmatrix}
$$

其中 $\Omega_x(t)$ 和 $\Omega_y(t)$ 是微波脉冲的**同相（I）和正交（Q）分量**。通过控制 I 和 Q，可以实现绕 $xy$ 平面中任意轴的旋转：

- $\Omega_y = 0$：绕 $x$ 轴旋转
- $\Omega_x = 0$：绕 $y$ 轴旋转
- $\Omega_x, \Omega_y$ 同时非零：绕 $xy$ 平面中某个轴的旋转

**物理实现与数学门的对应**：

| 物理操作 | 数学门 | 说明 |
|:---|:---|:---|
| $\pi$ 脉冲（沿 $x$） | $R_x(\pi)$ | 量子 NOT |
| $\pi/2$ 脉冲（沿 $x$） | $R_x(\pi/2)$ | $\sqrt{X}$ |
| $\pi/2$ 脉冲（沿 $y$） | $R_y(\pi/2)$ | Hadamard 的变体 |
| 虚拟帧更新 | $R_z(\theta)$ | 零时间、零误差 |

---

**小练习 1.12** 如果相位帧初始为 0，依次执行：物理 $R_x(\pi/2)$、虚拟 $R_z(\pi)$、物理 $R_x(\pi/2)$。写出总门矩阵。

**小练习 1.13** 拉比频率 $\Omega = 2\pi \times 50$ MHz，要实现一个 $\pi/2$ 脉冲需要多长时间？

**小练习 1.14** 为什么矩形脉冲的频谱旁瓣会导致泄漏问题？高斯脉冲如何改善这个问题？

---

## 1.6 单比特门校准简介

所有量子门都需要校准——即调整控制参数使实际门与理想门尽可能接近。

### 1.6.1 拉比振荡校准

**目的**：确定正确的脉冲长度（或幅度）以实现特定角度的旋转。

**步骤**：

1. 将量子比特初始化到 $|0\rangle$
2. 施加不同长度（或不同幅度）的驱动脉冲
3. 读取 $P(|1\rangle)$
4. 拟合 $P(|1\rangle) = A\sin^2(\Omega t/2 + \phi_0) + B$

**从拟合结果提取**：

- $\Omega$：拉比频率
- 正确的 $\pi$ 脉冲长度：$t_\pi = \pi/\Omega$
- 正确的 $\pi/2$ 脉冲长度：$t_{\pi/2} = \pi/(2\Omega)$

**常见问题**：

- 如果脉冲幅度不稳定，$\Omega$ 会随时间漂移——需要定期重新校准
- 如果量子比特频率漂移，共振条件被破坏，拉比振荡的频率和幅度都会变化

### 1.6.2 Ramsey 干涉校准

**目的**：校准量子比特频率并测量退相干时间 $T_2^*$。

**步骤**：

1. 制备 $|+\rangle$（用 $\pi/2$ 脉冲）
2. 等待时间 $\tau$
3. 施加第二个 $\pi/2$ 脉冲（相位相对于第一个偏移 $\phi$）
4. 测量 $P(|1\rangle)$

**理论**：在等待期间，量子比特以频率 $\omega_0$ 演化（由哈密顿量 $\hbar\omega_0\sigma_z/2$ 驱动）。如果第二个脉冲的相位与量子比特的演化相位一致，会发生相长干涉（$P=0$）；如果不一致，发生相消干涉（$P=1$）。

$$
P(|1\rangle) = \frac{1}{2}\left[1 - e^{-\tau/T_2^*} \cos(\Delta \tau)\right]
$$

其中 $\Delta$ 是驱动频率与量子比特频率的失谐，$T_2^*$ 是 Ramsey 退相干时间。

**校准用途**：

- 拟合 $\Delta$ 的值可精确确定量子比特频率（误差 < kHz）
- 拟合 $T_2^*$ 可诊断低频噪声环境

### 1.6.3 门保真度测量：随机基准测试

**随机基准测试（Randomized Benchmarking, RB）** 是目前最常用的门保真度测量方法。

**问题**：直接测量门保真度面临**态制备和测量误差（SPAM errors）**——你无法区分误差来自门还是来自准备/读取过程。

**RB 的核心思想**：

1. 随机生成 $m$ 个 Clifford 门序列（Clifford 门是量子门的一个子集，包含 $H$、$S$、$X$、$Y$、$Z$ 等）
2. 这些序列的最后一个门被选为"反转门"——使得整个序列的净效果是恒等操作
3. 执行序列并测量 $P(0)$（预期结果：$P(0) = 1$）
4. 对不同的 $m$ 重复，拟合 $P(0) = A p^m + B$

**保真度提取**：

$$
F_{\text{avg}} = 1 - \frac{d-1}{d}(1-p), \quad d = 2^n
$$

对于单比特（$d=2$）：

$$
F_{\text{avg}} = 1 - \frac{1}{2}(1-p)
$$

其中 $p$ 是 RB 拟合得到的**每门误差率**。

**RB 的优势**：

- **不受 SPAM 误差影响**：SPAM 误差被拟合参数 $A, B$ 吸收
- **对门误差的估计无偏**：随机序列平均了各种噪声源的影响
- **可扩展到两比特和多比特**

**典型 RB 结果**：

```
P(0)
1.0 |·
    | \
0.5 |  \
    |   \
0.0 |    ········→ 门数 m
    |
    +-------------------→
```

$P(0)$ 随 $m$ 指数衰减到 $1/2$（单比特）。衰减率 $p$ 给出了每门保真度。

---

**小练习 1.15** 在拉比振荡校准中，如果测得 $P(|1\rangle)$ 的振荡频率为 $\Omega/2\pi = 20$ MHz，那么 $\pi$ 脉冲的长度是多少？

**小练习 1.16** 为什么 RB 的拟合公式中有 $A$ 和 $B$ 两个自由参数？它们分别吸收了什么误差？

---

!!! tip "超导实现视角"
    **对象**：计算基 $\{|0\rangle,|1\rangle\}$、单比特门 $R_x/R_y/R_z$、门序列与虚拟 $Z$、单比特校准与 RB。
    **超导载体**：固定频率 Transmon 的最低两能级；芯片上的 $XY$ 驱动线；控制软件中的**相位帧**（实现虚拟 $Z$）；色散读出谐振器（用于观测 $|0\rangle/|1\rangle$）。
    **操作要点**：$R_x/R_y$ 由近谐振微波脉冲的包络与相位实现（拉比转动）；任意 $R_z$ 通常**不发射脉冲**，只更新后续驱动的参考相位；$\pi$ 脉宽、驱动幅度与帧对齐靠拉比/RB 等实验标定。泄漏到 $|2\rangle$ 由非谐性与脉冲整形约束（详见总汇章）。
    **深读**：ch12 §6.3 微波驱动与 $X$ 门、§6.4 虚拟 $Z$、§6.6 保真度与 $T_1/T_2$、§6.8 门校准；器件背景见 ch25。

**对照思考（选做）** 把电路中的 $R_z(\theta)\,R_x(\pi/2)$ 翻译成「需要下发几段物理微波、相位帧如何变」；说明为何 $R_z$ 本身往往不占用门时间。

---

## 1.7 本章习题

### ★ 基础题（第 1-8 题）

**1.** 判断以下状态是否是合法量子比特态。若不是，请归一化。

(a) $|\psi\rangle = \frac{1}{3}|0\rangle + \frac{2}{3}|1\rangle$

(b) $|\psi\rangle = \frac{1}{\sqrt{3}}|0\rangle + \sqrt{\frac{2}{3}}|1\rangle$

(c) $|\psi\rangle = \frac{1+i}{2}|0\rangle + \frac{1}{2}|1\rangle$

(d) $|\psi\rangle = 0.6|0\rangle + 0.8i|1\rangle$

**2.** 将以下量子态用布洛赫球面坐标 $(\theta, \varphi)$ 表示：

(a) $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$

(b) $\frac{1}{\sqrt{2}}(|0\rangle - i|1\rangle)$

(c) $\frac{\sqrt{3}}{2}|0\rangle + \frac{1}{2}|1\rangle$

(d) $0.8|0\rangle + 0.6i|1\rangle$

**3.** 计算以下门作用在给定态上的结果：

(a) $X|+\rangle$

(b) $Z|-\rangle$

(c) $H|0\rangle$

(d) $S H|0\rangle$

(e) $T S|+\rangle$

(f) $H T H|0\rangle$

**4.** 写出下列矩阵对应的量子门名称：

(a) $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$

(b) $\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

(c) $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$

(d) $\begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$

(e) $\begin{pmatrix} \cos\frac{\pi}{8} & -\sin\frac{\pi}{8} \\ \sin\frac{\pi}{8} & \cos\frac{\pi}{8} \end{pmatrix}$

**5.** 验证以下恒等式：

(a) $H S H = R_x(\pi/2)$（忽略全局相位）

(b) $X R_y(\theta) X = R_y(-\theta)$

(c) $S^\dagger = S^3$

**6.** 计算 $R_x(\pi/2)|0\rangle$ 和 $R_y(\pi/2)|0\rangle$，并解释它们在布洛赫球面上的几何意义。

**7.** 对于 $|\psi\rangle = \frac{1}{\sqrt{2}}(|0\rangle + e^{i\theta}|1\rangle)$，计算 $\langle\psi|X|\psi\rangle$。当 $\theta$ 从 0 变到 $2\pi$ 时，这个期望值如何变化？

**8.** 写出 $R_z(\theta)$ 的矩阵形式。证明 $R_z(\theta_1) R_z(\theta_2) = R_z(\theta_1 + \theta_2)$。

### ★★ 计算题（第 9-14 题）

**9.** 用 Z-Y 分解将 $H$ 门表示为 $e^{i\alpha} R_z(\beta) R_y(\gamma) R_z(\delta)$ 的形式（求出具体的 $\alpha, \beta, \gamma, \delta$）。

**10.** 证明：$H R_z(\theta) H = R_x(\theta)$。利用这个恒等式，将 $H T H$ 化简为单个 $R_x$ 门。

**11.** 考虑一个序列：$R_z(\pi/2) R_x(\pi/2) R_z(\pi/2)$。

(a) 写出这个序列的矩阵形式。

(b) 这个序列等于哪个单比特门（不包含全局相位）？

(c) 在布洛赫球面上描述这个序列的作用。

**12.** 用 Z-Y 分解定理证明：任意单比特门可以表示为 $R_z(\phi) R_x(\theta) R_z(\psi)$ 的形式。

**12′.** **$R_i(\theta)$ 从何而来？**  
(a) 由 $R_i(\theta)=e^{-i\theta\sigma_i/2}$（$i=x,y,z$）推导 $R_x(\theta),R_y(\theta),R_z(\theta)$ 的 $2\times2$ 矩阵（本征分解或级数任选）。  
(b) 任选 **ZYZ** 或 **XYX** 一种，说明任意 $U\in SU(2)$ 的角度如何从矩阵元反解（写出步骤即可，可对照定理 1.2）。  
(c) 用一句话说明：为何超导微波平台常把分解写成“虚拟 $R_z$ + 物理 $R_x$”，而不是三次都打失谐 $Z$ 脉冲？

**13.** **相位帧跟踪**：假设初始相位帧为 0。执行以下操作序列：

- 物理 $R_x(\pi/2)$
- 虚拟 $R_z(\pi/3)$
- 物理 $R_x(\pi/2)$
- 虚拟 $R_z(\pi/4)$
- 物理 $R_x(\pi/2)$

(a) 写出相位帧的每次更新值。

(b) 写出整个序列的净幺正算符（不计全局相位）。

**14.** **拉比振荡**：某量子比特的拉比频率 $\Omega = 2\pi \times 30$ MHz。

(a) 实现 $\pi$ 脉冲需要多长时间？

(b) 实现 $R_x(\pi/3)$ 需要多长时间？

(c) 如果脉冲形状是高斯的，峰值幅度 $\Omega_0 = 2\pi \times 30$ MHz，要实现 $\pi$ 脉冲，高斯脉冲的宽度 $\sigma$ 大约是多少？（假设脉冲面积 $A = \int \Omega(t) dt = \pi$，$\int_{-\infty}^{\infty} \exp(-t^2/2\sigma^2) dt = \sigma\sqrt{2\pi}$）

### ★★★ 综合题（第 15-18 题）

**15.** **欧拉分解的证明**：对于任意 $2 \times 2$ 幺正矩阵 $U$（设 $\det U = 1$），证明存在 $\alpha, \beta, \gamma \in \mathbb{R}$ 使得：

$$
U = e^{i\alpha} R_z(\beta) R_y(\gamma) R_z(\delta)
$$

提示：将 $U$ 参数化为 $\begin{pmatrix} a & b \\ -b^* & a^* \end{pmatrix}$，然后与 $R_z R_y R_z$ 的展开式比较。

**16.** **DRAG 原理**：超导量子比特的非谐性通常约为 200-400 MHz。假设 Transmon 的 $|0\rangle \leftrightarrow |1\rangle$ 频率为 5 GHz，$|1\rangle \leftrightarrow |2\rangle$ 频率为 4.7 GHz（非谐性 $-300$ MHz）。

(a) 如果使用高斯脉冲实现 $\pi$ 脉冲，脉冲频谱的旁瓣可能在什么频率上激发 $|1\rangle \leftrightarrow |2\rangle$ 跃迁？

(b) DRAG 脉冲通过添加 $y$ 分量来抵消泄漏。解释为什么 $\Omega_y(t) \propto \dot{\Omega}_x(t)$ 能够实现这一效果。

(c) 更快的门需要使用更宽的频谱——这增加了泄漏。解释为什么 DRAG 允许比高斯脉冲更快的门。

**17.** **随机基准测试的拟合**：单比特 RB 实验测得不同序列长度 $m$ 下的 $P(0)$：

| $m$ | $P(0)$ |
|:---:|:---:|
| 1 | 0.992 |
| 2 | 0.984 |
| 4 | 0.968 |
| 8 | 0.940 |
| 16 | 0.880 |
| 32 | 0.780 |
| 64 | 0.620 |

(a) 拟合 $P(0) = A p^m + B$，估算 $p$ 的值。

(b) 计算每门平均保真度 $F_{\text{avg}}$。

(c) 如果量子计算机有 100 个这样的单比特门，所有门都执行正确的概率大约是多少？（假设门误差独立）

**18.** **综合：从数学到物理**：你需要在超导量子比特上实现门 $U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}$。

(a) 这个门等于哪个参数化旋转门？写出它的名称和参数。

(b) 用欧拉 Z-Y 分解将 $U$ 拆解为 $R_z$ 和 $R_y$ 门的组合。

(c) 假设 $\Omega = 2\pi \times 40$ MHz，且所有物理旋转都通过微波脉冲实现，虚拟 $Z$ 门通过相位帧跟踪实现。写出实现 $U$ 的完整脉冲方案（包括哪些脉冲是物理的、哪些是虚拟的，以及每个脉冲的持续时间和相位）。

(d) 如果虚拟 $Z$ 门的相位帧跟踪因为软件 bug 导致 $1\%$ 的角度误差，最终门 $U$ 的保真度损失约为多少？（估算）

---

## 知识点索引

| 术语 | 页码 |
|:---|:---:|
| 量子比特（qubit） | 1.1 |
| 计算基 | 1.1 |
| 概率幅 | 1.1 |
| 叠加态 | 1.1 |
| 布洛赫球面 | 1.1 |
| 幺正算符 | 1.2 |
| 泡利 X 门 | 1.2 |
| 泡利 Y 门 | 1.2 |
| 泡利 Z 门 | 1.2 |
| Hadamard 门 | 1.2 |
| 相位门（S 门） | 1.2 |
| T 门（$\pi/8$ 门） | 1.2 |
| 参数化旋转门 | 1.3 |
| $R_x(\theta)$ 门 | 1.3 |
| $R_y(\theta)$ 门 | 1.3 |
| $R_z(\theta)$ 门 | 1.3 |
| 欧拉分解 | 1.3 |
| Z-Y 分解定理 | 1.3 |
| 门组合化简 | 1.4 |
| 相位门家族 | 1.4 |
| 虚拟 $Z$ 门 | 1.5 |
| 相位帧跟踪 | 1.5 |
| 门时间 | 1.5 |
| 门保真度 | 1.5 |
| 平均门保真度 | 1.5 |
| 拉比频率 | 1.5 |
| 拉比振荡 | 1.5 |
| 脉冲面积 | 1.5 |
| $\pi$ 脉冲 | 1.5 |
| $\pi/2$ 脉冲 | 1.5 |
| 高斯脉冲 | 1.5 |
| DRAG 脉冲 | 1.5 |
| 泄漏 | 1.5 |
| 非谐性 | 1.5 |
| 校准 | 1.6 |
| 拉比振荡校准 | 1.6 |
| Ramsey 干涉 | 1.6 |
| 随机基准测试（RB） | 1.6 |
| SPAM 误差 | 1.6 |
| Clifford 门 | 1.6 |

---

> **第 1 章结束**
>
> 下一章：第 2 章 多量子比特门与纠缠
