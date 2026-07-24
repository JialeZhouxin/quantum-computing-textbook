# 第2章 量子力学基本假设

> **本章导读**
>
> 量子力学用**态、可观察量、测量与演化**四个对象组织微观系统。本章给出（在量子信息中最常用的）工作公设：**态空间**、**可观察量**、**投影测量**、**时间演化**；并专节给出**不确定关系**（它是测量公设与对易结构下的**定理**，不是额外口号式公理）。
>
> 写法约定：每节先写**是什么**（公设陈述），再写**数学上是什么**，再写**怎么算**，最后给**完整数值例**。线代细节（内积、投影、谱分解、矩阵指数）见第 1 章；本章只绑定物理含义与计算流程。

---

## 2.1 状态空间公设

### 2.1.1 公设陈述（是什么）

**状态空间公设。** 每一个孤立的量子系统，都对应一个复内积空间——**Hilbert 空间** $\mathcal{H}$。系统在某一时刻的（纯）状态，由 $\mathcal{H}$ 中的一个**非零向量** $|\psi\rangle$ 描述；物理上使用**单位向量**（归一化）

$$
\langle\psi|\psi\rangle = 1.
$$

更精确地：全体 $e^{i\alpha}|\psi\rangle$（$\alpha\in\mathbb{R}$）代表**同一个**物理状态——状态是射线上的点，而不是带全局相位标签的单个箭头。

**它回答的问题：** “系统现在处于什么状态？”——答案是 $\mathcal{H}$ 里的一个（射线）向量，不是经典相空间里的点 $(x,p)$。

### 2.1.2 数学对象（怎么写）

| 对象 | 写法 | 含义 |
|---|---|---|
| 右矢（ket） | $\|\psi\rangle$ | 列向量，态 |
| 左矢（bra） | $\langle\psi\|$ | 行向量，$\langle\psi\| = (\|\psi\rangle)^\dagger$ |
| 内积 | $\langle\phi\|\psi\rangle$ | 标量；$|\langle\phi\|\psi\rangle|^2$ 进入测量概率 |
| 外积 | $\|\phi\rangle\langle\psi\|$ | 算符（矩阵） |
| 计算基（qubit） | $\|0\rangle=\begin{pmatrix}1\\0\end{pmatrix}$，$\|1\rangle=\begin{pmatrix}0\\1\end{pmatrix}$ | $\mathcal{H}=\mathbb{C}^2$ 的标准正交基（$Z$ 基） |

多比特：$\mathcal{H} = (\mathbb{C}^2)^{\otimes n}$，维数 $2^n$（张量积见 §1.8）。

线性代数操作规则见 §1.3–1.5；本节要求会：**归一化、内积、按基展开、区分 bra/ket**。

### 2.1.3 操作步骤（怎么做）

**写下一个态并检查是否合法：**

1. 选定 Hilbert 空间与一组标准正交基 $\{|i\rangle\}$。
2. 写展开 $|\psi\rangle = \sum_i c_i |i\rangle$，$c_i\in\mathbb{C}$。
3. 算范数平方 $N = \langle\psi|\psi\rangle = \sum_i |c_i|^2$。
4. 若 $N\neq 1$，归一化：$|\psi\rangle \leftarrow |\psi\rangle/\sqrt{N}$（$N=0$ 非法）。
5. 全局相位：用 $e^{i\alpha}|\psi\rangle$ 替换不改变任何投影测量统计（见 §2.3）。

**叠加原理（态空间的线性结构）：**  
若 $|\psi\rangle$、$|\phi\rangle$ 是 $\mathcal{H}$ 中的向量，则线性组合 $\alpha|\psi\rangle+\beta|\phi\rangle$（$\alpha,\beta\in\mathbb{C}$ 不全为 0）仍在 $\mathcal{H}$ 中；归一化后得到新的物理态。  
**注意：** 叠加是**相干**线性组合；“50% 是 $|0\rangle$、50% 是 $|1\rangle$”的**经典混合**要用密度矩阵（第 3 章），不能写成单个 ket 的“半半”。

**Dirac 运算口诀：**

- 内积 $\langle\phi|\psi\rangle$：先写 bra 再写 ket，结果是**标量**，可自由挪动（§1.7.4 系数规则）。
- 外积 $|\phi\rangle\langle\psi|$：结果是**算符**，不可当标量抽走。
- 由坐标：$|\psi\rangle=\begin{pmatrix}c_0\\c_1\end{pmatrix}$ 则 $\langle\psi|=\begin{pmatrix}\overline{c_0}&\overline{c_1}\end{pmatrix}$。

### 2.1.4 算例

**例 2.1（归一化）** 原始向量 $|\tilde\psi\rangle = 2|0\rangle + i|1\rangle$。

$$
\langle\tilde\psi|\tilde\psi\rangle = |2|^2 + |i|^2 = 4+1 = 5,
\quad
|\psi\rangle = \frac{1}{\sqrt{5}}(2|0\rangle + i|1\rangle)
= \begin{pmatrix} 2/\sqrt{5} \\ i/\sqrt{5} \end{pmatrix}.
$$

