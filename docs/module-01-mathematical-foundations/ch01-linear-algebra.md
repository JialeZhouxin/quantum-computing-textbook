# 第1章 线性代数

> **本章导读**
>
> 量子计算的语言是线性代数。不理解线性代数，就无法理解量子计算。本章从最基础的复数开始，一步步建立你需要的全部数学工具。狄拉克符号和张量积是初学者最大的两个痛点，我们会用大量实例把它们讲透。

---

## 1.1 复数回顾

### 1.1.1 为什么量子计算离不开复数？

在经典计算中，我们用 0 和 1 表示信息。但在量子世界，一个量子比特可以处于"既是 0 又是 1"的状态——我们称之为**叠加态**。描述叠加态需要"概率幅"，而概率幅正是复数。

换句话说：没有复数，就没有量子力学。

本节的目的是唤醒你对复数的记忆，并建立一些对后续章节至关重要的直觉。

### 1.1.2 复数的代数表示

一个**复数** $z$ 可以写成：

$$
z = a + bi
$$

其中 $a, b$ 是实数，$i$ 是**虚数单位**，满足 $i^2 = -1$。$a$ 称为 $z$ 的**实部**，记作 $\text{Re}(z)$；$b$ 称为 $z$ 的**虚部**，记作 $\text{Im}(z)$。

**例 1.1**  $z = 3 + 4i$，则 $\text{Re}(z) = 3$，$\text{Im}(z) = 4$。

**例 1.2**  $z = -2i$，则 $\text{Re}(z) = 0$，$\text{Im}(z) = -2$。这是一个纯虚数。

两个复数相等当且仅当它们的实部和虚部分别相等：

$$
a + bi = c + di \iff a = c \text{ 且 } b = d
$$

**复数加减法**：实部加实部，虚部加虚部。

$$
(a + bi) \pm (c + di) = (a \pm c) + (b \pm d)i
$$

**复数乘法**：像多项式一样展开，注意 $i^2 = -1$。

$$
(a + bi)(c + di) = ac + adi + bci + bdi^2 = (ac - bd) + (ad + bc)i
$$

**例 1.3**  $(2 + 3i)(1 - i) = 2(1) + 2(-i) + 3i(1) + 3i(-i) = 2 - 2i + 3i - 3i^2 = 2 + i + 3 = 5 + i$。

**复数除法**：利用共轭把分母实数化。

$$
\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}
$$

### 1.1.3 复平面与几何表示

把复数 $z = a + bi$ 看作二维平面上的一个点——横坐标是实部 $a$，纵坐标是虚部 $b$。这个平面称为**复平面**（或 Argand 平面）。

<svg viewBox="0 0 440 350" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; display: block; margin: 1.5em auto;">
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
  </defs>
  <line x1="35" y1="285" x2="415" y2="285" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <line x1="75" y1="305" x2="75" y2="20" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <line x1="159" y1="282" x2="159" y2="288" stroke="#aaa" stroke-width="1"/>
  <line x1="243" y1="282" x2="243" y2="288" stroke="#aaa" stroke-width="1"/>
  <line x1="327" y1="282" x2="327" y2="288" stroke="#aaa" stroke-width="1"/>
  <line x1="72" y1="201" x2="78" y2="201" stroke="#aaa" stroke-width="1"/>
  <line x1="72" y1="117" x2="78" y2="117" stroke="#aaa" stroke-width="1"/>
  <line x1="75" y1="159" x2="243" y2="159" stroke="#bbb" stroke-width="1" stroke-dasharray="5,4"/>
  <line x1="243" y1="285" x2="243" y2="165" stroke="#bbb" stroke-width="1" stroke-dasharray="5,4"/>
  <path d="M 120,285 A 45,45 0 0,1 111,258" fill="none" stroke="#e65100" stroke-width="1.8"/>
  <line x1="75" y1="285" x2="243" y2="159" stroke="#00695c" stroke-width="2.5"/>
  <circle cx="243" cy="159" r="5" fill="#00695c"/>
  <text x="400" y="280" font-family="Georgia, serif" font-size="16" fill="#333" font-style="italic">Re</text>
  <text x="30" y="30" font-family="Georgia, serif" font-size="16" fill="#333" font-style="italic">Im</text>
  <text x="55" y="283" font-family="Georgia, serif" font-size="15" fill="#333" font-weight="bold">O</text>
  <text x="233" y="305" font-family="Georgia, serif" font-size="14" fill="#555" font-style="italic">a = Re(z)</text>
  <text x="10" y="163" font-family="Georgia, serif" font-size="14" fill="#555" font-style="italic">b = Im(z)</text>
  <text x="252" y="152" font-family="Georgia, serif" font-size="15" fill="#00695c" font-weight="bold" font-style="italic">z</text>
  <text x="168" y="205" font-family="Georgia, serif" font-size="14" fill="#00695c" font-style="italic">r = |z|</text>
  <text x="95" y="268" font-family="Georgia, serif" font-size="15" fill="#e65100" font-style="italic">θ</text>
  <text x="295" y="152" font-family="Georgia, serif" font-size="13" fill="#888">a + bi</text>
</svg>

从原点到点 $z$ 的线段长度称为 $z$ 的**模**（或绝对值），记作 $|z|$：

$$
|z| = \sqrt{a^2 + b^2}
$$

从正实轴逆时针旋转到线段 $Oz$ 的角度称为 $z$ 的**幅角**，记作 $\arg(z)$：

$$
\arg(z) = \theta = \arctan\left(\frac{b}{a}\right)
$$

**例 1.4**  $z = 1 + i$，则 $|z| = \sqrt{1^2 + 1^2} = \sqrt{2}$，$\arg(z) = \arctan(1) = \pi/4$（即 45°）。

### 1.1.4 欧拉公式

欧拉公式是数学中最优美的公式之一：

$$
e^{i\theta} = \cos\theta + i\sin\theta
$$

**直观理解**：当 $\theta$ 从 0 增加到 $2\pi$ 时，$e^{i\theta}$ 在复平面上画出一个单位圆。$e^{i\theta}$ 的模永远是 1，幅角是 $\theta$。

$$
|e^{i\theta}| = \sqrt{\cos^2\theta + \sin^2\theta} = 1
$$

**特例**（欧拉恒等式）：

$$
e^{i\pi} = -1 \quad \text{或} \quad e^{i\pi} + 1 = 0
$$

这个公式把五个最重要的数学常数 $e, i, \pi, 1, 0$ 联系在了一起。

**为什么这对量子计算重要？** 量子态的演化经常用 $e^{-i\theta H}$ 这样的算符描述（见 1.10 节）。你现在只需要记住：复指数是三角函数的一种简洁写法。

**例 1.5**  用欧拉公式表示 $z = 1 + i$ 的极坐标形式。

解：$r = \sqrt{2}$，$\theta = \pi/4$，所以

$$
1 + i = \sqrt{2}e^{i\pi/4} = \sqrt{2}\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right)
$$

### 1.1.5 复共轭与模方

复数 $z = a + bi$ 的**复共轭**记作 $\overline{z}$ 或 $z^*$：

$$
\overline{z} = a - bi
$$

在复平面上，共轭就是把点关于实轴做镜像。

**重要性质**：
- $\overline{\overline{z}} = z$
- $\overline{z_1 \pm z_2} = \overline{z_1} \pm \overline{z_2}$
- $\overline{z_1 z_2} = \overline{z_1} \cdot \overline{z_2}$
- $\overline{(z_1 / z_2)} = \overline{z_1} / \overline{z_2}$

**模方**定义为一个复数乘以其共轭：

$$
|z|^2 = \overline{z} \cdot z = (a - bi)(a + bi) = a^2 + b^2
$$

注意 $|z|^2$ 是一个非负实数。这个性质在量子力学中极其重要——概率幅的模方就是概率。

**例 1.6**  $z = 3 + 4i$，$\overline{z} = 3 - 4i$，$|z|^2 = 3^2 + 4^2 = 25$，$|z| = 5$。

### 1.1.6 用 Python 画复数

虽然本书主要讲数学，但用代码验证能加深理解。以下 Python 代码在复平面上画出几个复数：

```python
import matplotlib.pyplot as plt
import numpy as np

# 定义几个复数
points = [1+2j, -2+1j, -1.5-1j, 2-1.5j, 1+0j]
labels = ['1+2i', '-2+i', '-1.5-i', '2-1.5i', '1']

plt.figure(figsize=(6,6))
for p, l in zip(points, labels):
    plt.plot(p.real, p.imag, 'o')
    plt.text(p.real+0.1, p.imag+0.1, l)

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.grid(True)
plt.xlabel('实部')
plt.ylabel('虚部')
plt.title('复平面上的点')
plt.axis('equal')
plt.show()
```

运行这段代码会看到复平面上五个点。你可以修改 `points` 列表来探索更多复数。

### 1.1.7 复数的应用：描述振荡

在量子力学中，一个自由粒子的波函数常用 $e^{i(kx - \omega t)}$ 描述。利用欧拉公式：

$$
e^{i(kx - \omega t)} = \cos(kx - \omega t) + i\sin(kx - \omega t)
$$

这描述了一个传播的波。复指数比三角函数更容易做微积分运算，这是物理学家喜欢用复数的原因之一。

---

**小练习**：计算 $(1 + 2i)(3 - i)$，并用极坐标形式表示结果。

**小练习**：验证 $|e^{i\theta}| = 1$ 对任意 $\theta$ 成立。

---

## 1.2 向量空间

### 1.2.1 从箭头到向量

你最早接触的"向量"可能是一个带箭头的线段：有大小、有方向。在物理中，速度、力都是向量。

在数学中，我们把向量的概念抽象化了。一个**向量**就是一个可以相加、可以被数乘的对象。这里的"数"可以是实数（$\mathbb{R}$）或复数（$\mathbb{C}$）。

**定义 1.1（向量空间）** 一个 **向量空间**（或线性空间）$V$ 是一个集合，其中的元素称为**向量**。向量空间满足以下公理：

1. **加法封闭性**：对任意 $u, v \in V$，$u + v \in V$
2. **加法交换律**：$u + v = v + u$
3. **加法结合律**：$(u + v) + w = u + (v + w)$
4. **零向量**：存在 $0 \in V$，使得 $v + 0 = v$
5. **负向量**：对每个 $v \in V$，存在 $-v \in V$，使得 $v + (-v) = 0$
6. **数乘封闭性**：对任意 $c \in \mathbb{F}$（$\mathbb{F}$ 是 $\mathbb{R}$ 或 $\mathbb{C}$）和 $v \in V$，$cv \in V$
7. **数乘结合律**：$c(dv) = (cd)v$
8. **数乘分配律 1**：$c(u + v) = cu + cv$
9. **数乘分配律 2**：$(c + d)v = cv + dv$
10. **单位元**：$1v = v$

你不需要死记这十条。直觉上：**向量空间就是一个可以做加法和数乘的集合，运算结果仍在集合里**。

### 1.2.2 Rⁿ 和 Cⁿ——最重要的向量空间

$\mathbb{R}^n$ 是所有 $n$ 维实向量的集合：

$$
\mathbb{R}^n = \left\{ \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} \bigg| x_i \in \mathbb{R} \right\}
$$

$\mathbb{C}^n$ 是所有 $n$ 维复向量的集合（分量可以是复数）：

$$
\mathbb{C}^n = \left\{ \begin{pmatrix} z_1 \\ z_2 \\ \vdots \\ z_n \end{pmatrix} \bigg| z_i \in \mathbb{C} \right\}
$$

量子力学中的态空间是 $\mathbb{C}^n$（更准确地说，是希尔伯特空间，但初学时可以当作 $\mathbb{C}^n$）。

**例 1.7**  $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$ 和 $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$ 是 $\mathbb{C}^2$ 中的向量，分别对应量子比特的 $|0\rangle$ 和 $|1\rangle$ 态。

**例 1.8**  $\begin{pmatrix} 1 + i \\ 2 \\ -3i \end{pmatrix}$ 是 $\mathbb{C}^3$ 中的向量。

### 1.2.3 线性组合与线性无关

给定一组向量 $v_1, v_2, \dots, v_k$ 和一组标量（系数）$c_1, c_2, \dots, c_k$，表达式

