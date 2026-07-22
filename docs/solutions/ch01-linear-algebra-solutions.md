# 习题解答 · 第1章 线性代数

> 本书习题不提供最终答案的数值——学习线性代数的意义在于掌握方法而非记住结果。
> 以下解答给出完整的推导步骤和中间结果，供读者自我检查。

---

### 基础题（1-8 题）

**1.** 计算下列复数：

**(a)** $(2 + 3i) + (4 - 5i)$

解：

$$
(2 + 3i) + (4 - 5i) = (2 + 4) + (3 - 5)i = 6 - 2i
$$

**(b)** $(1 + i)(2 - i)$

解：

$$
(1 + i)(2 - i) = 1\cdot 2 + 1\cdot(-i) + i\cdot 2 + i\cdot(-i) = 2 - i + 2i - i^2 = 2 + i + 1 = 3 + i
$$

**(c)** $\displaystyle\frac{3 + 2i}{1 - i}$

解：分子分母同乘共轭 $1 + i$：

$$
\frac{3 + 2i}{1 - i} = \frac{(3 + 2i)(1 + i)}{(1 - i)(1 + i)} = \frac{3 + 3i + 2i + 2i^2}{1 - i^2} = \frac{3 + 5i - 2}{1 + 1} = \frac{1 + 5i}{2} = \frac{1}{2} + \frac{5}{2}i
$$

**(d)** $\overline{(1 + i)(2 - 3i)}$

解：先计算乘积：

$$
(1 + i)(2 - 3i) = 2 - 3i + 2i - 3i^2 = 2 - i + 3 = 5 - i
$$

取共轭：

$$
\overline{5 - i} = 5 + i
$$

**2.** 将下列复数用极坐标 $re^{i\theta}$ 表示（$\theta$ 取主值 $[0, 2\pi)$）：

**(a)** $1 + i$

解：$r = \sqrt{1^2 + 1^2} = \sqrt{2}$，$\theta = \arctan(1/1) = \pi/4$，所以 $1 + i = \sqrt{2}e^{i\pi/4}$。

**(b)** $-2$

解：$r = 2$，$\theta = \pi$（负实轴），所以 $-2 = 2e^{i\pi}$。

**(c)** $3i$

解：$r = 3$，$\theta = \pi/2$（正虚轴），所以 $3i = 3e^{i\pi/2}$。

**(d)** $-1 - \sqrt{3}i$

解：$r = \sqrt{(-1)^2 + (-\sqrt{3})^2} = \sqrt{1 + 3} = 2$，$\theta = \arctan(\sqrt{3}/1) = \pi/3$，但点在第 III 象限，所以 $\theta = \pi + \pi/3 = 4\pi/3$。因此 $-1 - \sqrt{3}i = 2e^{i4\pi/3}$。

**3.** 设 $z = 1 + i$，计算 $z^2$、$z^3$、$z^4$，并观察规律。

解：

$$
z^2 = (1 + i)^2 = 1 + 2i + i^2 = 2i
$$

$$
z^3 = z^2 \cdot z = 2i(1 + i) = 2i + 2i^2 = -2 + 2i
$$

$$
z^4 = (z^2)^2 = (2i)^2 = -4
$$

规律：$1 + i = \sqrt{2}e^{i\pi/4}$，所以 $z^n = 2^{n/2}e^{in\pi/4}$，每 8 次幂回到起点（周期为 8）。

**4.** 用欧拉公式推导 $\cos(2\theta) = \cos^2\theta - \sin^2\theta$ 和 $\sin(2\theta) = 2\sin\theta\cos\theta$。

解：$e^{i\cdot 2\theta} = \cos(2\theta) + i\sin(2\theta)$。同时 $e^{i\cdot 2\theta} = (e^{i\theta})^2 = (\cos\theta + i\sin\theta)^2 = \cos^2\theta - \sin^2\theta + 2i\sin\theta\cos\theta$。比较实部和虚部即得。

**5.** 求 $z^3 = 1$ 的全部复数根并在复平面上画出。

解：$z = 1^{1/3} = e^{i(0 + 2k\pi)/3}$，$k = 0, 1, 2$：

$$
z_0 = e^{i0} = 1,\quad z_1 = e^{i2\pi/3} = -\frac{1}{2} + i\frac{\sqrt{3}}{2},\quad z_2 = e^{i4\pi/3} = -\frac{1}{2} - i\frac{\sqrt{3}}{2}
$$