**例 2.2（左矢右矢）** 对上式 $|\psi\rangle$，

$$
\langle 0|\psi\rangle = \frac{2}{\sqrt{5}},\quad
\langle 1|\psi\rangle = \frac{i}{\sqrt{5}},\quad
\langle\psi|0\rangle = \overline{\langle 0|\psi\rangle} = \frac{2}{\sqrt{5}}.
$$

外积 $|\psi\rangle\langle\psi|$ 是 $2\times 2$ 矩阵（密度算符雏形，见第 3 章）。

**例 2.3（叠加 vs 口头“混合”）**  
$|+\rangle=\frac{1}{\sqrt{2}}(|0\rangle+|1\rangle)$ 是叠加：在 $X$ 基下是确定的本征态。  
“以 $1/2$ 概率制备 $|0\rangle$，以 $1/2$ 概率制备 $|1\rangle$”是混合：单次实验中系统处于二者之一，无相对相位。二者在 $Z$ 测量上概率相同，在 $X$ 测量上可区分（§2.3）。

**小练习：** 为什么要求单位向量？若使用未归一的 $|\tilde\psi\rangle$ 直接套 Born 规则会发生什么？  
**小练习：** 设 $|\psi\rangle=2|0\rangle+i|1\rangle$（未归一），计算 $\langle\psi|\psi\rangle$ 并归一化。  
**小练习：** $|\psi\rangle=|0\rangle$ 与 $|\phi\rangle=e^{i\pi/3}|0\rangle$ 是否同一物理状态？  
**小练习：** 叠加态 $\frac{1}{\sqrt{2}}(|0\rangle+|1\rangle)$ 与混合（各 50% 的 $|0\rangle$、$|1\rangle$）本质区别是什么？  
**小练习：** 3 个量子比特的 $\dim\mathcal{H}$？$n$ 比特计算基有多少个向量？

### 2.1.5 射线、维度与偏振类比（压缩）

- **射线：** 物理状态 $\leftrightarrow$ 一维子空间（相差 $e^{i\alpha}$）。可观测的是**相对相位**（不同基矢系数之比），不是全局相位。  
- **维度：** $n$ 能级封闭系统 $\dim\mathcal{H}=n$；量子比特 $n=2$。  
- **光偏振类比：** 水平/垂直偏振 $\leftrightarrow |0\rangle/|1\rangle$；45° 线偏振 $\leftrightarrow |+\rangle$。Jones 向量的归一化与叠加，与 qubit 态同一套线性代数。

---

## 2.2 可观察量公设

### 2.2.1 公设陈述（是什么）

**可观察量公设。** 每一个物理上可测量的量（能量、自旋分量、光子数……）对应 Hilbert 空间上的一个**厄米算符**（自伴算符）$A=A^\dagger$。  
对该可观察量做（理想投影）测量时：

- 可能出现的数值结果，只能是 $A$ 的**本征值**；
- 对应的结果标签态是本征矢（可取标准正交本征基）。

**它回答的问题：** “能测什么、测出来是什么数？”——由 $A$ 的谱决定。

### 2.2.2 数学对象

- 厄米：$A^\dagger=A$ $\Rightarrow$ 本征值实、不同本征值本征矢正交、可谱分解（§1.5–1.6）

$$
A = \sum_k \lambda_k |\lambda_k\rangle\langle\lambda_k|
$$

（简并时把 $|\lambda_k\rangle\langle\lambda_k|$ 换成子空间投影。）

- **对易子** $[A,B]:=AB-BA$。若 $[A,B]=0$，则存在共同本征基（“可同时确定”的数学含义见 §2.4）。
- 量子比特常用可观察量：Pauli 矩阵

$$
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
$$

均厄米，本征值 $\pm 1$。

位置/动量/哈密顿在连续变量中出现；离散量子计算主线优先 Pauli 串。

### 2.2.3 操作步骤

**对给定矩阵 / 符号算符 $A$：**

1. 检查 $A^\dagger=A$（否则不能当标准可观察量）。
2. 解久期方程 $\det(A-\lambda I)=0$ 得本征值（§1.6、§1.10.4）。
3. 对每个 $\lambda$，解 $(A-\lambda I)|v\rangle=0$，正交归一化本征矢。
4. 写谱分解，供测量与 $f(A)$ 使用。
5. 需要算符函数时：$f(A)=\sum_k f(\lambda_k)|\lambda_k\rangle\langle\lambda_k|$（§1.10）。

### 2.2.4 算例

**例 2.4** $A=Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix}$。  
$A^\dagger=A$，本征值 $\pm 1$。  
$\lambda=1$：本征矢 $|+y\rangle=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\i\end{pmatrix}$；  
$\lambda=-1$：$|-y\rangle=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-i\end{pmatrix}$。  
谱分解：$Y = |+y\rangle\langle +y| - |-y\rangle\langle -y|$。

**例 2.5（算符函数）** $Z=|0\rangle\langle0|-|1\rangle\langle1|$，则