$$
c_1 v_1 + c_2 v_2 + \cdots + c_k v_k
$$

称为 $v_1, \dots, v_k$ 的**线性组合**。

**定义 1.2（线性无关）** 一组向量 $v_1, v_2, \dots, v_k$ 称为**线性无关**的，如果线性组合为零向量只能通过所有系数为零来实现：

$$
c_1 v_1 + c_2 v_2 + \cdots + c_k v_k = 0 \implies c_1 = c_2 = \cdots = c_k = 0
$$

换句话说，没有一个向量可以表示为其他向量的线性组合。

**例 1.9**  $v_1 = \begin{pmatrix}1 \\ 0\end{pmatrix}$，$v_2 = \begin{pmatrix}0 \\ 1\end{pmatrix}$ 线性无关。因为 $c_1 v_1 + c_2 v_2 = \begin{pmatrix}c_1 \\ c_2\end{pmatrix} = \begin{pmatrix}0 \\ 0\end{pmatrix}$ 必须 $c_1 = c_2 = 0$。

**例 1.10**  $v_1 = \begin{pmatrix}1 \\ 2\end{pmatrix}$，$v_2 = \begin{pmatrix}2 \\ 4\end{pmatrix}$ 线性相关，因为 $2v_1 - v_2 = 0$。

### 1.2.4 基与维度

**定义 1.3（基）** 一组向量 $\{b_1, \dots, b_n\}$ 称为向量空间 $V$ 的**基**，如果：
1. 它们线性无关
2. $V$ 中的每个向量都可以唯一地表示为它们的线性组合

空间的**维度**就是基中向量的个数。

**例 1.11**  $\mathbb{R}^2$ 的一组标准基是：

$$
e_1 = \begin{pmatrix}1 \\ 0\end{pmatrix}, \quad e_2 = \begin{pmatrix}0 \\ 1\end{pmatrix}
$$

任意向量 $\begin{pmatrix}x \\ y\end{pmatrix} = x e_1 + y e_2$，所以 $\dim(\mathbb{R}^2) = 2$。

**例 1.12**  $\mathbb{C}^n$ 作为复向量空间，维度是 $n$。同样地，$\mathbb{R}^n$ 作为实向量空间，维度也是 $n$。

**为什么这很重要？** 一个 $n$ 维量子系统的态空间有 $n$ 个基态。例如，一个量子比特（2 维系统）有两个基态 $|0\rangle$ 和 $|1\rangle$。两个量子比特的系统是 4 维的，基态为 $|00\rangle, |01\rangle, |10\rangle, |11\rangle$（见 1.8 节）。

### 1.2.5 基变换

同一个向量可以用不同的基表示。**基变换**就是用一组基表示另一组基下的坐标。

假设有两组基 $\{e_1, e_2\}$ 和 $\{f_1, f_2\}$。若

$$
f_1 = a e_1 + c e_2, \quad f_2 = b e_1 + d e_2
$$

则从 $\{e\}$-基到 $\{f\}$-基的**过渡矩阵**为 $P = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$。

向量 $v$ 在两组基下的坐标 $v_e$ 和 $v_f$ 满足：

$$
v_e = P v_f
$$

**例 1.13**  令 $e_1 = \begin{pmatrix}1 \\ 0\end{pmatrix}, e_2 = \begin{pmatrix}0 \\ 1\end{pmatrix}$，$f_1 = \begin{pmatrix}1 \\ 1\end{pmatrix}, f_2 = \begin{pmatrix}1 \\ -1\end{pmatrix}$。

则 $f_1 = e_1 + e_2$，$f_2 = e_1 - e_2$，过渡矩阵 $P = \begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}$。

向量 $v = \begin{pmatrix}3 \\ 1\end{pmatrix}$ 在标准基下是 $(3,1)^T$。在 $\{f\}$-基下：

$$
v_f = P^{-1} v_e = \frac{1}{2}\begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}^{-1} \begin{pmatrix}3 \\ 1\end{pmatrix}
$$

计算得 $v_f = \begin{pmatrix}2 \\ 1\end{pmatrix}$，即 $v = 2 f_1 + 1 f_2$。

验证：$2(1,1)^T + 1(1,-1)^T = (3,1)^T$，正确。

### 1.2.6 子空间

**定义 1.4（子空间）** $V$ 的子集 $W$ 称为**子空间**，如果 $W$ 本身也是一个向量空间（在同样的加法和数乘下）。

判断子空间的简便方法：检查 $W$ 是否对加法和数乘封闭，且包含零向量。

**例 1.14**  在 $\mathbb{R}^3$ 中，过原点的平面 $\{ (x,y,z) | x + y + z = 0 \}$ 是一个子空间。但不过原点的平面不是子空间（不含零向量）。

**例 1.15**  所有对角矩阵构成 $n \times n$ 矩阵空间的一个子空间。

在量子力学中，物理系统的可能状态集合是总希尔伯特空间的一个子空间。

---

**小练习**：判断 $\left\{ \begin{pmatrix} x \\ y \end{pmatrix} \in \mathbb{R}^2 \bigg| x \geq 0, y \geq 0 \right\}$ 是否是 $\mathbb{R}^2$ 的子空间。为什么？

**小练习**：找出 $\mathbb{R}^3$ 中向量 $(1,2,3)$ 和 $(0,1,1)$ 的所有线性组合构成的子空间的维度。

---

## 1.3 内积与正交性

### 1.3.1 从点积到内积

在 $\mathbb{R}^2$ 或 $\mathbb{R}^3$ 中，你学过**点积**（点乘、数量积）：

$$
u \cdot v = |u||v| \cos\theta
$$

其中 $\theta$ 是两个向量的夹角。点积为零 $\iff$ 两个向量垂直。

现在我们要把这个概念推广到复向量空间，并改名为**内积**。

### 1.3.2 内积的定义

**定义 1.5（内积）** 向量空间 $V$ 上的**内积**是一个函数 $\langle \cdot, \cdot \rangle: V \times V \to \mathbb{C}$，满足：

1. **正定性**：$\langle v, v \rangle \geq 0$，且 $\langle v, v \rangle = 0 \iff v = 0$
2. **共轭对称性**：$\langle u, v \rangle = \overline{\langle v, u \rangle}$
3. **线性性（第一变元）**：$\langle c_1 u_1 + c_2 u_2, v \rangle = c_1 \langle u_1, v \rangle + c_2 \langle u_2, v \rangle$

注意：对第二变元，内积是共轭线性的：

$$
\langle u, c_1 v_1 + c_2 v_2 \rangle = \overline{c_1} \langle u, v_1 \rangle + \overline{c_2} \langle u, v_2 \rangle
$$

### 1.3.3 标准内积

在 $\mathbb{C}^n$ 中，**标准内积**（也叫欧几里得内积）定义为：

$$
\langle u, v \rangle = \sum_{i=1}^n \overline{u_i} v_i = \overline{u_1} v_1 + \overline{u_2} v_2 + \cdots + \overline{u_n} v_n
$$

注意共轭加在第一个向量上。如果把向量写成列向量，则：

$$
\langle u, v \rangle = u^\dagger v = \begin{pmatrix} \overline{u_1} & \overline{u_2} & \cdots & \overline{u_n} \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix}
$$

其中 $u^\dagger$ 是 $u$ 的**共轭转置**（先转置，再取共轭）。

**例 1.16**  $u = \begin{pmatrix} 1 + i \\ 2 \end{pmatrix}$, $v = \begin{pmatrix} 3 \\ 4i \end{pmatrix}$。

$$
\langle u, v \rangle = \overline{1+i} \cdot 3 + \overline{2} \cdot 4i = (1-i) \cdot 3 + 2 \cdot 4i = 3 - 3i + 8i = 3 + 5i
$$

**例 1.17**  若 $u, v$ 都是实向量（所有分量为实数），则标准内积退化为点积：

$$
\langle u, v \rangle = u^T v = u_1 v_1 + \cdots + u_n v_n
$$

### 1.3.4 范数（长度）

**定义 1.6（范数）** 向量 $v$ 的**范数**（长度）定义为：

$$
\| v \| = \sqrt{\langle v, v \rangle}
$$

**性质**：
- $\| v \| \geq 0$，$\| v \| = 0 \iff v = 0$
- $\| c v \| = |c| \| v \|$（缩放性质）
- **三角不等式**：$\| u + v \| \leq \| u \| + \| v \|$
- **柯西-施瓦茨不等式**：$|\langle u, v \rangle| \leq \| u \| \cdot \| v \|$

**例 1.18**  计算 $v = \begin{pmatrix} 1 + i \\ 2 - i \end{pmatrix}$ 的范数。

$$
\langle v, v \rangle = (1-i)(1+i) + (2+i)(2-i) = (1+1) + (4+1) = 7
$$

所以 $\| v \| = \sqrt{7}$。

**归一化**：把一个非零向量除以它的范数，得到**单位向量**：

$$
\hat{v} = \frac{v}{\| v \|}
$$

这个过程称为**归一化**。量子力学中，所有态向量都是归一化的：$\langle \psi | \psi \rangle = 1$。

### 1.3.5 正交性

**定义 1.7（正交）** 两个向量 $u, v$ 称为**正交**的，如果 $\langle u, v \rangle = 0$。

在实空间中，正交就是"垂直"。在复空间中，这个几何直觉仍然适用。

**例 1.19**  $u = \begin{pmatrix}1 \\ 0\end{pmatrix}$, $v = \begin{pmatrix}0 \\ 1\end{pmatrix}$ 在 $\mathbb{C}^2$ 中正交：

$$
\langle u, v \rangle = 1 \cdot 0 + 0 \cdot 1 = 0
$$

**例 1.20**  $|0\rangle = \begin{pmatrix}1 \\ 0\end{pmatrix}$ 和 $|1\rangle = \begin{pmatrix}0 \\ 1\end{pmatrix}$ 正交。这是量子比特的两个基态。

**正交补**：子空间 $W$ 的**正交补** $W^\perp$ 是所有与 $W$ 中每个向量正交的向量的集合：

$$
W^\perp = \{ v \in V \mid \langle v, w \rangle = 0, \forall w \in W \}
$$

### 1.3.6 标准正交基

**定义 1.8（标准正交基）** 一组基 $\{ e_1, e_2, \dots, e_n \}$ 称为**标准正交基**（orthonormal basis），如果：
1. $\langle e_i, e_j \rangle = 0$ 当 $i \neq j$（正交）
2. $\| e_i \| = 1$（归一）

**例 1.21**  $\mathbb{R}^2$ 的标准正交基：

$$
e_1 = \begin{pmatrix}1 \\ 0\end{pmatrix}, \quad e_2 = \begin{pmatrix}0 \\ 1\end{pmatrix}
$$

**例 1.22**  $\mathbb{R}^2$ 的另一组标准正交基（旋转 45°）：

$$
e_1' = \frac{1}{\sqrt{2}}\begin{pmatrix}1 \\ 1\end{pmatrix}, \quad e_2' = \frac{1}{\sqrt{2}}\begin{pmatrix}1 \\ -1\end{pmatrix}
$$

验证：$\langle e_1', e_2' \rangle = \frac{1}{2}(1\cdot 1 + 1\cdot (-1)) = 0$，且 $\| e_1' \| = \| e_2' \| = 1$。

### 1.3.7 施密特正交化

给定一组线性无关的向量，**施密特正交化**过程可以生成一组标准正交基。

**算法**（两步法）：

输入：线性无关的向量 $v_1, v_2, \dots, v_n$

1. **正交化**：

$$
u_1 = v_1
$$

$$
u_k = v_k - \sum_{j=1}^{k-1} \frac{\langle u_j, v_k \rangle}{\| u_j \|^2} u_j \quad (k = 2, 3, \dots, n)
$$

2. **归一化**：

$$
e_k = \frac{u_k}{\| u_k \|}
$$

**例 1.23**  在 $\mathbb{R}^2$ 中，对 $v_1 = \begin{pmatrix}1 \\ 2\end{pmatrix}$, $v_2 = \begin{pmatrix}1 \\ 1\end{pmatrix}$ 做施密特正交化。

**步骤 1（正交化）**：
$u_1 = v_1 = \begin{pmatrix}1 \\ 2\end{pmatrix}$

