# HelloWorld

一个最小化的 Python 项目，用于演示标准的 `src` 目录布局、可执行入口和自动化测试。

## 运行要求

- Python 3.9+

## 运行程序

方式一，直接运行：

```powershell
$env:PYTHONPATH="src"
python -m helloworld
```

方式二，安装为可编辑包后运行：

```powershell
python -m pip install -e .
helloworld
```

预期输出：

```text
helloWord
```

## 运行测试

```powershell
$env:PYTHONPATH="src"
python -m unittest discover -s tests -v
```