$$
e^{i\theta Z} = e^{i\theta}|0\rangle\langle0| + e^{-i\theta}|1\rangle\langle1|
= \begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}.
$$

**小练习：** 验证 $Z$ 厄米，求本征值与本征矢。  
**小练习：** 计算 $\sigma_x\sigma_y$ 与 $\sigma_y\sigma_x$，确认不对易。  
**小练习：** 由 $Z$ 的谱分解求 $e^{i\theta Z}$。  
**小练习（选做）：** 一维谐振子 $H=p^2/2m+\frac12 m\omega^2 x^2$，在位置表象写微分形式。

---

## 2.3 投影测量公设

### 2.3.1 公设陈述（是什么）

**投影测量公设（理想 von Neumann 测量）。** 测量可观察量 $A=\sum_m \lambda_m P_m$（$P_m$ 为属于本征值 $\lambda_m$ 的谱投影，$P_m^\dagger=P_m=P_m^2$，$\sum_m P_m=I$）时：

1. **结果：** 得到某个本征值 $\lambda_m$（离散谱）。
2. **概率（Born 规则）：** 对归一态 $|\psi\rangle$，

$$
\Pr(\lambda_m) = \langle\psi|P_m|\psi\rangle.
$$

非简并且 $P_m=|m\rangle\langle m|$ 时，$\Pr(m)=|\langle m|\psi\rangle|^2$。

3. **坍缩（更新规则）：** 若得到 $\lambda_m$，则事后态为

$$
|\psi\rangle \ \longmapsto\ \frac{P_m|\psi\rangle}{\sqrt{\langle\psi|P_m|\psi\rangle}}.
$$

非简并时即（全局相位不计）本征态 $|m\rangle$。

**它回答的问题：** “怎么从态读出经典数据？测完态变成什么？”——概率由投影给出，状态按投影更新。

POVM 是更一般测量（元件不必两两正交投影）；主线先会算投影测量。

### 2.3.2 数学对象

- 投影：$P^2=P=P^\dagger$（§1.7）。
- 完备性：$\sum_m P_m = I$。
- 期望值（重复制备同一 $|\psi\rangle$ 多次测 $A$ 的平均）：

$$
\langle A\rangle = \langle\psi|A|\psi\rangle = \sum_m \lambda_m \Pr(\lambda_m).
$$

### 2.3.3 操作步骤（投影测量计算清单）

给定 $|\psi\rangle$ 与要测的 $A$（或测量基 $\{|m\rangle\}$）：

1. 把 $A$ 谱分解，列出 $\{(\lambda_m,P_m)\}$ 或正交本征基 $\{|m\rangle\}$。
2. 确认 $|\psi\rangle$ 已归一；否则先归一。
3. 算每个结果的概率 $p_m=\langle\psi|P_m|\psi\rangle$ 或 $|\langle m|\psi\rangle|^2$。检查 $\sum_m p_m=1$。
4. 若问坍缩后态：对观测到的 $m$，算 $P_m|\psi\rangle$ 再除以 $\sqrt{p_m}$。
5. 若问期望：$\langle A\rangle=\langle\psi|A|\psi\rangle$，或 $\sum_m \lambda_m p_m$。
6. **重复测量：** 坍缩后若立即再测**同一** $A$，结果以概率 1 仍为 $\lambda_m$（理想情况）。

### 2.3.4 算例

**例 2.6（$Z$ 基测量）** $|\psi\rangle=|+\rangle=\frac{1}{\sqrt{2}}(|0\rangle+|1\rangle)$。  
$P_0=|0\rangle\langle0|$，$P_1=|1\rangle\langle1|$。

$$
p_0=|\langle0|+\rangle|^2=\frac12,\quad p_1=\frac12,\quad
\langle Z\rangle = \langle+|Z|+\rangle = 0.
$$

若得到 $0$，坍缩后 $|\psi\rangle\to|0\rangle$；再测 $Z$ 必得 $0$。

**例 2.7（$X$ 基测量）** 同一 $|+\rangle$。$X$ 本征态 $|+\rangle,|-\rangle$，本征值 $\pm1$。  
$p_{+}=|\langle+|+\rangle|^2=1$，$p_{-}=0$。  
故 $X$ 测量确定得到 $+1$，坍缩后仍是 $|+\rangle$。

**例 2.8（一般态）** $|\psi\rangle=\frac{1}{\sqrt{5}}(2|0\rangle+i|1\rangle)$ 测 $Z$：  
$p_0=4/5$，$p_1=1/5$，$\langle Z\rangle=(4/5)-(1/5)=3/5$。

**小练习：** $P_0=|0\rangle\langle0|$，$P_1=|1\rangle\langle1|$，验证 $P_0^2=P_0$，$P_0P_1=0$。  
**小练习：** $|+\rangle$ 测 $Z$，求 $p_0$ 与 $\langle Z\rangle$。  
**小练习：** 对 $|+\rangle$ 测 $Z$ 得到 $|0\rangle$ 后，再测 $Z$ 结果？  
**小练习：** 计算 $|+\rangle$ 的 $\langle X\rangle$。  
**小练习：** POVM 与投影测量的根本区别？何时必须用 POVM？（预习：元件 $\{E_m\}$ 满足 $E_m\ge0$、$\sum_m E_m=I$，但不要求 $E_m$ 为正交投影。）