三个根均匀分布在单位圆上，互成 $120^\circ$。

**6.** 判断集合 $V = \{(x, y) \in \mathbb{R}^2 \mid x + y = 0\}$ 是否为向量空间。

解：是。
- 加法封闭：$(x_1, y_1) + (x_2, y_2) = (x_1 + x_2, y_1 + y_2)$，$(x_1 + x_2) + (y_1 + y_2) = (x_1 + y_1) + (x_2 + y_2) = 0 + 0 = 0$
- 数乘封闭：$c(x, y) = (cx, cy)$，$cx + cy = c(x + y) = 0$
- 零元：$(0, 0)$ 满足 $0 + 0 = 0$
- 逆元：$(x, y)$ 的逆为 $(-x, -y)$，$(-x) + (-y) = -(x + y) = 0$
因此是 $\mathbb{R}^2$ 的子空间（一条过原点的直线）。

**7.** 判断 $S = \{(1, 0, 1), (0, 1, 0), (1, 1, 1)\}$ 是否线性无关。

解：设 $a(1,0,1) + b(0,1,0) + c(1,1,1) = (0,0,0)$，得方程组：

$$
\begin{cases}
a + c = 0 \\
b + c = 0 \\
a + c = 0
\end{cases}
$$

第一和第三式相同。由 $a + c = 0$ 得 $a = -c$，由 $b + c = 0$ 得 $b = -c$。取 $c = 1$ 则 $a = -1, b = -1$ 为非零解。因此线性相关。

几何解释：$(1,0,1) + (0,1,0) = (1,1,1)$，所以 $(1,1,1)$ 是前两个的和。

**8.** 求 $M_2(\mathbb{R})$（$2\times 2$ 实矩阵）的一组基和维数。

解：标准基为：

$$
E_{11} = \begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix},\; 
E_{12} = \begin{pmatrix}0 & 1 \\ 0 & 0\end{pmatrix},\; 
E_{21} = \begin{pmatrix}0 & 0 \\ 1 & 0\end{pmatrix},\; 
E_{22} = \begin{pmatrix}0 & 0 \\ 0 & 1\end{pmatrix}
$$

任意实 $2\times 2$ 矩阵可唯一表示为这四个矩阵的线性组合。维数 $= 4$。

---

### 提高题（9-14 题）

**9.** 证明 $|z_1 + z_2|^2 + |z_1 - z_2|^2 = 2(|z_1|^2 + |z_2|^2)$（平行四边形恒等式）。

解：

$$
|z_1 + z_2|^2 = (z_1 + z_2)(\overline{z_1 + z_2}) = (z_1 + z_2)(\overline{z_1} + \overline{z_2}) = |z_1|^2 + z_1\overline{z_2} + \overline{z_1}z_2 + |z_2|^2
$$

$$
|z_1 - z_2|^2 = (z_1 - z_2)(\overline{z_1} - \overline{z_2}) = |z_1|^2 - z_1\overline{z_2} - \overline{z_1}z_2 + |z_2|^2
$$

两式相加，交叉项抵消，得 $2(|z_1|^2 + |z_2|^2)$。

几何意义：平行四边形对角线的平方和等于四边平方和。

**10.** 证明向量 $v_1 = (1, 1, 0)$，$v_2 = (1, 0, 1)$，$v_3 = (0, 1, 1)$ 是 $\mathbb{R}^3$ 的一组基，并将 $w = (2, 3, 4)$ 用该基表示。

**(a)** 证明线性无关：设 $a v_1 + b v_2 + c v_3 = (0,0,0)$，得：

$$
\begin{cases}
a + b = 0 \\
a + c = 0 \\
b + c = 0
\end{cases}
$$

由第一式 $b = -a$，代入第三式 $-a + c = 0$ 得 $c = a$，代入第二式 $a + a = 0$ 得 $a = 0$，进而 $b = 0, c = 0$。线性无关。三个向量在 $\mathbb{R}^3$ 中线性无关即构成基。

**(b)** 求 $w$ 在基 $\{v_1, v_2, v_3\}$ 下的坐标：设 $w = a v_1 + b v_2 + c v_3$：