计算投影：

$$
\frac{\langle u_1, v_2 \rangle}{\| u_1 \|^2} = \frac{1\cdot 1 + 2\cdot 1}{1^2 + 2^2} = \frac{3}{5}
$$

$$
u_2 = v_2 - \frac{3}{5} u_1 = \begin{pmatrix}1 \\ 1\end{pmatrix} - \frac{3}{5}\begin{pmatrix}1 \\ 2\end{pmatrix} = \begin{pmatrix}2/5 \\ -1/5\end{pmatrix}
$$

**步骤 2（归一化）**：

$$
e_1 = \frac{1}{\sqrt{5}}\begin{pmatrix}1 \\ 2\end{pmatrix}, \quad e_2 = \frac{\sqrt{5}}{\sqrt{1}}\begin{pmatrix}2/5 \\ -1/5\end{pmatrix} = \frac{1}{\sqrt{5}}\begin{pmatrix}2 \\ -1\end{pmatrix}
$$

验证：$\langle e_1, e_2 \rangle = \frac{1}{5}(1\cdot 2 + 2\cdot (-1)) = 0$，$\| e_1 \| = \| e_2 \| = 1$。

施密特正交化在量子力学中的应用：从一组线性无关的态构造标准正交基。

---

**小练习**：验证例 1.22 中的 $e_1'$ 和 $e_2'$ 确实是标准正交的。

**小练习**：在 $\mathbb{R}^3$ 中，对 $v_1 = (1, 1, 0)^T$，$v_2 = (1, 0, 1)^T$ 做施密特正交化。

---

## 1.4 狄拉克符号

### 1.4.1 为什么需要新符号？

你在前面的章节中已经看到，我们用列向量表示量子态，用矩阵表示算符。但物理学家保罗·狄拉克发现，在处理量子力学时，有一套更简洁、更强大的符号系统——**狄拉克符号**（也叫 bra-ket 符号）。

这套符号是量子计算的"母语"。**不懂狄拉克符号，就看不懂量子计算文献**。

### 1.4.2 右矢 |v⟩——表示列向量

一个**右矢**（ket）$|v\rangle$ 表示一个列向量。

$$
|v\rangle = \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix}
$$

**例 1.24**  量子比特的两个基态：

$$
|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

**例 1.25**  叠加态：

$$
|+\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)
$$

### 1.4.3 左矢 ⟨v|——表示行向量（共轭转置）

一个**左矢**（bra）$\langle v|$ 是 $|v\rangle$ 的**共轭转置**（厄米共轭，记作 $^\dagger$）：

$$
\langle v| = |v\rangle^\dagger = \begin{pmatrix} \overline{v_1} & \overline{v_2} & \cdots & \overline{v_n} \end{pmatrix}
$$

**步骤**：先转置（行变列、列变行），再取每个分量的复共轭。

**例 1.26**  若 $|v\rangle = \begin{pmatrix} 1 + i \\ 2 - i \end{pmatrix}$，则

$$
\langle v| = \begin{pmatrix} 1 - i & 2 + i \end{pmatrix}
$$

**例 1.27**  基矢的左矢：

$$
\langle 0| = \begin{pmatrix} 1 & 0 \end{pmatrix}, \quad \langle 1| = \begin{pmatrix} 0 & 1 \end{pmatrix}
$$

### 1.4.4 内积 ⟨φ|ψ⟩

左矢和右矢组合起来——⟨φ| 放在左边，|ψ⟩ 放在右边——就得到**内积**：

$$
\langle \varphi | \psi \rangle = \langle \varphi | 乘以 | \psi \rangle = \text{行向量} \times \text{列向量} = \text{标量}
$$

$$
\langle \varphi | \psi \rangle = \sum_i \overline{\varphi_i} \psi_i
$$

**性质**：
- $\langle \psi | \psi \rangle = \| |\psi\rangle \|^2 \geq 0$（模方）
- $\langle \varphi | \psi \rangle = \overline{\langle \psi | \varphi \rangle}$（共轭对称）

**例 1.28**  计算 $\langle 0 | 1 \rangle$：

$$
\langle 0 | 1 \rangle = \begin{pmatrix} 1 & 0 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = 0
$$

$|0\rangle$ 和 $|1\rangle$ 正交。

**例 1.29**  计算 $\langle 0 | 0 \rangle$：

$$
\langle 0 | 0 \rangle = \begin{pmatrix} 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = 1
$$

归一化。

**例 1.30**  $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$，其中 $|\alpha|^2 + |\beta|^2 = 1$。则：

$$
\langle \psi | \psi \rangle = ( \overline{\alpha}\langle 0| + \overline{\beta}\langle 1| ) ( \alpha|0\rangle + \beta|1\rangle )
$$

$$
= \overline{\alpha}\alpha \langle 0|0\rangle + \overline{\alpha}\beta \langle 0|1\rangle + \overline{\beta}\alpha \langle 1|0\rangle + \overline{\beta}\beta \langle 1|1\rangle
$$

$$
= |\alpha|^2 + 0 + 0 + |\beta|^2 = 1
$$

这就是归一化条件 $|\alpha|^2 + |\beta|^2 = 1$ 的由来。

### 1.4.5 外积 |ψ⟩⟨φ|

把右矢放在左边、左矢放在右边——**外积**——得到一个矩阵：

$$
|\psi\rangle \langle \varphi| = \text{列向量} \times \text{行向量} = \text{矩阵}
$$

**例 1.31**  $|0\rangle \langle 0| = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$

**例 1.32**  $|1\rangle \langle 1| = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$

**例 1.33**  $|0\rangle \langle 1| = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$

外积在后续的投影算子（1.7 节）和密度矩阵中非常重要。

### 1.4.6 符号对照表

| 你熟悉的符号 | 狄拉克符号 | 说明 |
|:---:|:---:|:---|
| $v$（列向量） | $\lvert v\rangle$ | 右矢 |
| $v^\dagger$（共轭转置） | $\langle v\rvert$ | 左矢 |
| $u^\dagger v$（内积） | $\langle u \vert v \rangle$ | 括号 |
| $u v^\dagger$（外积） | $\lvert u\rangle \langle v\rvert$ | 外积 |
| $A\lvert v\rangle$ | $A\lvert v\rangle$ | 矩阵乘向量 |
| $\langle u\vert A\vert v\rangle$ | $\langle u\vert A\vert v\rangle$ | 矩阵元 |
| $\overline{c}$ | $c^*$ | 复共轭 |

### 1.4.7 狄拉克符号的代数操作

狄拉克符号的核心优势在于：你可以像处理代数表达式一样操作它，而不必每次都展开成坐标形式。

**例 1.34**  展开 $(\langle 0| + \langle 1|) |\psi\rangle$，其中 $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$：

$$
(\langle 0| + \langle 1|) |\psi\rangle = \langle 0|\psi\rangle + \langle 1|\psi\rangle
$$

$$
= \langle 0|(\alpha|0\rangle + \beta|1\rangle) + \langle 1|(\alpha|0\rangle + \beta|1\rangle)
$$

$$
= \alpha \langle 0|0\rangle + \beta\langle 0|1\rangle + \alpha\langle 1|0\rangle + \beta\langle 1|1\rangle
$$

$$
= \alpha + \beta
$$

**例 1.35**  计算 $(|0\rangle \langle 0|) |1\rangle$：

$$
(|0\rangle \langle 0|) |1\rangle = |0\rangle (\langle 0|1\rangle) = |0\rangle \cdot 0 = 0
$$

$|0\rangle\langle 0|$ 把 $|1\rangle$ 变成了零向量。

**例 1.36**  计算 $(|0\rangle \langle 0|) |0\rangle$：

$$
(|0\rangle \langle 0|) |0\rangle = |0\rangle (\langle 0|0\rangle) = |0\rangle \cdot 1 = |0\rangle
$$

$|0\rangle\langle 0|$ 保持 $|0\rangle$ 不变。这是一个投影算子（见 1.7 节）。

### 1.4.8 量子比特的常见态

用狄拉克符号表示量子比特的一些常见态：

$$
|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad
|1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

$$
|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

$$
|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$

这四个态在量子计算中频繁出现。$|+\rangle$ 和 $|-\rangle$ 也是正交的：$\langle+|-\rangle = \frac{1}{2}(1-1) = 0$。

---

**小练习**：计算 $\langle + | 0 \rangle$。

**小练习**：将 $(|0\rangle \langle 1| + |1\rangle \langle 0|)$ 作用于 $|0\rangle$，结果是什么？

---

## 1.5 矩阵运算

### 1.5.1 矩阵——量子算符的表示

在量子力学中，**算符**（operator）是把一个态变成另一个态的映射，而矩阵就是算符在特定基下的表示。

量子门（如 Hadamard 门、Pauli 门）都是矩阵。理解矩阵运算是理解量子电路的基础。

### 1.5.2 矩阵加法与数乘

两个同型矩阵相加，对应元素相加：

$$
\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} + \begin{pmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{pmatrix} = \begin{pmatrix} a_{11}+b_{11} & a_{12}+b_{12} \\ a_{21}+b_{21} & a_{22}+b_{22} \end{pmatrix}
$$

数乘：每个元素乘以该数：

$$
c \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} = \begin{pmatrix} c a_{11} & c a_{12} \\ c a_{21} & c a_{22} \end{pmatrix}
$$

### 1.5.3 矩阵乘法

$A$ 是 $m \times n$ 矩阵，$B$ 是 $n \times p$ 矩阵，乘积 $C = AB$ 是 $m \times p$ 矩阵：

$$
C_{ik} = \sum_{j=1}^n A_{ij} B_{jk}
$$

**关键规则**：左矩阵的列数必须等于右矩阵的行数。

**例 1.37**  计算 $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$：

$$
\begin{pmatrix} 1\cdot 0 + 2\cdot 1 & 1\cdot 1 + 2\cdot 0 \\ 3\cdot 0 + 4\cdot 1 & 3\cdot 1 + 4\cdot 0 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 4 & 3 \end{pmatrix}
$$

**例 1.38**  Pauli-X 门（量子非门）作用于 $|0\rangle$：

$$
X|0\rangle = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = |1\rangle
$$

**矩阵乘法不交换**：一般 $AB \neq BA$。

**例 1.39**  令 $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$，$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$。

$$
XZ = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
$$

$$
ZX = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
$$

$$
XZ \neq ZX
$$

### 1.5.4 转置与共轭转置

**转置** $A^T$：交换行列，$(A^T)_{ij} = A_{ji}$。

$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix}^T = \begin{pmatrix} a & c \\ b & d \end{pmatrix}
$$

**共轭转置** $A^\dagger$（也称厄米共轭）：先取转置，再取每个元素的复共轭。$A^\dagger = \overline{A^T}$。

$$
\begin{pmatrix} 1+i & 2 \\ 3-2i & 0 \end{pmatrix}^\dagger = \begin{pmatrix} 1-i & 3+2i \\ 2 & 0 \end{pmatrix}
$$

**性质**：
- $(A^\dagger)^\dagger = A$
- $(AB)^\dagger = B^\dagger A^\dagger$（注意顺序反转！）
- $(A + B)^\dagger = A^\dagger + B^\dagger$

在狄拉克符号中，左矢就是右矢的共轭转置：$\langle v| = (|v\rangle)^\dagger$。

### 1.5.5 逆矩阵

如果 $A$ 是方阵，且存在矩阵 $A^{-1}$ 使得：

$$
A A^{-1} = A^{-1} A = I
$$

则 $A$ 称为**可逆的**（非奇异的），$A^{-1}$ 是 $A$ 的**逆矩阵**。

对于 $2 \times 2$ 矩阵，逆有公式：

$$
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \quad \det(A) = ad - bc
$$

$$
A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
$$

当 $\det(A) \neq 0$ 时，逆存在。

**例 1.40**  $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$，$\det(X) = -1$，$X^{-1} = \frac{1}{-1} \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = X$。

$X$ 的逆是它自己。事实上，所有 Pauli 门都是自逆的。

### 1.5.6 幺正矩阵

**定义 1.9（幺正矩阵）** 一个方阵 $U$ 称为**幺正的**（unitary），如果：

$$
U^\dagger U = U U^\dagger = I
$$