---

## 2.4 不确定关系与对易

### 2.4.1 定位（定理，不是额外口号公设）

**不确定关系是定理：** 在态空间 + 可观察量 + 测量（用标准差刻画涨落）的框架下，由内积不等式与对易子代数推出。它说的是：**同一量子态上**，两个可观察量的统计涨落不能同时任意小——根源是算符不对易，而不是“仪器不够好”的唯象抱怨。

### 2.4.2 数学对象

对归一态 $|\psi\rangle$ 与厄米 $A$：

$$
\langle A\rangle=\langle\psi|A|\psi\rangle,\quad
\Delta A := \sqrt{\langle(A-\langle A\rangle)^2\rangle}
= \sqrt{\langle A^2\rangle-\langle A\rangle^2}.
$$

**Robertson 关系：**

$$
\Delta A\,\Delta B \ \ge\ \frac12 \bigl|\langle[A,B]\rangle\bigr|.
$$

- 若 $[A,B]=0$，右边可为 0：存在共同本征态，使 $\Delta A=\Delta B=0$（同时有确定值）。
- 若 $[A,B]\neq0$，则**不存在**使两者标准差同时为 0 的态；下界由 $\langle[A,B]\rangle$ 控制。

Pauli：$[X,Y]=2iZ$（循环），故例如 $\Delta X\Delta Y\ge|\langle Z\rangle|$。

位置–动量：$[x,p]=i\hbar$ $\Rightarrow$ $\Delta x\Delta p\ge\hbar/2$。  
能量–时间常用 $\Delta E\,\Delta t$ 的估计，但 $\Delta t$ **不是**与 $H$ 共轭的自伴“时间算符”的标准差，数学地位与 $[x,p]$ 不同。

### 2.4.3 操作步骤

1. 算 $\langle A\rangle,\langle A^2\rangle$，得 $\Delta A$；同理 $\Delta B$。
2. 算 $[A,B]$，再算 $\langle[A,B]\rangle$。
3. 检查是否满足 $\Delta A\Delta B\ge\frac12|\langle[A,B]\rangle|$。
4. 判断能否同时确定：看是否对易 / 是否处于共同本征态。

### 2.4.4 算例

**例 2.9** 态 $|0\rangle$，$A=X$，$B=Y$。  
$\langle X\rangle=\langle0|X|0\rangle=0$，$\langle X^2\rangle=\langle0|I|0\rangle=1$ $\Rightarrow$ $\Delta X=1$。  
同理 $\Delta Y=1$。  
$[X,Y]=2iZ$，$\langle[X,Y]\rangle=2i\langle Z\rangle=2i$，故 $\frac12|\langle[X,Y]\rangle|=1$。  
$\Delta X\Delta Y=1\ge1$，饱和。

**例 2.10（对易则可同时确定）** $[Z,I]=0$；任意 $Z$ 本征态上 $\Delta Z=0$。  
$[X,Z]=-2iY\neq0$：不存在态使 $\Delta X=\Delta Z=0$ 同时成立。

**小练习：** 不确定关系的根源是测量技术极限，还是算符代数与态的统计结构？  
**小练习：** 证明（提纲）$\Delta A\Delta B\ge\frac12|\langle[A,B]\rangle|$。  
**小练习：** 为何能量–时间写法与位置–动量在数学地位上不同？  
**小练习：** 证明若 $[A,B]=0$，则 $A,B$ 可有共同本征基（提纲即可）。

---

## 2.5 时间演化公设

### 2.5.1 公设陈述（是什么）

**时间演化公设（封闭系统）。** 孤立系统的纯态随时间的变化由**薛定谔方程**给出：

$$
i\hbar\frac{d}{dt}|\psi(t)\rangle = H(t)\,|\psi(t)\rangle,
$$

其中 $H(t)=H(t)^\dagger$ 是哈密顿（能量）算符。  
等价地：存在**幺正**演化算符 $U(t,t_0)$，

$$
|\psi(t)\rangle = U(t,t_0)\,|\psi(t_0)\rangle,\quad U^\dagger U=I.
$$

$H$ 不显含时：$U(t,0)=e^{-iHt/\hbar}$（矩阵指数见 §1.10）。

**它回答的问题：** “不测的时候，态怎么变？”——确定性、可逆的线性幺正演化；**随机性进入测量步骤，不进入封闭演化步骤**。

开放系统：系统+环境联合幺正，再对环境偏迹 → 信道（§1.9.3、第 3 章、第 21 章）。

### 2.5.2 数学对象与操作

1. 写出 $H$（或 Pauli 分解）。
2. 若 $H$ 与时间无关：谱分解 $H=\sum_n E_n|n\rangle\langle n|$，则

