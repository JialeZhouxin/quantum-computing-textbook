# 习题解答 · 第19章 量子线性代数与模拟

---

### 基础题（1-5）

**7.1** 振幅编码。

**(a)** $|x\rangle = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle = |+\rangle$。电路：一个 H 门。

**(b)** $|x\rangle = \frac{1}{\sqrt{6}}(|00\rangle + 2|01\rangle + |10\rangle + 0|11\rangle)$。归一化自动满足。

**(c)** $|x\rangle = |11\rangle$（1 在 $|11\rangle$ 位置）。

**7.2** 角度编码。

$|\psi\rangle = \bigotimes_{i=0}^2 R_y(x_i)|0\rangle = R_y(0)|0\rangle \otimes R_y(\pi)|0\rangle \otimes R_y(2\pi)|0\rangle = |0\rangle \otimes |1\rangle \otimes |0\rangle$（因为 $R_y(\pi)|0\rangle = |1\rangle$，$R_y(2\pi)|0\rangle = -|0\rangle$，不计全局相位）。

**7.3** HHL 三步：

1. **相位估计**：对 $e^{iA\tau}$ 做 QPE，将 $|b\rangle$ 的本征值编码到辅助寄存器
2. **受控旋转**：根据本征值 $\lambda_j$ 的倒数 $\lambda_j^{-1}$ 旋转辅助比特——振幅编码 $1/\lambda$
3. **逆相位估计**：清除辅助寄存器，得到 $|x\rangle = A^{-1}|b\rangle$

**7.4** $A = \text{diag}(1, 2)$，$|b\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$。

本征值 $\lambda_0 = 1$（$|0\rangle$），$\lambda_1 = 2$（$|1\rangle$）。
$A^{-1}|b\rangle = \frac{1}{\sqrt{2}}(1\cdot|0\rangle + \frac12\cdot|1\rangle) = \frac{1}{\sqrt{2}}(|0\rangle + \frac12|1\rangle)$。

归一化：$|x\rangle = \frac{1}{\sqrt{1 + 1/4}}(\frac{1}{\sqrt{2}}|0\rangle + \frac{1}{2\sqrt{2}}|1\rangle) = \frac{2}{\sqrt{5}}\cdot\frac{1}{\sqrt{2}}(2|0\rangle + |1\rangle) = \frac{1}{\sqrt{10}}(2|0\rangle + |1\rangle)$。

验证：$A|x\rangle = \frac{1}{\sqrt{10}}(2\cdot 1|0\rangle + 1\cdot 2|1\rangle) = \frac{2}{\sqrt{10}}(|0\rangle + |1\rangle) \propto |b\rangle$ ✓

**7.5** 一阶 Trotter 误差：$e^{-i(A+B)\Delta t} = e^{-iA\Delta t}e^{-iB\Delta t} + O(\Delta t^2)$，来自 $[A,B] \neq 0$ 时 Baker-Campbell-Hausdorff 公式的截断误差。

二阶 Trotter-Suzuki：$e^{-i(A+B)\Delta t} \approx e^{-iA\Delta t/2}e^{-iB\Delta t}e^{-iA\Delta t/2} + O(\Delta t^3)$。对称化消去了奇次幂误差项。

---

### 提高题（6-9）

**7.6** $[X_1 X_2, Z_1 Z_2] = [X_1, Z_1] X_2 Z_2 + Z_1 X_1 [X_2, Z_2] = 0$（因为 $[X_i, Z_i] = -2iY_i$，因子 $X_2Z_2$ 和 $Z_1X_1$ 不等，但 $[X_1X_2, Z_1Z_2] = (X_1Z_1 - Z_1X_1)X_2Z_2 = 0$）。精确实现：$e^{-i(X_1X_2 + Z_1Z_2)t} = e^{-iX_1X_2 t} e^{-iZ_1Z_2 t}$。

**7.8** $1/\kappa^2 = 10^{-6}$。期望运行次数 $10^6$ ——巨大开销。除非 $\kappa$ 很小（< 10），HHL 的实际运行次数远超理想化分析。$1/\kappa^2$ 限制了 HHL 在病态问题上的实用性。

---

### 综合题（10-12）

**7.10** HHL 的 QPE 需要实现 $e^{iA\tau}$。如果 $A$ 是稀疏矩阵且可分解为局部项的和（如 $A = \sum H_i$），$e^{iA\tau}$ 用 Trotter 近似实现。总误差 $\varepsilon_{\text{total}}^2 = \varepsilon_T^2 + \varepsilon_{\text{QPE}}^2$。

**7.12** 20 量子比特 Heisenberg 模型。

**(a)** 一阶 Trotter：$r = O(t^2/\varepsilon_T)$步。$\varepsilon_T \leq 0.01$，$t=10$，约需 $r > 100t^2/\varepsilon_T \approx 10^5$ 步。二阶 Trotter 可大幅减少步数。

**(b)** 每步 3 个链项 × (20-1) 个相互作用 × 每个 Trotter 步约 3 个两比特门 ≈ 每步 171 个两比特门。$r=100$ 时总门数约 17100。

**(c)** 门保真度 $0.995^{17100} \approx 10^{-37}$，极低。硬件和 Trotter 误差共同使保真度趋近于零。

**(d)** 不可能达到 50%。需要量子纠错或将 $t$ 大幅减小（< 0.1）。