即 $U^{-1} = U^\dagger$。

**幺正矩阵的重要性质**：

1. **保内积**：$\langle U\psi | U\varphi \rangle = \langle \psi | \varphi \rangle$
2. **保范数**：$\| U|\psi\rangle \| = \| |\psi\rangle \|$
3. **本征值的模为 1**：若 $U|v\rangle = \lambda |v\rangle$，则 $|\lambda| = 1$

**为什么这对量子计算重要？** 量子门的演化是幺正的。这意味着：
- 量子计算是可逆的（除了测量）
- 概率总和守恒（归一化态矢演化后仍然归一化）

**例 1.41**  Hadamard 门 $H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ 是幺正的：

$$
H^\dagger H = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = I
$$

（因为 $H$ 是实对称的，所以 $H^\dagger = H^T = H$。）

**例 1.42**  Pauli 矩阵都是幺正的：

$$
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad
Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

验证 $X^\dagger X = X^2 = I$，$Y^\dagger Y = I$，$Z^\dagger Z = I$。

### 1.5.7 厄米矩阵

**定义 1.10（厄米矩阵）** 一个方阵 $H$ 称为**厄米的**（Hermitian），如果：

$$
H^\dagger = H
$$

即 $H_{ij} = \overline{H_{ji}}$。对角元必须是实数。

**厄米矩阵的重要性质**：

1. **本征值是实数**（这对量子力学至关重要——可观测量必须有实数的测量结果）
2. **不同本征值对应的本征矢正交**
3. **可对角化**（更准确地说，可被幺正对角化）

**例 1.43**  Pauli 矩阵都是厄米的：

$$
X^\dagger = X, \quad Y^\dagger = Y, \quad Z^\dagger = Z
$$

**例 1.44**  一般形式：$H = \begin{pmatrix} a & b \\ \overline{b} & d \end{pmatrix}$ 是厄米的，其中 $a, d \in \mathbb{R}$。

**幺正 vs 厄米**：
- $U^\dagger U = I$（幺正——可逆演化）
- $H^\dagger = H$（厄米——可观测量）

一个矩阵可以同时是幺正和厄米的吗？可以。例如 Pauli 矩阵和 Hadamard 门。这样的矩阵满足 $U^\dagger = U^{-1} = U$，即 $U^2 = I$。

### 1.5.8 对易子与反对易子

**对易子**（commutator）：

$$
[A, B] = A B - B A
$$

如果 $[A, B] = 0$，则称 $A$ 和 $B$ **对易**（commute）。

**反对易子**（anticommutator）：

$$
\{A, B\} = A B + B A
$$

如果 $\{A, B\} = 0$，则称 $A$ 和 $B$ **反对易**（anticommute）。

**例 1.45**  Pauli 矩阵的对易关系：

$$
[X, Y] = XY - YX = iZ
$$

$$
[Y, Z] = YZ - ZY = iX
$$

$$
[Z, X] = ZX - XZ = iY
$$

总结为 $[\sigma_i, \sigma_j] = 2i \varepsilon_{ijk} \sigma_k$。（其中 $\varepsilon_{ijk}$ 是 Levi-Civita 符号）

**例 1.46**  Pauli 矩阵两两反对易：

$$
\{X, Y\} = XY + YX = 0
$$

$$
\{Y, Z\} = YZ + ZY = 0
$$

$$
\{Z, X\} = ZX + XZ = 0
$$

**为什么对易子重要？**
- 如果两个算符对易，它们有共同的本征态，并且可以同时测量。
- 如果两个算符不对易（如位置和动量），它们满足不确定关系。
- 对易子在量子力学中无处不在，从海森堡运动方程到李代数。

---

**小练习**：验证 $H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ 是幺正且厄米的。

**小练习**：计算 $[Z, H]$，其中 $H$ 是 Hadamard 门。

---

## 1.6 本征值与本征矢

### 1.6.1 什么叫"本征"？

"本征"（eigen）来自德语，意思是"自身的"、"特征性的"。一个矩阵作用于一个向量，通常向量的方向和长度都会改变。但对于某些特殊的向量，矩阵的作用只是缩放（乘以一个标量），方向不变。这些向量就是**本征矢**，相应的缩放因子就是**本征值**。

这是量子力学最核心的数学概念：**测量一个可观测量，得到的结果一定是该算符的某个本征值**。

### 1.6.2 本征方程

**定义 1.11（本征值与本征矢）** 对于方阵 $A$，如果存在非零向量 $|v\rangle$ 和标量 $\lambda$ 使得：

$$
A |v\rangle = \lambda |v\rangle
$$

则 $\lambda$ 是 $A$ 的**本征值**（eigenvalue），$|v\rangle$ 是对应的**本征矢**（eigenvector）。

**例 1.47**  $Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$。

$Z|0\rangle = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} = 1 \cdot |0\rangle$，所以 $|0\rangle$ 是 $Z$ 的本征矢，本征值 $1$。

$Z|1\rangle = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ -1 \end{pmatrix} = -1 \cdot |1\rangle$，所以 $|1\rangle$ 是 $Z$ 的本征矢，本征值 $-1$。

**例 1.48**  $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$。

$X|+\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = 1 \cdot |+\rangle$，本征值 $1$。

$X|-\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} -1 \\ 1 \end{pmatrix} = -1 \cdot |-\rangle$，本征值 $-1$。

**几何理解**：$X$ 门是 $\mathbb{R}^2$ 中关于 $y=x$ 轴的反射。$|+\rangle$ 在这条轴上，反射不变；$|-\rangle$ 垂直于这条轴，反射后反向。

### 1.6.3 特征多项式

如何求解本征值？把本征方程改写：

$$
A |v\rangle = \lambda |v\rangle \implies (A - \lambda I) |v\rangle = 0
$$

因为 $|v\rangle \neq 0$，所以矩阵 $A - \lambda I$ 必须**奇异**（行列式为零）：

$$
\det(A - \lambda I) = 0
$$

这个方程称为**特征方程**，左边的多项式称为**特征多项式**。在物理文献中，同一条件也常被称为**久期方程**（secular equation）。

**例 1.49**  求 $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ 的本征值。

$$
\det(X - \lambda I) = \det\begin{pmatrix} -\lambda & 1 \\ 1 & -\lambda \end{pmatrix} = \lambda^2 - 1 = 0
$$

解得 $\lambda = \pm 1$。

**例 1.50**  求 $H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ 的本征值。

$$
\det(H - \lambda I) = \det\begin{pmatrix} 1/\sqrt{2} - \lambda & 1/\sqrt{2} \\ 1/\sqrt{2} & -1/\sqrt{2} - \lambda \end{pmatrix}
$$

$$
= (1/\sqrt{2} - \lambda)(-1/\sqrt{2} - \lambda) - 1/2 = -\frac{1}{2} - \frac{\lambda}{\sqrt{2}} + \frac{\lambda}{\sqrt{2}} + \lambda^2 - \frac{1}{2} = \lambda^2 - 1
$$

解得 $\lambda = \pm 1$。

### 1.6.4 本征矢的求解

找到本征值后，代入 $(A - \lambda I)|v\rangle = 0$ 解出本征矢。

**例 1.51**  续上例，求 $H$ 的本征矢。

对 $\lambda = 1$：

$$
\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x \\ y \end{pmatrix}
$$

$$
\frac{1}{\sqrt{2}}(x + y) = x \implies y = (\sqrt{2} - 1)x
$$

$$
\frac{1}{\sqrt{2}}(x - y) = y \implies x - y = \sqrt{2}y \implies x = (\sqrt{2} + 1)y
$$

两个方程一致。取 $x = 1$，得 $y = \sqrt{2} - 1$。归一化后：

$$
|v_1\rangle = \frac{1}{\sqrt{4 - 2\sqrt{2}}} \begin{pmatrix} 1 \\ \sqrt{2} - 1 \end{pmatrix}
$$

实际上 $H$ 的本征矢是 $|+\rangle$（对应 $\lambda=1$）和 $|-\rangle$（对应 $\lambda=-1$）—— 验证留作练习。

### 1.6.5 对角化

如果一个 $n \times n$ 矩阵 $A$ 有 $n$ 个线性无关的本征矢，那么它可被**对角化**：

$$
A = P D P^{-1}
$$

其中 $D$ 是对角矩阵（对角元是本征值），$P$ 的列是本征矢。

对于**厄米矩阵**和**幺正矩阵**，有更强的结论：它们可以被**幺正对角化**：

$$
A = U D U^\dagger
$$

其中 $U$ 是幺正矩阵（列是标准正交的本征矢）。

**例 1.52**  $Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ 已经是对角矩阵。本征值 $1, -1$，本征矢 $|0\rangle, |1\rangle$。

**例 1.53**  对角化 $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$。

本征值 $\pm 1$，本征矢 $(1,1)^T/\sqrt{2}$ 和 $(1,-1)^T/\sqrt{2}$。

$$
U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = H
$$

$$
X = H Z H^\dagger = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

验证：$H Z H = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = X$。

### 1.6.6 谱分解定理——量子力学的基石

**定理 1.1（谱分解）** 任何厄米矩阵 $H$ 可以写成：

$$
H = \sum_{i} \lambda_i |\lambda_i\rangle \langle \lambda_i|
$$

其中 $\lambda_i$ 是 $H$ 的本征值，$|\lambda_i\rangle$ 是对应的本征矢（构成标准正交基）。

**这是量子力学最重要的定理之一**。它告诉我们：
- 一个可观测量（厄米算符）的"谱"就是它的本征值集合——所有可能的测量结果。
- 谱分解把算符写成投影算子的加权和。

**例 1.54**  $Z = 1 \cdot |0\rangle \langle 0| + (-1) \cdot |1\rangle \langle 1|$

验证：$|0\rangle\langle 0| = \begin{pmatrix}1&0\\0&0\end{pmatrix}$，$|1\rangle\langle 1| = \begin{pmatrix}0&0\\0&1\end{pmatrix}$。

$1\cdot|0\rangle\langle 0| + (-1)\cdot|1\rangle\langle 1| = \begin{pmatrix}1&0\\0&-1\end{pmatrix} = Z$。

**例 1.55**  $X = 1 \cdot |+\rangle \langle +| + (-1) \cdot |-\rangle \langle -|$

其中 $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$，$|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$。

验证：$|+\rangle\langle +| = \frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}$，$|-\rangle\langle -| = \frac{1}{2}\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$。

$|+\rangle\langle +| - |-\rangle\langle -| = \frac{1}{2}\begin{pmatrix}2&0\\0&-2\end{pmatrix} = \begin{pmatrix}1&0\\0&-1\end{pmatrix} \neq X$？

等一等，让我重新仔细计算。

事实上，$|+\rangle\langle +| = \frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}$，$|-\rangle\langle -| = \frac{1}{2}\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$。

$$
|+\rangle\langle +| - |-\rangle\langle -| = \frac{1}{2}\begin{pmatrix}1-1 & 1-(-1) \\ 1-(-1) & 1-1\end{pmatrix} = \frac{1}{2}\begin{pmatrix}0 & 2 \\ 2 & 0\end{pmatrix} = \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix} = X
$$

正确。

**谱分解的用途**：有了谱分解，我们可以定义算符的函数（见 1.10 节）：

$$
f(H) = \sum_i f(\lambda_i) |\lambda_i\rangle \langle \lambda_i|
$$

---

**小练习**：求 $Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$ 的本征值和本征矢。

**小练习**：写出 $Y$ 的谱分解。

---

## 1.7 投影算子与完备性关系

### 1.7.1 什么是投影？

投影的几何直觉：一束光垂直照射一个向量，它在平面上的影子就是投影。投影算子做了类似的事——把一个向量"投影"到某个子空间上。

在量子力学中，投影算子描述**测量过程**：当一个量子态被测量时，它以一定概率"坍缩"到某个本征态上，而这个坍缩就是投影。

### 1.7.2 投影算子的定义

**定义 1.12（投影算子）** 一个线性算符 $P$ 称为**投影算子**（projector），如果它是**幂等**的：

$$
P^2 = P
$$

如果 $P$ 还是厄米的（在量子力学中通常如此），则称为**正交投影算子**。

**例 1.56**  $P_0 = |0\rangle\langle 0| = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$。