$$
U(t)=\sum_n e^{-iE_n t/\hbar}|n\rangle\langle n|.
$$

3. 初态 $|\psi(0)\rangle=\sum_n c_n|n\rangle$ $\Rightarrow$
   $|\psi(t)\rangle=\sum_n c_n e^{-iE_n t/\hbar}|n\rangle$。
4. **定态：** 若 $|\psi(0)\rangle$ 已是 $H$ 的本征态，则只多全局相位 $e^{-iEt/\hbar}$，任何可观察量期望值不随时间变。
5. 检查幺正：$U^\dagger U=I$ 保证范数守恒。

量子门：在电路模型里，$U$ 由门序列实现；理想门即某段有效 $H$ 下的 $U$。

### 2.5.3 算例

**例 2.11** $H=\hbar\omega Z/2$，则

$$
U(t)=e^{-i\omega t Z/2}
= \begin{pmatrix}e^{-i\omega t/2}&0\\0&e^{i\omega t/2}\end{pmatrix}.
$$

初态 $|+\rangle$：

$$
|\psi(t)\rangle = \frac{1}{\sqrt{2}}\big(e^{-i\omega t/2}|0\rangle + e^{i\omega t/2}|1\rangle\big)
= \frac{e^{-i\omega t/2}}{\sqrt{2}}\big(|0\rangle + e^{i\omega t}|1\rangle\big).
$$

相对相位 $\omega t$ 随时间转；$Z$ 期望恒为 0，$X$ 期望 $\langle X\rangle=\cos(\omega t)$ 振荡。

**例 2.12（定态）** $|\psi(0)\rangle=|0\rangle$ 是 $H$ 本征态，能量 $E=\hbar\omega/2$，  
$|\psi(t)\rangle=e^{-i\omega t/2}|0\rangle$，与 $|0\rangle$ 同射线；$\langle Z\rangle=1$ 恒定。

**小练习：** 证明 $U=e^{-iHt/\hbar}$（$H$ 厄米）幺正。  
**小练习：** $H=\hbar\omega Z/2$，初态 $|+\rangle$，求 $|\psi(t)\rangle$。  
**小练习：** Ehrenfest 定理在期望值层面如何联系经典方程？（选读。）

---

> **衔接：** 以上 2.1–2.5 给出可计算的公设核心。下面 §2.6 二能级与布洛赫球、§2.7 不可克隆等，是在这些公设上的**应用与推论**骨架；几何与门语言的完整展开见模块三第 1 章。

## 2.6 二能级系统

### 2.6.1 是什么

**二能级系统（TLS / qubit）** 是 $\dim\mathcal{H}=2$ 的量子系统：只保留两个计算相关能级，记为 $|0\rangle$、$|1\rangle$（更高能级视为泄漏，硬件章再谈）。

物理实例（同一套数学）：

- 自旋 $1/2$ 沿某轴的两个投影；
- 两极化正交模式中的单光子偏振；
- 超导 Transmon 的基态/第一激发态（近似二能级）；
- 原子的钟跃迁两能级。

**它回答的问题：** 量子信息里“一个比特”的状态空间长什么样、如何参数化、驱动下如何翻转。

### 2.6.2 数学对象：一般纯态

任意归一纯态（取 $|0\rangle$ 系数非负的相位约定）可写成

$$
|\psi\rangle
= \cos\frac{\theta}{2}\,|0\rangle
+ e^{i\varphi}\sin\frac{\theta}{2}\,|1\rangle,
\quad
\theta\in[0,\pi],\ \varphi\in[0,2\pi).
$$

- $\theta$：极角，控制 $|0\rangle/|1\rangle$ 布居（$p_0=\cos^2\frac{\theta}{2}$，$p_1=\sin^2\frac{\theta}{2}$）。
- $\varphi$：**相对相位**（$|1\rangle$ 相对 $|0\rangle$）；**不是**全局相位。
- 全局相位 $e^{i\alpha}|\psi\rangle$ 不进入上式参数，因射线等价（§2.1）。

等价地，纯态密度算符 $\rho=|\psi\rangle\langle\psi|$ 可用 **Bloch 矢量** $\vec{r}=(r_x,r_y,r_z)$ 写

$$
\rho = \frac{I+\vec{r}\cdot\vec{\sigma}}{2},
\quad
\vec{r}
=
\big(
\langle X\rangle,\langle Y\rangle,\langle Z\rangle
\big),
\quad
|\vec{r}|=1\ \text{（纯态）}.
$$

坐标与 $(\theta,\varphi)$ 的关系：

$$
r_x=\sin\theta\cos\varphi,\quad
r_y=\sin\theta\sin\varphi,\quad
r_z=\cos\theta.
$$

球面上的点 $\leftrightarrow$ 纯态；球**内**点 $|\vec{r}|<1$ 是混合态（第 3 章）。门与旋转图像的系统训练在模块三 ch07；此处只建立参数字典。

### 2.6.3 操作步骤

**由参数写态 / 由态读参数：**