$$
\begin{cases}
a + b = 2 \\
a + c = 3 \\
b + c = 4
\end{cases}
$$

三式相加得 $2(a + b + c) = 9$，$a + b + c = 9/2$。
减去第一式得 $c = 9/2 - 2 = 5/2$；减去第二式得 $b = 9/2 - 3 = 3/2$；减去第三式得 $a = 9/2 - 4 = 1/2$。
坐标：$[w]_{B} = (1/2, 3/2, 5/2)^\mathsf{T}$。

**11.** 给出 $A = \begin{pmatrix}2 & 1 \\ 1 & 2\end{pmatrix}$ 的谱分解。

**(a)** 求本征值：

$$
\det(A - \lambda I) = \det\begin{pmatrix}2-\lambda & 1 \\ 1 & 2-\lambda\end{pmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda - 1)(\lambda - 3) = 0
$$

本征值 $\lambda_1 = 1$，$\lambda_2 = 3$。

**(b)** 求本征向量：
$\lambda_1 = 1$：$(A - I)v = \begin{pmatrix}1 & 1 \\ 1 & 1\end{pmatrix}v = 0$，得 $v_1 = \frac{1}{\sqrt{2}}(1, -1)^\mathsf{T}$。
$\lambda_2 = 3$：$(A - 3I)v = \begin{pmatrix}-1 & 1 \\ 1 & -1\end{pmatrix}v = 0$，得 $v_2 = \frac{1}{\sqrt{2}}(1, 1)^\mathsf{T}$。

**(c)** 谱分解：

$$
A = 1 \cdot |v_1\rangle\langle v_1| + 3 \cdot |v_2\rangle\langle v_2|
= 1 \cdot \frac{1}{2}\begin{pmatrix}1 & -1 \\ -1 & 1\end{pmatrix} + 3 \cdot \frac{1}{2}\begin{pmatrix}1 & 1 \\ 1 & 1\end{pmatrix}
$$

**12.** 对向量 $|+\rangle$ 应用 Pauli 矩阵 $X, Y, Z$。

$|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$。

$$
X|+\rangle = \frac{1}{\sqrt{2}}(|1\rangle + |0\rangle) = |+\rangle
$$

$$
Y|+\rangle = \frac{1}{\sqrt{2}}(i|1\rangle - i|0\rangle) = -i|-\rangle
$$

$$
Z|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) = |-\rangle
$$

**13.** 计算 $\text{Tr}(X\rho)$，其中 $\rho = \frac{1}{2}(I + \vec{r}\cdot\vec{\sigma})$。

解：$\text{Tr}(X\rho) = \frac{1}{2}\text{Tr}(X) + \frac{1}{2}\text{Tr}(X(\vec{r}\cdot\vec{\sigma}))$。$\text{Tr}(X) = 0$。$\vec{r}\cdot\vec{\sigma} = r_x X + r_y Y + r_z Z$。利用 $\text{Tr}(X^2) = \text{Tr}(I) = 2$，$\text{Tr}(XY) = \text{Tr}(iZ) = 0$，$\text{Tr}(XZ) = 0$：

$$
\text{Tr}(X\rho) = \frac{1}{2} \cdot r_x \cdot 2 = r_x
$$

**14.** 推导 $A = \begin{pmatrix}a & b \\ c & d\end{pmatrix}$ 是 Hermitian 矩阵的条件。

解：Hermitian 要求 $A^\dagger = A$。
$A^\dagger = (\overline{A})^\mathsf{T} = \begin{pmatrix}\overline{a} & \overline{c} \\ \overline{b} & \overline{d}\end{pmatrix}$。
因此条件：$\overline{a} = a$（$a$ 为实数），$\overline{d} = d$（$d$ 为实数），$\overline{c} = b$。

---

### 挑战题（15-20 题）

**15.** 证明 Pauli 矩阵满足 $XYZ = iI$。

解：

$$
XYZ = \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix} \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix} \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}
$$

先计算 $XY = \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix} \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix} = \begin{pmatrix}i & 0 \\ 0 & -i\end{pmatrix} = iZ$。
再乘 $Z$：$(iZ)Z = iZ^2 = iI$。

**16.** 证明 $AB = I \implies BA = I$（有限维）。