验证：$P_0^2 = |0\rangle\langle 0|0\rangle\langle 0| = |0\rangle \cdot 1 \cdot \langle 0| = |0\rangle\langle 0| = P_0$。

$P_0$ 把任意向量投影到 $|0\rangle$ 方向。例如：

$$
P_0 |1\rangle = |0\rangle\langle 0|1\rangle = |0\rangle \cdot 0 = 0
$$

$$
P_0 |+\rangle = |0\rangle\langle 0|+\rangle = |0\rangle \cdot \frac{1}{\sqrt{2}} = \frac{1}{\sqrt{2}}|0\rangle
$$

**例 1.57**  $P_1 = |1\rangle\langle 1| = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$。同样 $P_1^2 = P_1$。

### 1.7.3 完备性关系

对于一组标准正交基 $\{|i\rangle\}$，有：

$$
\sum_{i} |i\rangle \langle i| = I
$$

这个公式称为**完备性关系**（completeness relation）。代数上，它表明该组基**张满**整个空间：各一维投影拼起来等于单位算符，没有遗漏的方向。

物理内核不止“维数凑齐”。**完备性**问的是：在你选定的**表象**（一组基）下，投影分辨率 $\sum_i |i\rangle\langle i|$ 能否完整描述任意态——任一 $|\psi\rangle$ 的分量是否都能被这组基读干净。缺一条基，就有态的一部分落在“坐标轴外”，该表象对这个态不完整。

选取某可观测量的本征基，就是在选一种**物理表象入口**（例如能量表象、$Z$ 表象）。本节主语始终是**基 / 表象是否完备**，而不是“算符空间本身完备”。

**验证**（在 $\mathbb{C}^2$ 中）：

$$
|0\rangle\langle 0| + |1\rangle\langle 1| = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
$$

**例 1.58**  在基 $\{|+\rangle, |-\rangle\}$ 下验证完备性：

$$
|+\rangle\langle +| + |-\rangle\langle -| = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} + \frac{1}{2}\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
$$

同一抽象态空间，换一组完备基就换一套合法表象；$\{|0\rangle,|1\rangle\}$ 与 $\{|+\rangle,|-\rangle\}$ 都能完整描述 $\mathbb{C}^2$ 中的任意态，只是坐标不同。

### 1.7.4 用完备性关系展开态矢

完备性关系给出把抽象态**投到选定表象**的标准手续。插入 $I = \sum_i |i\rangle\langle i|$，不是花招，而是把 $|\psi\rangle$ 分解为该表象下的坐标展开：

$$
|\psi\rangle = I |\psi\rangle = \left( \sum_i |i\rangle \langle i| \right) |\psi\rangle = \sum_i |i\rangle \langle i|\psi\rangle = \sum_i \langle i|\psi\rangle \cdot |i\rangle
$$

逐步读：

1. $|\psi\rangle$ 本身是表象无关的抽象态矢（Dirac 对象）。
2. 对每个基矢，内积 $c_i := \langle i|\psi\rangle$ 是**复数标量**——它是 $|\psi\rangle$ 在方向 $|i\rangle$ 上的坐标，不再是 ket，也不再是矩阵。
3. 再与 $|i\rangle$ 相乘并求和，得到该表象中的展开式 $\sum_i c_i |i\rangle$。

换一组完备基 $\{|i'\rangle\}$ 重复同一手续，得到另一套系数 $\{c_i'\}$：这就是**表象变换**（同一态，不同坐标）。  
（脚注式提醒：若表象取连续位置基 $\{|x\rangle\}$，则坐标函数 $c(x)=\langle x|\psi\rangle$ 即通常所说的波函数 $\psi(x)$；本章正文统一用语为态矢与表象坐标。）

**系数规则（务必分清“数”与“矢”）**

- $c_i = \langle i|\psi\rangle \in \mathbb{C}$：行矢量与列矢量收缩后的结果是**标量**。
- 标量与任何 ket / bra / 算符相乘时**可随意左右挪动**（在线性代数约定下，复数与向量乘法可交换书写位置）：例如 $|i\rangle c_i = c_i |i\rangle$。
- **不可**把仍带 Dirac 结构的对象当标量挪——$|i\rangle$、$\langle i|$、$|i\rangle\langle i|$ 都不是数；尤其不能把投影算子 $|i\rangle\langle i|$ 从式中“当系数抽走”。
- 记忆口诀：先完成 $\langle\cdot|\cdot\rangle$ 收缩得到 $c_i$，之后只有 $c_i$ 能自由挪；收缩前的 ket / bra / 外积必须保持算符次序。

**例 1.59**  在标准基（$Z$ 表象）下展开 $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$：

$$
|+\rangle = |0\rangle\langle 0|+\rangle + |1\rangle\langle 1|+\rangle = |0\rangle \cdot \frac{1}{\sqrt{2}} + |1\rangle \cdot \frac{1}{\sqrt{2}}
$$

其中 $c_0 = \langle 0|+\rangle = \frac{1}{\sqrt{2}}$，$c_1 = \langle 1|+\rangle = \frac{1}{\sqrt{2}}$ 都是标量，故可写成 $\frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle$，也可写成 $|0\rangle\frac{1}{\sqrt{2}} + |1\rangle\frac{1}{\sqrt{2}}$——两种写法等价。  
直接算系数：$\langle 0|+\rangle = \frac{1}{\sqrt{2}}\langle 0|(|0\rangle+|1\rangle) = \frac{1}{\sqrt{2}}(\langle 0|0\rangle + \langle 0|1\rangle) = \frac{1}{\sqrt{2}}$。

**例 1.60**  用完备性关系计算内积 $\langle \varphi | \psi \rangle$：

$$
\langle \varphi | \psi \rangle = \langle \varphi | I | \psi \rangle = \sum_i \langle \varphi | i \rangle \langle i | \psi \rangle = \sum_i \overline{\langle i | \varphi \rangle} \langle i | \psi \rangle
$$

这就是内积的**坐标表示**：两边的态都先投到同一完备表象，再对系数做（共轭）点乘。

### 1.7.5 投影算子的性质

1. **幂等性**：$P^2 = P$
2. **厄米性**（正交投影）：$P^\dagger = P$
3. **本征值**：只能是 $0$ 或 $1$
   - 本征值 $1$ 对应的本征矢构成投影的目标子空间
   - 本征值 $0$ 对应的本征矢构成正交补空间
4. **正交投影**：如果 $P_1 P_2 = 0$，则两个投影互为正交

**例 1.61**  $P_0$ 和 $P_1$ 是正交的：$P_0 P_1 = |0\rangle\langle 0|1\rangle\langle 1| = 0$。

### 1.7.6 一般投影算子

投影不一定只投影到一维子空间。例如，投影到 $\mathbb{C}^2$ 中由 $|0\rangle$ 和 $|1\rangle$ 张成的整个空间就是单位矩阵。更一般地：

$$
P_W = \sum_{i \in \text{索引集}} |i\rangle \langle i|
$$

其中 $\{|i\rangle\}$ 是子空间 $W$ 的一组标准正交基。

**例 1.62**  在 $\mathbb{C}^3$ 中，投影到由 $(1,0,0)^T$ 和 $(0,1,0)^T$ 张成的子空间：

$$
P = |e_1\rangle\langle e_1| + |e_2\rangle\langle e_2| = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}
$$

**投影算子在测量中的角色**（预览）：测量某可观测量，实质上是把态**投到该可观测量的本征表象**上——完备性保证结果标签 $i$ 能盖住全部可能结局。得到结果 $i$ 的概率为 $\langle \psi | P_i | \psi \rangle$，测量后的态为 $\frac{P_i |\psi\rangle}{\sqrt{\langle \psi | P_i | \psi \rangle}}$。完整测量公设见第 2 章。

---

**小练习**：证明 $I - |0\rangle\langle 0|$ 也是一个投影算子，它投影到哪个子空间？

**小练习**：计算 $|+\rangle\langle +|$ 作用于 $|0\rangle$ 的结果。

---

## 1.8 张量积

### 1.8.1 为什么需要张量积？

一个量子比特用 $\mathbb{C}^2$ 描述。两个量子比特呢？答案不是把两个二维空间**并排放进更大容器却互不往来**，而是 $\mathbb{C}^2 \otimes \mathbb{C}^2$——它们的**张量积**空间，维度为 $2 \times 2 = 4$。

**核心思想**：复合系统的状态空间是各子系统状态空间的张量积。

张量积的计算过程，就是在做一件有物理含义的事：**把小空间张成大空间**。新空间里不仅有各子系统各自的自由度，还**预留了跨子系统的关联结构**——可分离态 $|a\rangle\otimes|b\rangle$ 只是其中一类；Bell 型叠加活在同一张量积空间里，却不能再拆成单个因子态。这是量子纠缠的数学根源，也是叠加原理在复合系统上的推广。

这里要分清两层语言：

- **运动学（态空间）**：选用 $\otimes$ 表示“允许关联甚至纠缠”的复合方式；大空间本身已经能装下关联。
- **动力学（相互作用）**：真实的**耦合**（相互作用哈密顿量、两比特门）是后来写在这个大空间上的算符，不是张量积符号本身自动产生的力。

初学者常头疼张量积的形式规则；下面先用**直和**对照“另一种张大空间的方式”，再进入形式定义与克罗内克计算。

### 1.8.2 对照：直和——块对角地张开，不内建关联

构造更大空间还有一条常见代数路线：**直和**（direct sum）。

**定义（直和，本节用）** 若 $V$、$W$ 为向量空间，直和 $V \oplus W$ 由有序对 $(v, w)$（常写作 $v \oplus w$）组成，线性运算分量式进行。若 $\dim V = m$、$\dim W = n$，则

$$
\dim(V \oplus W) = m + n
$$

在选取“先 $V$ 基、后 $W$ 基”的坐标下，作用在 $V \oplus W$ 上、且不把两块混在一起的算符呈**块对角**形：

$$
A \oplus B = \begin{pmatrix} A & 0 \ 0 & B \end{pmatrix}
$$

块与块之间没有矩阵元：对落在 $V$ 块里的矢量，$B$ 那一块“看不见”它。因此，直和是在**并置**两个空间——维数相加、结构分家——**并不内建跨块的关联或纠缠通道**。若物理上两个系统之间可以产生关联，态空间的默认复合方式应是张量积，而不是直和。

| | 张量积 $V \otimes W$ | 直和 $V \oplus W$ |
|---|---|---|
| 维数 | $m \cdot n$（相乘） | $m + n$（相加） |
| 矩阵图像 | 克罗内克“块复制” | 块对角并置 |
| 运动学 | 允许跨子系统关联 / 纠缠 | 跨块默认断开 |
| 典型场景 | 多量子比特、复合量子系统 | 正交扇区、按量子数分级的子空间、某些多模分解 |

**与高斯 / 光量子的一句出口**（供连续变量读者对照，本章不展开）：多模光场里，**不同正交模 / 模式**的希尔伯特空间常用张量积复合；而按光子数、宇称等**互不混合的扇区**组织时，则常见直和（块对角）结构。离散比特主线后文仍以 $\otimes$ 为准；连续变量与高斯量子信息可把此处对照当作入口地图。

### 1.8.3 张量积的定义

**定义 1.13（张量积）** 如果 $V$ 和 $W$ 是向量空间，它们的**张量积** $V \otimes W$ 是一个新的向量空间。对于 $v \in V$ 和 $w \in W$，$v \otimes w$ 是 $V \otimes W$ 中的元素。

张量积满足：

1. **双线性**：
   - $(c_1 v_1 + c_2 v_2) \otimes w = c_1(v_1 \otimes w) + c_2(v_2 \otimes w)$
   - $v \otimes (c_1 w_1 + c_2 w_2) = c_1(v \otimes w_1) + c_2(v \otimes w_2)$

2. **数乘**：$c(v \otimes w) = (c v) \otimes w = v \otimes (c w)$

如果 $\dim(V) = m$，$\dim(W) = n$，则 $\dim(V \otimes W) = mn$。

### 1.8.4 克罗内克积——张量积的具体计算

在坐标表示下，张量积通过**克罗内克积**（Kronecker product）计算。

对于向量：