1. 归一化 $|\psi\rangle=c_0|0\rangle+c_1|1\rangle$。
2. 抽全局相位使 $c_0$ 为实且 $\ge 0$：$|\psi\rangle\leftarrow e^{-i\arg c_0}|\psi\rangle$（若 $c_0=0$ 则态在南极，$|1\rangle$ 相位可整体规范）。
3. $\theta=2\arccos(|c_0|)$（或 $\cos\theta=|c_0|^2-|c_1|^2$）。
4. $\varphi=\arg(c_1)-\arg(c_0)$（在上述规范下即 $\arg c_1$）。
5. 需要 Bloch 矢量时：算 $\langle X\rangle,\langle Y\rangle,\langle Z\rangle$。

**相对相位 vs 全局相位（可操作判据）：**

- 全局：$|\psi\rangle\mapsto e^{i\alpha}|\psi\rangle$ → 一切 $\langle A\rangle$ 与投影概率不变。
- 相对：只改 $c_1/c_0$ 的辐角 → 例如 $\langle X\rangle,\langle Y\rangle$ 会变；$Z$ 基概率可不变。

### 2.6.4 算例

**例 2.13** $\theta=\pi/3$，$\varphi=\pi/4$：

$$
|\psi\rangle
= \cos\frac{\pi}{6}|0\rangle + e^{i\pi/4}\sin\frac{\pi}{6}|1\rangle
= \frac{\sqrt{3}}{2}|0\rangle + e^{i\pi/4}\frac{1}{2}|1\rangle.
$$

$p_0=3/4$，$p_1=1/4$；
$r_z=\cos(\pi/3)=1/2$，
$r_x=\sin(\pi/3)\cos(\pi/4)=\sqrt{6}/4$，
$r_y=\sin(\pi/3)\sin(\pi/4)=\sqrt{6}/4$。

**例 2.14（特殊点）**

| 态 | $(\theta,\varphi)$ | $\vec{r}$ |
|---|---|---|
| $\|0\rangle$ | $(0,\cdot)$ | $(0,0,1)$ |
| $\|1\rangle$ | $(\pi,\cdot)$ | $(0,0,-1)$ |
| $\|+\rangle$ | $(\pi/2,0)$ | $(1,0,0)$ |
| $\|-\rangle$ | $(\pi/2,\pi)$ | $(-1,0,0)$ |
| $\|+y\rangle$ | $(\pi/2,\pi/2)$ | $(0,1,0)$ |

**例 2.15（相对相位可观测）**  
$|\psi_0\rangle=\frac{1}{\sqrt{2}}(|0\rangle+|1\rangle)$ 与
$|\psi_1\rangle=\frac{1}{\sqrt{2}}(|0\rangle+i|1\rangle)$  
$Z$ 基概率同为 $1/2$，但 $\langle X\rangle$ 分别为 $1$ 与 $0$，$\langle Y\rangle$ 分别为 $0$ 与 $1$。相对相位 $\pi/2$ 被 $X/Y$ 测出来；整体乘 $e^{i\alpha}$ 则三者皆不变。

### 2.6.5 拉比振荡（驱动下的二能级）

在旋转波近似下，近共振驱动的有效哈密顿常取（$\hbar=1$ 单位）

$$
H = \frac{\Omega}{2}\,X
\quad\text{（共振，驱动相位取 0）},
$$

则

$$
U(t)=e^{-i\Omega t X/2}
= \cos\frac{\Omega t}{2}\,I - i\sin\frac{\Omega t}{2}\,X.
$$

初态 $|0\rangle$：

$$
|\psi(t)\rangle
= \cos\frac{\Omega t}{2}|0\rangle - i\sin\frac{\Omega t}{2}|1\rangle,
\quad
p_1(t)=\sin^2\frac{\Omega t}{2}.
$$

- **$\pi$ 脉冲：** $\Omega t=\pi$ $\Rightarrow$ $p_1=1$（布居翻转）。
- **$\pi/2$ 脉冲：** $\Omega t=\pi/2$ $\Rightarrow$ 等权叠加（差一相位约定）。

**例 2.16** $\Omega=2\pi\times 10\,\mathrm{MHz}=2\pi\cdot 10^7\,\mathrm{rad/s}$，  
$t_\pi=\pi/\Omega = 50\,\mathrm{ns}$。

完整脉冲形状、失谐、 Bloch 章动与硬件校准见 ch07 / ch12 / ch27；此处只要会从 $H$ 写 $U(t)$ 与 $p_1(t)$。

**小练习：** 举三个二能级物理实例。  
**小练习：** 写出 $\theta=\pi/3$，$\varphi=\pi/4$ 的态，并算 $p_0$。  
**小练习：** $|+\rangle$、$|-\rangle$ 的 Bloch 坐标。  
**小练习：** $\Omega=2\pi\times 10\,\mathrm{MHz}$ 的 $\pi$ 脉冲时长。  
**小练习：** $\frac{1}{\sqrt{2}}(|0\rangle+e^{i\pi/2}|1\rangle)$ 的相对相位？$\langle X\rangle,\langle Y\rangle$？

---

## 2.7 量子信息特有的结论