解：$AB = I$，则 $A$ 是可逆映射（满射 + 单射）。在有限维下，线性映射是单射当且仅当它是满射。$B$ 是 $A$ 的右逆，但右逆在有限维下也是左逆。因此 $BA = I$。

反例（无限维）：在序列空间 $\ell^2$ 上定义右移位算子 $R(x_1, x_2, \ldots) = (0, x_1, x_2, \ldots)$ 和左移位算子 $L(x_1, x_2, \ldots) = (x_2, x_3, \ldots)$。$LR = I$ 但 $RL(x_1, x_2, \ldots) = (0, x_2, x_3, \ldots) \neq I$。

**17.** 用 Gram-Schmidt 正交化 $\{(1, 0, 1), (1, 1, 0), (0, 1, 1)\}$。

解：设 $v_1 = (1, 0, 1)$，$v_2 = (1, 1, 0)$，$v_3 = (0, 1, 1)$。

$e_1 = \frac{v_1}{\|v_1\|} = \frac{1}{\sqrt{2}}(1, 0, 1)$。

$u_2 = v_2 - \langle v_2, e_1\rangle e_1 = (1,1,0) - \frac{1}{\sqrt{2}}\cdot\frac{1}{\sqrt{2}}(1,0,1) = (1,1,0) - \frac{1}{2}(1,0,1) = (\frac12, 1, -\frac12)$。
$e_2 = \frac{u_2}{\|u_2\|} = \frac{1}{\sqrt{1/4 + 1 + 1/4}}(\frac12, 1, -\frac12) = \frac{1}{\sqrt{3/2}}(\frac12, 1, -\frac12) = \frac{1}{\sqrt{6}}(1, 2, -1)$。

$u_3 = v_3 - \langle v_3, e_1\rangle e_1 - \langle v_3, e_2\rangle e_2$。
$\langle v_3, e_1\rangle = \frac{1}{\sqrt{2}}(0+0+1) = \frac{1}{\sqrt{2}}$。
$\langle v_3, e_2\rangle = (0,1,1)\cdot\frac{1}{\sqrt{6}}(1,2,-1) = \frac{1}{\sqrt{6}}(0 + 2 - 1) = \frac{1}{\sqrt{6}}$。
$u_3 = (0,1,1) - \frac{1}{2}(1,0,1) - \frac{1}{6}(1,2,-1) = (-\frac{1}{2} - \frac{1}{6}, 1 - \frac{1}{3}, 1 - \frac{1}{2} + \frac{1}{6})$。
$u_3 = (-\frac{2}{3}, \frac{2}{3}, \frac{2}{3})$。
$e_3 = \frac{u_3}{\|u_3\|} = \frac{1}{\sqrt{3}}(-1, 1, 1)$。

**18.** 证明：若 $A$ 正定，则 $A^{-1}$ 也正定。

解：$A$ 正定意味着 $A^\dagger = A$ 且所有本征值 $\lambda_i > 0$。$A^{-1}$ 的本征值为 $1/\lambda_i > 0$，且 $(A^{-1})^\dagger = (A^\dagger)^{-1} = A^{-1}$。因此 $A^{-1}$ 也正定。

**19.** 计算 $(\sigma \cdot \vec{a})(\sigma \cdot \vec{b})$。

解：$\sigma \cdot \vec{a} = a_x X + a_y Y + a_z Z$。利用 Pauli 矩阵乘法关系 $(\sigma_i \sigma_j) = \delta_{ij} I + i\epsilon_{ijk}\sigma_k$：

$$
(\sigma \cdot \vec{a})(\sigma \cdot \vec{b}) = (\vec{a} \cdot \vec{b})I + i\sigma \cdot (\vec{a} \times \vec{b})
$$

**20.** 讨论 $d = 2$ 的情况。

解：$d = 2$ 时，两个向量 $v_1, v_2$ 线性相关当且仅当其中一个被另一个线性表示，即 $v_1 = \lambda v_2$。因此二维空间中两组线性无关的向量组：
- $\{(1,0), (0,1)\}$（标准基）
- $\{(1,1), (1,-1)\}$（也构成基，行列式 $-2 \neq 0$）
- 任意两个不共线的向量均可。

---

> **说明**：本章共 20 题。完整解答覆盖复数运算、向量空间、内积正交、狄拉克符号、矩阵运算、谱分解等全部知识点。建议在尝试自行解答后再对照。