$$
\begin{pmatrix} a \\ b \end{pmatrix} \otimes \begin{pmatrix} c \\ d \end{pmatrix} = \begin{pmatrix} a \begin{pmatrix} c \\ d \end{pmatrix} \\ b \begin{pmatrix} c \\ d \end{pmatrix} \end{pmatrix} = \begin{pmatrix} a c \\ a d \\ b c \\ b d \end{pmatrix}
$$

**例 1.63**  计算 $|0\rangle \otimes |1\rangle$（简写为 $|01\rangle$）：

$$
|0\rangle \otimes |1\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \otimes \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \cdot \begin{pmatrix} 0 \\ 1 \end{pmatrix} \\ 0 \cdot \begin{pmatrix} 0 \\ 1 \end{pmatrix} \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}
$$

**例 1.64**  $|+\rangle \otimes |-\rangle$：

$$
|+\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad |-\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$

$$
|+\rangle \otimes |-\rangle = \frac{1}{2} \begin{pmatrix} 1 \cdot \begin{pmatrix} 1 \\ -1 \end{pmatrix} \\ 1 \cdot \begin{pmatrix} 1 \\ -1 \end{pmatrix} \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1 \\ -1 \\ 1 \\ -1 \end{pmatrix}
$$

对于矩阵：

$$
A \otimes B = \begin{pmatrix} a_{11}B & a_{12}B & \cdots \\ a_{21}B & a_{22}B & \cdots \\ \vdots & \vdots & \ddots \end{pmatrix}
$$

**例 1.65**  $X \otimes Z$：

$$
X \otimes Z = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \otimes \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 \cdot Z & 1 \cdot Z \\ 1 \cdot Z & 0 \cdot Z \end{pmatrix}
$$

$$
= \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \end{pmatrix}
$$

**例 1.66**  $I \otimes X$（这是两个量子比特中，在第二个比特上作用 $X$ 门）：

$$
I \otimes X = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \otimes \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} X & 0 \\ 0 & X \end{pmatrix} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}
$$

### 1.8.5 张量积的性质

1. **分配律**：
   - $(A + B) \otimes C = A \otimes C + B \otimes C$
   - $A \otimes (B + C) = A \otimes B + A \otimes C$

2. **结合律**：
   - $(A \otimes B) \otimes C = A \otimes (B \otimes C)$，所以可以简写为 $A \otimes B \otimes C$

3. **数乘**：$(cA) \otimes B = c(A \otimes B) = A \otimes (cB)$

4. **混合积性质**（最重要！）：

$$
(A \otimes B)(C \otimes D) = (AC) \otimes (BD)
$$

   前提是矩阵维度匹配。

**例 1.67**  验证混合积性质：

$$
(X \otimes I)(I \otimes X) = (X \cdot I) \otimes (I \cdot X) = X \otimes X
$$

直接展开验证：$X \otimes I = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \otimes I = \begin{pmatrix} 0 & I \\ I & 0 \end{pmatrix}$。

$(X \otimes I)(I \otimes X) = \begin{pmatrix} 0 & I \\ I & 0 \end{pmatrix} \begin{pmatrix} X & 0 \\ 0 & X \end{pmatrix} = \begin{pmatrix} 0 & X \\ X & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix}$。

而 $X \otimes X = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix}$，确实相等。

5. **转置和共轭转置**：
   $(A \otimes B)^\dagger = A^\dagger \otimes B^\dagger$

6. **迹**：
   $\text{Tr}(A \otimes B) = \text{Tr}(A) \cdot \text{Tr}(B)$

### 1.8.6 多量子比特的计算基

两个量子比特的张量积空间 $\mathbb{C}^2 \otimes \mathbb{C}^2 \cong \mathbb{C}^4$，标准正交基为：

$$
|00\rangle = |0\rangle \otimes |0\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \quad
|01\rangle = |0\rangle \otimes |1\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}
$$

$$
|10\rangle = |1\rangle \otimes |0\rangle = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \quad
|11\rangle = |1\rangle \otimes |1\rangle = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}
$$

这称为**计算基**（computational basis）。任意双量子比特态可以写成：

$$
|\psi\rangle = \alpha_{00}|00\rangle + \alpha_{01}|01\rangle + \alpha_{10}|10\rangle + \alpha_{11}|11\rangle
$$

其中 $\sum |\alpha_{ij}|^2 = 1$。

**例 1.68**  Bell 态（最大纠缠态）：

$$
|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)
$$

这个态**不能**写成 $|a\rangle \otimes |b\rangle$ 的形式（不可分离），这正是量子纠缠的核心特征。

**例 1.69**  $|+\rangle \otimes |+\rangle$ 是可分离态：

$$
|+\rangle \otimes |+\rangle = \frac{1}{2}(|0\rangle + |1\rangle) \otimes (|0\rangle + |1\rangle) = \frac{1}{2}(|00\rangle + |01\rangle + |10\rangle + |11\rangle)
$$

这和 Bell 态不同——Bell 态缺少 $|01\rangle$ 和 $|10\rangle$ 项。

### 1.8.7 三量子比特及更多

三量子比特的空间维度是 $2^3 = 8$，计算基为 $\{|000\rangle, |001\rangle, \dots, |111\rangle\}$。

一般地，$n$ 量子比特的张量积空间维度为 $2^n$。这就是量子计算"指数加速"的数学根源——$n$ 个量子比特的态空间是 $2^n$ 维的。

**例 1.70**  三量子比特的 $W$ 态：

$$
|W\rangle = \frac{1}{\sqrt{3}}(|001\rangle + |010\rangle + |100\rangle)
$$

这是一个三体纠缠态。

### 1.8.8 张量积下的算符作用

一个算符只作用在某个子系统中，在全局空间中的表示为该算符与恒等算符的张量积。

**例 1.71**  在两个量子比特的系统中，只翻转第一个量子比特（在第一个比特上作用 $X$ 门）：

$$
X \otimes I = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \otimes \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}
$$

验证作用于 $|10\rangle$：

$$
(X \otimes I) |10\rangle = (X \otimes I)(|1\rangle \otimes |0\rangle) = (X|1\rangle) \otimes |0\rangle = |0\rangle \otimes |0\rangle = |00\rangle
$$

正确——第一个比特从 $|1\rangle$ 翻转为 $|0\rangle$，第二个比特不变。

**例 1.72**  CNOT 门（受控非门）——一个量子比特控制另一个的翻转：

$$
CNOT = |0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes X = \begin{pmatrix} I & 0 \\ 0 & X \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}
$$

CNOT 是量子计算中最基本的双比特门之一。

---

**小练习**：计算 $(Z \otimes Z) |\Phi^+\rangle$，其中 $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$。

**小练习**：判断 $|\psi\rangle = \frac{1}{\sqrt{2}}(|01\rangle + |10\rangle)$ 是否可写成单个张量积的形式。

---

## 1.9 部分迹与施密特分解

### 1.9.1 迹运算

**定义 1.14（迹）** 方阵 $A$ 的**迹**等于其对角元之和：

$$
\text{Tr}(A) = \sum_i A_{ii}
$$

**性质**：
- $\text{Tr}(A + B) = \text{Tr}(A) + \text{Tr}(B)$
- $\text{Tr}(cA) = c \cdot \text{Tr}(A)$
- **循环不变性（有向轮转）**：在矩阵乘积可定义的前提下，
  $$
  \text{Tr}(ABC) = \text{Tr}(BCA) = \text{Tr}(CAB)
  $$
  即把乘积**整体循环轮转**（最左边的因子接到最右边，或反过来）时迹不变。一般**不能**任意重排，例如通常
  $$
  \text{Tr}(ABC) \neq \text{Tr}(ACB)
  $$
  （后者是对换，不是循环）。两因子时 $\text{Tr}(AB)=\text{Tr}(BA)$ 看起来像“随便对调”，其实只是三因子有向轮转的退化：$B$ 与 $A$ 对调等价于把 $AB$ 写成 $BA$ 这一种循环，**并不**说明迹对任意置换对称。
- $\text{Tr}(A \otimes B) = \text{Tr}(A) \cdot \text{Tr}(B)$
- $\text{Tr}(U^\dagger A U) = \text{Tr}(A)$（幺正变换下不变；本身也是循环：$\text{Tr}(U^\dagger A U)=\text{Tr}(A U U^\dagger)=\text{Tr}(A)$）

**例 1.73**  $\text{Tr}\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = 1 + 4 = 5$。

**例（循环有向）** 取
$A=\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$，
$B=\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$，
$C=\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$。
则 $ABC=\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$，$\text{Tr}(ABC)=1$；
$BCA=\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$，$\text{Tr}(BCA)=1$；
而 $ACB=\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$，$\text{Tr}(ACB)=0$。  
可见循环相等、对换一般不等。

**例 1.74**  $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$，密度矩阵 $\rho = |\psi\rangle\langle \psi|$：

$$
\rho = \begin{pmatrix} |\alpha|^2 & \alpha \overline{\beta} \\ \overline{\alpha} \beta & |\beta|^2 \end{pmatrix}
$$

$$
\text{Tr}(\rho) = |\alpha|^2 + |\beta|^2 = 1
$$

密度矩阵的迹总是 1（归一化条件的体现）。

### 1.9.2 部分迹——对子系统"求和"

部分迹是量子信息论中最具威力的工具之一。它描述当你"忽略"多体系统中的某个子系统时，剩下的系统处于什么状态。

**定义 1.15（部分迹）** 对于两体系统 $H_A \otimes H_B$ 上的算符 $M_{AB}$，关于子系统 $B$ 的**部分迹** $\text{Tr}_B(M_{AB})$ 是 $H_A$ 上的算符。

在计算基下，部分迹的定义最清楚。设 $M_{AB}$ 的矩阵元为 $M_{ij,kl}$，其中 $i,j$ 对应 $A$ 子系统，$k,l$ 对应 $B$ 子系统：

$$
(\text{Tr}_B(M_{AB}))_{ij} = \sum_k M_{ik, jk}
$$

**例 1.75**  对两量子比特的密度矩阵 $\rho_{AB} = |\Phi^+\rangle\langle \Phi^+|$ 取部分迹 $\text{Tr}_B$。

$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$。

$$
\rho_{AB} = \frac{1}{2}\big(|00\rangle\langle 00| + |00\rangle\langle 11| + |11\rangle\langle 00| + |11\rangle\langle 11|\big)
$$

在计算基 $\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$ 下：

$$
\rho_{AB} = \frac{1}{2}\begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 1 \end{pmatrix}
$$

取部分迹 $\text{Tr}_B$（对 $B$ 的指标求和）：

$$
(\text{Tr}_B(\rho_{AB}))_{ij} = \sum_{k=0,1} \rho_{ik, jk}
$$

$\rho_A = \text{Tr}_B(\rho_{AB}) = \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \frac{I}{2}$

这是**最大混合态**。一个纯的纠缠态，在子系统看来却是混合态——这是纠缠的典型特征。

**例 1.76**  对可分离态 $\rho_{AB} = |00\rangle\langle 00|$ 取部分迹：

$$
\rho_{AB} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}
$$

$$
\rho_A = \text{Tr}_B(\rho_{AB}) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = |0\rangle\langle 0|
$$

子系统处于纯态 $|0\rangle$。

### 1.9.3 部分迹的物理意义

部分迹的物理意义：当我们只关心子系统 $A$ 而对 $B$ “无知”时，$A$ 的状态由 $\rho_A = \text{Tr}_B(\rho_{AB})$ 描述。

**为什么这很重要？** 真实器件里，量子比特几乎从不孤立：它与读出腔、两能级泄漏空间、热浴等构成**系统–环境**联合体。把量子比特（及我们想研究的门作用对象）记为 $S$，其余记为环境 $E$，则联合态落在 $H_S\otimes H_E$ 上；实验上往往只能访问 $S$，有效描述就是约化态

$$
\rho_S = \text{Tr}_E(\rho_{SE})
$$

这正是开放量子系统的语言入口：对环境取偏迹之后，$S$ 上看到的不再保证是纯态，纠缠与噪声都以混合态形式出现——退相干是其典型后果之一。

