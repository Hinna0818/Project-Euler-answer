# Machine learning
## Introduction
  


## 1. linear regression
### 1. 简单线性回归模型

考虑一个简单线性回归模型：

$$
Y = \beta_0 + \beta_1 X + \varepsilon
$$


### 2. 矩阵表示

对于多个观测值，模型可以表示为矩阵形式：

$$
\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}
$$

对于简单线性回归（一个自变量），设计矩阵如下：

$$
\mathbf{X} =
\begin{bmatrix}
1 & X_1 \\
1 & X_2 \\
\vdots & \vdots \\
1 & X_n \\
\end{bmatrix}
$$

### 3. 最小二乘法（Ordinary Least Squares, OLS）

目标是最小化残差平方和（RSS）：

$$
RSS = \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2 = \sum_{i=1}^{n} (Y_i - \beta_0 - \beta_1 X_i)^2
$$

### 4. 正规方程（Normal Equation）

通过对 RSS 关于回归系数求偏导并令其为零，可以得到正规方程：

$$
\frac{\partial RSS}{\partial \beta} = -2\mathbf{X}^\top (\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}) = 0
$$

整理得：

$$
\mathbf{X}^\top \mathbf{Y} = \mathbf{X}^\top \mathbf{X} \boldsymbol{\beta}
$$

解得回归系数：

$$
\boldsymbol{\beta} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{Y}
$$

<mark>具体的python函数如下：  
```{python}
import numpy as np
x = np.array([xxx])
y = np.array([xxx]).reshape(-1,1) ## y是一个列向量
x_transpose = x.T ## 计算x的转置

## 使用np.linalg.inv()计算矩阵的逆，.dot()计算矩阵乘法
theta = np.linalg.inv(x_transpose.dot(x)).dot(x_transpose).dot(y)

## 也可以用@来计算矩阵乘法
theta = np.linalg.inv(x_transpose@x)@x_transpose@y
```