本节结论都从 §2.1–2.5 **推出来**，不是新公设。统一问题：信息能否被复制、区分、在测量中无损读取。

### 2.7.1 量子不可克隆定理

**陈述。** 不存在这样一个幺正 $U$（作用在系统+空白辅助上），使得对**所有**态 $|\psi\rangle$ 都有

$$
U\big(|\psi\rangle\otimes|0\rangle\big)
= |\psi\rangle\otimes|\psi\rangle.
$$

**证明思路（线性）：** 假设存在。取正交 $|0\rangle,|1\rangle$，则

$$
U|0\rangle|0\rangle=|0\rangle|0\rangle,\quad
U|1\rangle|0\rangle=|1\rangle|1\rangle.
$$

对 $|+\rangle=\frac{1}{\sqrt{2}}(|0\rangle+|1\rangle)$，左边线性给出

$$
U|+\rangle|0\rangle
= \frac{1}{\sqrt{2}}\big(|00\rangle+|11\rangle\big),
$$

右边若完美克隆应为 $|+\rangle|+\rangle=\frac{1}{2}(|00\rangle+|01\rangle+|10\rangle+|11\rangle)$。二者不等。矛盾。  
故：**未知通用态**不可完美复制。

**不禁止什么：**

- 已知态的**制备程序**可跑两遍（你知道经典描述，不是“复制未知量子态”）；
- 正交态可在测量后按结果重新制备（测量已破坏原叠加）；
- 近似克隆、概率克隆有界可行（本课不展开）。

**例 2.17** 若可完美克隆，则可对克隆体测 $X$、对本体测 $Z$，从而同时获知不对易信息，与 §2.4 冲突——不可克隆与不确定关系同族。

### 2.7.2 非正交态不可完美区分

**陈述。** 若 $|\psi\rangle$、$|\phi\rangle$ 满足 $0<|\langle\psi|\phi\rangle|<1$，则**不存在**只输出 $\{0,1\}$ 的测量，使得

$$
\Pr(\text{判 }\psi\,|\,\text{真是 }\psi)=1
\quad\text{且}\quad
\Pr(\text{判 }\phi\,|\,\text{真是 }\phi)=1.
$$

**操作含义：** 单次投影测量最多给出有限区分力。对两个等先验非正交纯态，最优成功概率有 Helstrom 界

$$
P_{\mathrm{succ}}
= \frac{1}{2}+\frac{1}{2}\sqrt{1-|\langle\psi|\phi\rangle|^2}
\ >\ \frac12
\quad\text{（仍可 }<\ 1\text{）}.
$$

正交时 $|\langle\psi|\phi\rangle|=0$ $\Rightarrow$ $P_{\mathrm{succ}}=1$（例如 $|0\rangle$ vs $|1\rangle$ 的 $Z$ 测量）。

**例 2.18** $|0\rangle$ 与 $|+\rangle$：$\langle0|+\rangle=1/\sqrt{2}$，  
$P_{\mathrm{succ}}=\frac12+\frac12\sqrt{1/2}=\frac12+\frac{\sqrt{2}}{4}\approx 0.853$。  
可优于瞎猜 50%，但不能 100%。

**小练习：** 两非正交态能否确定性区分？能否以 $>50\%$ 概率区分？

### 2.7.3 测量是交互，不是只读

投影测量公设已规定：得到结果 $m$ 后态变为 $P_m|\psi\rangle$ 的归一化。因此：

- 测量**写入**仪器与系统的关联，不是读取硬盘式的无损拷贝；
- 想“看一眼还保持原叠加”，一般不可能（与不可克隆、非正交不可区分一致）；
- **退相干**（预告）：系统与环境纠缠后，只看系统相当于对环境取偏迹（§1.9.3），相干项被压掉——像“环境替你做了一场未读出的测量”。完整噪声模型见 ch21。

### 2.7.4 量子计算三段式（可视化总结）

把公设串成算法骨架：

1. **制备：** 在 $\mathcal{H}$ 中准备 $|{\psi_0}\rangle$（态空间公设）。  
2. **演化：** 施加门序列 = 幺正 $U$（时间演化公设；理想封闭）。  
3. **测量：** 对约定可观察量做投影测量，得经典比特串（测量公设）。

中间可插入“只看子系统”的偏迹描述（开放），但标准电路图默认 1–2–3。  
二能级几何（Bloch 上的旋转）是第 2 步在 $n=1$ 时的图画；多比特纠缠在 ch08。

**例 2.19（最小电路）** 制备 $|0\rangle$ → 应用 $H$ → 测 $Z$：  
$|0\rangle\mapsto|+\rangle$，得 0/1 各 $1/2$。这是“制备–演化–测量”的最小实例。

**小练习：** 为何不可克隆不禁止“按配方再做一份已知态”？  
**小练习：** 简述不可克隆证明中线性性如何制造矛盾。  
**小练习：** 退相干与偏迹的一句话关系。  
**小练习：** 用三步骤描述：从 $|0\rangle$ 出发，Hadamard 后测 $Z$。