对**量子门**同样如此。理想闭系统里，门是 $H_S$ 上的幺正 $U_S$。一旦演化实际发生在 $S+E$ 上再对 $E$ 取偏迹，比特上诱导的有效操作一般**不是**单个幺正，而是一条把 $\rho_S$ 映到 $\rho_S'$ 的**量子信道**（完全正、保迹映射）。工程上标定的“门错误”“读出混淆”等，都是在问这条约化动力学偏离理想 $U_S$ 有多远。完整信道与 Kraus 表示见密度矩阵与噪声章节（模块一 ch03、模块五 ch21）；此处只需建立：**偏迹 = 从联合演化抽出开放比特 / 开放门的标准接口**。

### 1.9.4 施密特分解

**定理 1.2（施密特分解）** 对于两体系统 $H_A \otimes H_B$ 中的任意纯态 $|\psi\rangle_{AB}$，存在**施密特分解**：

$$
|\psi\rangle_{AB} = \sum_{i=1}^{r} \sigma_i |a_i\rangle \otimes |b_i\rangle
$$

其中：
- $\sigma_i > 0$ 是**施密特系数**，满足 $\sum_i \sigma_i^2 = 1$
- $\{|a_i\rangle\}$ 是 $H_A$ 中的标准正交集
- $\{|b_i\rangle\}$ 是 $H_B$ 中的标准正交集
- $r$ 称为**施密特秩**（Schmidt rank）

**关键点**：$|a_i\rangle$ 和 $|b_i\rangle$ 的数量相同（都是 $r$ 个），且 $r \leq \min(\dim(H_A), \dim(H_B))$。

### 1.9.5 施密特分解的计算

给定 $|\psi\rangle_{AB}$，施密特分解可以通过以下步骤计算：

1. 写出 $|\psi\rangle$ 在乘积基下的展开
2. 重组为矩阵形式 $M$（$M_{ij}$ 对应 $\langle i_A| \otimes \langle j_B| \psi\rangle$）
3. 对 $M$ 做奇异值分解：$M = U \Sigma V^\dagger$
4. 施密特系数就是 $M$ 的奇异值
5. $|a_i\rangle = U$ 的列，$|b_i\rangle = V$ 的列（的复共轭）

**例 1.77**  求 $|\psi\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |01\rangle + |10\rangle - |11\rangle)$ 的施密特分解。

写出系数矩阵（行对应 $A$，列对应 $B$）：

$$
M = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

这是 $\sqrt{2} \cdot H$（Hadamard 矩阵）。奇异值分解：

$$
M = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = H
$$

$H$ 已经是对称的，$H = H^\dagger$，且 $H^2 = I$，所以 $H = U \Sigma U^\dagger$，奇异值为 $1, 1$。

施密特分解：

$$
|\psi\rangle = 1 \cdot |+\rangle \otimes |+\rangle + 1 \cdot |-\rangle \otimes |-\rangle
$$

等等，需要归一化。$1^2 + 1^2 = 2$，应该是 $\frac{1}{\sqrt{2}}$ 系数。

实际上我搞混了。让我重新仔细算。

$|\psi\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |01\rangle + |10\rangle - |11\rangle)$。

系数矩阵：$M_{ij} = \langle i j | \psi \rangle$，即：

$M_{00} = 1/\sqrt{2}$，$M_{01} = 1/\sqrt{2}$，$M_{10} = 1/\sqrt{2}$，$M_{11} = -1/\sqrt{2}$。

$$M = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$
奇异值：$\sigma_1 = 1$，$\sigma_2 = 1$。

$U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$，$V = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$？

不，$M$ 是厄米的且幺正的，所以 $M = U \Sigma U^\dagger$，$U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$。

施密特系数 $\sigma_1 = \sigma_2 = 1$。

施密特分解：$|\psi\rangle = |a_1\rangle|b_1\rangle + |a_2\rangle|b_2\rangle$，其中 $|a_i\rangle = U$ 的列，$|b_i\rangle = \overline{V}$ 的列。

$|a_1\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |+\rangle$
$|a_2\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) = |-\rangle$
$|b_1\rangle = |+\rangle$
$|b_2\rangle = |-\rangle$

验证：

$$
|+\rangle|+\rangle + |-\rangle|-\rangle = \frac{1}{2}(|0\rangle+|1\rangle)(|0\rangle+|1\rangle) + \frac{1}{2}(|0\rangle-|1\rangle)(|0\rangle-|1\rangle)
$$

$$
= \frac{1}{2}(|00\rangle + |01\rangle + |10\rangle + |11\rangle) + \frac{1}{2}(|00\rangle - |01\rangle - |10\rangle + |11\rangle)
$$

$$
= |00\rangle + |11\rangle
$$

不对，这给出 $|00\rangle + |11\rangle$，不是我们原来的态。

让我重新做。$|\psi\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |01\rangle + |10\rangle - |11\rangle)$。

其实 $M = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$。奇异值分解：

$M = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = U \Sigma V^\dagger$

$M M^\dagger = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = I$

所以奇异值是 $\sigma_1 = \sigma_2 = 1$。

$U$ 可以是任意幺正矩阵... 实际上 $M$ 本身是幺正的（$M M^\dagger = I$），所以 $U = M$，$\Sigma = I$，$V = I$。

那么施密特分解：

$$
|\psi\rangle = \sum_{i,j} M_{ij} |i\rangle|j\rangle = \sum_{i,j} \sum_k U_{ik} \Sigma_k V_{jk}^* |i\rangle|j\rangle
$$

$$
= \sum_k \sigma_k (\sum_i U_{ik}|i\rangle) (\sum_j V_{jk}^* |j\rangle) = \sum_k \sigma_k |a_k\rangle |b_k\rangle
$$

这里 $\sigma_1 = \sigma_2 = 1$，$|a_1\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |+\rangle$，$|a_2\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) = |-\rangle$，$|b_1\rangle = |0\rangle$，$|b_2\rangle = |1\rangle$。

验证：

$$
|+\rangle|0\rangle + |-\rangle|1\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)|0\rangle + \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)|1\rangle
$$

$$
= \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle + |01\rangle - |11\rangle) = \frac{1}{\sqrt{2}}(|00\rangle + |01\rangle + |10\rangle - |11\rangle)
$$

正确！

### 1.9.6 施密特秩与纠缠

**施密特秩** $r$ 是一个态是否纠缠的判据：

- 如果 $r = 1$，态是**可分离的**（可以写成 $|\psi\rangle = |a\rangle \otimes |b\rangle$）
- 如果 $r > 1$，态是**纠缠的**
- $r$ 越大，纠缠"程度"通常越高

**例 1.78**  $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$。系数矩阵：

$$
M = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

奇异值：$\sigma_1 = \sigma_2 = 1/\sqrt{2}$，施密特秩 $r = 2$，所以 $|\Phi^+\rangle$ 是纠缠态。

**例 1.79**  $|\psi\rangle = |00\rangle$。系数矩阵：

$$
M = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}
$$

奇异值：$\sigma_1 = 1$，$\sigma_2 = 0$，施密特秩 $r = 1$，所以是可分离态。

**施密特系数与部分迹的关系**：

$$
\rho_A = \text{Tr}_B(|\psi\rangle\langle\psi|) = \sum_i \sigma_i^2 |a_i\rangle\langle a_i|
$$

从 $\rho_A$ 的本征值可以直接读出施密特系数的平方。

---

**小练习**：求 $|\psi\rangle = \frac{1}{\sqrt{3}}(|00\rangle + |01\rangle + |10\rangle)$ 的施密特分解和施密特秩。

**小练习**：计算 Bell 态 $|\Phi^+\rangle$ 的部分迹 $\text{Tr}_A$。结果是什么？为什么？

---

## 1.10 矩阵函数与算符

### 1.10.1 从函数到矩阵函数

我们熟悉实数函数 $f(x) = e^x$ 或 $f(x) = \sin x$。如果 $x$ 换成矩阵 $A$，$e^A$ 是什么意思？

矩阵函数通过**幂级数**定义——把函数的泰勒级数中的变量 $x$ 替换为矩阵 $A$。

### 1.10.2 矩阵指数

**定义 1.16（矩阵指数）** 方阵 $A$ 的**矩阵指数**定义为：

$$
e^{A} = \sum_{n=0}^{\infty} \frac{A^n}{n!} = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \cdots
$$

这和泰勒级数 $e^x = \sum x^n/n!$ 一模一样。

**例 1.80**  计算 $e^{X}$，其中 $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$。

先计算 $X$ 的幂：

$$
X^0 = I, \quad X^1 = X, \quad X^2 = I, \quad X^3 = X, \quad X^4 = I, \dots
$$

因为 $X^2 = I$。

所以：

$$
e^{X} = I + X + \frac{I}{2!} + \frac{X}{3!} + \frac{I}{4!} + \frac{X}{5!} + \cdots
$$

$$
= I(1 + \frac{1}{2!} + \frac{1}{4!} + \cdots) + X(1 + \frac{1}{3!} + \frac{1}{5!} + \cdots)
$$

$$
= I \cosh(1) + X \sinh(1)
$$

$$
= \begin{pmatrix} \cosh(1) & \sinh(1) \\ \sinh(1) & \cosh(1) \end{pmatrix}
$$

**例 1.81**  更常见的量子计算场景：$e^{-i\theta X}$。

$$
e^{-i\theta X} = I + (-i\theta X) + \frac{(-i\theta X)^2}{2!} + \frac{(-i\theta X)^3}{3!} + \cdots
$$

注意 $X^2 = I$，所以：

$$
e^{-i\theta X} = I(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \cdots) - iX(\theta - \frac{\theta^3}{3!} + \cdots)
$$

$$
= I \cos\theta - i X \sin\theta = \begin{pmatrix} \cos\theta & -i\sin\theta \\ -i\sin\theta & \cos\theta \end{pmatrix}
$$

当 $\theta = \pi/2$ 时，$e^{-i(\pi/2) X} = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix} = -iX$。

### 1.10.3 矩阵指数的幺正性

**重要定理**：如果 $A$ 是**反厄米矩阵**（$A^\dagger = -A$），则 $e^A$ 是**幺正矩阵**。

更常见的形式：如果 $H$ 是厄米矩阵（$H^\dagger = H$），则 $e^{-i\theta H}$ 是幺正矩阵。

**验证**：

$$
(e^{-i\theta H})^\dagger = e^{i\theta H^\dagger} = e^{i\theta H} = (e^{-i\theta H})^{-1}
$$

所以 $e^{-i\theta H} (e^{-i\theta H})^\dagger = I$。

**为什么这对量子计算至关重要？** 量子态的演化由**薛定谔方程**描述：

$$
i\hbar \frac{d}{dt}|\psi(t)\rangle = H |\psi(t)\rangle
$$

其解为 $|\psi(t)\rangle = e^{-iHt/\hbar} |\psi(0)\rangle$。演化算符 $U = e^{-iHt/\hbar}$ 是幺正的，保证了量子计算的**可逆性**。

单比特门在布洛赫球上的旋转图像——$R_x, R_y, R_z$ 与 $S, T$ 等——依赖态的几何表示与门语言，放在**模块三第 1 章（单比特门）**系统展开；本节只准备矩阵指数与谱工具。

### 1.10.4 通过谱分解计算矩阵函数

要用谱分解写 $f(H)$，须先知道 $H$ 的本征值（谱）。回顾 **§1.6**：把本征方程 $H|v\rangle=\lambda|v\rangle$ 写成 $(H-\lambda I)|v\rangle=0$，非零解存在当且仅当

$$
\det(H - \lambda I) = 0
$$

该方程即**特征方程**；左边多项式是特征多项式。物理与量子化学文献里常把它叫做**久期方程**（secular equation）——名字不同，手续相同：解久期方程得 $\{\lambda_i\}$，再求本征矢，凑成谱分解 $H=\sum_i \lambda_i |\lambda_i\rangle\langle\lambda_i|$（厄米情形本征矢可取标准正交，见 §1.6.6）。

有了谱之后，矩阵函数极简：

$$
f(H) = \sum_i f(\lambda_i) |\lambda_i\rangle\langle \lambda_i|
$$

**这比直接对幂级数逐项算方便得多**——代价是把计算压力前移到“求谱”这一步。

**例 1.84**  用谱分解计算 $e^{-i\theta Z}$。

$Z$ 已对角，久期方程立刻给出本征值 $\pm 1$，谱分解：$Z = 1\cdot|0\rangle\langle 0| + (-1)\cdot|1\rangle\langle 1|$。

$$
e^{-i\theta Z} = e^{-i\theta \cdot 1} |0\rangle\langle 0| + e^{-i\theta \cdot (-1)} |1\rangle\langle 1|
$$

$$
= e^{-i\theta} |0\rangle\langle 0| + e^{i\theta} |1\rangle\langle 1|
$$

$$
= \begin{pmatrix} e^{-i\theta} & 0 \ 0 & e^{i\theta} \end{pmatrix}
$$

当 $\theta$ 很小时，$e^{-i\theta Z} \approx I - i\theta Z$。

### 1.10.5 奇异值分解

**定理 1.3（奇异值分解，SVD）** 任意 $m \times n$ 矩阵 $M$ 可以分解为：

$$
M = U \Sigma V^\dagger
$$

其中：
- $U$ 是 $m \times m$ 幺正矩阵
- $V$ 是 $n \times n$ 幺正矩阵
- $\Sigma$ 是 $m \times n$ 对角矩阵，对角元 $\sigma_i \geq 0$ 称为**奇异值**

**几何解释**：SVD 把任意线性变换分解为三个阶段：
1. $V^\dagger$：旋转（或反射）
2. $\Sigma$：沿坐标轴拉伸/压缩
3. $U$：再旋转（或反射）

**例 1.85**  $M = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ 的 SVD。

计算 $M M^\dagger = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$，本征值为 $(3 \pm \sqrt{5})/2$，奇异值为 $\sigma_1 = \sqrt{(3+\sqrt{5})/2}$，$\sigma_2 = \sqrt{(3-\sqrt{5})/2}$。

SVD 在量子信息中的应用：
- 施密特分解的数学基础（1.9 节）
- 量子态层析
- 矩阵压缩和噪声分析

### 1.10.6 极分解

**定理 1.4（极分解）** 任意方阵 $M$ 可以分解为：

$$
M = U P
$$

其中 $U$ 是幺正矩阵，$P$ 是半正定的厄米矩阵。

极分解和 SVD 密切相关：如果 $M = U_1 \Sigma U_2^\dagger$ 是 SVD，则 $U = U_1 U_2^\dagger$，$P = U_2 \Sigma U_2^\dagger$。

**几何解释**：极分解把线性变换分解为一个拉伸/压缩（$P$）后跟一个旋转（$U$），类比于极坐标 $z = re^{i\theta}$。

---

**小练习**：计算 $e^{-i\theta Y}$ 的矩阵形式（提示：$Y^2 = I$）。

**小练习**：验证 $e^{-i\theta Z/2} |0\rangle = e^{-i\theta/2} |0\rangle$。

---

## 1.11 本章小结

### 1.11.1 概念关系图

本章的所有概念围绕一条主线：**为了描述量子系统，我们需要一套数学语言**。

```
复数 ──→ 复向量空间 ──→ 内积空间 ──→ 希尔伯特空间
│                                         │
│                                         ├── 狄拉克符号（简洁表示）
│                                         ├── 矩阵运算（算符表示）
│                                         ├── 本征值问题（测量理论）
│                                         ├── 投影与完备性（概率解释）
│                                         ├── 张量积（复合系统）
│                                         ├── 部分迹与施密特分解（纠缠）
│                                         └── 矩阵函数（演化）
```

**核心脉络**：
1. 量子态是 $\mathbb{C}^n$ 中的归一化向量——用 $|\psi\rangle$ 表示
2. 量子算符是厄米或幺正矩阵——用 $A$ 表示
3. 复合系统用张量积描述——$\mathbb{C}^2 \otimes \mathbb{C}^2 = \mathbb{C}^4$
4. 测量是投影——结果为本征值，概率由内积给出
5. 演化是幺正的——$|\psi(t)\rangle = e^{-iHt} |\psi(0)\rangle$

### 1.11.2 狄拉克符号速查表

| 符号 | 含义 | 等价线性代数表示 |
|:---:|:---|:---:|
| $\lvert v\rangle$ | 右矢（列向量） | $v \in \mathbb{C}^n$ |
| $\langle v\rvert$ | 左矢（行向量共轭转置） | $v^\dagger$ |
| $\langle u \mid v \rangle$ | 内积 | $u^\dagger v$ |
| $\lvert u\rangle \langle v\rvert$ | 外积（矩阵） | $u v^\dagger$ |
| $\langle u \mid A \mid v \rangle$ | 矩阵元 | $u^\dagger A v$ |
| $A\lvert v\rangle$ | 矩阵乘向量 | $A v$ |
| $\sum_i \lvert i\rangle\langle i\rvert$ | 完备性关系 | $I$ |
| $\lvert i\rangle\langle i\rvert$ | 投影算子 | $P_i$ |
| $\lvert a\rangle \otimes \lvert b\rangle$ | 张量积 | $a \otimes b$ |
| $A \otimes B$ | 矩阵张量积 | 克罗内克积 |

### 1.11.3 关键公式

- 欧拉公式：$e^{i\theta} = \cos\theta + i\sin\theta$
- 内积：$\langle \varphi | \psi \rangle = \sum_i \overline{\varphi_i} \psi_i$
- 归一化：$\langle \psi | \psi \rangle = 1$
- 幺正条件：$U^\dagger U = I$
- 厄米条件：$H^\dagger = H$
- 本征方程：$A|v\rangle = \lambda|v\rangle$
- 谱分解：$H = \sum_i \lambda_i |\lambda_i\rangle\langle \lambda_i|$
- 投影幂等：$P^2 = P$
- 完备性：$\sum_i |i\rangle\langle i| = I$
- 张量积维度：$\dim(V \otimes W) = \dim(V) \cdot \dim(W)$
- 混合积性质：$(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$
- 施密特分解：$|\psi\rangle = \sum_i \sigma_i |a_i\rangle \otimes |b_i\rangle$
- 部分迹：$\rho_A = \text{Tr}_B(\rho_{AB})$
- 矩阵指数：$e^{A} = \sum_{n=0}^\infty A^n/n!$
- 演化算符：$U = e^{-i\theta H}$（$H$ 厄米 $\Rightarrow U$ 幺正）

---

## 1.12 本章习题

### ★ 基础题（1-8 题）

**1.** 计算下列复数：
- (a) $(2 + 3i) + (4 - 5i)$
- (b) $(1 + i)(2 - i)$
- (c) $\frac{3 + 2i}{1 - i}$
- (d) $\overline{(1 + i)(2 - 3i)}$

**2.** 将下列复数用极坐标 $re^{i\theta}$ 表示：
- (a) $1 + i$
- (b) $-2$
- (c) $3i$
- (d) $-1 - \sqrt{3}i$

**3.** 判断下列向量组是否线性无关：
- (a) $\{(1, 2)^T, (2, 4)^T\}$
- (b) $\{(1, 0, 1)^T, (0, 1, 1)^T, (1, 1, 2)^T\}$
- (c) $\{(1, i)^T, (i, -1)^T\}$（在 $\mathbb{C}^2$ 中）

**4.** 计算下列内积：
- (a) $\langle (1, 2), (3, 4) \rangle$
- (b) $\langle (1 + i, 2), (3, 4i) \rangle$
- (c) $\langle 0|+\rangle$
- (d) $\langle +|-\rangle$

**5.** 用狄拉克符号简化：
- (a) $(|0\rangle\langle 0|)(|0\rangle\langle 0|)$
- (b) $(|0\rangle\langle 1|)(|1\rangle\langle 0|)$
- (c) $(|0\rangle\langle 0| + |1\rangle\langle 1|)|+\rangle$

**6.** 计算矩阵乘积：
- (a) $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$
- (b) $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$

**7.** 验证 $Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$ 是厄米且幺正的。

**8.** 求 $X$ 矩阵的本征值和本征矢。

### ★★ 计算题（9-16 题）

**9.** 对 $v_1 = (1, 1, 0)^T$，$v_2 = (1, 0, 1)^T$ 做施密特正交化。

**10.** 证明 $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ 和 $|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$ 构成 $\mathbb{C}^2$ 的一组标准正交基。写出完备性关系。

**11.** 写出下列矩阵的谱分解：
- (a) $Z$
- (b) $X$
- (c) $Y$
- (d) $H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

**12.** 计算 $X \otimes X$，并用混合积性质验证 $(X \otimes I)(I \otimes X) = X \otimes X$。

**13.** 求 $|\psi\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$ 的施密特分解和施密特秩。这个态是否纠缠？

**14.** 对 $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ 的密度矩阵 $\rho = |\Phi^+\rangle\langle \Phi^+|$，计算 $\text{Tr}_A(\rho)$ 和 $\text{Tr}_B(\rho)$。

**15.** 计算 $e^{-i\theta Z}$ 的矩阵形式。验证它是幺正的。

**16.** 计算 $[X, Y]$ 和 $\{X, Y\}$。

### ★★★ 综合题（17-20 题）

**17.** 证明：如果 $A$ 和 $B$ 对易（$[A, B] = 0$），则 $e^{A+B} = e^A e^B$。如果 $[A, B] \neq 0$，这个公式还成立吗？给出反例。

**18.** 一个量子比特的任意态可以写成 $|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle$。计算 $\langle \psi | X | \psi \rangle$、$\langle \psi | Y | \psi \rangle$ 和 $\langle \psi | Z | \psi \rangle$。你能发现什么规律？

**19.** 对于 $|\psi\rangle = \alpha|00\rangle + \beta|01\rangle + \gamma|10\rangle + \delta|11\rangle$，写出其密度矩阵 $\rho = |\psi\rangle\langle\psi|$ 的矩阵形式。然后计算 $\text{Tr}_A(\rho)$ 和 $\text{Tr}_B(\rho)$。$\text{Tr}_A(\rho)$ 是纯态还是混合态的条件是什么？

**20.** 证明：一个两比特纯态可分离当且仅当其施密特秩为 1。利用施密特分解证明 $|\Phi^+\rangle$ 不可能写成 $|a\rangle \otimes |b\rangle$ 的形式。

---

## 知识点索引

| 术语 | 页码 |
|:---|:---:|
| 复数 | 1-2 |
| 复平面 | 2-3 |
| 模（绝对值） | 3 |
| 幅角 | 3 |
| 欧拉公式 | 4 |
| 复共轭 | 5 |
| 模方 | 5 |
| 向量空间 | 7-8 |
| 线性组合 | 9 |
| 线性无关 | 9 |
| 基 | 10 |
| 维度 | 10 |
| 基变换 | 11 |
| 子空间 | 12 |
| 内积 | 13-14 |
| 标准内积 | 14 |
| 范数 | 15 |
| 柯西-施瓦茨不等式 | 15 |
| 归一化 | 16 |
| 正交 | 16 |
| 正交补 | 17 |
| 标准正交基 | 17-18 |
| 施密特正交化 | 18-19 |
| 狄拉克符号 | 20-24 |
| 右矢（ket） | 20 |
| 左矢（bra） | 21 |
| 内积（狄拉克） | 22 |
| 外积 | 23 |
| 矩阵乘法 | 26-27 |
| 共轭转置 | 28 |
| 逆矩阵 | 29 |
| 幺正矩阵 | 30 |
| 厄米矩阵 | 31 |
| 对易子 | 32 |
| 反对易子 | 33 |
| 本征值 | 34-35 |
| 本征矢 | 34-35 |
| 特征多项式 | 36 |
| 对角化 | 37-38 |
| 谱分解 | 38-39 |
| 投影算子 | 40-41 |
| 幂等性 | 40 |
| 完备性关系 | 42 |
| 张量积 | 44-50 |
| 克罗内克积 | 45-46 |
| 混合积性质 | 48 |
| 计算基 | 49 |
| Bell 态 | 49 |
| 迹 | 51 |
| 部分迹 | 52-53 |
| 施密特分解 | 54-56 |
| 施密特秩 | 56 |
| 纠缠 | 57 |
| 矩阵指数 | 58-59 |
| 反厄米矩阵 | 60 |
| 谱分解与矩阵函数 | 61 |
| 久期方程 | 61 |
| 奇异值分解 | 62-63 |
| 极分解 | 64 |
| 薛定谔方程 | 60 |