'''---

### 知识点索引

| 术语 | 英文 | 章节 |
|------|------|------|
| Born 规则 | Born rule | 2.3 |
| Dirac 符号 | Dirac notation / bra-ket notation | 2.1 |
| POVM | Positive Operator-Valued Measure | 2.3 |
| 不确定性原理 | Uncertainty principle | 2.4 |
| 布洛赫球面 | Bloch sphere | 2.6.3 |
| 态空间 | State space | 2.1 |
| 定态 | Stationary state | 2.5 |
| 对易子 | Commutator | 2.4 |
| 二能级系统 | Two-level system | 2.6 |
| 非正交态不可区分 | Non-orthogonal state indistinguishability | 2.7.2 |
| 哈密顿算符 | Hamiltonian | 2.2 |
| Hermitian 算符 | Hermitian operator | 2.2 |
| 可观察量 | Observable | 2.2 |
| 拉比振荡 | Rabi oscillation | 2.6.4 |
| 量子比特 | Qubit | 2.6.1 |
| 量子不可克隆定理 | No-cloning theorem | 2.7.1 |
| 期望值 | Expectation value | 2.3 |
| 全局相位 | Global phase | 2.1 |
| 射线表示 | Ray representation | 2.1 |
| 时间演化算符 | Time evolution operator | 2.5 |
| 坍缩 | Collapse | 2.3 |
| 投影测量 | Projective measurement | 2.3 |
| 投影算符 | Projector | 2.3 |
| 退相干 | Decoherence | 2.7.3 |
| 相对相位 | Relative phase | 2.6 |
| 薛定谔方程 | Schrödinger equation | 2.5 |
| 幺正算符 | Unitary operator | 2.5.3 |
| 标准差 | Standard deviation | 2.4 |
| 叠加原理 | Superposition principle | 2.1 |
| 自旋 | Spin | 2.2 |
| 最小不确定态 | Minimum uncertainty state | 2.4 |

---

> **本章小结**
>
> 1. **态空间**：系统 ↔ Hilbert 空间；纯态 ↔ 归一 ket（射线）；会归一化、展开、Dirac 运算。
> 2. **可观察量**：物理量 ↔ 厄米算符；结果 ∈ 谱；会谱分解与算符函数。
> 3. **投影测量**：概率 ⟨P_m⟩，坍缩后归一化 P_m|ψ⟩；会算 p_m、事后态、⟨A⟩。
> 4. **不确定关系（定理）**：ΔA ΔB ≥ (1/2)|⟨[A,B]⟩|；对易方可同时确定。
> 5. **时间演化**：封闭系统 iℏ ψ̇ = Hψ，U 幺正；会算 U(t)|ψ⟩。
> 6. **二能级**：参数 $(\theta,\varphi)$ 与 Bloch 矢量；相对相位可观测；拉比 $p_1=\sin^2(\Omega t/2)$。
> 7. **信息论推论**：不可克隆、非正交不可完美区分；测量有更新；算法=制备–演化–测量。
>
> 下一章：密度矩阵与混合态——把「开放系统只看子系统」变成日常语言。

---

## 2.9 本章习题

**基础题（1-6题）**

1. 为什么全局相位不可观测？举一个具体的例子说明 $|\psi\rangle$ 和 $e^{i\alpha}|\psi\rangle$ 在投影测量下的区别。

2. 算符 $\hat{A} = \begin{pmatrix}0 & -i\\ i & 0\end{pmatrix}$ 是否厄米？求本征值和本征态。

3. 对处于 $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ 的量子比特进行 Z 基测量，求：(a) 测得 $|0\rangle$ 的概率 (b) 期望值 $\langle Z\rangle$。

4. 证明若 $[A,B]=0$，则 $A$ 和 $B$ 有共同的本征态集合。

5. 一个二能级系统的哈密顿量为 $H = \hbar\omega Z/2$，初始态为 $|+\rangle$，求任意时刻 $t$ 的态矢量。

6. 简述量子不可克隆定理的证明思路。

**提高题（7-12题）**

7. 证明不确定关系 $\Delta A \Delta B \ge \frac{1}{2}|\langle[A,B]\rangle|$。

8. 一个量子比特的布洛赫矢量为 $\vec{r} = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$，求对应的态矢量。

9. 对处于 $|0\rangle$ 的量子比特施加 $R_y(\theta)$ 门，然后测量 X。求测量结果为 $|+\rangle$ 的概率。

10. 给定 $|+\rangle$ 态，设计一个测量区分它和 $|-\rangle$，成功概率为多少？

11. 证明时间演化算符的幺正性。

12. 解释非正交态不可区分性的物理意义。

**拓展题（13-15题）**

13. POVM 测量与投影测量有何不同？举例说明 POVM 在量子态区分中的优势。

14. 一个二能级系统与谐振子耦合，写出总哈密顿量并解释 RWA 近似的适用条件。

15. （思考题）"量子测量导致坍缩"是量子力学的公设。有没有不依赖于坍缩的量子力学解释？简要说明多世界解释的观点。

